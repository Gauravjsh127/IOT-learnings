#!/usr/bin/python
import picamera
import time
import time
import os
import logging
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

## Custom pi packages
import picam
import pimqtt

def run_Cam(self, params, packet):
	print(packet.payload)
	print("run_Cam executed ")
	p1 = picam.picam(1280, 720)
	p1.SetResolution(1280,720)
	respDict = json.loads(packet.payload)
	command=respDict["mode"]
	print(command)
	if(command=="pic"):
		p1.ClickPicture("pic","jpg")
	else:
		p1.RecordVideo("video","h264",20)
	
	
pimqttclient = pimqtt.pimqttClient("pihome","a2yj40rcma4sm-ats.iot.us-west-2.amazonaws.com")
pimqttclient.mqttConfigureCertificates("/home/pi/code/IOT-learnings/AWSDemo/pi-cert/")
pimqttclient.mqttConfiguration()
pimqttclient.mqttConnect()
pimqttclient.mqttDisconnect()
pimqttclient.mqttConnect()
pimqttclient.mqttSubscribe("run/cam",run_Cam)
counter=1
testData = {}
while True:
	time.sleep(5)
	testData['counter'] = counter
	jtestData = json.dumps(testData)
	pimqttclient.mqttPublish("run/pub",jtestData)
	print("Publish Test Data "+ str(counter))
	counter=counter+1
