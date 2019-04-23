#!/bin/bash
IFS=$'\n'; while read -r line; do mpc search any \"$line\" |head -n 1; done < out 
