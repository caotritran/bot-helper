#!/bin/bash
domain_name=$1

last=$(echo $domain_name | awk -F"." '{print $1}')
last=$(echo $last | awk -F"-" '{print $1}')

if [ ${#last} > 12 ]; then
        last=${last:$i:10}
fi

custom_domain=$last
found=false


for i in `rclone listremotes --config /opt/rclone.conf`; do
    rclone ls $i --config /opt/rclone.conf | grep $custom_domain > /dev/null 2>&1
    if [[ $? -eq 0 ]]; then
        rclone ls $i --config /opt/rclone.conf | grep $custom_domain
        echo "files backup exist at remote **$i**"
        echo "==================================="
        found=true
    fi
done

if [ "$found" = false ]; then
    echo "Not found: Files backup does not exist for domain $custom_domain"
fi

