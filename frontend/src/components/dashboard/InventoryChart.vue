<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  metrics: {
    type: Object,
    required: true
  }
})

const chartElement = ref(null)
let chart = null

const chartData = computed(() => [
  { value: props.metrics.available_products, name: 'Disponible' },
  { value: props.metrics.low_stock_products, name: 'Bajo stock' },
  { value: props.metrics.out_of_stock_products, name: 'Agotado' }
])

function renderChart() {
  if (!chartElement.value) return

  if (!chart) {
    chart = echarts.init(chartElement.value)
  }

  chart.setOption({
    color: ['#0078d4', '#f2c94c', '#d13438'],
    tooltip: {
      trigger: 'item'
    },
    legend: {
      bottom: 0,
      icon: 'circle',
      textStyle: {
        color: '#536579'
      }
    },
    series: [
      {
        name: 'Estado',
        type: 'pie',
        radius: ['58%', '78%'],
        center: ['50%', '45%'],
        avoidLabelOverlap: true,
        label: {
          formatter: '{b}',
          color: '#24364b'
        },
        data: chartData.value
      }
    ]
  })
}

function resizeChart() {
  chart?.resize()
}

onMounted(async () => {
  await nextTick()
  renderChart()
  window.addEventListener('resize', resizeChart)
})

watch(chartData, renderChart, { deep: true })

onBeforeUnmount(() => {
  window.removeEventListener('resize', resizeChart)
  chart?.dispose()
})
</script>

<template>
  <section class="panel chart-panel">
    <div class="panel-header">
      <div>
        <h2>Estado del inventario</h2>
        <p>Distribución por disponibilidad de stock</p>
      </div>
    </div>
    <div ref="chartElement" class="inventory-chart"></div>
  </section>
</template>
