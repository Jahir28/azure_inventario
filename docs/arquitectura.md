# Arquitectura

Azure Inventario se organiza en frontend, backend, infraestructura y pipelines.

- El frontend usa Vue 3 con Vite.
- El backend usa FastAPI y SQLite.
- Docker separa la aplicación en dos imágenes: backend y frontend.
- Azure Container Instances ejecutará un Container Group con dos contenedores.
