import json
import boto3
import botocore

def lambda_handler(event, context):
    # TODO implement

    # Get the S3 Resource
    s3 = boto3.resource('s3')

    # S3 Bucket
    bucketName = s3.Bucket('NAJHEMETAF')

    # Name of JSON object in S3 Bucket
    fileName = 'myJasmine.JSON'
    
    # I am assuming there is a folder in the buvket called NAJIDHAM
    # Remember we are already in the root of Bucket, therefore, you
    # don't need to put '/' before the folder's name
    pathOfFile = 'NAJIDHAM/' + fileName

    # You need to create a temp file for loading the contents of
    # The file located in S3 Bucket. I am using original name!
    # The Lambda creates the temp folder automatically at each envoke (/tmp/)
    tempFileName = '/tmp/' + fileName

    # Let's load the file
    try:
        # Here we can check if the file is existed in the mentioned path or not
        # I try to load the file using download_file function and check the response
        bucketName.download_file(pathOfFile, tempFileName)
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == "404":
            # The object does not exist! :-(
            # You can do stuff here if there is not such a file
        else:
            # Something else has gone wrong.
            raise
    else:
        # Yay, the object does exist! :-)
        # We know that the file exists and let's load S3 file to the Temp JSON file
        bucketName.download_file(pathOfFile, tempFileName)
        with open(tempFileName) as jsonInput:
            data = json.load(jsonInput)

    # You have loaded all the contents of JSON object located in S3
    # Please do something for poor people with your data!

    return {
        "statusCode": 200,
        "body": json.dumps('Cheers from Lambda!')
    }
