# Description:
# BootstrapAction is an object reperesenting a bootstrap action in Elastic Map
# Reduce (EMR), a script that gets run before the EMR job executes.
from boto.emr.bootstrap_action import BootstrapAction
from boto.emr.connection import EmrConnection

# Description:
# BootstrapAction is an object reperesenting a bootstrap action in Elastic Map
# Reduce (EMR), a script that gets run before the EMR job executes.

# initialize a bootstrap action
bootstrapSetup = BootstrapAction("Bootstrap Name",
                                 "s3://<my-bucket>/<my-bootstrap-action>",
                                 ["arg1=hello", "arg2=world"])

# initialize emr connection
emr_job = EmrConnection("<aws-access-key-id>", "<aws-secret-access-key>")

# run emr job flow with defined bootstrap action
emr_job.run_jobflow(bootstrap_actions=[bootstrapSetup])
