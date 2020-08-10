import maya.cmds as cmds

# Function to be called by the script job when a dag node is created
def on_dag_object_created():
    print("New DAG Object Created")

# Create a new script job for when a DAG object is created
my_job_number = cmds.scriptJob(event=["DagObjectCreated", "on_dag_object_created()"])


# Kill the scriptJob when done with it
if cmds.scriptJob(exists=my_job_number):
    cmds.scriptJob(kill=my_job_number)

