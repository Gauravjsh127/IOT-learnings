import csv
import boto3
from botocore.exceptions import ClientError

## The image must be formatted as a PNG or JPEG file
t1='t1.jpeg'
t2='t2.jpg'
t3='t3.jpg'

bucketname="gauravjsh127"
class AWSS3:
	def __init__(self,access_key_id,secret_access_key):
		self.client = boto3.client('s3',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name='us-west-2')

	def listBuckets(self):
		self.response = self.client.list_buckets()

	def createBucket(self,bucketname):
		self.client.create_bucket(Bucket=bucketname,CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
		
	def deleteBucket(self,bucketname):
		self.client.delete_bucket(Bucket=bucketname)
		
	def uploadFile(self,bucketname,filename):
		self.client.upload_file(filename,bucketname,filename)
		
	def deleteFile(self,bucketname,filename):
		self.client.delete_object(Bucket=bucketname, Key=filename)			
					
if __name__ == "__main__":

	#access_key_id=""
	#secret_acess_key=""
	with open('credentials.csv','r') as input:
		next(input)
		reader=csv.reader(input)
		for line in reader:
			access_key_id=line[2]
			secret_access_key=line[3]
			
	AWSS3 = AWSS3(access_key_id, secret_access_key)

	print("#######List All Bucket #####################")
	AWSS3.listBuckets()
	print(AWSS3.response)
	for bucket in AWSS3.response['Buckets']:
		print("Bucket Name  : "+ bucket['Name'])
	
	print("#######Add a new bucket #####################")
	AWSS3.createBucket("gauravbucket11111")

	print("#######List All Bucket #####################")
	AWSS3.listBuckets()
	for bucket in AWSS3.response['Buckets']:
		print("Bucket Name  : "+ bucket['Name'])

	print("#######Delete a bucket #####################")
	AWSS3.deleteBucket("gauravbucket11111")

	print("#######List All Bucket #####################")
	AWSS3.listBuckets()
	for bucket in AWSS3.response['Buckets']:
		print("Bucket Name  : "+ bucket['Name'])
					
	print("#######Add a file inside Bucket #####################")
	AWSS3.uploadFile(bucketname,t1)
	AWSS3.uploadFile(bucketname,t2)
	AWSS3.uploadFile(bucketname,t3)
	
	print("#######Deelete a file inside Bucket #####################")
	AWSS3.deleteFile(bucketname,t1)
	AWSS3.deleteFile(bucketname,t2)
	
