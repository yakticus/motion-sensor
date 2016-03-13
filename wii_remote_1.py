#!/usr/bin/python
#
# wii_remote_1.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1101
#
# Author : Matt Hawkins
# Date   : 30/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time
import soco
from soco import SoCo
import time
import socket

office_ip = socket.gethostbyname('sonosoffice')
family_ip = socket.gethostbyname('sonosfamily')
parlor_ip = socket.gethostbyname('sonosparlor')

selected_zone = SoCo(family_ip)

button_delay = 0.3

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Previous track'
    selected_zone.previous()
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Next track'
    selected_zone.next()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'volume up'
    vol = selected_zone.volume
    selected_zone.volume = vol + 1        
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'volume down'
    vol = selected_zone.volume
    selected_zone.volume = vol - 1      
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    info = selected_zone.get_current_transport_info()
#    print info
    if info['current_transport_state'] == 'PLAYING':
      print 'pausing'
      selected_zone.pause()
    else:
      print 'playing'
      selected_zone.play()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'button B pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
