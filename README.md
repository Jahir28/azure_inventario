# Azure Inventario

Aplicación web de gestión de inventario desplegada mediante Docker, Terraform y pipelines CI/CD en Microsoft Azure.

## Descripción

Azure Inventario permite administrar productos, controlar stock y visualizar métricas generales mediante un dashboard web.

El objetivo principal del proyecto es demostrar un flujo completo de integración y despliegue continuo en Azure.

## Estructura del proyecto 
azure_inventario/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── terraform/
├── docs/
├── .github/
│   └── workflows/
├── AGENTS.md
├── CONTEXTO_PROYECTO.md
├── DECISIONES.md
├── PLAN_DESARROLLO.md
├── README.md
└── .gitignore

## Tecnologías

### Frontend

- Vue 3
- Vite
- Tailwind CSS
- PrimeVue
- Lucide Icons
- ECharts

### Backend

- FastAPI
- SQLite
- API REST
- Swagger

### DevOps y Cloud

- Docker
- Terraform
- GitHub Actions
- Azure Container Registry
- Azure Container Instances
- Azure Virtual Network
- Azure Subnet

## Funcionalidades

- Dashboard de inventario.
- Registro de productos.
- Listado de productos.
- Edición de productos.
- Eliminación de productos.
- Cálculo automático del estado del stock.
- Métricas generales del inventario.

## Estados de stock

```text
Stock = 0      -> Agotado
Stock 1 a 5    -> Bajo stock
Stock > 5      -> Disponible
```

## GitHub Actions

El proyecto usa tres pipelines:

- `infrastructure.yml`: valida y aplica infraestructura base con Terraform.
- `build-and-publish.yml`: construye backend, frontend e imágenes Docker, y publica en ACR.
- `deploy.yml`: actualiza Azure Container Instances usando Terraform con la imagen seleccionada.

### Secrets requeridos

Configurar en GitHub Repository Settings > Secrets and variables > Actions:

```text
AZURE_CREDENTIALS
AZURE_SUBSCRIPTION_ID
ACR_LOGIN_SERVER
ACR_USERNAME
ACR_PASSWORD
RESOURCE_GROUP_NAME
CONTAINER_GROUP_NAME
```

### Variables requeridas

Configurar en GitHub Repository Settings > Secrets and variables > Actions > Variables:

```text
ACI_DNS_NAME
AZURE_LOCATION
```

### Backend remoto de Terraform

Terraform guarda el estado compartido en Azure Storage:

```text
Resource Group: rg-terraform-state
Storage Account: stazureinvstate3435
Container: tfstate
State file: azure-inventario-dev.tfstate
```

Después de configurar el backend remoto se debe ejecutar:

```bash
cd terraform
terraform init
```
