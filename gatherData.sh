#!/bin/bash


timestamp=$(date +"%T") 
echo "Current time for EMERSON: $timestamp" &>>output.txt
speedtest-cli &>>output.txt
printf "\n" &>>output.txt

timestamp=$(date +"%T") 
echo "Current time for STEVEN: $timestamp" &>>output.txt
speedtest-cli &>>output.txt
printf "\n" &>>output.txt
