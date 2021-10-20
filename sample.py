from azureml.core.workspace import Workspace
from azure.ml.component import dsl
from example.assets.example_components import microsoft_com_azureml_samples_hello_world_with_cpu_image,\
    microsoft_com_azureml_samples_parallel_copy_files_v1, datasets


@dsl.pipeline(default_compute_target='cpu-cluster')
def example_assets_pipeline(dataset):
    basic_component = microsoft_com_azureml_samples_hello_world_with_cpu_image(input_path=dataset,
                                                                               string_parameter="string_param")
    parallel_component = microsoft_com_azureml_samples_parallel_copy_files_v1(input_folder=basic_component.outputs.output_path)
    return parallel_component.outputs


# Generate pipeline
workspace = Workspace.from_config()
pipeline = example_assets_pipeline(datasets.atomic_atomic)

# Validate pipeline
pipeline.validate(workspace=workspace)

# Submit pipeline
pipeline.submit(workspace=workspace)