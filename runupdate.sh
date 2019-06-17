#!/bin/bash

d2=$(cat /opt/demoupdate/demoupdate2/ver.md)
d1=$(cat /home/pi/demoapp/ver.md)

if [ $d2 -gt $d1 ]; then
	echo "begin update..."
	unzip -o /opt/demoupdate/demoupdate2/ud.zip -d /opt/demoupdate/demoupdate2/
	mv /home/pi/demoapp/demoapp /home/pi/demoapp/demoapp_bk
        cp /opt/demoupdate/demoupdate2/demoapp /home/pi/demoapp/
        mv /home/pi/demoapp/ver.md /home/pi/demoapp/ver_bk.md
        cp /opt/demoupdate/demoupdate2/ver.md /home/pi/demoapp	
	echo "update finish"
	sudo reboot
fi


