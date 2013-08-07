from boto import Config as BotoConfig

# Description:
# How to use boto's config library

boto_config = BotoConfig()

aws_key     = boto_config.get('Credentials', 'aws_access_key_id')
aws_secret  = boto_config.get('Credentials', 'aws_secret_access_key')
