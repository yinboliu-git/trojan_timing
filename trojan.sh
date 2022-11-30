#! /bin/bash

cur_date="2`date +%m%d`"
echo -e "${cur_date}" | trojan port
