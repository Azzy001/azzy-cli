
# ==============================================================
# boto3 client
# a client is a low-level interface that allows you to interact with AWS services 
# using raw API calls. It provides access to all AWS service operations 
# with a one-to-one mapping to AWS's underlying HTTP API.
#
# difference between clients and resource
# client
#   Low-level API, returns dictionaries, closer to AWS's raw API calls.
# resource
#   High-level API, uses objects for easier interaction.
#
# Use clients when you need full control, lower latency, and direct API calls.
# use resources when you want a more Pythonic way to interact with AWS services.
# ==============================================================

import boto3

"""
Client (boto3.client)
* Low-level API: Direct AWS API calls (one-to-one mapping with AWS SDK).
* Faster & Lightweight: Returns raw dictionaries (JSON-like responses).
* Best for: Simple interactions, bulk operations, automation scripts.
"""

print()
s3_client = boto3.client("s3")
buckets = s3_client.list_buckets()
# returns a dictionary
print(buckets)

"""
Resource (boto3.resource)
* High-level API: Object-oriented abstraction over AWS services.
* More Pythonic: Uses objects instead of raw responses.
* Best for: Complex interactions, easier navigation, iterating over resources.
"""

print()
s3_resource = boto3.resource("s3")
for bucket in s3_resource.buckets.all():
    print(bucket.name)
