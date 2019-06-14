#!/usr/bin/python
import picamera
import time

class picam:
	def __init__(self,resolutionX=1280, resolutionY=720):
		self.camera=picamera.PiCamera()
		self.x=resolutionX
		self.y=resolutionY
		self.camera.resolution=(self.x,self.y)	
		print("picam Initialization successfull ")
	
	def SetResolution(self, resolutionX,resolutionY):
		self.x=resolutionX
		self.y=resolutionY
		self.camera.resolution=(self.x,self.y)	
	
	def ClickPicture(self, imagename,imageformat):
		self.camera.start_preview()
		time.sleep(3)
		self.camera.capture(imagename+'.'+imageformat)
		self.camera.stop_preview()
	
	def RecordVideo(self, videoname,videotype, timer):
		self.camera.start_recording(videoname+"."+videotype)
		self.camera.wait_recording(timer)
		self.camera.stop_recording()
	  
if __name__ == "__main__":
	### Use this to test the Camera Module of Pi
	p1 = picam(1280, 720)
	p1.SetResolution(1280,720)
	p1.ClickPicture("t1","jpg")
	p1.RecordVideo("my_video","h264",20)
