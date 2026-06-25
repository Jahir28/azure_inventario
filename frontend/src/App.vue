<script setup>
import { computed, ref } from 'vue'
import ConfirmDialog from './components/common/ConfirmDialog.vue'
import ToastStack from './components/common/ToastStack.vue'
import AppSidebar from './components/layout/AppSidebar.vue'
import AppNavbar from './components/layout/AppNavbar.vue'
import DashboardView from './views/DashboardView.vue'
import ProductsView from './views/ProductsView.vue'
import { useInventory } from './composables/useInventory'

const activeView = ref('dashboard')
const {
  error,
  loading,
  metrics,
  products,
  loadInventory,
  removeProduct,
  saveProduct
} = useInventory()

const pageTitle = computed(() => (
  activeView.value === 'dashboard' ? 'Dashboard de inventario' : 'Gestión de productos'
))

const toasts = ref([])
const productToDelete = ref(null)

function pushToast(type, title, message) {
  const id = crypto.randomUUID()
  toasts.value.push({ id, type, title, message })
  window.setTimeout(() => dismissToast(id), 4200)
}

function dismissToast(id) {
  toasts.value = toasts.value.filter((toast) => toast.id !== id)
}

async function handleRefresh() {
  const success = await loadInventory()
  if (!success) {
    pushToast('error', 'API no disponible', 'No se pudieron cargar productos y métricas.')
  }
}

async function handleSave(product, selectedProduct) {
  const success = await saveProduct(product, selectedProduct)
  if (success) {
    pushToast(
      'success',
      selectedProduct ? 'Producto actualizado' : 'Producto creado',
      selectedProduct ? 'Los cambios se guardaron correctamente.' : 'El producto fue agregado al inventario.'
    )
    return
  }

  pushToast('error', 'No se pudo guardar', 'Revisa los datos o confirma que la API esté activa.')
}

function requestDelete(product) {
  productToDelete.value = product
}

async function confirmDelete() {
  if (!productToDelete.value) return

  const productName = productToDelete.value.name
  const success = await removeProduct(productToDelete.value.id)
  productToDelete.value = null

  if (success) {
    pushToast('success', 'Producto eliminado', `${productName} fue eliminado del inventario.`)
    return
  }

  pushToast('error', 'No se pudo eliminar', 'La petición al backend no se completó.')
}
</script>

<template>
  <div class="app-shell">
    <AppSidebar :active-view="activeView" @change-view="activeView = $event" />
    <main class="main-content">
      <AppNavbar :title="pageTitle" :loading="loading" @refresh="handleRefresh" />
      <div v-if="error" class="alert-banner">
        {{ error }}
      </div>
      <DashboardView
        v-if="activeView === 'dashboard'"
        :metrics="metrics"
        :products="products"
        :loading="loading"
        :has-error="Boolean(error)"
      />
      <ProductsView
        v-else
        :products="products"
        :loading="loading"
        @delete="requestDelete"
        @save="handleSave"
      />
    </main>
    <ToastStack :toasts="toasts" @dismiss="dismissToast" />
    <ConfirmDialog
      :visible="Boolean(productToDelete)"
      :product="productToDelete"
      @cancel="productToDelete = null"
      @confirm="confirmDelete"
    />
  </div>
</template>
