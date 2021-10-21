from azure.ml.component import dsl

assets = {
    'example_components': [
        'file:./components/**/*.yaml',
        'azureml://feeds/azureml',
        'azureml://feeds/huggingface',
    ],
}

source_dir = './generated_package'
dsl.generate_package(force_regenerate=True, assets=assets, package_name='example-assets', source_directory=source_dir, mode='snapshot')