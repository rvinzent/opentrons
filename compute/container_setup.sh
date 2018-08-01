#! /usr/bin/env bash

# Clean up opentrons package dir if it's a first start of a new container
touch /data/id
previous_id=$(cat /data/id)
current_id=$CONTAINER_ID
if [ "$previous_id" != "$current_id" ] ; then
    echo 'First start of a new container. Deleting local Opentrons installation'
    rm -rf /data/packages/usr/local/lib/python3.6/site-packages/opentrons*
    rm -rf /data/packages/usr/local/lib/python3.6/site-packages/ot2serverlib*
    rm -rf /data/packages/usr/local/lib/python3.6/site-packages/otupdate*
    python -c "import opentrons; opentrons.provision()"
    echo "$current_id" > /data/id
fi

mkdir -p /run/nginx
