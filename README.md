# Orient-Express
ECE1779-A3-Function as a Service(AWS Lambda function)

API Gateway Link: https://fk03bgn9ul.execute-api.us-east-1.amazonaws.com/dev

## How to test locally
```
source venv/bin/activate
./start.sh
```
## How to deploy
```
zappa deploy
```
## How to update 
```
zappa update
```
## How to update static files in S3?
```
python upload_s3.py
```
After uploading successfully, please change the metadata of the "css" folder in s3 and write content-type as "text/css".
