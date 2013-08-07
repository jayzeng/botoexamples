from boto.s3.connection import S3Connection

# Description:
# 1. Connect to an existing s3 bucket
# 2. Retrieve a key
# 3. Prints out a boolean to indicate whether key exists

s3_conn = S3Connection('aws_key', 'aws_secret')
bucket = conn.get_bucket(s3_conn)

# returns an iterator of Keys
existing_keys = bucket.list(prefix='relative_path')

for key in existing_keys:
    # See https://github.com/boto/boto/blob/develop/boto/s3/key.py for details
    # Key name
    print key.name
