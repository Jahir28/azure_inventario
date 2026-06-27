locals {
  # Azure Container Registry exige nombres sin guiones y en minúscula.
  normalized_name = replace(lower(var.project_name), "-", "")
  common_tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "azurerm_resource_group" "main" {
  name     = "rg-${var.project_name}-${var.environment}"
  location = var.location
  tags     = local.common_tags
}

resource "azurerm_virtual_network" "main" {
  name                = "vnet-${var.project_name}-${var.environment}"
  address_space       = var.address_space
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  tags                = local.common_tags
}

resource "azurerm_subnet" "aci" {
  name                 = "snet-aci-${var.environment}"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = var.subnet_address_prefixes

  delegation {
    name = "aci-delegation"

    service_delegation {
      # La delegación permite ejecutar Azure Container Instances dentro de esta subnet.
      name    = "Microsoft.ContainerInstance/containerGroups"
      actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
    }
  }
}

resource "azurerm_container_registry" "main" {
  name                = "acr${local.normalized_name}${var.environment}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  # Se habilita admin para que ACI pueda descargar imágenes privadas del ACR.
  admin_enabled = true
  tags          = local.common_tags
}

resource "azurerm_container_group" "main" {
  # Pipeline Infrastructure crea la base; Pipeline Deploy activa el Container Group.
  count = var.deploy_container_group ? 1 : 0

  name                = "aci-${var.project_name}-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  ip_address_type     = "Public"
  # El FQDN público cumple el entregable de URL de acceso sin agregar recursos costosos.
  dns_name_label = "${var.project_name}-${var.environment}"
  restart_policy = "Always"
  tags           = local.common_tags

  image_registry_credential {
    server   = azurerm_container_registry.main.login_server
    username = azurerm_container_registry.main.admin_username
    password = azurerm_container_registry.main.admin_password
  }

  container {
    # Backend FastAPI: expone API REST, Swagger y /health.
    name   = "backend"
    image  = var.backend_image
    cpu    = var.container_cpu
    memory = var.container_memory

    ports {
      port     = var.backend_port
      protocol = "TCP"
    }

    environment_variables = {
      DATABASE_URL = "sqlite:///./data/inventory.db"
    }
  }

  container {
    # Frontend Vue compilado y servido con Nginx.
    name   = "frontend"
    image  = var.frontend_image
    cpu    = var.container_cpu
    memory = var.container_memory

    ports {
      port     = var.frontend_port
      protocol = "TCP"
    }
  }
}
