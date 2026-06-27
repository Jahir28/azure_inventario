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

## Estado actual del proyecto

El proyecto ya cuenta con la estructura principal necesaria para la entrega académica:

- Backend FastAPI funcional.
- Frontend Vue 3 funcional.
- Dockerfiles para backend y frontend.
- Docker Compose para ejecución local.
- Terraform para infraestructura en Azure.
- Tres pipelines de GitHub Actions.
- Despliegue en Azure Container Instances.

La documentación final y las evidencias deben mantenerse actualizadas con capturas reales de GitHub Actions y Azure Portal.

### Flujo de actualización

Si se modifica el frontend, backend o configuración del proyecto, el cambio debe subirse a GitHub para que los pipelines lo usen:

```text
Cambios locales
Commit
Push a GitHub
Build and Publish
Deploy
Validación en Azure
```

Los cambios que solo existen en la máquina local no son visibles para GitHub Actions.

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

### URL de API para el frontend

El frontend se compila con:

```text
VITE_API_URL=http://azure-inventario-dev.eastus.azurecontainer.io:8000
```

### Acceso público

La aplicación se accede por HTTP:

```text
http://azure-inventario-dev.eastus.azurecontainer.io
```

El uso de HTTP se mantiene para evitar recursos adicionales con costo como Application Gateway o Front Door.

### Backend público

El backend está disponible en el puerto 8000 para facilitar la validación de la API:

```text
http://azure-inventario-dev.eastus.azurecontainer.io:8000
```

Para producción, el backend debería protegerse detrás de una red privada, gateway o proxy con HTTPS. Para este proyecto académico se mantiene público porque la asignación solicita una URL de acceso a la aplicación y no exige HTTPS.

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

## Nota sobre el entorno local

En esta máquina, las herramientas como Docker, Terraform y Azure CLI pueden estar disponibles desde la terminal de Windows y no necesariamente desde WSL Ubuntu.

Eso es válido siempre que:

- Docker funcione desde Windows.
- Terraform pueda ejecutarse desde Windows.
- Azure CLI esté autenticado desde Windows.
- Los pipelines de GitHub Actions ejecuten correctamente el flujo completo.
