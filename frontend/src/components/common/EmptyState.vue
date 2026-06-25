<script setup>
import { PackageOpen } from 'lucide-vue-next'

defineProps({
  title: {
    type: String,
    required: true
  },
  message: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="empty-state">
    <PackageOpen :size="36" />
    <h3>{{ title }}</h3>
    <p>{{ message }}</p>
  </div>
</template>
