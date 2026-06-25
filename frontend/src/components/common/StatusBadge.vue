<script setup>
defineProps({
  status: {
    type: String,
    required: true
  }
})

function statusClass(status) {
  if (status === 'Disponible') return 'available'
  if (status === 'Bajo stock') return 'low'
  return 'empty'
}
</script>

<template>
  <span class="status-badge" :class="statusClass(status)">
    {{ status }}
  </span>
</template>
