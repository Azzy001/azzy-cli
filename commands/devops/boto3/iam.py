import boto3
import click
from pathlib import Path
import sys
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# ------------------------------------------------------------------------
# default profile = the AWS credentials stored onto your local system.
# done by using "aws configure".
# the script will go through all IAM users in your AWS account and print their names.
# ------------------------------------------------------------------------

# create a new AWS session using the "default" profile from aws credentials
aws_management_console = boto3.session.Session(profile_name="default")
# get the IAM (Identity & Access Management) resource object
iam_console = aws_management_console.resource("iam")

# iterate through all the IAM users in the AWS account
# return username, arn and creation date and time
for each_user in iam_console.users.all():
    print(f"User: {each_user.name}\nARN: {each_user.arn}\nCreated: {each_user.create_date}.")
    print()

# this prints all the available attributes and methods of the aws_management_console object.
# lists attributes/methods of the object.
print(dir(aws_management_console))
# prints list of ll available high-level AWS resource services (like S3, EC2, DynamoDB).
# lists AWS services available as resources (high-level API).
print("\n", aws_management_console.get_available_resources())