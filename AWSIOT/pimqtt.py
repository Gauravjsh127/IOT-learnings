#!/usr/bin/python
import time
import os
import logging
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

     
def run_customCallback(self, params, packet):
	print("run_testfunction executed ")
	print(packet.payload)
	respDict = json.loads(packet.payload)
	print(respDict["message"])
	
class pimqttClient:
	def __init__(self,mqttClient,endPoint):
		self.mqttClient = AWSIoTMQTTClient(mqttClient) 
		self.mqttClient.configureEndpoint(endPoint,8883)
		print("pimqttClient Initialization successfull ")
	
	def mqttConfigureCertificates(self, certpath):
		self.mqttClient.configureCredentials("{}root-ca.pem".format(certpath), "{}cloud.pem.key".format(certpath), "{}cloud.pem.crt".format(certpath))
   
	def mqttConfiguration(self):
		self.mqttClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
		self.mqttClient.configureDrainingFrequency(2) # Draining: 2 Hz
		self.mqttClient.configureConnectDisconnectTimeout(10) # 10 sec
		self.mqttClient.configureMQTTOperationTimeout(5) # 5 sec

	def mqttConnect(self):
		self.mqttClient.connect()
		print("pimqttClient Connection successfully ")

	def mqttSubscribe(self, topic,customCallback):
		self.mqttClient.subscribe(topic, 1, customCallback)

	def mqttunSubscribe(self, topic):
		self.mqttClient.unsubscribe(topic)

	def mqttPublish(self, topic , payload):
		self.mqttClient.publish(topic, payload, 0)

	def mqttDisconnect(self):
		self.mqttClient.disconnect()
		print("pimqttClient Disconnected successfully ")
			
if __name__ == "__main__":
	### Use this to test the Mqtt connection
	pimqttclient = pimqttClient("pihome","a2yj40rcma4sm-ats.iot.us-west-2.amazonaws.com")
	pimqttclient.mqttConfigureCertificates("/home/pi/code/IOT-learnings/AWSIOT/pi-cert/")
	pimqttclient.mqttConfiguration()
	pimqttclient.mqttConnect()
	pimqttclient.mqttDisconnect()
	pimqttclient.mqttConnect()
	pimqttclient.mqttSubscribe("run/sub",run_customCallback)
	count=1
	testData = {}
	while True:
		time.sleep(5)
		testData['count'] = count
		jtestData = json.dumps(testData)
		pimqttclient.mqttPublish("run/pub",jtestData)
		print("Publish Test Data "+ str(count))
		count=count+1
		
