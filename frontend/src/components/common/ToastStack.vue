<script setup>
import { AlertCircle, CheckCircle2, Info, X } from 'lucide-vue-next'

defineProps({
  toasts: {
    type: Array,
    required: true
  }
})

defineEmits(['dismiss'])

function iconFor(type) {
  if (type === 'success') return CheckCircle2
  if (type === 'error') return AlertCircle
  return Info
}
</script>

<template>
  <div class="toast-stack" aria-live="polite">
    <article v-for="toast in toasts" :key="toast.id" class="toast" :class="`toast-${toast.type}`">
      <component :is="iconFor(toast.type)" :size="19" />
      <div>
        <strong>{{ toast.title }}</strong>
        <p>{{ toast.message }}</p>
      </div>
      <button class="toast-close" type="button" aria-label="Cerrar mensaje" @click="$emit('dismiss', toast.id)">
        <X :size="16" />
      </button>
    </article>
  </div>
</template>
