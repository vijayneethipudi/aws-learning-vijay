import boto3

def delete_employeedetails(name, age, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('employee_details')
    response = table.delete_item(
        Key={
            'Name': name,
            'age': age
        }
    )
    return response

if __name__ == '__main__':
    output = delete_employeedetails('Jony', 25)
    print(output)