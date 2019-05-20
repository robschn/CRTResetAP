# CRTResetAP
This script when ran with SecureCRT will reset an AP then send the command to the AP's master controller so it can be cleared from the database. The script will wait for outputs from the AP, so it can be ran continuously while you switch from AP to AP. 

Must have the APs consoled in the first tab and the master controller in the second. Master controller must be logged in and in configure terminal mode.

Works with Aruba
APBoot 2.1.4.7
Controller 6.5.4.9
