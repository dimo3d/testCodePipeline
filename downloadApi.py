import boto3
s3 = boto3.resource('s3')

bucket = s3.Bucket('dimodoc')
client = boto3.client('apigateway')
apiname = u"testPip"
apis = (client.get_rest_apis())["items"]
apiId = ""
for api in apis:
	print api["name"]
	if api["name"] == apiname:
		apiId = api["id"]

if apiId == "":
	exit(0)

response = client.get_export(
restApiId=apiId,
stageName='dev',
exportType='swagger')
bucket.upload_fileobj(response["body"], 'swagger.json') 