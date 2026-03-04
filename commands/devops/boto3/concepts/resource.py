
# ==============================================================
# boto3 resources
# a resource is a high-level, object-oriented interface that simplifies interactions with AWS services
# instead of manually handling API requests and responses (as with boto3.client())
# resources allow you to work with AWS services as Python objects.
#
# benefits
# simplifies AWS operations – No need to manually format API calls.
# object-oriented approach – Treat AWS services like Python objects with attributes and methods.
# automatically handles API requests – Boto3 makes the necessary AWS API calls under the hood.
# easier iteration – Provides collection-based access (e.g., for bucket in s3.buckets.all()).
# ==============================================================

import boto3

print("\n========== S3 Resource")
# create an s3 resource
s3 = boto3.resource("s3")
ttl_buckets = 0
# iterate through all s3 buckets
for bucket in s3.buckets.all():
    ttl_buckets += 1
    print(f"{ttl_buckets}: {bucket.name}")

print("========== S3 Resource")
# create an ec2 resource
ec2 = boto3.resource("ec2")
# list all running ec2 instances
for instance in ec2.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}]):
    print(f"Instance ID: {instance.id}, State: {instance.state['Name']}")

