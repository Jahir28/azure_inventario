# Arquitectura

Azure Inventario se organiza en frontend, backend, infraestructura y pipelines.

- El frontend usa Vue 3 con Vite.
- El backend usa FastAPI y SQLite.
- Docker separa la aplicación en dos imágenes: backend y frontend.
- Azure Container Registry almacena las imágenes Docker publicadas.
- Azure Container Instances ejecuta un Container Group público con dos contenedores.
- Terraform administra la infraestructura y usa estado remoto en Azure Storage.

## Flujo general

```text
Usuario
  ↓
Frontend en ACI mediante HTTP público
  ↓
Backend FastAPI en ACI
  ↓
SQLite dentro del contenedor backend
```

## Flujo CI/CD

```text
GitHub
  ↓
GitHub Actions
  ↓
Docker build
  ↓
Azure Container Registry
  ↓
Terraform apply
  ↓
Azure Container Instances
```

## Decisión de red

El proyecto crea Virtual Network y Subnet como parte de la infraestructura requerida. Para cumplir el entregable de URL de acceso a la aplicación sin agregar costos, el Container Group se expone públicamente mediante FQDN.

## Acceso HTTP público

La aplicación se accede por HTTP:

```text
http://azure-inventario-dev.eastus.azurecontainer.io
```

Azure Container Instances entrega un FQDN público cuando el Container Group usa IP pública y `dns_name_label`.

Para exponer la aplicación públicamente con HTTPS sería necesario agregar componentes adicionales, por ejemplo:

- Dominio personalizado.
- Certificado TLS.
- Azure Application Gateway.
- Azure Front Door.
- Servicio intermedio que termine TLS.

Esos componentes aumentan la complejidad, el costo y el tiempo de explicación. Por eso el proyecto mantiene el alcance en ACI, VNet, ACR, Terraform y GitHub Actions.

## Backend público para demostración

Estado actual:

```text
Frontend público: http://azure-inventario-dev.eastus.azurecontainer.io
Backend público:  http://azure-inventario-dev.eastus.azurecontainer.io:8000
```

Para una aplicación productiva, el backend debería quedar privado y exponerse mediante una capa controlada como Application Gateway o Front Door. Para esta entrega se prioriza una URL pública de acceso a la aplicación sin agregar recursos costosos a la cuenta de estudiante.

Respuesta sugerida si el profesor pregunta:

```text
La VNet y la subnet se crean como parte de la infraestructura. También se validó que ACI puede desplegarse con IP privada dentro de la subnet, pero para la entrega se usa FQDN público porque la asignación solicita una URL de acceso a la aplicación y se busca evitar recursos adicionales con costo.
```

## Contenedores

El Container Group ejecuta dos contenedores:

- `backend`: ejecuta FastAPI en el puerto 8000.
- `frontend`: sirve la aplicación Vue compilada usando Nginx en el puerto 80.

La separación facilita explicar que cada parte tiene su propia imagen Docker, sus propias dependencias y su propio proceso de construcción.

## Nota sobre red privada

Una versión productiva podría integrar el ACI directamente a la subnet con IP privada y exponerlo mediante Application Gateway o Azure Front Door. Esa variante no se mantiene como despliegue final porque agrega costo y complejidad fuera del alcance principal del semestral.
