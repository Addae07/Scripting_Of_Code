#how to describe one vpc based on vpc id
import boto3

client=boto3.client("ec2")

#how to describe all vpc is available in your account
x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
#how to describe one vpc based on vpc id
#x=client.describe_vpcs(VpcIds=["vpc-06f85a6d","vpc-0726e99e7bc27be14"])
#x


#how to describe vpc based on filter
#x=client.describe_vpcs??

#x=client.describe_vpcs(Filters=[
 #         {
  #            'Name': 'vpc-id',
   #              'vpc-06f85a6d',
    #              'vpc-0726e99e7bc27be14'
     #             
      #        ]
       #   },
      #])
      
   #   x
