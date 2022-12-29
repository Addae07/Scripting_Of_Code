import boto3 

ec2 = boto3.resource('ec2')
ec2.Instance('i-08c7a58c7cde35d5e').stop()
ec2.Instance('i-0bfa25adb92551733').stop()
ec2.Instance('i-0a5807bf76a8ab4a6').stop()