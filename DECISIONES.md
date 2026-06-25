# DECISIONES.md

# Registro de Decisiones de Arquitectura (ADR)

Este documento registra las decisiones técnicas y de arquitectura tomadas durante el desarrollo de Azure Inventario.

Cada ADR documenta el problema, las alternativas evaluadas, la decisión tomada y su justificación.

---

# ADR-001

## Nombre del proyecto

### Estado

✅ Aprobado

### Problema

Definir un nombre para el proyecto.

### Alternativas

- Azure Inventory
- Inventory Manager
- Stock Manager
- Azure Inventario

### Decisión

Azure Inventario

### Justificación

Describe claramente el propósito de la aplicación y su relación con Microsoft Azure.

### Impacto

El nombre será utilizado en toda la documentación y la interfaz.

### Posible pregunta

¿Por qué ese nombre?

### Respuesta

Porque representa el propósito de la aplicación y la tecnología principal utilizada.

---

# ADR-002

## Tipo de aplicación

### Estado

✅ Aprobado

### Problema

Definir qué tipo de aplicación desarrollar.

### Alternativas

- API únicamente
- Aplicación web
- Aplicación de escritorio

### Decisión

Aplicación web.

### Justificación

Permite demostrar visualmente el funcionamiento durante la exposición sin aumentar demasiado la complejidad.

### Impacto

Será necesario construir frontend y backend.

### Posible pregunta

¿Por qué no solamente una API?

### Respuesta

Porque una interfaz facilita demostrar el funcionamiento del sistema y mejora la experiencia durante la presentación.

---

# ADR-003

## Framework Frontend

### Estado

✅ Aprobado

### Decisión

Vue 3 + Vite.

### Alternativas

- React
- Angular
- Vue

### Justificación

Vue ofrece una excelente relación entre simplicidad, rendimiento y mantenibilidad para el alcance del proyecto.

### Impacto

Arquitectura basada en componentes.

---

# ADR-004

## Diseño del Frontend

### Estado

✅ Aprobado

### Decisión

Dashboard moderno.

### Características

- Sidebar
- Navbar
- Cards
- Tabla moderna
- Responsive
- Iconografía
- Gráficos

### Justificación

Una interfaz moderna mejora la presentación del proyecto y facilita la visualización del inventario.

---

# ADR-005

## Librerías del Frontend

### Estado

✅ Aprobado

### Decisión

- Tailwind CSS
- PrimeVue
- Lucide Icons
- Apache ECharts

### Justificación

Reducen el tiempo de desarrollo y permiten construir una interfaz profesional utilizando componentes reutilizables.

---

# ADR-006

## Framework Backend

### Estado

✅ Aprobado

### Decisión

FastAPI.

### Alternativas

- Flask
- Django
- FastAPI

### Justificación

Genera documentación automática, tiene buen rendimiento y una estructura sencilla para APIs REST.

---

# ADR-007

## Base de Datos

### Estado

✅ Aprobado

### Decisión

SQLite.

### Alternativas

- PostgreSQL
- MySQL
- Azure SQL
- SQLite

### Justificación

Disminuye la complejidad del proyecto sin afectar los objetivos del curso.

---

# ADR-008

## Contenerización

### Estado

✅ Aprobado

### Decisión

Docker.

### Justificación

Es un requisito del proyecto y permite empaquetar la aplicación para su despliegue.

---

# ADR-009

## Infraestructura como Código

### Estado

✅ Aprobado

### Decisión

Terraform.

### Justificación

Automatiza la creación de infraestructura y cumple con los requerimientos del Pipeline 1.

---

# ADR-010

## Servicios de Azure

### Estado

✅ Aprobado

### Recursos

- Resource Group
- Virtual Network
- Subnet
- Azure Container Registry
- Azure Container Instances

### Justificación

Son exactamente los servicios necesarios para cumplir el alcance del proyecto.

---

# ADR-011

## Herramienta CI/CD

### Estado

✅ Aprobado

### Decisión

GitHub Actions.

### Alternativas

- Azure DevOps
- GitHub Actions

### Justificación

Integra fácilmente el repositorio con Azure y simplifica la configuración de los pipelines.

---

# ADR-012

## Organización del Proyecto

### Estado

✅ Aprobado

### Decisión

Separar el proyecto en:

- frontend/
- backend/
- terraform/
- docs/
- .github/

### Justificación

Mejora la organización y facilita el mantenimiento.

---

# ADR-013

## Alcance Funcional

### Estado

✅ Aprobado

### Funcionalidades

- Dashboard
- CRUD Productos
- Categorías
- Métricas
- Estados de stock

### Justificación

Cumple con el objetivo académico sin agregar complejidad innecesaria.

---

# ADR-014

## Funcionalidades fuera del alcance

### Estado

✅ Aprobado

### No implementar

- Login
- Roles
- Facturación
- Pagos
- Reportes avanzados
- Kubernetes
- Azure SQL

### Justificación

No aportan valor a los objetivos evaluados.

---

# ADR-015

## Forma de desarrollo

### Estado

✅ Aprobado

### Decisión

El proyecto se desarrollará por fases.

Cada fase deberá cumplir:

1. Diseño.
2. Validación.
3. Implementación.
4. Revisión.
5. Documentación.

### Justificación

Reduce errores y facilita comprender cada parte del proyecto.

---

# ADR-016

## Uso de Codex

### Estado

✅ Aprobado

### Decisión

Codex será el encargado de implementar.

Las decisiones técnicas serán tomadas previamente y documentadas.

### Justificación

Permite mantener el control del proyecto y comprender cada implementación antes de aceptarla.

# ADR-017

## Contenedores del proyecto

### Estado

✅ Aprobado

### Decisión

Se utilizarán dos contenedores:

- Un contenedor para el backend.
- Un contenedor para el frontend.

### Justificación

Frontend y backend tienen dependencias, procesos y responsabilidades diferentes. Separarlos mejora la organización y facilita el despliegue.

---

# ADR-018

## Conexión Frontend - Backend

### Estado

✅ Aprobado

### Decisión

El frontend consumirá el backend mediante una variable de entorno:

```env
VITE_API_URL=http://localhost:8000
```

### Justificación

Permite cambiar la URL del backend entre desarrollo local y despliegue en Azure sin modificar el código fuente del frontend.

### Impacto

El frontend debe leer la URL base de la API desde `VITE_API_URL`.

---

# ADR-019

## Despliegue en Azure Container Instances

### Estado

✅ Aprobado

### Decisión

Se utilizará un Azure Container Group con dos contenedores:

- Un contenedor para el backend.
- Un contenedor para el frontend.

Cada contenedor tendrá su propia imagen Docker publicada en Azure Container Registry.

### Justificación

El backend y el frontend tienen procesos, puertos y dependencias diferentes. Usar un Container Group permite desplegarlos juntos en Azure Container Instances manteniendo responsabilidades separadas.

### Impacto

Terraform y los pipelines deberán considerar dos imágenes Docker y un único Container Group con ambos contenedores.
