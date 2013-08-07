## Create a bucket
```python
from boto.s3.connection import S3Connection
conn = S3Connection('<aws access key>', '<aws secret key>')
bucket = conn.create_bucket('mybucket')
```
