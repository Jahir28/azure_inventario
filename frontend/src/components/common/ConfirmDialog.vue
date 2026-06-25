<script setup>
import { AlertTriangle } from 'lucide-vue-next'

defineProps({
  visible: {
    type: Boolean,
    required: true
  },
  product: {
    type: Object,
    default: null
  }
})

defineEmits(['cancel', 'confirm'])
</script>

<template>
  <Teleport to="body">
    <div v-if="visible" class="confirm-backdrop">
      <section class="confirm-dialog" role="dialog" aria-modal="true" aria-labelledby="confirm-title">
        <div class="confirm-icon">
          <AlertTriangle :size="24" />
        </div>
        <div>
          <h2 id="confirm-title">Eliminar producto</h2>
          <p>
            Esta acción eliminará
            <strong>{{ product?.name }}</strong>
            del inventario.
          </p>
        </div>
        <div class="confirm-actions">
          <button class="secondary-button" type="button" @click="$emit('cancel')">
            Cancelar
          </button>
          <button class="danger-solid-button" type="button" @click="$emit('confirm')">
            Eliminar
          </button>
        </div>
      </section>
    </div>
  </Teleport>
</template>
