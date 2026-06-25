<script setup>
import { ref } from 'vue'
import ProductForm from '../components/products/ProductForm.vue'
import ProductTable from '../components/products/ProductTable.vue'

defineProps({
  products: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['delete', 'save'])
const selectedProduct = ref(null)

function handleSave(product) {
  emit('save', product, selectedProduct.value)
  selectedProduct.value = null
}

function handleEdit(product) {
  selectedProduct.value = product
}

function handleDelete(product) {
  emit('delete', product)
}
</script>

<template>
  <section class="products-layout">
    <section class="panel form-panel">
      <div class="panel-header">
        <div>
          <h2>{{ selectedProduct ? 'Editar producto' : 'Nuevo producto' }}</h2>
          <p>{{ selectedProduct ? 'Actualiza la información del inventario' : 'Registra artículos con precio, categoría y stock' }}</p>
        </div>
      </div>
      <ProductForm
        :selected-product="selectedProduct"
        @cancel="selectedProduct = null"
        @submit="handleSave"
      />
    </section>

    <section class="panel">
      <div class="panel-header">
        <div>
          <h2>Catálogo de productos</h2>
          <p>{{ loading ? 'Sincronizando datos' : `${products.length} productos registrados` }}</p>
        </div>
      </div>
      <ProductTable
        :products="products"
        :loading="loading"
        @delete="handleDelete"
        @edit="handleEdit"
      />
    </section>
  </section>
</template>
