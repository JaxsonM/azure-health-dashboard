output "web_vm_public_ip" {
  description = "Public IP of the web server"
  value       = azurerm_public_ip.web.ip_address
}

output "web_vm_private_ip" {
  description = "Private IP of the web server"
  value       = azurerm_network_interface.web.private_ip_address
}

output "db_vm_private_ip" {
  description = "Private IP of the database server (no public IP)"
  value       = azurerm_network_interface.db.private_ip_address
}

output "resource_group" {
  description = "Resource group name"
  value       = azurerm_resource_group.main.name
}

output "ssh_web_command" {
  description = "SSH command to connect to web VM"
  value       = "ssh azureuser@${azurerm_public_ip.web.ip_address}"
}