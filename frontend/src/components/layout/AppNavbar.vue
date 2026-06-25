<script setup>
import { RefreshCw } from 'lucide-vue-next'

defineProps({
  title: {
    type: String,
    required: true
  },
  loading: {
    type: Boolean,
    required: true
  }
})

defineEmits(['refresh'])
</script>

<template>
  <header class="navbar">
    <div>
      <span class="eyebrow">Azure Inventory</span>
      <h1>{{ title }}</h1>
    </div>
    <button class="icon-text-button" type="button" :disabled="loading" @click="$emit('refresh')">
      <RefreshCw :size="17" :class="{ spinning: loading }" />
      Actualizar
    </button>
  </header>
</template>
