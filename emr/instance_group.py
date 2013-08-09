from boto.emr.connection import EmrConnection
from boto.emr.instance_group import InstanceGroup

# Description:
# The InstanceGroup object can be useful for customizing
# the nodes of an EMR(Elastic Map Reduce) job.

# build up our instance groups
namenode_instance_group = InstanceGroup(num_instances=1,
                                        role="MASTER",
                                        type="c1.xlarge",
                                        market="ON_DEMAND",
                                        name="MASTER_GROUP")

core_nodes = InstanceGroup(num_instances=20,
                           role="MASTER",
                           type="c1.xlarge",
                           market="SPOT",
                           name="MASTER_GROUP")

task_nodes = InstanceGroup(num_instances=10,
                           role="TASK",
                           type="c1.xlarge",
                           market="ON_DEMAND",
                           name="INITIAL_TASK_GROUP")

instance_groups = [namenode_instance_group, core_nodes, task_nodes]


# run the job
conn = EmrConnection("<aws-access-key-id>", "<aws-secret-access-key>")
conn.run_jobflow(name="My Job Flow",
                 instance_groups=instance_groups)


