<script setup>
import Button from 'primevue/button'
import Column from 'primevue/column'
import DataTable from 'primevue/datatable'
import { Pencil, Trash2 } from 'lucide-vue-next'
import EmptyState from '../common/EmptyState.vue'
import StatusBadge from '../common/StatusBadge.vue'

defineProps({
  products: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  },
  readonly: {
    type: Boolean,
    default: false
  }
})

defineEmits(['delete', 'edit'])
</script>

<template>
  <DataTable
    :value="products"
    :loading="loading"
    data-key="id"
    striped-rows
    responsive-layout="scroll"
    class="inventory-table"
  >
    <template #empty>
      <EmptyState
        title="Sin productos registrados"
        message="Crea el primer producto para visualizar métricas del inventario."
      />
    </template>

    <Column field="name" header="Producto" sortable class="product-name-column">
      <template #body="{ data }">
        <strong>{{ data.name }}</strong>
      </template>
    </Column>
    <Column field="category" header="Categoría" sortable class="product-category-column" />
    <Column field="price" header="Precio" sortable class="product-price-column">
      <template #body="{ data }">
        ${{ Number(data.price).toFixed(2) }}
      </template>
    </Column>
    <Column field="quantity" header="Stock" sortable class="product-stock-column" />
    <Column field="status" header="Estado" sortable class="product-status-column">
      <template #body="{ data }">
        <StatusBadge :status="data.status" />
      </template>
    </Column>
    <Column v-if="!readonly" header="Acciones" class="product-actions-column">
      <template #body="{ data }">
        <div class="actions">
          <Button class="table-action-button" type="button" :aria-label="`Editar ${data.name}`" @click="$emit('edit', data)">
            <Pencil :size="16" />
          </Button>
          <Button class="table-danger-button" type="button" :aria-label="`Eliminar ${data.name}`" @click="$emit('delete', data)">
            <Trash2 :size="16" />
          </Button>
        </div>
      </template>
    </Column>
  </DataTable>
</template>
