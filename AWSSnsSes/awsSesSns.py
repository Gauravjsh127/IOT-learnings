import csv
import boto3
from botocore.exceptions import ClientError

import boto3
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Gaurav Joshi <gauravatmunich@gmail.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT = "krisgaurav127@gmail.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
#CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-west-2"

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """            
# The character encoding for the email.
CHARSET = "UTF-8"




class AWSSesSns:
	def __init__(self,access_key_id,secret_access_key):
		self.client = boto3.client('ses',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name='us-west-2')

	def sendEmail(self):
		# Try to send the email.
		try:
			#Provide the contents of the email.
			response = self.client.send_email(
				Destination={
					'ToAddresses': [
						RECIPIENT,
					],
				},
				Message={
					'Body': {
						'Html': {
							'Charset': CHARSET,
							'Data': BODY_HTML,
						},
						'Text': {
							'Charset': CHARSET,
							'Data': BODY_TEXT,
						},
					},
					'Subject': {
						'Charset': CHARSET,
						'Data': SUBJECT,
					},
				},
				Source=SENDER,
				# If you are not using a configuration set, comment or delete the
				# following line
				#ConfigurationSetName=CONFIGURATION_SET,
			)
		# Display an error if something goes wrong.	
		except ClientError as e:
			print(e.response['Error']['Message'])
		else:
			print("Email sent! Message ID:"),
			print(response['MessageId'])

					
if __name__ == "__main__":

	#access_key_id=""
	#secret_acess_key=""
	with open('credentials.csv','r') as input:
		next(input)
		reader=csv.reader(input)
		for line in reader:
			access_key_id=line[2]
			secret_access_key=line[3]
			
	AWSSesSns = AWSSesSns(access_key_id, secret_access_key)

	print("#######Send Email #####################")
	AWSSesSns.sendEmail()


