# Evidencias

Este documento servirá para registrar capturas y resultados de la entrega:

- Infraestructura creada en Azure.
- Imágenes publicadas en Azure Container Registry.
- Container Group ejecutándose en Azure Container Instances.
- URL pública de la aplicación.

## Estado de evidencias

| Evidencia | Estado | Qué debe mostrar |
| --- | --- | --- |
| Pipeline Infrastructure | Pendiente de captura | Workflow ejecutado correctamente en GitHub Actions |
| Pipeline Build and Publish | Pendiente de captura | Pruebas, build, Docker build y push a ACR completados |
| Pipeline Deploy | Pendiente de captura | Terraform apply, validación `/health` y URLs finales |
| Resource Group | Pendiente de captura | Grupo de recursos del proyecto en Azure |
| Azure Container Registry | Pendiente de captura | Repositorios de backend y frontend con tags publicados |
| Azure Container Instances | Pendiente de captura | Container Group en estado `Running` |
| FQDN público del ACI | Pendiente de captura | DNS público asignado al Container Group |
| Frontend público | Pendiente de captura | Aplicación abierta por HTTP |
| Backend health | Pendiente de captura | Respuesta de `/health` con estado correcto |
| Swagger | Pendiente de captura | Documentación automática de FastAPI en `/docs` |

## URLs a validar

Frontend:

```text
http://azure-inventario-dev.eastus.azurecontainer.io
```

Backend health:

```text
http://azure-inventario-dev.eastus.azurecontainer.io:8000/health
```

Swagger:

```text
http://azure-inventario-dev.eastus.azurecontainer.io:8000/docs
```

## Capturas recomendadas

### GitHub Actions

Capturar:

- Lista de workflows.
- Ejecución exitosa de `Infrastructure`.
- Ejecución exitosa de `Build and Publish`.
- Ejecución exitosa de `Deploy`.
- Paso donde se valida el endpoint `/health`.
- Paso donde se muestran las URLs finales.

### Azure Portal

Capturar:

- Resource Group del proyecto.
- Azure Container Registry.
- Repositorios de imágenes Docker.
- Tags `latest` y SHA corto.
- Azure Container Instance en ejecución.
- Contenedores `backend` y `frontend`.
- FQDN público del Container Group.

### Aplicación

Capturar:

- Dashboard principal.
- Tabla de productos.
- Formulario de creación o edición.
- Swagger del backend.
- Respuesta del endpoint `/health`.

## Explicación para la exposición

Estas evidencias prueban que el proyecto no solo funciona localmente, sino que también cumple el flujo CI/CD:

```text
Código en GitHub
↓
GitHub Actions
↓
Pruebas y build
↓
Imágenes Docker
↓
Azure Container Registry
↓
Terraform
↓
Azure Container Instances
↓
Aplicación pública por HTTP
```
