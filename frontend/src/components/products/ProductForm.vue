<script setup>
import { reactive, ref, watch } from 'vue'
import Button from 'primevue/button'
import InputNumber from 'primevue/inputnumber'
import InputText from 'primevue/inputtext'
import { Save, X } from 'lucide-vue-next'

const props = defineProps({
  selectedProduct: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['cancel', 'submit'])

const form = reactive({
  name: '',
  category: '',
  price: 0,
  quantity: 0
})

const touched = ref(false)

const errors = reactive({
  name: '',
  category: '',
  price: '',
  quantity: ''
})

watch(
  () => props.selectedProduct,
  (product) => {
    form.name = product?.name || ''
    form.category = product?.category || ''
    form.price = product?.price || 0
    form.quantity = product?.quantity || 0
    touched.value = false
    clearErrors()
  },
  { immediate: true }
)

function clearErrors() {
  errors.name = ''
  errors.category = ''
  errors.price = ''
  errors.quantity = ''
}

function validateForm() {
  clearErrors()

  if (form.name.trim().length < 2) {
    errors.name = 'Ingresa al menos 2 caracteres.'
  }

  if (form.category.trim().length < 2) {
    errors.category = 'Ingresa una categoría válida.'
  }

  if (form.price === null || Number(form.price) < 0) {
    errors.price = 'El precio no puede ser negativo.'
  }

  if (form.quantity === null || Number(form.quantity) < 0) {
    errors.quantity = 'El stock no puede ser negativo.'
  }

  return !errors.name && !errors.category && !errors.price && !errors.quantity
}

function submitForm() {
  touched.value = true

  if (!validateForm()) {
    return
  }

  emit('submit', {
    name: form.name.trim(),
    category: form.category.trim(),
    price: Number(form.price),
    quantity: Number(form.quantity)
  })

  form.name = ''
  form.category = ''
  form.price = 0
  form.quantity = 0
  touched.value = false
  clearErrors()
}
</script>

<template>
  <form class="product-form" @submit.prevent="submitForm">
    <div class="form-field">
      <label for="product-name">Producto</label>
      <InputText id="product-name" v-model="form.name" :class="{ invalid: touched && errors.name }" placeholder="Laptop empresarial" required />
      <small v-if="touched && errors.name" class="field-error">{{ errors.name }}</small>
    </div>
    <div class="form-field">
      <label for="product-category">Categoría</label>
      <InputText id="product-category" v-model="form.category" :class="{ invalid: touched && errors.category }" placeholder="Computadoras" required />
      <small v-if="touched && errors.category" class="field-error">{{ errors.category }}</small>
    </div>
    <div class="form-field">
      <label for="product-price-input">Precio</label>
      <InputNumber
        v-model="form.price"
        :class="{ invalid: touched && errors.price }"
        :min="0"
        :min-fraction-digits="2"
        :max-fraction-digits="2"
        input-id="product-price-input"
      />
      <small v-if="touched && errors.price" class="field-error">{{ errors.price }}</small>
    </div>
    <div class="form-field">
      <label for="product-quantity-input">Stock</label>
      <InputNumber id="product-quantity" v-model="form.quantity" :class="{ invalid: touched && errors.quantity }" :min="0" input-id="product-quantity-input" />
      <small v-if="touched && errors.quantity" class="field-error">{{ errors.quantity }}</small>
    </div>
    <Button class="primary-button" type="submit" :aria-label="selectedProduct ? 'Guardar cambios' : 'Crear producto'">
      <Save :size="16" />
      <span>{{ selectedProduct ? 'Guardar' : 'Crear' }}</span>
    </Button>
    <Button
      v-if="selectedProduct"
      class="secondary-button"
      type="button"
      @click="$emit('cancel')"
    >
      <X :size="16" />
      Cancelar
    </Button>
  </form>
</template>
