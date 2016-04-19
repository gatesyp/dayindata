#!/bin/bash


timestamp=$(date +"%T") 
echo "Current time: $timestamp" &>>output.txt
speedtest-cli &>>output.txt
printf "\n" &>>output.txt
