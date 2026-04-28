output "public_ip_address" {
  description = "The public IP address of the VM"
  value       = azurerm_public_ip.demo.ip_address
}

output "resource_group_name" {
  description = "The resource group name"
  value       = azurerm_resource_group.demo.name
}

output "vm_name" {
  description = "The VM name"
  value       = azurerm_linux_virtual_machine.demo.name
}