#how to create aws ebs volume from snapshot using boto3 and python
import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1a',
      Encrypted=True,
      Size=10,
      SnapshotId='snap-0eb8802c60cc7a226',
      VolumeType='gp2')