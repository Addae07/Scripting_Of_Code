import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-0eb8802c60cc7a226')