from boto.emr.connection import EmrConnection

# Description:
# EmrConnection can be used to create a new emr job

# initialize emr connection
conn = EmrConnection("<aws-access-key-id>", "<aws-secret-access-key>")

# run job flow with 10 instances
conn.run_jobflow(num_instances=10, 
                 master_instance_type="m1.small", 
                 slave_instance_type="m1.small")

