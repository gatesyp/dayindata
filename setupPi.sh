$!/bin/bash
#chmod u+x <filename>

sudo apt-get install pip
sudo pip install speedtest-cli
sudo apt-get install arp-scan
# edit path variable 
CONFIG=/home/user/config.inc
API=/home/user/api.txt

sed -e "$API" >> $CONFIG

*/15 * * * * pi /home/pi/dayindata/<arp/speedtestscripts>.sh
