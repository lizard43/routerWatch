#!/usr/bin/python

# this is mostly reused from https://github.com/StephenWetzel/routerReboot

import checkInternet
import powerCycle
import time
import datetime

sleepSuccess = 30 #seconds to wait after we test internet again if it was up
sleepFail = 600 #seconds to wait after internet was down, and we power cycle
sleepInitial = 100 #seconds to sleep after starting to allow router to boot before we begin checking
numFailsReboot = 10 #how many failures to ping we need before we reboot

numFails = 0 #how many times we could not ping internet in a row

powerCycle.powerCycle()
time.sleep(sleepInitial)

while True:
	internetStatus = checkInternet.checkUp()
	if internetStatus == "up":
		print str(datetime.datetime.now()) + " Internet works"
		numFails = 0
		time.sleep(sleepSuccess)

	elif internetStatus == "down":
		print str(datetime.datetime.now()) + " Router down"
		numFails = 0 #if we are rebooting router, then might as well reset failure count
		powerCycle.powerCycle()
		time.sleep(sleepFail)

	else:
		print str(datetime.datetime.now()) + " Internet down"
		numFails += 1
		if numFails > numFailsReboot:
			numFails = 0
			powerCycle.powerCycle()
			time.sleep(sleepFail)
