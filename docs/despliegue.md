# Despliegue

El despliegue se realiza mediante tres pipelines de GitHub Actions:

1. `Infrastructure`
   - Ejecuta Terraform.
   - Crea infraestructura base.
   - Usa estado remoto en Azure Storage.

2. `Build and Publish`
   - Instala dependencias.
   - Ejecuta pruebas del backend.
   - Construye frontend.
   - Construye imágenes Docker.
   - Publica imágenes en Azure Container Registry.

3. `Deploy`
   - Ejecuta Terraform con las imágenes publicadas.
   - Crea o actualiza Azure Container Instances.
   - Valida el endpoint `/health`.
   - Muestra las URLs finales del despliegue.

## Orden recomendado

```text
Infrastructure → Build and Publish → Deploy
```

## Estado actual

Según la validación del proyecto, los tres pipelines ya existen y forman el flujo completo de CI/CD:

- `infrastructure.yml`
- `build-and-publish.yml`
- `deploy.yml`

Los comandos de Azure CLI, Terraform y Docker se gestionan desde la terminal de Windows, donde el entorno ya está configurado. En WSL Ubuntu puede que estas herramientas no aparezcan instaladas, pero eso no invalida el proyecto si el flujo funcional está en Windows y GitHub Actions.

## Actualizar la aplicación

Cuando se hace un cambio en frontend, backend, Docker, Terraform o workflows:

```text
Modificar localmente
Commit
Push a GitHub
Ejecutar workflows necesarios
Validar en Azure
```

Para cambios de aplicación normalmente se ejecuta:

```text
Build and Publish → Deploy
```

Para cambios de infraestructura normalmente se ejecuta:

```text
Infrastructure → Deploy
```

## URL pública

La aplicación se accede por HTTP usando el FQDN público del Container Group:

```text
http://azure-inventario-dev.eastus.azurecontainer.io
```

El backend puede validarse con:

```text
http://azure-inventario-dev.eastus.azurecontainer.io:8000/health
```

Swagger puede revisarse con:

```text
http://azure-inventario-dev.eastus.azurecontainer.io:8000/docs
```

## Por qué HTTP público

La asignación solicita una URL o dirección de acceso a la aplicación. Azure Container Instances entrega un FQDN público cuando el Container Group usa IP pública.

Para HTTPS o entrada pública hacia un ACI privado se requeriría una capa adicional, por ejemplo:

- Application Gateway.
- Azure Front Door.
- Proxy público con certificado TLS.

No se agrega esa capa para mantener bajo costo en la cuenta de estudiante y enfocar el proyecto en los tres pipelines solicitados.

## Pasos desde GitHub

1. Entrar al repositorio en GitHub.
2. Ir a `Actions`.
3. Ejecutar `Infrastructure`.
4. Si se desea aplicar infraestructura, seleccionar `apply=true`.
5. Ejecutar `Build and Publish`.
6. Esperar que publique las imágenes en Azure Container Registry.
7. Ejecutar `Deploy`.
8. Ingresar la etiqueta de imagen a desplegar, por ejemplo `latest`.
9. Revisar que el job valide correctamente `/health`.
10. Abrir la URL pública del frontend.

## Pasos desde Azure Portal

1. Entrar a Azure Portal.
2. Buscar el Resource Group del proyecto.
3. Revisar Azure Container Registry.
4. Confirmar que existan las imágenes:
   - `azure-inventario-backend`
   - `azure-inventario-frontend`
5. Revisar Azure Container Instances.
6. Confirmar que el Container Group esté en estado `Running`.
7. Confirmar que existan dos contenedores:
   - `backend`
   - `frontend`
8. Copiar el FQDN público.
9. Probar el frontend, `/health` y `/docs`.
