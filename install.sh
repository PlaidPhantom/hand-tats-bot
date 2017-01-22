#!/bin/bash

INSTALLDIR="/opt/handtats/"
SYSTEMD_DIR="/etc/systemd/system/"

echo "Creating service user..."
adduser --system handtats

echo "Creating install directory $INSTALLDIR..."
mkdir $INSTALLDIR
cp ./* $INSTALLDIR
cd $INSTALLDIR

echo "settings permissions..."
chown -R handtats $INSTALLDIR
chmod +x run.sh

make configure

echo "Creating service definition in $SYSTEMD_DIR..."
cp tats.service $SYSTEMD_DIR

systemctl enable tats

echo "Hand Tats bot service has been set up.  Make sure to create the "
echo "secrets.json file and set appropriate permissions, then start the service"
echo "using the command `systemctl start tats`"
