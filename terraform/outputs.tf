output "resource_group_name" {
  description = "Name of the created Resource Group."
  value       = azurerm_resource_group.main.name
}

output "virtual_network_name" {
  description = "Name of the created Virtual Network."
  value       = azurerm_virtual_network.main.name
}

output "subnet_name" {
  description = "Name of the delegated subnet for Azure Container Instances."
  value       = azurerm_subnet.aci.name
}

output "container_registry_name" {
  description = "Name of the Azure Container Registry."
  value       = azurerm_container_registry.main.name
}

output "container_registry_login_server" {
  description = "ACR login server used by Docker images."
  value       = azurerm_container_registry.main.login_server
}

output "container_group_name" {
  description = "Name of the Azure Container Group."
  value       = try(azurerm_container_group.main[0].name, null)
}

output "container_group_fqdn" {
  description = "Public FQDN assigned to the Azure Container Group."
  value       = try(azurerm_container_group.main[0].fqdn, null)
}

output "frontend_url" {
  description = "Public URL for the frontend container."
  value       = try("http://${azurerm_container_group.main[0].fqdn}", null)
}

output "backend_health_url" {
  description = "Public backend health endpoint."
  value       = try("http://${azurerm_container_group.main[0].fqdn}:${var.backend_port}/health", null)
}

output "swagger_url" {
  description = "Public Swagger documentation URL for the backend."
  value       = try("http://${azurerm_container_group.main[0].fqdn}:${var.backend_port}/docs", null)
}
