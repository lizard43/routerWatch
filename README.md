# routerWatch
Router reboot with Raspberry Pi and Python.

My Westell DSL router locks up several times a day. Frontier won't do anything except send me a new one. I now have 4 routers and all behave the same. If I pull the power plug for 10 seconds, the router reboots and I have intenet access for a few more hours.

These Python scripts and approach are based on work by others:
- https://github.com/StephenWetzel/routerReboot
- https://github.com/dough10/rebooter

Clone this repo onto your Raspberry Pi. I'm using an older Pi 2 because I don't need a faster Pi 3 but I do want a CAT 5 wire into my router.

Edit the crontab so that the script runs at reboot
- crontab -e
- @reboot /home/pi/routerWatch/routerWatch.sh

The routerWatch.sh file writes log messages to /tmp/routerWatch.txt 
It will overwrite this file at each Pi reboot. If your SD card is low on space, this file could grow unbounded.

I'm using a cheap relay from eBay to rest the routers power. I'm tapping into the router's 9v power line so I'm not worried about mains power.

