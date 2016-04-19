$!/bin/bash
#chmod u+x <filename>

sudo apt-get install pip
sudo pip install speedtest-cli
# edit path variable 
CONFIG=/home/user/config.inc
API=/home/user/api.txt

sed -e "$API" >> $CONFIG

sudo apt-get install arp-scan

