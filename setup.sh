#!/bin/bash

# Update packages:
sudo apt-get update
sudo apt-get upgrade

# Install Pre-requisites:
sudo apt-get install git make autoconf libltdl-dev libusb-dev libexif-dev libpopt-dev libxml2-dev libjpeg-dev libgd-dev gettext autopoint

# Clone and compile libgphoto2:
cd ~
git clone https://github.com/gphoto/libgphoto2.git
cd ~/libgphoto2
autoreconf --install --symlink
./configure
make
sudo make install

# Clone and compile ghoto2:
cd ~
git clone https://github.com/gphoto/gphoto2.git
cd ~/gphoto2
autoreconf --install --symlink
./configure
make
sudo make install

# Refresh the config cache:
sudo ldconfig
/usr/local/lib/libgphoto2/print-camera-list udev-rules version 201 group plugdev mode 0660 | sudo tee /etc/udev/rules.d/90-libgphoto2.rules
/usr/local/lib/libgphoto2/print-camera-list hwdb | sudo tee /etc/udev/hwdb.d/20-gphoto.hwdb

# Install pip:

# Install necessary python packages:
sudo apt-get install python3-pip
sudo pip install opencv-python sh