<script setup>
import { Boxes, CheckCircle2, CircleDollarSign, PackageX, TriangleAlert } from 'lucide-vue-next'
import InventoryChart from '../components/dashboard/InventoryChart.vue'
import MetricCard from '../components/dashboard/MetricCard.vue'
import SystemStatus from '../components/dashboard/SystemStatus.vue'
import ProductTable from '../components/products/ProductTable.vue'

defineProps({
  metrics: {
    type: Object,
    required: true
  },
  products: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    required: true
  },
  hasError: {
    type: Boolean,
    required: true
  }
})

function formatCurrency(value) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(value)
}
</script>

<template>
  <section class="content-stack">
    <SystemStatus :loading="loading" :has-error="hasError" />

    <div class="metrics-grid">
      <MetricCard label="Total productos" :value="metrics.total_products" :icon="Boxes" tone="blue" />
      <MetricCard label="Disponibles" :value="metrics.available_products" :icon="CheckCircle2" tone="green" />
      <MetricCard label="Bajo stock" :value="metrics.low_stock_products" :icon="TriangleAlert" tone="yellow" />
      <MetricCard label="Agotados" :value="metrics.out_of_stock_products" :icon="PackageX" tone="red" />
      <MetricCard label="Valor estimado" :value="formatCurrency(metrics.inventory_value)" :icon="CircleDollarSign" tone="slate" />
    </div>

    <div class="dashboard-grid">
      <InventoryChart :metrics="metrics" />
      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Productos registrados</h2>
            <p>{{ loading ? 'Cargando inventario' : `${products.length} productos en sistema` }}</p>
          </div>
        </div>
        <ProductTable :products="products" :loading="loading" readonly />
      </section>
    </div>
  </section>
</template>
