#!/bin/bash
echo 'backing up...'
docker exec -t autograder_db pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
echo 'backup complete.'
