# $language = "python"
# $interface = "1.0"

# CRTResetAP.py

# Works with Aruba:
#	APBoot 2.1.4.7
#	Controller 6.5.4.9

# Decription:
# 	This script when ran with SecureCRT will reset an AP then send the
# 	command to the AP's master controller so it can be cleared from the
#	database. The script will wait for outputs from the AP, so it can be ran
#	continuously while you switch from AP to AP. Must have the APs consoled in
#	the first tab and the master controller in the second. Master controller
#	must be logged in and in configure terminal mode.

# Starts loop
while True :

	# Script will look for this to stop autoboot
	enterPrompt = "Hit <Enter> to stop autoboot:"

	# Script will look for this to stop recording screen output
	szPrompt = "apboot>"

	# Using GetScriptTab() will make this script 'tab safe'
	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True
	objTab.Screen.IgnoreEscape = True

	# Wait for enterPrompt then send enter command
	objTab.Screen.WaitForString(enterPrompt)
	objTab.Screen.Send("\r\n")

	# Send intial commands to AP
	objTab.Screen.Send("purge" + "\r\n")
	objTab.Screen.Send("save" + "\r\n")

	# Send command for the output to be captured
	szCommand = "mfginfo"
	objTab.Screen.Send(szCommand + "\r\n")

	# Wait for the command to finish
	objTab.Screen.WaitForString(szCommand + "\r\n")

	# This will cause ReadString() to capture data until we see the szPrompt
	szResult = objTab.Screen.ReadString(szPrompt)

	# Split output into string
	SendResult = szResult.split()

	# Grab wired MAC address from output
	apMAC = SendResult[7]

	# Tell CRT that we want to intilize tab 2
	tab = crt.GetTab(2)
	tab.Activate()

	# Send command with wired MAC to second tab, the master controller
	tab.Screen.Send("clear gap-db wired-mac " + apMAC + "\r\n")

	# Return back to first tab
	tab = crt.GetTab(1)
	tab.Activate()
