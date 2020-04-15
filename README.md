# AWS Lambda Function Code for API Gateway Backend API
This README explains the Serverless Backend built on AWS API Gateway and AWS Lambda Functions with dynamoDB as the data store. The following components were set up:
## AWS Lambda Function
The Lambda Function `lambda_function.py` contained in this folder contains teh code used to interact with dynamoDB. The code is based off using API Gateway with Lambda Proxy Intergration. This configuration was chosen as to allow the code to be able to read in the request headers and path parameters. In addition to this; this allowed one function to be used for multiple requests.

To re-create the Lambda function just copy the code from the file and paste it in the AWS Lambda Function Console in a python 3.8 runtime.

## API Gateway
Once the Lambda Function has been created, API methods can be created for POST and GET requests using lambda proxy integration and pointing to the same lambda function.