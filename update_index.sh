#!/bin/bash

source /home/wsa/searchienv/bin/activate

while [ 1 ] ; do
        ipython3 /home/wsa/searchie/searchie/manage.py update_index
        sleep 15
done
