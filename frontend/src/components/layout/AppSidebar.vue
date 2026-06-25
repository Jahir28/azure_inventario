<script setup>
import { BarChart3, Boxes, Cloud, Package } from 'lucide-vue-next'

defineProps({
  activeView: {
    type: String,
    required: true
  }
})

defineEmits(['change-view'])
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <span class="brand-mark">
        <Cloud :size="22" />
      </span>
      <span>
        Azure Inventario
        <small>CI/CD demo</small>
      </span>
    </div>
    <div class="sidebar-section">Operación</div>
    <button
      class="nav-button"
      :class="{ active: activeView === 'dashboard' }"
      type="button"
      @click="$emit('change-view', 'dashboard')"
    >
      <BarChart3 :size="18" />
      Dashboard
    </button>
    <button
      class="nav-button"
      :class="{ active: activeView === 'products' }"
      type="button"
      @click="$emit('change-view', 'products')"
    >
      <Package :size="18" />
      Productos
    </button>
    <div class="sidebar-footer">
      <Boxes :size="18" />
      <span>FastAPI + Vue + Azure</span>
    </div>
  </aside>
</template>
