from azure.ml.component import dsl


dsl.generate_package(
    assets='assets.yaml',
    package_name='.',
    force_regenerate=False,
    mode='snapshot',
)
