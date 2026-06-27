import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) return undefined

          if (id.includes('echarts')) return undefined
          if (id.includes('primevue')) return 'primevue'
          if (id.includes('lucide-vue-next')) return 'icons'

          return 'vendor'
        }
      }
    }
  },
  server: {
    port: 5173
  }
})
