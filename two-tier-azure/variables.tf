variable "location" {
  description = "Azure region"
  type        = string
  default     = "canadacentral"
}

variable "resource_group_name" {
  description = "Resource group for two-tier app"
  type        = string
  default     = "two-tier-rg"
}

variable "vm_size" {
  description = "Size for both VMs"
  type        = string
  default     = "Standard_D2s_v3"
}

variable "admin_username" {
  description = "Admin username for both VMs"
  type        = string
  default     = "azureuser"
}

variable "web_vm_name" {
  description = "Name of the web server VM"
  type        = string
  default     = "web-vm"
}

variable "db_vm_name" {
  description = "Name of the database VM"
  type        = string
  default     = "db-vm"
}