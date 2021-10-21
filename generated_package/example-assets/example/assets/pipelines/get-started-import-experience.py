import os

# get workspace
from azureml.core import Workspace

config_path = ".azureml/config.json"
try:
    ws = Workspace.from_config(path=config_path)
except Exception as ex:
    # NOTE: Update following workspace information if not correctly configure before
    subscription_id="<your subscription ID>"
    resource_group="<your resource group>"
    workspace_name="<your workspace name>"

    if subscription_id.startswith("<"): 
        raise ex
    else: # write and reload from config file
        config = {"Scope": "/subscriptions/" + subscription_id + "/resourceGroups/" + resource_group + "/providers/Microsoft.MachineLearningServices/workspaces/" + workspace_name +"/projects/samples"}
        import json
        import os
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as fo:
            fo.write(json.dumps(config))
        ws = Workspace.from_config(path=config_path)

# get compute
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.compute_target import ComputeTargetException

cluster_name = "cpu-cluster"
if cluster_name not in ws.compute_targets:
    print('Creating a new compute target...')
    compute_config = AmlCompute.provisioning_configuration(vm_size="Standard_D2_v2",
                                                               max_nodes=4)
    compute_target = ComputeTarget.create(ws, cluster_name, compute_config)
    compute_target.wait_for_completion(show_output=True, timeout_in_minutes=20)


from azureml.core import Dataset

# get dataset
train_data = Dataset.File.from_files(path=['https://dprepdata.blob.core.windows.net/demo/Titanic.csv'])
test_data = Dataset.File.from_files(path=['https://dprepdata.blob.core.windows.net/demo/Titanic.csv'])


from example.assets.example_components import samples_train, samples_evaluate, samples_score
from azure.ml.component import dsl, Pipeline

# define a pipeline
@dsl.pipeline(name = 'A_training_pipeline_including_train_score_eval', 
              description = 'train model and evaluate model performance',
              default_compute_target = cluster_name)
def training_pipeline(input_data, learning_rate) -> Pipeline:
    train = samples_train(
        training_data=input_data, 
        max_epochs=5, 
        learning_rate=learning_rate)

    score = samples_score(
        model_input=train.outputs.model_output, 
        test_data=test_data)

    eval = samples_evaluate(scoring_result=score.outputs.score_output)


# create a pipeline and visualize the graph
pipeline = training_pipeline(train_data, 0.01)
# Specify the workspace for workspace independent component when validating the pipeline.
pipeline.validate(workspace=ws)

# run pipeline locally
# run pipeline with user-managed environment
# Specify the workspace to tracke the pipeline run history.
pipeline._run(experiment_name = 'pipeline-with-train-score-eval-components', mode='host', workspace=ws) 

# run pipeline with system-managed conda-based environment
#pipeline._run(experiment_name = 'pipeline-with-train-score-eval-components', mode='conda', workspace=ws)

# run pipeline with system-managed docker-based environment
#pipeline._run(experiment_name = 'pipeline-with-train-score-eval-components', mode='docker', workspace=ws)

# ## Run pipeline on remote compute
# Specify the workspace for workspace independent component when submitting the pipeline.
run = pipeline.submit(experiment_name = 'pipeline-with-train-score-eval-components', workspace=ws)

# show detail information of run
run

# Wait until the run completes
run.wait_for_completion()