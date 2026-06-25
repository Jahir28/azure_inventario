import { onMounted, ref } from 'vue'
import { createProduct, deleteProduct, getMetrics, getProducts, updateProduct } from '../services/api'

const emptyMetrics = {
  total_products: 0,
  available_products: 0,
  low_stock_products: 0,
  out_of_stock_products: 0,
  inventory_value: 0
}

export function useInventory() {
  const loading = ref(false)
  const error = ref('')
  const products = ref([])
  const metrics = ref({ ...emptyMetrics })

  async function loadInventory() {
    loading.value = true
    error.value = ''

    try {
      const [productList, inventoryMetrics] = await Promise.all([
        getProducts(),
        getMetrics()
      ])

      products.value = productList
      metrics.value = inventoryMetrics
    } catch (requestError) {
      error.value = 'No se pudo conectar con la API del inventario.'
      return false
    } finally {
      loading.value = false
    }

    return true
  }

  async function saveProduct(product, selectedProduct = null) {
    loading.value = true
    error.value = ''

    try {
      if (selectedProduct) {
        await updateProduct(selectedProduct.id, product)
      } else {
        await createProduct(product)
      }

      await loadInventory()
    } catch (requestError) {
      error.value = 'No se pudo guardar el producto.'
      return false
    } finally {
      loading.value = false
    }

    return true
  }

  async function removeProduct(id) {
    loading.value = true
    error.value = ''

    try {
      await deleteProduct(id)
      await loadInventory()
    } catch (requestError) {
      error.value = 'No se pudo eliminar el producto.'
      return false
    } finally {
      loading.value = false
    }

    return true
  }

  onMounted(loadInventory)

  return {
    error,
    loading,
    metrics,
    products,
    loadInventory,
    removeProduct,
    saveProduct
  }
}
