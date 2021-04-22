#!/usr/bin/bash

nfiles=200
if [[ $1 == "" ]]; then
    echo You need to specify a output path
    exit 1
fi
for ((i=0;i<$nfiles;i++))
do 
	python ./src/generate_sinogram.py "$1/streaking.${i}.${HOSTNAME}" 100 &
done
