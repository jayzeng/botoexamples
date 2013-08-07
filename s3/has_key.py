from boto.s3.connection import S3Connection

# Description:
# 1. Connect to an existing s3 bucket
# 2. Retrieve a key
# 3. Prints out a boolean to indicate whether key exists

s3_conn = S3Connection('aws_key', 'aws_secret')
bucket = conn.get_bucket(s3_conn)
k = Key(bucket)

# input: s3://example/foo/bar.py
# relative_path: foo/bar.py
k.key = 'relative_path'
print k.exists()
