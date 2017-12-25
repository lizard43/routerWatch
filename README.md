# Router reboot with Raspberry Pi and Python.

My Westell DSL router locks up several times a day. Frontier customer service isn't very helpful and they end up just sending me a new router instead of helping. I now have 4 routers and all behave the same. If I pull the power plug for 10 seconds, the router reboots and then I have intenet access for a few more hours until it hangs yet again.

My solution is now to use a cheap Rasperry Pi and a relay. The Pi runs a Python script that watches for internet connectivity to drop. The Pi will toggle the normally closed relay for 10 seconds (which cuts power to the router). 

| <img src="https://github.com/lizard43/routerWatch/blob/master/images/beast.png" width="600" /> |
|-|

These Python scripts and approach are based on work by others:
- https://github.com/StephenWetzel/routerReboot
- https://github.com/dough10/rebooter

Clone this repo onto your Raspberry Pi. I'm using an older Pi 2 because I don't need a faster Pi 3 but I do want a CAT 5 wire into my router.
- git clone https://github.com/lizard43/routerWatch.git

Edit the Pi's crontab so that the main Python script runs at reboot:
- crontab -e
- at bottom, add this line:
    - @reboot /home/pi/routerWatch/routerWatch.sh
- ctrl-o to write file and press enter
- ctrl-x to exit editor

The routerWatch.sh file writes log messages to /tmp/routerWatch.txt 
It will overwrite this file at each Pi reboot. If your SD card is low on space, this file could grow unbounded.

I'm using a cheap relay from eBay to rest the routers power. I'm tapping into the router's 12v power line so I'm not worried about mains power.

| Relay Pin | Pi Pin | Wire Color |
| --- | --- | --- |
| VDC | Pin 1 - 3V | Red |
| GND | Pin 6 - GND | Black |
| IN | Pin 16 - GPIO23 | Green |

| <img src="https://github.com/lizard43/routerWatch/blob/master/images/Raspberry-Pi-GPIO.2.png" width="800" /> |
|-|

I cut into the power supply's positive line and that is what will be toggled by the normally closed relay. I chose normally closed rather than normally open so that when the Pi is turned off, the relay will be closed and the router will act as if nothing was in the loop.

| Relay Pin | Power | Wire Color |
| --- | --- | --- |
| NC - Top | Positive from Plug | Red |
| Cmn - Center | Postive to Router | Red |

FYI - This is the difference between a normally open relay and normally closed:

| <img src="https://github.com/lizard43/routerWatch/blob/master/images/relay.jpg" width="600" /> |
|-|
