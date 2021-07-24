import boto3

client = boto3.client('dynamodb')

response = client.scan(TableName='employee_details')
for data in response['Items']:
    print(data['Name'])
