#!/bin/bash
echo 'robz' | sudo -S mount -t drvfs '\\s14\UP2DATA\Files' /mnt/s
echo 'robz' | sudo -S mount -t drvfs '\\capdc01\sistemas\Advisory Backup\Dados de Mercado Comum\Dados Batatais' /mnt/n
#visudo