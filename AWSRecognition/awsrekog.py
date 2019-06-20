import csv
import boto3

## The image must be formatted as a PNG or JPEG file
LabelImage='test.jpg'
BikiniImage="Bikini.jpeg"
girlsmiling="girl-smiling.jpg"
Billionares="Billionares.jpeg"
two_girls_smiling="two_girls_smiling.jpeg"

BucketName="gauravjsh127"

class AWSRekog:
	def __init__(self,access_key_id,secret_access_key,MaxLabels=2, MinConfidence=80):
		self.client = boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name='us-west-2')
		self.MaxLabels=MaxLabels
		self.MinConfidence=MinConfidence

	def base64_encodeinputimage(self,image):
		with open(image,'rb') as sourceimage:
			self.sourceBytes=sourceimage.read()

	def inputimageRemote(self,image):
		self.image=image

	def inputimageLocal(self,image):
		self.image=image
		self.base64_encodeinputimage(image)
		
	def detectLablesLocalImage(self):
		self.response=self.client.detect_labels(Image={'Bytes': self.sourceBytes},MaxLabels=self.MaxLabels, MinConfidence=self.MinConfidence)

	#https://us-west-2.console.aws.amazon.com/rekognition/home?region=us-west-2#/label-detection
	def detectLablesS3DB(self):
		self.response=self.client.detect_labels(Image={'S3Object': {'Bucket': BucketName , 'Name': self.image}},MaxLabels=self.MaxLabels, MinConfidence=self.MinConfidence)		
	
	#https://us-west-2.console.aws.amazon.com/rekognition/home?region=us-west-2#/image-moderation
	def detecModerationS3DB(self):
		self.response=self.client.detect_moderation_labels(Image={'S3Object': {'Bucket': BucketName , 'Name': self.image}})		

	#https://us-west-2.console.aws.amazon.com/rekognition/home?region=us-west-2#/face-detection
	def detecFaceS3DB(self):
		self.response=self.client.detect_faces(Image={'S3Object': {'Bucket': BucketName , 'Name': self.image}}, Attributes=['ALL'])
		
	#https://us-west-2.console.aws.amazon.com/rekognition/home?region=us-west-2#/face-detection
	def detecMultipleFaceS3DB(self):
		self.response=self.client.detect_faces(Image={'S3Object': {'Bucket': BucketName , 'Name': self.image}}, Attributes=['ALL'])

	#https://us-west-2.console.aws.amazon.com/rekognition/home?region=us-west-2#/face-detection
	def detecCelebretiesS3DB(self):
		self.response=self.client.recognize_celebrities(Image={'S3Object': {'Bucket': BucketName , 'Name': self.image}})
			
					
if __name__ == "__main__":

	#access_key_id=""
	#secret_acess_key=""
	with open('credentials.csv','r') as input:
		next(input)
		reader=csv.reader(input)
		for line in reader:
			access_key_id=line[2]
			secret_access_key=line[3]
			
	AWSRekog = AWSRekog(access_key_id, secret_access_key)

	print("#######Local Image Detect Lables#####################")
	AWSRekog.inputimageLocal(LabelImage)
	AWSRekog.detectLablesLocalImage()
	print(AWSRekog.response)
	
	print("#######S3 DB Image Detect Lables #####################")
	AWSRekog.inputimageRemote(LabelImage)
	AWSRekog.detectLablesS3DB()
	print(AWSRekog.response)

	print("#######S3 DB Image Moderation #####################")
	AWSRekog.inputimageRemote(BikiniImage)
	AWSRekog.detecModerationS3DB()
	print(AWSRekog.response)
	
	print("#######S3 DB Detect Facial attributes #####################")
	AWSRekog.inputimageRemote(girlsmiling)
	AWSRekog.detecFaceS3DB()
	print(AWSRekog.response)

	print("#######S3 DB Detect Multiple Faces Facial attributes #####################")
	AWSRekog.inputimageRemote(two_girls_smiling)
	AWSRekog.detecMultipleFaceS3DB()
	print(AWSRekog.response)
	
	for key,value in AWSRekog.response.items():
		if key=="FaceDetails":
			for people_att in value:
				print (people_att)
				print("*********************************************************")
			
			
	print("#######S3 DB Detect Celebreties #####################")
	AWSRekog.inputimageRemote(Billionares)
	AWSRekog.detecCelebretiesS3DB()
	print(AWSRekog.response)
	
	for key,value in AWSRekog.response.items():
		if key=="CelebrityFaces":
			for people in value:
				print (people)
				print("*********************************************************")
			
