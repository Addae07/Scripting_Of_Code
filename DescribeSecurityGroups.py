#describe security groups using boto3
import boto3

client=boto3.client("ec2")

x=client.describe_security_groups()

no_of_security_groups=len(x["SecurityGroups"])

no_of_security_groups

for group in x["SecurityGroups"]:
    print(group["GroupId"])
    
# How to describe security groups using security group id
#x=client.describe_security_groups(GroupIds=[
     #     'sg-0427426178c361b9e','sg-0df724f9bdd4cea2a'
    #  ])
    
#x


#How to describe security groups using filters
#x=client.describe_security_groups??

#x=client.describe_security_groups(Filters=[
#          {
 #            'Values': [
  #                'sg-0427426178c361b9e','sg-9ca9a9e1'
   #           ]
    #      },
     # ],)
     
     #x
