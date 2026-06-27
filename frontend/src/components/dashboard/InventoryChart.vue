<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'

const props = defineProps({
  metrics: {
    type: Object,
    required: true
  }
})

const chartElement = ref(null)
let echarts = null
let chart = null

const chartData = computed(() => [
  { value: props.metrics.available_products, name: 'Disponible' },
  { value: props.metrics.low_stock_products, name: 'Bajo stock' },
  { value: props.metrics.out_of_stock_products, name: 'Agotado' }
])

async function loadEcharts() {
  if (!echarts) {
    // Solo se cargan los módulos necesarios para el gráfico de pastel.
    const [
      { init, use },
      { PieChart },
      { LegendComponent, TooltipComponent },
      { CanvasRenderer }
    ] = await Promise.all([
      import('echarts/core'),
      import('echarts/charts'),
      import('echarts/components'),
      import('echarts/renderers')
    ])

    use([PieChart, LegendComponent, TooltipComponent, CanvasRenderer])
    echarts = { init }
  }
}

async function renderChart() {
  if (!chartElement.value) return

  await loadEcharts()

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
  await renderChart()
  window.addEventListener('resize', resizeChart)
})

watch(chartData, () => {
  void renderChart()
}, { deep: true })

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
