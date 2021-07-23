# AWS VPC Peering Connection

Download peering.yaml file.
If you have aws cli setup in your local machine use below commands to create stack

`aws cloudformation validate-stack --template-body file://peering.yaml` 

`aws cloudformation create-stack --stack-name stackname --template-body file://peering.yaml`

It will return a stack id in response

You can use `describe-stack-events` to know the current events

  `aws cloudformation describe-stack-events --stack-name stackname`
  
Or you could simply use AWS console to deploy the stack
 
Creating Peering connection:
---
  1. Once the stack provisioned resources, navigate to VPC console
  2. Click on VPC Peering on the left side bar.
  3. Click on create peering connection
  4. Enter Name
  5. Select VPC's
  6. Click on Create
 
Update Route Tables
 ---
  1. On the left side navigation bar, click on Route Tables
  2. Click on VPC A Route table and click on edit routes down below
  3. Enter 10.17.10.0/24 and select peering connection then click on Create
  4. Click on VPC B route table and click on edit routes down below
  5. Enter 10.16.10.0/24 and select peering connection then click on Create
 
Testing
 ---
 1. Navigate to EC2 console
 2. Copy B instance IPv4 address
 3. Connect to A instance using ec2 browser method
 3. Ping B instance IPv4 address
 5. You should see ping requests are success. 
 
You can test it for A instance IPv4 address on B instance
 
 
 Decommissioning the infrastructure:
 ---
  1. Navigate to VPC console and delete peering connection
  2. from command prompt enter below command
  Note: replace [stackname] with your stack name
  
 `aws cloudformation delete-stack --stack-name [stackname]`
 
 Or you can decommission it using aws console -> CloudFormation -> click on stack -> Select stack -> Delete stack
 
 That should delete provisioned resources. Ensure all resources are deleted otherwise you will be billed according to the aws pricing. 
