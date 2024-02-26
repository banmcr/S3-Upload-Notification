import os
import uuid
import boto3
import json
from urllib.parse import urlparse
import urllib


S3 = boto3.resource('s3')

def lambda_handler(event, context):
    
    
    sourceS3Bucket = event['Records'][0]['s3']['bucket']['name']
    S3Key = event['Records'][0]['s3']['object']['key']
    sourceS3Key = urllib.parse.unquote_plus(S3Key)
    print(sourceS3Bucket)
    print(sourceS3Key)
    
    notification = "File uploaded to "+sourceS3Bucket+"\n\n File name is "+sourceS3Key+"\n"
    client = boto3.client('sns')
    sub="File uploaded to S3 bucket "+sourceS3Bucket
    response = client.publish (
        TargetArn = "arn:aws:sns:ap-south-1:5555222333444:SNS-TOPIC-NAME",
        Message = json.dumps({'default': notification}),
        MessageStructure = 'json',
        Subject=sub
    )
