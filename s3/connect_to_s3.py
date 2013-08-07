from boto.s3.connection import S3Connection

# Description:
# How to create a s3 bucket

s3_conn = S3Connection('aws_key', 'aws_secret')
bucket = conn.create_bucket(s3_conn)
