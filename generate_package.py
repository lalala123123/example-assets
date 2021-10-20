from azure.ml.component import dsl

assets = {
    'components': [
        'file:./local_components/mpi/component.yaml',
        'file:./local_components/copy_files/component.yaml',
        'file:./local_components/hdi-component/component_spec.yaml',
        'file:./local_components/scope_component/toss/component_spec.yaml',
        'file:./local_components/sweep_component/sweep.spec.yaml',
        'azureml://feeds/azureml',
        'azureml://feeds/huggingface',
    ],
}

source_dir = './generated_package'
dsl.generate_package(force_regenerate=True, assets=assets, package_name='example-assets', source_directory=source_dir, mode='snapshot')