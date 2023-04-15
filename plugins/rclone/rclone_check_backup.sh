#!/bin/bash
domain_name=$1

last=$(echo $domain_name | awk -F"." '{print $1}')
last=$(echo $last | awk -F"-" '{print $1}')

if [ ${#last} > 12 ]; then
        last=${last:$i:10}
fi

custom_domain=$last

for i in `rclone listremotes`; do
    rclone ls $i | grep $custom_domain > /dev/null 2>&1
    if [[ $? -eq 0 ]]; then
        rclone ls $i | grep $custom_domain
        echo "files backup exist at remote *** $i ***"
    fi
done
