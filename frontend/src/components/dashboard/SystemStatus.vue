<script setup>
import { CheckCircle2, Database, PackageCheck, Server } from 'lucide-vue-next'

defineProps({
  loading: {
    type: Boolean,
    required: true
  },
  hasError: {
    type: Boolean,
    required: true
  }
})

const items = [
  {
    label: 'API',
    description: 'FastAPI respondiendo',
    icon: Server
  },
  {
    label: 'Base de datos',
    description: 'SQLite inicializada',
    icon: Database
  },
  {
    label: 'Inventario',
    description: 'Métricas sincronizadas',
    icon: PackageCheck
  }
]
</script>

<template>
  <section class="system-status-panel">
    <div class="system-status-copy">
      <span class="eyebrow">Estado del sistema</span>
      <h2>{{ hasError ? 'Revisión requerida' : 'Servicios operativos' }}</h2>
      <p>{{ loading ? 'Actualizando estado del inventario' : 'Componentes principales listos para la demostración' }}</p>
    </div>
    <div class="system-status-grid">
      <article v-for="item in items" :key="item.label" class="system-status-card" :class="{ muted: hasError }">
        <component :is="item.icon" :size="22" />
        <div>
          <strong>{{ item.label }}</strong>
          <span>{{ hasError ? 'Sin confirmar' : item.description }}</span>
        </div>
        <CheckCircle2 v-if="!hasError" class="status-check" :size="18" />
      </article>
    </div>
  </section>
</template>
