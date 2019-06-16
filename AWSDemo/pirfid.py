#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import MFRC522

####Look for GPIO pins setup https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
#### Look for python SPI libraries setup : https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/

class pirfid:
	def __init__(self,):
		# Create an object of the class MFRC522
		self.MIFAREReader = MFRC522.MFRC522()
		print("pirfid Initialization successfull ")

	def getUID(self):
		# Scan for cards
		(self.status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)	
		# Get the UID of the card
		(self.status,self.uid) = self.MIFAREReader.MFRC522_Anticoll()
		# If we have the UID, continue
		if self.status == self.MIFAREReader.MI_OK:
			return 1
		else:
			return -1
			
	def ReadData(self, resolutionX,resolutionY):
		print("pirfid Read Data ")	
	
	def WriteData(self):
		print("pirfid Write Data ")	
	
	  
if __name__ == "__main__":
	### Use this to test the RFID Module of Pi
	rfid = pirfid()

	# Welcome message
	print("Looking for cards")
	print("Press Ctrl-C to stop.")
	# This loop checks for chips. If one is near it will get the UID	
	counter=1;
	try:
		while True:
			status=rfid.getUID()
			if(status==1):
				# Print UID
				print("Card Read successfull : "+str(counter))
				print("UID: "+str(rfid.uid[0])+","+str(rfid.uid[1])+","+str(rfid.uid[2])+","+str(rfid.uid[3]))
				counter=counter+1
			time.sleep(2)
		
	except KeyboardInterrupt:
	  GPIO.cleanup()
	
	
