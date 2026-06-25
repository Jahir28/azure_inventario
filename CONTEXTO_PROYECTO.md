# CONTEXTO_PROYECTO.md

# Azure Inventory

## Nombre del estudiante

Jahir Rangel

## Título del proyecto

Azure Inventory: Sistema web de inventario desplegado con Docker, Terraform y pipelines CI/CD en Microsoft Azure.

## Descripción general

Azure Inventory es una aplicación web para la gestión básica de inventario. Permite registrar, visualizar, editar y eliminar productos, además de calcular automáticamente el estado del stock.

El objetivo principal del proyecto no es construir un sistema empresarial complejo, sino demostrar un flujo completo de integración y despliegue continuo utilizando Microsoft Azure, Docker, Terraform y pipelines CI/CD.

## Objetivo académico

Construir tres pipelines en Microsoft Azure o integrados con Azure:

1. Pipeline de infraestructura.
2. Pipeline de construcción y publicación de imagen Docker.
3. Pipeline de despliegue del contenedor.

## Alcance funcional

La aplicación debe permitir:

- Visualizar un dashboard general del inventario.
- Registrar productos.
- Listar productos.
- Editar productos.
- Eliminar productos.
- Clasificar productos por categoría.
- Registrar precio y cantidad disponible.
- Calcular automáticamente el estado del producto según el stock.

## Estados del producto

El estado se calcula de la siguiente manera:

- Stock igual a 0: Agotado.
- Stock entre 1 y 5: Bajo stock.
- Stock mayor a 5: Disponible.

## Métricas del dashboard

El dashboard debe mostrar:

- Total de productos.
- Cantidad de productos disponibles.
- Cantidad de productos con bajo stock.
- Cantidad de productos agotados.
- Valor total del inventario.

## Tecnologías definidas

Frontend:

- Vue 3.
- Interfaz web visual y clara.
- Tabla de productos.
- Formularios para crear y editar productos.
- Tarjetas de métricas para el dashboard.

Backend:

- FastAPI.
- API REST.
- Validación de datos.
- Documentación automática con Swagger.

Base de datos:

- SQLite.
- Se usará para simplificar el despliegue y evitar costos adicionales.

Contenedores:

- Docker.
- La aplicación completa debe ejecutarse dentro de un contenedor.

Infraestructura:

- Terraform.
- Debe crear los recursos requeridos en Azure.

Cloud:

- Microsoft Azure.

Servicios de Azure:

- Azure Virtual Network.
- Subnet.
- Azure Container Registry.
- Azure Container Instances.
- Permisos para que ACI pueda obtener imágenes desde ACR.

CI/CD:

- GitHub Actions.

## Pipelines requeridos

### Pipeline 1: Infraestructura

Debe crear la infraestructura necesaria mediante Terraform:

- Resource Group.
- Virtual Network.
- Subnet.
- Azure Container Registry.
- Azure Container Instance.
- Permisos necesarios para que el contenedor pueda obtener imágenes desde ACR.

### Pipeline 2: Construcción y publicación

Debe encargarse de:

- Obtener el código desde el repositorio.
- Instalar dependencias.
- Ejecutar pruebas.
- Construir la aplicación.
- Construir la imagen Docker.
- Asignar una etiqueta/version a la imagen.
- Publicar la imagen en Azure Container Registry.

### Pipeline 3: Despliegue

Debe encargarse de:

- Seleccionar la imagen publicada en ACR.
- Crear o actualizar el contenedor en Azure Container Instances.
- Configurar variables de entorno necesarias.
- Verificar que el contenedor esté en ejecución.
- Validar que la aplicación sea accesible.

## Entregables finales

El proyecto debe incluir:

- Código fuente de la aplicación.
- Dockerfile.
- Código de infraestructura como código.
- Archivos de configuración de los tres pipelines.
- Evidencia de infraestructura creada en Azure.
- Evidencia de imagen publicada en ACR.
- Evidencia del contenedor desplegado en ACI.
- URL o dirección de acceso a la aplicación.
- Documento breve explicando la solución.
- Diagrama de arquitectura y flujo de los pipelines.

## Fuera de alcance

No se debe implementar:

- Login.
- Roles de usuario.
- Facturación.
- Pagos.
- Reportes complejos.
- Azure SQL.
- Kubernetes.
- Microservicios.
- Arquitectura distribuida compleja.

## Criterio principal del proyecto

El proyecto debe ser sencillo, funcional, visualmente presentable y suficientemente completo para demostrar correctamente:

- Infraestructura como código.
- Contenerización con Docker.
- Publicación de imágenes en ACR.
- Despliegue en ACI.
- Automatización mediante pipelines.
- Validación de despliegue en Azure.

## Enfoque de exposición

Durante la exposición se debe explicar:

1. Qué problema resuelve Azure Inventory.
2. Qué tecnologías se usaron.
3. Cómo está organizada la aplicación.
4. Cómo funciona Docker en el proyecto.
5. Qué crea Terraform.
6. Qué hace cada pipeline.
7. Cómo se publica la imagen en ACR.
8. Cómo se despliega el contenedor en ACI.
9. Qué evidencias demuestran que el sistema funciona.
10. Qué URL permite acceder a la aplicación.