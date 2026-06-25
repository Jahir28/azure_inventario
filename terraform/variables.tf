variable "location" {
  description = "Azure region where resources will be created."
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Base name for Azure resources. Use lowercase letters, numbers and hyphens."
  type        = string
  default     = "azure-inventario"
}

variable "environment" {
  description = "Environment name used in resource tags."
  type        = string
  default     = "dev"
}

variable "address_space" {
  description = "Address space for the virtual network."
  type        = list(string)
  default     = ["10.20.0.0/16"]
}

variable "subnet_address_prefixes" {
  description = "Address prefixes for the Azure Container Instances subnet."
  type        = list(string)
  default     = ["10.20.1.0/24"]
}

variable "deploy_container_group" {
  description = "Controls whether the Azure Container Group is created."
  type        = bool
  default     = false
}

variable "backend_image" {
  description = "Full backend Docker image stored in Azure Container Registry."
  type        = string
  default     = ""
}

variable "frontend_image" {
  description = "Full frontend Docker image stored in Azure Container Registry."
  type        = string
  default     = ""
}

variable "backend_port" {
  description = "Public backend port."
  type        = number
  default     = 8000
}

variable "frontend_port" {
  description = "Public frontend port."
  type        = number
  default     = 80
}

variable "container_cpu" {
  description = "CPU assigned to each container."
  type        = number
  default     = 0.5
}

variable "container_memory" {
  description = "Memory in GB assigned to each container."
  type        = number
  default     = 1.0
}
