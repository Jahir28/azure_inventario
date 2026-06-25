const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    },
    ...options
  })

  if (!response.ok) {
    const message = await response.text()
    throw new Error(message || `API request failed with status ${response.status}`)
  }

  if (response.status === 204) {
    return null
  }

  return response.json()
}

export function getProducts() {
  return request('/api/products/')
}

export function getMetrics() {
  return request('/api/products/metrics')
}

export function createProduct(product) {
  return request('/api/products/', {
    method: 'POST',
    body: JSON.stringify(product)
  })
}

export function updateProduct(id, product) {
  return request(`/api/products/${id}`, {
    method: 'PUT',
    body: JSON.stringify(product)
  })
}

export function deleteProduct(id) {
  return request(`/api/products/${id}`, {
    method: 'DELETE'
  })
}

export { API_URL }
