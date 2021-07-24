import boto3

def put_employeedetails(name, age, email, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('employee_details')
    response = table.put_item(
        Item={
            'Name': name,
            'age': age,
            'email': email
        }
    )

    return response

if __name__ == '__main__':
    output = put_employeedetails('Jony', 25, 'jony777@gmail.com')
    print(output)