#!/bin/bash

if [ "$1" == "" ]

then
echo "You forgot IP address!"
echo "Syntax: ./ipsweep.sh"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

fi