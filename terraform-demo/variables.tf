variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "demo-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "canadacentral"
}

variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
  default     = "demo-vm"
}

variable "vm_size" {
  description = "Size of the virtual machine"
  type        = string
  default     = "Standard_B2als_v2"
}