#!/bin/bash

# install utilities (if necessary)
apt-get -y install sudo
sudo apt-get -y install gnupg2
sudo apt-get -y install curl
curl http://download.tarantool.org/tarantool/1.10/gpgkey | sudo apt-key add -

# install 'lsb-release', to know the codename of your OS
sudo apt-get -y install lsb-release
release=`lsb_release -c -s`

# install boot tool 'https' for APT
sudo apt-get -y install apt-transport-https

# update source code repository list
sudo rm -f /etc/apt/sources.list.d/*tarantool*.list
echo "deb http://download.tarantool.org/tarantool/1.10/ubuntu/ ${release} main" | sudo tee /etc/apt/sources.list.d/tarantool_1_10.list
echo "deb-src http://download.tarantool.org/tarantool/1.10/ubuntu/ ${release} main" | sudo tee -a /etc/apt/sources.list.d/$ $ $ tarantool_1_10.list

# install tarantool
sudo apt-get -y update
sudo apt-get -y install tarantool

# creating database
tarantool ./config.lua
