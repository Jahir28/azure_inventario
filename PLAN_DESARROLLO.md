# PLAN_DESARROLLO.md

# Plan de desarrollo - Azure Inventario

Este documento describe el orden de construcción del proyecto y el estado actual validado para la presentación.

---

# Fase 1 - Preparación

Objetivo:

Crear la estructura inicial del proyecto.

Tareas:

- Crear backend.
- Crear frontend.
- Inicializar repositorio.
- Configurar dependencias.

Estado:

✅ Completado

Resultado:

- Estructura del repositorio creada.
- Carpetas principales separadas en `backend/`, `frontend/`, `terraform/`, `.github/` y `docs/`.
- Dependencias definidas para backend y frontend.

---

# Fase 2 - Backend

Objetivo:

Construir la API REST.

Tareas:

- Configurar FastAPI.
- Crear modelo Producto.
- CRUD de productos.
- Documentación Swagger.
- Validaciones.

Estado:

✅ Completado

Resultado:

- API REST construida con FastAPI.
- Modelo de producto definido.
- CRUD de productos implementado.
- Endpoint `/health` disponible para validaciones.
- Documentación Swagger disponible en `/docs`.
- Validaciones básicas de datos implementadas.

---

# Fase 3 - Frontend

Objetivo:

Construir la interfaz web.

Tareas:

- Dashboard.
- Sidebar.
- Navbar.
- Tabla de productos.
- Formulario de productos.
- Cards de métricas.
- Integración con la API.

Estado:

✅ Completado

Resultado:

- Dashboard de inventario implementado.
- Sidebar y navbar implementados.
- Tabla de productos implementada.
- Formulario de creación y edición implementado.
- Cards de métricas implementadas.
- Gráfico de estado de inventario implementado.
- Integración con el backend mediante `VITE_API_URL`.

---

# Fase 4 - Docker

Objetivo:

Contenerizar la aplicación.

Tareas:

- Dockerfile.
- Build local.
- Pruebas.

Estado:

✅ Completado

Resultado:

- Dockerfile del backend creado.
- Dockerfile del frontend creado.
- `docker-compose.yml` creado para ejecución local.
- El proyecto usa dos contenedores: backend y frontend.

Nota:

La validación local con Docker se realiza desde el entorno de Windows, porque Docker Desktop y la integración correspondiente están disponibles allí.

---

# Fase 5 - Terraform

Objetivo:

Crear infraestructura en Azure.

Tareas:

- Resource Group.
- Virtual Network.
- Subnet.
- Azure Container Registry.
- Azure Container Instance.

Estado:

✅ Completado

Resultado:

- Terraform define Resource Group.
- Terraform define Virtual Network.
- Terraform define Subnet delegada para Azure Container Instances.
- Terraform define Azure Container Registry.
- Terraform define Azure Container Group con dos contenedores.
- El estado remoto de Terraform se almacena en Azure Storage.

Nota:

Los comandos de Terraform se ejecutan desde la terminal de Windows, donde está instalado y configurado el entorno de Azure.

---

# Fase 6 - Pipeline 1

Objetivo:

Automatizar la creación de infraestructura.

Estado:

✅ Completado

Resultado:

- Workflow `infrastructure.yml` creado.
- Ejecuta formato, inicialización, validación y plan de Terraform.
- Permite aplicar cambios de infraestructura cuando se ejecuta manualmente con `apply=true`.

---

# Fase 7 - Pipeline 2

Objetivo:

Construir y publicar la imagen Docker.

Estado:

✅ Completado

Resultado:

- Workflow `build-and-publish.yml` creado.
- Ejecuta pruebas del backend.
- Compila el frontend.
- Construye imágenes Docker para backend y frontend.
- Publica las imágenes en Azure Container Registry.
- Usa etiquetas `latest` y SHA corto del commit.

---

# Fase 8 - Pipeline 3

Objetivo:

Desplegar automáticamente la aplicación.

Estado:

✅ Completado

Resultado:

- Workflow `deploy.yml` creado.
- Recibe la etiqueta de imagen a desplegar.
- Ejecuta Terraform con `deploy_container_group=true`.
- Actualiza Azure Container Instances.
- Valida el endpoint `/health`.
- Muestra URLs finales de frontend, backend y Swagger.

---

# Fase 9 - Documentación

Objetivo:

Preparar la entrega.

Tareas:

- Capturas.
- Diagrama.
- Documento explicativo.
- Verificación final.

Estado:

🟨 En progreso

Resultado actual:

- Documentación base creada.
- Arquitectura documentada.
- Proceso de despliegue documentado.
- Evidencias pendientes de completar con capturas reales de GitHub Actions y Azure.

Pendiente:

- Agregar capturas de los tres pipelines ejecutados correctamente.
- Agregar captura del Azure Container Registry con las imágenes publicadas.
- Agregar captura del Azure Container Instance en ejecución.
- Agregar URL final de la aplicación.
- Preparar guion final de exposición.

---

# Objetivo final

Completar la documentación final, registrar evidencias y preparar la explicación de la solución para la exposición.
