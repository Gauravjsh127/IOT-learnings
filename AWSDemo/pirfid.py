#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import MFRC522

####Look for GPIO pins setup https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
#### Look for python SPI libraries setup : https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/

class pirfid:
	def __init__(self,key):
		# Create an object of the class MFRC522
		self.MIFAREReader = MFRC522.MFRC522()
		print("pirfid Initialization successfull ")
		self.key=key

	def rfidUID(self):
		# Scan for cards
		(self.status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)	
		# Get the UID of the card
		(self.status,self.uid) = self.MIFAREReader.MFRC522_Anticoll()
		# If we have the UID, continue
		if self.status == self.MIFAREReader.MI_OK:
			return 1
		else:
			return -1
			
	def rfidAuthenthication(self):
		# Select the scanned tag
		self.MIFAREReader.MFRC522_SelectTag(self.uid)

		# Authenticate
		self.status = self.MIFAREReader.MFRC522_Auth(self.MIFAREReader.PICC_AUTHENT1A, 8, self.key, self.uid)
        # Check if authenticated
		if self.status == self.MIFAREReader.MI_OK:
			return 1
		else:
			return -1
			
	def rfidRead(self):
		print("pirfid Read Data ")	
		self.MIFAREReader.MFRC522_Read(8)
	
	def rfidWrite(self,data):
		print("pirfid Write Data ")	
		self.MIFAREReader.MFRC522_Write(8, data)
	
	  
if __name__ == "__main__":
	# Welcome message
	print("Looking for cards")
	print("Press Ctrl-C to stop.")
	# This loop checks for chips. If one is near it will get the UID	
	counter=1;
	try:
		while True:
			### Use this to test the RFID Module of Pi
			key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
			rfid = pirfid(key)
			status=rfid.rfidUID()
			if(status==1):
				# Print UID
				print("Card Read successfull : "+str(counter))
				print("UID: "+str(rfid.uid[0])+","+str(rfid.uid[1])+","+str(rfid.uid[2])+","+str(rfid.uid[3]))
				status=rfid.rfidAuthenthication()
				# Variable for the data to write
				data = []
				if(status==1):
					# Read block 8
					rfid.rfidRead()				
					# Fill the data with 0xFF
					for x in range(0,16):
						data.append(counter)
					rfid.rfidWrite(data)
					# Read block 8
					rfid.rfidRead()				
				else:
					print("\n Authentication unsuccessful ")		
				counter=counter+1	
			time.sleep(2)
		
	except KeyboardInterrupt:
	  GPIO.cleanup()
	
	
