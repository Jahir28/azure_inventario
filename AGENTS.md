# AGENTS.md

# Azure Inventory - Reglas de trabajo para el agente

Este documento define las reglas que todo agente (Codex o similar) debe seguir durante el desarrollo del proyecto.

Estas reglas tienen prioridad sobre cualquier sugerencia o decisión automática del agente.

---

# 1. Objetivo principal

El objetivo del proyecto es construir una aplicación web llamada Azure Inventory que sirva como demostración para un proyecto académico sobre CI/CD y Microsoft Azure.

El objetivo NO es construir un ERP completo.

El enfoque principal es demostrar correctamente:

- Docker
- Terraform
- Azure
- Azure Container Registry
- Azure Container Instances
- GitHub Actions
- Integración continua
- Despliegue continuo

La aplicación debe mantenerse sencilla, organizada y fácil de explicar durante una exposición.

---

# 2. Forma de trabajar

Antes de realizar cualquier cambio importante, el agente deberá explicar:

- Qué hará.
- Por qué lo hará.
- Qué archivos piensa modificar.
- Qué impacto tendrá.

Después deberá esperar aprobación cuando corresponda.

Nunca asumir que una decisión importante está aprobada.

---

# 3. Comunicación

Siempre responder utilizando el siguiente formato.

## Objetivo

Explicar qué se pretende lograr.

## Archivos

Indicar qué archivos serán modificados.

## Explicación

Explicar por qué se realizará ese cambio.

## Riesgos

Indicar si existe algún riesgo.

## Estado

Esperar aprobación cuando sea necesario.

---

# 4. Decisiones

Si existen varias formas de implementar una solución:

NO seleccionar una automáticamente.

Mostrar:

Opción A

Ventajas

Desventajas

Opción B

Ventajas

Desventajas

Recomendación

Esperar aprobación.

---

# 5. Arquitectura

No modificar la arquitectura del proyecto sin autorización.

No mover carpetas.

No cambiar la estructura.

No eliminar módulos.

---

# 6. Dependencias

Nunca instalar nuevas librerías sin autorización.

Antes de instalar cualquier dependencia indicar:

- Motivo.
- Beneficio.
- Tamaño aproximado.
- Posibles alternativas.

Esperar aprobación.

---

# 7. Versiones

No actualizar versiones de frameworks automáticamente.

No cambiar:

- Vue
- FastAPI
- Python
- Terraform

Sin autorización.

---

# 8. Código

Todo código debe cumplir:

- Legible.
- Modular.
- Reutilizable.
- Fácil de explicar.
- Fácil de mantener.

Evitar soluciones excesivamente complejas.

---

# 9. Comentarios

Agregar comentarios únicamente cuando aporten valor.

Ejemplo correcto:

"Calcula automáticamente el estado del inventario según el stock."

Ejemplo incorrecto:

"Variable x."

---

# 10. Frontend

El frontend debe mantener una apariencia profesional.

Debe parecer una aplicación empresarial moderna.

No utilizar estilos antiguos.

Preferencias:

- Diseño limpio.
- Sidebar.
- Dashboard.
- Tarjetas.
- Tablas modernas.
- Responsive.

---

# 11. Backend

Mantener una arquitectura organizada.

Separar:

- Modelos.
- Esquemas.
- Servicios.
- Rutas.

Evitar lógica duplicada.

---

# 12. Base de datos

Utilizar SQLite.

No migrar hacia otra base de datos sin autorización.

---

# 13. Docker

No modificar el Dockerfile sin explicar el motivo.

Si existe una optimización posible:

Explicarla antes de implementarla.

---

# 14. Terraform

No agregar recursos de Azure que no formen parte del alcance aprobado.

No incrementar costos innecesariamente.

Priorizar recursos gratuitos o de bajo costo.

---

# 15. Azure

No crear recursos adicionales sin autorización.

No eliminar recursos automáticamente.

No ejecutar acciones destructivas.

---

# 16. Git

Nunca ejecutar automáticamente:

- git push
- git merge
- git rebase
- git reset
- git clean

Esperar autorización.

---

# 17. Manejo de errores

Cuando ocurra un error:

No intentar resolver múltiples problemas al mismo tiempo.

Responder:

Problema encontrado.

Posibles causas.

Forma de validarlo.

Recomendación.

Esperar aprobación antes de aplicar cambios importantes.

---

# 18. Explicaciones técnicas

Al finalizar una tarea incluir:

## ¿Qué hicimos?

## ¿Por qué era necesario?

## ¿Cómo funciona?

## ¿Qué podría preguntar el profesor?

## Respuesta sugerida.

---

# 19. Resumen de tarea

Al finalizar incluir:

Archivos modificados.

Cambios realizados.

Pendientes.

Siguientes pasos.

---

# 20. Alcance

No implementar funcionalidades que no hayan sido aprobadas.

Evitar:

- Login
- Roles
- Facturación
- Pagos
- Reportes avanzados

---

# 21. Calidad

Priorizar:

Claridad.

Legibilidad.

Documentación.

Mantenibilidad.

---

# 22. Seguridad

No eliminar archivos.

No sobrescribir configuraciones.

No modificar secretos.

No modificar variables de entorno sin autorización.

---

# 23. Aprendizaje

Después de completar una fase incluir una breve explicación orientada al aprendizaje.

Debe permitir comprender:

- Qué se construyó.
- Qué tecnologías participaron.
- Cómo se relaciona con el objetivo del proyecto.

---

# 24. Exposición

Siempre que una tarea sea relevante para la exposición incluir:

Cómo explicar esta parte.

Qué conceptos mencionar.

Qué preguntas podrían surgir.

---

# 25. Regla principal

Ante cualquier duda:

Preguntar.

Nunca asumir.

Es preferible solicitar confirmación que realizar cambios incorrectos.