#!/bin/bash

INSTALLDIR="/opt/handtats/"
SYSTEMD_DIR="/usr/local/systemd/system/"

echo "Creating service user..."
adduser -r handtats

echo "Creating install directory $INSTALLDIR..."
mkdir $INSTALLDIR
cp ./* $INSTALLDIR
cd $INSTALLDIR

chown -R handtats $INSTALLDIR
chmod +x run.sh

make configure

cp tats.service $SYSTEMD_DIR
systemctl enable tats
