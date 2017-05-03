#!/bin/bash

INSTALLDIR=$(pwd)
SYSTEMD_DIR="/etc/systemd/system"

echo "Creating service user..."
adduser --system handtats

echo "settings permissions..."
chown -R handtats .
chmod +x run.sh

make configure

echo "Creating service definition in $SYSTEMD_DIR..."
tee $SYSTEMD_DIR/handtats.service <<SERVICE
[Unit]
Description=Hand_Tats bot

[Service]
Type=simple
WorkingDirectory=$INSTALLDIR
ExecStart=$INSTALLDIR/run.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target
SERVICE

systemctl enable tats

echo "Hand Tats bot service has been set up.  Make sure to create the "
echo "secrets.json file and set appropriate permissions, then start the service"
echo "using the command `systemctl start tats`"
