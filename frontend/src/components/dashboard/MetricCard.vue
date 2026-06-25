<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: {
    type: String,
    required: true
  },
  value: {
    type: [String, Number],
    required: true
  },
  tone: {
    type: String,
    default: 'blue'
  },
  icon: {
    type: Object,
    required: true
  }
})

const isLongValue = computed(() => String(props.value).length >= 10)
</script>

<template>
  <article class="metric-card" :class="`tone-${tone}`">
    <div class="metric-icon">
      <component :is="icon" :size="22" />
    </div>
    <div>
      <div class="metric-label">{{ label }}</div>
      <div class="metric-value" :class="{ compact: isLongValue }">{{ value }}</div>
    </div>
  </article>
</template>
