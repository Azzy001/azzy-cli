
# ==============================================================
# boto3 session
# A session in Boto3 acts as a connection to AWS, managing:
#   - Credentials (access keys, profiles)
#   - Region settings
#   - Configurations
#
# Using a session allows you to:
#   - Work with multiple AWS accounts (via profiles)
#   - Specify different AWS regions
#   - Use temporary credentials (e.g., Assume Role)
# ==============================================================

import boto3

# create a session using the default AWS profile
session = boto3.Session()

# create an IAM resource using the session
iam_resource = session.resource("iam")

# list and print all IAM users
for user in iam_resource.users.all():
    print(f"User: {user.name}")