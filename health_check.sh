#!/bin/bash

LOGFILE="/var/log/health_check.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

DISK=$(df -h / | awk 'NR==2 {print $5}')
MEMORY=$(free -m | awk 'NR==2 {printf "%.1f%%", $3/$2*100}')
LOAD=$(uptime | awk -F'load average:' '{print $2}' | xargs)
NGINX=$(systemctl is-active nginx)

echo "[$TIMESTAMP] Disk: $DISK | Memory: $MEMORY | Load: $LOAD | Nginx: $NGINX" >> $LOGFILE
