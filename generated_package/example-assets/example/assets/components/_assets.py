# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
# Components included in this generated file:
#  - microsoft.com.azureml.samples.hello_world_with_cpu_image::0.0.1
#  - microsoft.com.azureml.samples.parallel_copy_files_v1::0.0.2
#  - microsoft.com.azureml.samples.train-in-spark::0.0.1
#  - bing.relevance.convert2ss::0.0.4
#  - microsoft.com.azureml.samples.tune::0.0.4
#  - azureml://Add Columns::0.0.159
#  - azureml://Add Rows::0.0.159
#  - azureml://Apply Image Transformation::0.0.39
#  - azureml://Apply Math Operation::0.0.80
#  - azureml://Apply SQL Transformation::0.0.80
#  - azureml://Apply Transformation::0.0.159
#  - azureml://Assign Data to Clusters::0.0.159
#  - azureml://Boosted Decision Tree Regression::0.0.159
#  - azureml://Clean Missing Data::0.0.159
#  - azureml://Clip Values::0.0.80
#  - azureml://Convert Word to Vector::0.0.159
#  - azureml://Convert to CSV::0.0.159
#  - azureml://Convert to Dataset::0.0.159
#  - azureml://Convert to Image Directory::0.0.39
#  - azureml://Convert to Indicator Values::0.0.159
#  - azureml://Create Python Model::0.0.159
#  - azureml://Cross Validate Model::0.0.159
#  - azureml://Decision Forest Regression::0.0.159
#  - azureml://DenseNet::0.0.43
#  - azureml://Edit Metadata::0.0.159
#  - azureml://Enter Data Manually::0.0.159
#  - azureml://Evaluate Model::0.0.159
#  - azureml://Evaluate Recommender::0.0.159
#  - azureml://Execute Python Script::0.0.159
#  - azureml://Execute R Script::0.0.159
#  - azureml://Export Data::0.0.63
#  - azureml://Extract N-Gram Features from Text::0.0.159
#  - azureml://Fast Forest Quantile Regression::0.0.159
#  - azureml://Feature Hashing::0.0.159
#  - azureml://Filter Based Feature Selection::0.0.159
#  - azureml://Group Data into Bins::0.0.159
#  - azureml://Import Data::0.0.63
#  - azureml://Init Image Transformation::0.0.39
#  - azureml://Join Data::0.0.159
#  - azureml://K-Means Clustering::0.0.159
#  - azureml://Latent Dirichlet Allocation::0.0.159
#  - azureml://Linear Regression::0.0.159
#  - azureml://MultiClass Boosted Decision Tree::0.0.159
#  - azureml://Multiclass Decision Forest::0.0.159
#  - azureml://Multiclass Logistic Regression::0.0.159
#  - azureml://Multiclass Neural Network::0.0.159
#  - azureml://Neural Network Regression::0.0.159
#  - azureml://Normalize Data::0.0.159
#  - azureml://One-vs-All Multiclass::0.0.159
#  - azureml://One-vs-One Multiclass::0.0.159
#  - azureml://PCA-Based Anomaly Detection::0.0.159
#  - azureml://Partition and Sample::0.0.159
#  - azureml://Permutation Feature Importance::0.0.159
#  - azureml://Poisson Regression::0.0.159
#  - azureml://Preprocess Text::0.0.159
#  - azureml://Remove Duplicate Rows::0.0.159
#  - azureml://ResNet::0.0.43
#  - azureml://SMOTE::0.0.159
#  - azureml://Score Image Model::0.0.43
#  - azureml://Score Model::0.0.159
#  - azureml://Score SVD Recommender::0.0.159
#  - azureml://Score Vowpal Wabbit Model::0.0.32
#  - azureml://Score Wide and Deep Recommender::0.0.37
#  - azureml://Select Columns Transform::0.0.159
#  - azureml://Select Columns in Dataset::0.0.159
#  - azureml://Split Data::0.0.159
#  - azureml://Split Image Directory::0.0.39
#  - azureml://Summarize Data::0.0.80
#  - azureml://Train Anomaly Detection Model::0.0.159
#  - azureml://Train Clustering Model::0.0.159
#  - azureml://Train Model::0.0.159
#  - azureml://Train PyTorch Model::0.0.43
#  - azureml://Train SVD Recommender::0.0.159
#  - azureml://Train Vowpal Wabbit Model::0.0.32
#  - azureml://Train Wide and Deep Recommender::0.0.37
#  - azureml://Tune Model Hyperparameters::0.0.159
#  - azureml://Two-Class Averaged Perceptron::0.0.159
#  - azureml://Two-Class Boosted Decision Tree::0.0.159
#  - azureml://Two-Class Decision Forest::0.0.159
#  - azureml://Two-Class Logistic Regression::0.0.159
#  - azureml://Two-Class Neural Network::0.0.159
#  - azureml://Two-Class Support Vector Machine::0.0.159
#  - fine_tune_for_huggingface_text_classification::0.0.1
#  - fine_tune_for_huggingface_text_generation::0.0.1
#  - fine_tune_for_huggingface_token_classification::0.0.1
#  - score_for_huggingface_text_classification::0.0.1
#  - score_for_huggingface_text_generation::0.0.1
#  - score_for_huggingface_token_classification::0.0.1
#  - sweep_for_huggingface_text_classification::0.0.1
#  - sweep_for_huggingface_text_generation::0.0.1
#  - sweep_for_huggingface_token_classification::0.0.1
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Union

from azure.ml.component import Component
from azure.ml.component.component import Input, Output
from azure.ml.component.dsl import _assets

from . import _workspace


SOURCE_DIRECTORY = Path(__file__).parent / ".."


class _DistributedComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shared_volumes: bool
    """Indicates whether to use shared volumes. Set to False if necessary to work around shared volume bugs on Windows. The default is True."""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""
    use_docker: bool
    """Specifies whether the environment to run the experiment should be Docker-based. Amlcompute linux clusters require that jobs running inside Docker containers. The backend will override the value to be true for Amlcompute linux clusters."""


class _DistributedComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _DistributedComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""
    node_count: int
    """Number of nodes in the compute target used for training. (min: 1)"""
    process_count_per_instance: int
    """Number of processes per instance. If greater than 1, mpi distributed job will be run. Only AmlCompute compute target is supported for distributed jobs. (min: 1, max: 8)"""


class _DistributedComponentRunsettingTargetSelector:
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""
    allow_spot_vm: bool
    """Flag to enable target selector service to send job to low priority VM. Currently it only works for AmlK8s."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    my_resource_only: bool
    """Flag to control whether the job should be sent to the cluster owned by user. If False, target selector may send the job to shared cluster. Currently it only works for AmlK8s."""
    regions: Union[str, list]
    """List of region that would like to submit job to. If no region specified, all regions are allowed."""
    vc_block_list: Union[str, list]
    """User specified block list of VC."""


class _DistributedComponentRunsetting:
    """Run setting configuration for DistributedComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _DistributedComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _DistributedComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    resource_layout: _DistributedComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    target_selector: _DistributedComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _ParallelComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shared_volumes: bool
    """Indicates whether to use shared volumes. Set to False if necessary to work around shared volume bugs on Windows. The default is True."""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""
    use_docker: bool
    """Specifies whether the environment to run the experiment should be Docker-based. Amlcompute linux clusters require that jobs running inside Docker containers. The backend will override the value to be true for Amlcompute linux clusters."""


class _ParallelComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _ParallelComponentRunsettingParallel:
    """This section contains specific settings for parallel component."""
    error_threshold: int
    """The number of record failures for TabularDataset and file failures for FileDataset that should be ignored during processing. If the error count goes above this value, then the job will be aborted. Error threshold is for the entire input and not for individual mini-batches sent to run() method. The range is [-1, int.max]. -1 indicates ignore all failures during processing. (min: -1, max: 2147483647)"""
    logging_level: str
    """A string of the logging level name, which is defined in 'logging'. Possible values are 'WARNING', 'INFO', and 'DEBUG'."""
    max_node_count: int
    """The maximum node count that the Parallel job can scale out to."""
    mini_batch_size: str
    """For FileDataset input, this field is the number of files user script can process in one run() call. For TabularDataset input, this field is the approximate size of data the user script can process in one run() call. Example values are 1024, 1024KB, 10MB, and 1GB."""
    node_count: int
    """Number of nodes in the compute target used for running the Parallel Run."""
    partition_keys: Union[str, list]
    """The keys used to partition dataset into mini-batches. If specified, the data with the same key will be partitioned into the same mini-batch. If both \"Partition keys\" and \"Mini batch size\" are specified, \"Mini batch size\" will be ignored. It should be a list of str element each being a key used to partition the input dataset."""
    process_count_per_node: int
    """Number of processes executed on each node. Optional, default value is number of cores on node."""
    run_invocation_timeout: int
    """Timeout in seconds for each invocation of the run() method."""
    run_max_try: int
    """The number of maximum tries for a failed or timeout mini batch. A mini batch with dequeue count greater than this won't be processed again and will be deleted directly. (min: 1)"""
    version: str
    """The version of back-end to serve the module. Please set as \"preview\" only if you are using preview feature and instructed to do so. Otherwise use the default value."""


class _ParallelComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""


class _ParallelComponentRunsettingTargetSelector:
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""
    allow_spot_vm: bool
    """Flag to enable target selector service to send job to low priority VM. Currently it only works for AmlK8s."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    my_resource_only: bool
    """Flag to control whether the job should be sent to the cluster owned by user. If False, target selector may send the job to shared cluster. Currently it only works for AmlK8s."""
    regions: Union[str, list]
    """List of region that would like to submit job to. If no region specified, all regions are allowed."""
    vc_block_list: Union[str, list]
    """User specified block list of VC."""


class _ParallelComponentRunsetting:
    """Run setting configuration for ParallelComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _ParallelComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _ParallelComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    parallel: _ParallelComponentRunsettingParallel
    """This section contains specific settings for parallel component."""
    resource_layout: _ParallelComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    target_selector: _ParallelComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _HDInsightComponentRunsettingHdinsight:
    """_HDInsightComponentRunsettingHdinsight"""
    conf: Union[str, dict]
    """Spark configuration properties"""
    driver_cores: int
    """Number of cores to use for the driver process"""
    driver_memory: str
    """Amount of memory to use for the driver process.It's the same format as JVM memory strings. Use lower-case suffixes, e.g. k, m, g, t, and p, for kibi-, mebi-, gibi-, tebi-, and pebibytes, respectively."""
    executor_cores: int
    """Number of cores to use for each executor"""
    executor_memory: str
    """Amount of memory to use per executor process. It's the same format as JVM memory strings. Use lower-case suffixes, e.g. k, m, g, t, and p, for kibi-, mebi-, gibi-, tebi-, and pebibytes, respectively."""
    name: str
    """The name of this session"""
    number_executors: int
    """Number of executors to launch for this session"""
    queue: str
    """The name of the YARN queue to which submitted"""


class _HDInsightComponentRunsetting:
    """Run setting configuration for HDInsightComponent"""
    target: str
    """Hdi Compute name that is attached to AML"""
    hdinsight: _HDInsightComponentRunsettingHdinsight
    """_HDInsightComponentRunsettingHdinsight"""


class _ScopeComponentRunsettingScope:
    """This section contains specific settings for scope component."""
    adla_account_name: str
    """The name of the Cosmos-migrated Azure Data Lake Analytics account to submit scope job."""
    custom_job_name_suffix: str
    """Optional parameter defining custom string to append to job name."""
    scope_param: str
    """Parameters to pass to scope e.g. Nebula parameters, VC allocation parameters etc."""


class _ScopeComponentRunsetting:
    """Run setting configuration for ScopeComponent"""
    scope: _ScopeComponentRunsettingScope
    """This section contains specific settings for scope component."""


class _SweepComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shared_volumes: bool
    """Indicates whether to use shared volumes. Set to False if necessary to work around shared volume bugs on Windows. The default is True."""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""
    use_docker: bool
    """Specifies whether the environment to run the experiment should be Docker-based. Amlcompute linux clusters require that jobs running inside Docker containers. The backend will override the value to be true for Amlcompute linux clusters."""


class _SweepComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _SweepComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""
    node_count: int
    """Number of nodes in the compute target used for training. (min: 1)"""


class _SweepComponentRunsettingEarlyTermination:
    """This section contains specific early termination settings for sweep component."""
    delay_evaluation: int
    """delays the first policy evaluation for a specified number of intervals."""
    evaluation_interval: int
    """the frequency for applying the policy."""
    policy_type: str
    """The early termination policy type. Current default means no termination policy. (enum: ['default', 'bandit', 'median_stopping', 'truncation_selection'])"""
    slack_amount: float
    """the slack amount allowed with respect to the best performing training run."""
    slack_factor: float
    """the slack ratio allowed with respect to the best performing training run."""
    truncation_percentage: int
    """the percentage of lowest performing runs to terminate at each evaluation interval. An integer value between 1 and 99. (min: 1, max: 99)"""


class _SweepComponentRunsettingLimits:
    """This section contains specific limits settings for sweep component."""
    max_concurrent_trials: int
    """Maximum number of runs that can run concurrently. If not specified, all runs launch in parallel. If specified, must be an integer between 1 and 100. (min: 1, max: 100)"""
    max_total_trials: int
    """Maximum number of training runs. Must be an integer between 1 and 1000. (min: 1, max: 1000)"""
    timeout_minutes: int
    """Maximum duration, in minutes, of the hyperparameter tuning experiment. Runs after this duration are canceled. (min: 0)"""


class _SweepComponentRunsettingObjective:
    """This section contains specific objective settings for sweep component."""
    goal: str
    """Whether the primary metric will be maximized or minimized when evaluating the runs. (enum: ['minimize', 'maximize'])"""
    primary_metric: str
    """The name of the primary metric needs to exactly match the name of the metric logged by the training script."""


class _SweepComponentRunsettingSweep:
    """_SweepComponentRunsettingSweep"""
    early_termination: _SweepComponentRunsettingEarlyTermination
    """This section contains specific early termination settings for sweep component."""
    limits: _SweepComponentRunsettingLimits
    """This section contains specific limits settings for sweep component."""
    objective: _SweepComponentRunsettingObjective
    """This section contains specific objective settings for sweep component."""


class _SweepComponentRunsettingTargetSelector:
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""
    allow_spot_vm: bool
    """Flag to enable target selector service to send job to low priority VM. Currently it only works for AmlK8s."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    my_resource_only: bool
    """Flag to control whether the job should be sent to the cluster owned by user. If False, target selector may send the job to shared cluster. Currently it only works for AmlK8s."""
    regions: Union[str, list]
    """List of region that would like to submit job to. If no region specified, all regions are allowed."""
    vc_block_list: Union[str, list]
    """User specified block list of VC."""


class _SweepComponentRunsetting:
    """Run setting configuration for SweepComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _SweepComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _SweepComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    resource_layout: _SweepComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    sweep: _SweepComponentRunsettingSweep
    """_SweepComponentRunsettingSweep"""
    target_selector: _SweepComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _CommandComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shared_volumes: bool
    """Indicates whether to use shared volumes. Set to False if necessary to work around shared volume bugs on Windows. The default is True."""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""
    use_docker: bool
    """Specifies whether the environment to run the experiment should be Docker-based. Amlcompute linux clusters require that jobs running inside Docker containers. The backend will override the value to be true for Amlcompute linux clusters."""


class _CommandComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _CommandComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""
    node_count: int
    """Number of nodes in the compute target used for training. (min: 1)"""


class _CommandComponentRunsettingTargetSelector:
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""
    allow_spot_vm: bool
    """Flag to enable target selector service to send job to low priority VM. Currently it only works for AmlK8s."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    my_resource_only: bool
    """Flag to control whether the job should be sent to the cluster owned by user. If False, target selector may send the job to shared cluster. Currently it only works for AmlK8s."""
    regions: Union[str, list]
    """List of region that would like to submit job to. If no region specified, all regions are allowed."""
    vc_block_list: Union[str, list]
    """User specified block list of VC."""


class _CommandComponentRunsetting:
    """Run setting configuration for CommandComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _CommandComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _CommandComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    resource_layout: _CommandComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    target_selector: _CommandComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageInput:
    input_path: Input = None
    """The directory contains dataframe."""
    string_parameter: str = None
    """A parameter accepts a string value. (optional)"""


class _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageOutput:
    output_path: Output = None
    """The directory contains a dataframe."""


class _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageComponent(Component):
    inputs: _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageInput
    outputs: _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageOutput
    runsettings: _DistributedComponentRunsetting


_microsoft_com_azureml_samples_hello_world_with_cpu_image = None


def microsoft_com_azureml_samples_hello_world_with_cpu_image(
    input_path: Path = None,
    string_parameter: str = None,
) -> _MicrosoftComAzuremlSamplesHelloWorldWithCpuImageComponent:
    """A hello world tutorial to create a module for ml.azure.com.
    
    :param input_path: The directory contains dataframe.
    :type input_path: Path
    :param string_parameter: A parameter accepts a string value. (optional)
    :type string_parameter: str
    :output output_path: The directory contains a dataframe.
    :type: output_path: Output
    """
    global _microsoft_com_azureml_samples_hello_world_with_cpu_image
    if _microsoft_com_azureml_samples_hello_world_with_cpu_image is None:
        _microsoft_com_azureml_samples_hello_world_with_cpu_image = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/microsoft_com_azureml_samples_hello_world_with_cpu_image/0.0.1/component.yaml")
    return _microsoft_com_azureml_samples_hello_world_with_cpu_image(
            input_path=input_path,
            string_parameter=string_parameter,)


class _MicrosoftComAzuremlSamplesParallelCopyFilesV1Input:
    input_folder: Input = None
    """AnyDirectory"""


class _MicrosoftComAzuremlSamplesParallelCopyFilesV1Output:
    output_folder: Output = None
    """Output images"""


class _MicrosoftComAzuremlSamplesParallelCopyFilesV1Component(Component):
    inputs: _MicrosoftComAzuremlSamplesParallelCopyFilesV1Input
    outputs: _MicrosoftComAzuremlSamplesParallelCopyFilesV1Output
    runsettings: _ParallelComponentRunsetting


_microsoft_com_azureml_samples_parallel_copy_files_v1 = None


def microsoft_com_azureml_samples_parallel_copy_files_v1(
    input_folder: Path = None,
) -> _MicrosoftComAzuremlSamplesParallelCopyFilesV1Component:
    """A sample Parallel module to copy files.
    
    :param input_folder: AnyDirectory
    :type input_folder: Path
    :output output_folder: Output images
    :type: output_folder: Output
    """
    global _microsoft_com_azureml_samples_parallel_copy_files_v1
    if _microsoft_com_azureml_samples_parallel_copy_files_v1 is None:
        _microsoft_com_azureml_samples_parallel_copy_files_v1 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/microsoft_com_azureml_samples_parallel_copy_files_v1/0.0.2/component.yaml")
    return _microsoft_com_azureml_samples_parallel_copy_files_v1(
            input_folder=input_folder,)


class _MicrosoftComAzuremlSamplesTrainInSparkInput:
    input_path: Input = None
    """Iris csv file"""
    regularization_rate: float = 0.01
    """Regularization rate when training with logistic regression (optional)"""


class _MicrosoftComAzuremlSamplesTrainInSparkOutput:
    output_path: Output = None
    """The output path to save the trained model to"""


class _MicrosoftComAzuremlSamplesTrainInSparkComponent(Component):
    inputs: _MicrosoftComAzuremlSamplesTrainInSparkInput
    outputs: _MicrosoftComAzuremlSamplesTrainInSparkOutput
    runsettings: _HDInsightComponentRunsetting


_microsoft_com_azureml_samples_train_in_spark = None


def microsoft_com_azureml_samples_train_in_spark(
    input_path: Path = None,
    regularization_rate: float = 0.01,
) -> _MicrosoftComAzuremlSamplesTrainInSparkComponent:
    """Train a Spark ML model using an HDInsight Spark cluster
    
    :param input_path: Iris csv file
    :type input_path: Path
    :param regularization_rate: Regularization rate when training with logistic regression (optional)
    :type regularization_rate: float
    :output output_path: The output path to save the trained model to
    :type: output_path: Output
    """
    global _microsoft_com_azureml_samples_train_in_spark
    if _microsoft_com_azureml_samples_train_in_spark is None:
        _microsoft_com_azureml_samples_train_in_spark = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/microsoft_com_azureml_samples_train_in_spark/0.0.1/component_spec.yaml")
    return _microsoft_com_azureml_samples_train_in_spark(
            input_path=input_path,
            regularization_rate=regularization_rate,)


class _BingRelevanceConvert2SsInput:
    TextData: Input = None
    """relative path on ADLS storage"""
    ExtractionClause: str = None
    """the extraction clause, something like \"column1:string, column2:int\""""


class _BingRelevanceConvert2SsOutput:
    SSPath: Output = None
    """output path of ss"""


class _BingRelevanceConvert2SsComponent(Component):
    inputs: _BingRelevanceConvert2SsInput
    outputs: _BingRelevanceConvert2SsOutput
    runsettings: _ScopeComponentRunsetting


_bing_relevance_convert2ss = None


def bing_relevance_convert2ss(
    TextData: Path = None,
    ExtractionClause: str = None,
) -> _BingRelevanceConvert2SsComponent:
    """Convert ADLS test data to SS format
    
    :param TextData: relative path on ADLS storage
    :type TextData: Path
    :param ExtractionClause: the extraction clause, something like \"column1:string, column2:int\"
    :type ExtractionClause: str
    :output SSPath: output path of ss
    :type: SSPath: Output
    """
    global _bing_relevance_convert2ss
    if _bing_relevance_convert2ss is None:
        _bing_relevance_convert2ss = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/bing_relevance_convert2ss/0.0.4/component_spec.yaml")
    return _bing_relevance_convert2ss(
            TextData=TextData,
            ExtractionClause=ExtractionClause,)


class _MicrosoftComAzuremlSamplesTuneInput:
    training_data: Input = None
    """Training data organized in the torchvision format/structure"""
    max_epochs: int = None
    """Maximum number of epochs for the training"""
    learning_rate: float = None
    """learning_rate (min: 0.001, max: 0.1)"""
    subsample: float = None
    """learning_rate (min: 0.1, max: 0.5)"""


class _MicrosoftComAzuremlSamplesTuneOutput:
    best_model: Output = None
    """model"""
    saved_model: Output = None
    """path"""
    other_output: Output = None
    """path"""


class _MicrosoftComAzuremlSamplesTuneComponent(Component):
    inputs: _MicrosoftComAzuremlSamplesTuneInput
    outputs: _MicrosoftComAzuremlSamplesTuneOutput
    runsettings: _SweepComponentRunsetting


_microsoft_com_azureml_samples_tune = None


def microsoft_com_azureml_samples_tune(
    training_data: Path = None,
    max_epochs: int = None,
    learning_rate: float = None,
    subsample: float = None,
) -> _MicrosoftComAzuremlSamplesTuneComponent:
    """A dummy hyperparameter tuning component
    
    :param training_data: Training data organized in the torchvision format/structure
    :type training_data: Path
    :param max_epochs: Maximum number of epochs for the training
    :type max_epochs: int
    :param learning_rate: learning_rate (min: 0.001, max: 0.1)
    :type learning_rate: float
    :param subsample: learning_rate (min: 0.1, max: 0.5)
    :type subsample: float
    :output best_model: model
    :type: best_model: Output
    :output saved_model: path
    :type: saved_model: Output
    :output other_output: path
    :type: other_output: Output
    """
    global _microsoft_com_azureml_samples_tune
    if _microsoft_com_azureml_samples_tune is None:
        _microsoft_com_azureml_samples_tune = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/microsoft_com_azureml_samples_tune/0.0.4/sweep.spec.yaml")
    return _microsoft_com_azureml_samples_tune(
            training_data=training_data,
            max_epochs=max_epochs,
            learning_rate=learning_rate,
            subsample=subsample,)


class _AzuremlAddColumnsInput:
    left_dataset: Input = None
    """Left dataset"""
    right_dataset: Input = None
    """Right dataset"""


class _AzuremlAddColumnsOutput:
    combined_dataset: Output = None
    """Combined dataset"""


class _AzuremlAddColumnsComponent(Component):
    inputs: _AzuremlAddColumnsInput
    outputs: _AzuremlAddColumnsOutput
    runsettings: _CommandComponentRunsetting


_azureml_add_columns = None


def azureml_add_columns(
    left_dataset: Path = None,
    right_dataset: Path = None,
) -> _AzuremlAddColumnsComponent:
    """Adds a set of columns from one dataset to another.
    
    :param left_dataset: Left dataset
    :type left_dataset: Path
    :param right_dataset: Right dataset
    :type right_dataset: Path
    :output combined_dataset: Combined dataset
    :type: combined_dataset: Output
    """
    global _azureml_add_columns
    if _azureml_add_columns is None:
        _azureml_add_columns = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Add Columns', version=None, feed='azureml')
    return _azureml_add_columns(
            left_dataset=left_dataset,
            right_dataset=right_dataset,)


class _AzuremlAddRowsInput:
    dataset1: Input = None
    """Dataset rows to be added to the output dataset first"""
    dataset2: Input = None
    """Dataset rows to be appended to the first dataset"""


class _AzuremlAddRowsOutput:
    results_dataset: Output = None
    """Dataset that contains all rows of both input datasets"""


class _AzuremlAddRowsComponent(Component):
    inputs: _AzuremlAddRowsInput
    outputs: _AzuremlAddRowsOutput
    runsettings: _CommandComponentRunsetting


_azureml_add_rows = None


def azureml_add_rows(
    dataset1: Path = None,
    dataset2: Path = None,
) -> _AzuremlAddRowsComponent:
    """Appends a set of rows from an input dataset to the end of another dataset.
    
    :param dataset1: Dataset rows to be added to the output dataset first
    :type dataset1: Path
    :param dataset2: Dataset rows to be appended to the first dataset
    :type dataset2: Path
    :output results_dataset: Dataset that contains all rows of both input datasets
    :type: results_dataset: Output
    """
    global _azureml_add_rows
    if _azureml_add_rows is None:
        _azureml_add_rows = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Add Rows', version=None, feed='azureml')
    return _azureml_add_rows(
            dataset1=dataset1,
            dataset2=dataset2,)


class _AzuremlApplyImageTransformationModeEnum(Enum):
    for_training = 'For training'
    for_inference = 'For inference'


class _AzuremlApplyImageTransformationInput:
    input_image_transformation: Input = None
    """Input image transformation"""
    input_image_directory: Input = None
    """Input image directory"""
    mode: _AzuremlApplyImageTransformationModeEnum = None
    """Should exclude 'Random' transform operations in inference but keep them in training (enum: ['For training', 'For inference'])"""


class _AzuremlApplyImageTransformationOutput:
    output_image_directory: Output = None
    """Output image directory"""


class _AzuremlApplyImageTransformationComponent(Component):
    inputs: _AzuremlApplyImageTransformationInput
    outputs: _AzuremlApplyImageTransformationOutput
    runsettings: _CommandComponentRunsetting


_azureml_apply_image_transformation = None


def azureml_apply_image_transformation(
    input_image_transformation: Path = None,
    input_image_directory: Path = None,
    mode: _AzuremlApplyImageTransformationModeEnum = None,
) -> _AzuremlApplyImageTransformationComponent:
    """Applies a image transformation to a image directory.
    
    :param input_image_transformation: Input image transformation
    :type input_image_transformation: Path
    :param input_image_directory: Input image directory
    :type input_image_directory: Path
    :param mode: Should exclude 'Random' transform operations in inference but keep them in training (enum: ['For training', 'For inference'])
    :type mode: _AzuremlApplyImageTransformationModeEnum
    :output output_image_directory: Output image directory
    :type: output_image_directory: Output
    """
    global _azureml_apply_image_transformation
    if _azureml_apply_image_transformation is None:
        _azureml_apply_image_transformation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Apply Image Transformation', version=None, feed='azureml')
    return _azureml_apply_image_transformation(
            input_image_transformation=input_image_transformation,
            input_image_directory=input_image_directory,
            mode=mode,)


class _AzuremlApplyMathOperationCategoryEnum(Enum):
    basic = 'Basic'
    compare = 'Compare'
    operations = 'Operations'
    rounding = 'Rounding'
    special = 'Special'
    trigonometric = 'Trigonometric'


class _AzuremlApplyMathOperationBasicFuncEnum(Enum):
    abs = 'Abs'
    atan2 = 'Atan2'
    conj = 'Conj'
    cuberoot = 'Cuberoot'
    doublefactorial = 'DoubleFactorial'
    eps = 'Eps'
    exp = 'Exp'
    exp2 = 'Exp2'
    expminus1 = 'ExpMinus1'
    factorial = 'Factorial'
    hypotenuse = 'Hypotenuse'
    imaginarypart = 'ImaginaryPart'
    ln = 'Ln'
    lnplus1 = 'LnPlus1'
    log = 'Log'
    log10 = 'Log10'
    log2 = 'Log2'
    nthroot = 'NthRoot'
    pow = 'Pow'
    realpart = 'RealPart'
    sqrt = 'Sqrt'
    sqrtpi = 'SqrtPi'
    square = 'Square'


class _AzuremlApplyMathOperationBasicArgTypeEnum(Enum):
    constant = 'Constant'
    columnset = 'ColumnSet'


class _AzuremlApplyMathOperationCompareFuncEnum(Enum):
    equalto = 'EqualTo'
    greaterthan = 'GreaterThan'
    greaterthanorequalto = 'GreaterThanOrEqualTo'
    lessthan = 'LessThan'
    lessthanorequalto = 'LessThanOrEqualTo'
    notequalto = 'NotEqualTo'
    pairmax = 'PairMax'
    pairmin = 'PairMin'


class _AzuremlApplyMathOperationCompareArgTypeEnum(Enum):
    constant = 'Constant'
    columnset = 'ColumnSet'


class _AzuremlApplyMathOperationOperationsFuncEnum(Enum):
    add = 'Add'
    divide = 'Divide'
    multiply = 'Multiply'
    subtract = 'Subtract'


class _AzuremlApplyMathOperationOperationsArgTypeEnum(Enum):
    constant = 'Constant'
    columnset = 'ColumnSet'


class _AzuremlApplyMathOperationRoundingFuncEnum(Enum):
    ceiling = 'Ceiling'
    ceilingpower2 = 'CeilingPower2'
    floor = 'Floor'
    mod = 'Mod'
    quotient = 'Quotient'
    remainder = 'Remainder'
    rounddigits = 'RoundDigits'
    rounddown = 'RoundDown'
    roundup = 'RoundUp'
    toeven = 'ToEven'
    tomultiple = 'ToMultiple'
    toodd = 'ToOdd'
    truncate = 'Truncate'


class _AzuremlApplyMathOperationRoundingArgTypeEnum(Enum):
    constant = 'Constant'
    columnset = 'ColumnSet'


class _AzuremlApplyMathOperationSpecialFuncEnum(Enum):
    beta = 'Beta'
    betaln = 'BetaLn'
    ellipticintegrale = 'EllipticIntegralE'
    ellipticintegralk = 'EllipticIntegralK'
    erf = 'Erf'
    erfc = 'Erfc'
    erfcscaled = 'ErfcScaled'
    erfinverse = 'ErfInverse'
    exponentialintegralein = 'ExponentialIntegralEin'
    gamma = 'Gamma'
    gammaln = 'GammaLn'
    gammaregularizedp = 'GammaRegularizedP'
    gammaregularizedpinverse = 'GammaRegularizedPInverse'
    gammaregularizedq = 'GammaRegularizedQ'
    gammaregularizedqinverse = 'GammaRegularizedQInverse'
    polygamma = 'Polygamma'


class _AzuremlApplyMathOperationSpecialArgTypeEnum(Enum):
    constant = 'Constant'
    columnset = 'ColumnSet'


class _AzuremlApplyMathOperationTrigonometricFuncEnum(Enum):
    acos = 'Acos'
    acosdegrees = 'AcosDegrees'
    acosh = 'Acosh'
    acot = 'Acot'
    acotdegrees = 'AcotDegrees'
    acoth = 'Acoth'
    acsc = 'Acsc'
    acscdegrees = 'AcscDegrees'
    acsch = 'Acsch'
    arg = 'Arg'
    asec = 'Asec'
    asecdegrees = 'AsecDegrees'
    asech = 'Asech'
    asin = 'Asin'
    asindegrees = 'AsinDegrees'
    asinh = 'Asinh'
    atan = 'Atan'
    atandegrees = 'AtanDegrees'
    atanh = 'Atanh'
    cis = 'Cis'
    cos = 'Cos'
    cosdegrees = 'CosDegrees'
    cosh = 'Cosh'
    cot = 'Cot'
    cotdegrees = 'CotDegrees'
    coth = 'Coth'
    csc = 'Csc'
    cscdegrees = 'CscDegrees'
    csch = 'Csch'
    degreestoradians = 'DegreesToRadians'
    radianstodegrees = 'RadiansToDegrees'
    sec = 'Sec'
    secdegrees = 'SecDegrees'
    sech = 'Sech'
    sign = 'Sign'
    sin = 'Sin'
    sinc = 'Sinc'
    sindegrees = 'SinDegrees'
    sinh = 'Sinh'
    tan = 'Tan'
    tandegrees = 'TanDegrees'
    tanh = 'Tanh'


class _AzuremlApplyMathOperationOutputModeEnum(Enum):
    append = 'Append'
    inplace = 'Inplace'
    resultonly = 'ResultOnly'


class _AzuremlApplyMathOperationInput:
    input: Input = None
    """DataFrameDirectory"""
    category: _AzuremlApplyMathOperationCategoryEnum = _AzuremlApplyMathOperationCategoryEnum.basic
    """enum (enum: ['Basic', 'Compare', 'Operations', 'Rounding', 'Special', 'Trigonometric'])"""
    basic_func: _AzuremlApplyMathOperationBasicFuncEnum = _AzuremlApplyMathOperationBasicFuncEnum.abs
    """enum (optional, enum: ['Abs', 'Atan2', 'Conj', 'Cuberoot', 'DoubleFactorial', 'Eps', 'Exp', 'Exp2', 'ExpMinus1', 'Factorial', 'Hypotenuse', 'ImaginaryPart', 'Ln', 'LnPlus1', 'Log', 'Log10', 'Log2', 'NthRoot', 'Pow', 'RealPart', 'Sqrt', 'SqrtPi', 'Square'])"""
    basic_arg_type: _AzuremlApplyMathOperationBasicArgTypeEnum = _AzuremlApplyMathOperationBasicArgTypeEnum.constant
    """enum (optional, enum: ['Constant', 'ColumnSet'])"""
    basic_constant: float = 1
    """float (optional)"""
    basic_column_selector: str = None
    """ColumnPicker (optional)"""
    compare_func: _AzuremlApplyMathOperationCompareFuncEnum = _AzuremlApplyMathOperationCompareFuncEnum.equalto
    """enum (optional, enum: ['EqualTo', 'GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'PairMax', 'PairMin'])"""
    compare_arg_type: _AzuremlApplyMathOperationCompareArgTypeEnum = _AzuremlApplyMathOperationCompareArgTypeEnum.constant
    """enum (optional, enum: ['Constant', 'ColumnSet'])"""
    compare_constant: float = 1
    """float (optional)"""
    compare_column_selector: str = None
    """ColumnPicker (optional)"""
    operations_func: _AzuremlApplyMathOperationOperationsFuncEnum = _AzuremlApplyMathOperationOperationsFuncEnum.add
    """enum (optional, enum: ['Add', 'Divide', 'Multiply', 'Subtract'])"""
    operations_arg_type: _AzuremlApplyMathOperationOperationsArgTypeEnum = _AzuremlApplyMathOperationOperationsArgTypeEnum.constant
    """enum (optional, enum: ['Constant', 'ColumnSet'])"""
    operations_constant: float = 1
    """float (optional)"""
    operations_column_selector: str = None
    """ColumnPicker (optional)"""
    rounding_func: _AzuremlApplyMathOperationRoundingFuncEnum = _AzuremlApplyMathOperationRoundingFuncEnum.ceiling
    """enum (optional, enum: ['Ceiling', 'CeilingPower2', 'Floor', 'Mod', 'Quotient', 'Remainder', 'RoundDigits', 'RoundDown', 'RoundUp', 'ToEven', 'ToMultiple', 'ToOdd', 'Truncate'])"""
    rounding_arg_type: _AzuremlApplyMathOperationRoundingArgTypeEnum = _AzuremlApplyMathOperationRoundingArgTypeEnum.constant
    """enum (optional, enum: ['Constant', 'ColumnSet'])"""
    rounding_constant: float = 1
    """float (optional)"""
    rounding_column_selector: str = None
    """ColumnPicker (optional)"""
    special_func: _AzuremlApplyMathOperationSpecialFuncEnum = _AzuremlApplyMathOperationSpecialFuncEnum.beta
    """enum (optional, enum: ['Beta', 'BetaLn', 'EllipticIntegralE', 'EllipticIntegralK', 'Erf', 'Erfc', 'ErfcScaled', 'ErfInverse', 'ExponentialIntegralEin', 'Gamma', 'GammaLn', 'GammaRegularizedP', 'GammaRegularizedPInverse', 'GammaRegularizedQ', 'GammaRegularizedQInverse', 'Polygamma'])"""
    special_arg_type: _AzuremlApplyMathOperationSpecialArgTypeEnum = _AzuremlApplyMathOperationSpecialArgTypeEnum.constant
    """enum (optional, enum: ['Constant', 'ColumnSet'])"""
    special_constant: float = 1
    """float (optional)"""
    special_column_selector: str = None
    """ColumnPicker (optional)"""
    trigonometric_func: _AzuremlApplyMathOperationTrigonometricFuncEnum = _AzuremlApplyMathOperationTrigonometricFuncEnum.acos
    """enum (optional, enum: ['Acos', 'AcosDegrees', 'Acosh', 'Acot', 'AcotDegrees', 'Acoth', 'Acsc', 'AcscDegrees', 'Acsch', 'Arg', 'Asec', 'AsecDegrees', 'Asech', 'Asin', 'AsinDegrees', 'Asinh', 'Atan', 'AtanDegrees', 'Atanh', 'Cis', 'Cos', 'CosDegrees', 'Cosh', 'Cot', 'CotDegrees', 'Coth', 'Csc', 'CscDegrees', 'Csch', 'DegreesToRadians', 'RadiansToDegrees', 'Sec', 'SecDegrees', 'Sech', 'Sign', 'Sin', 'Sinc', 'SinDegrees', 'Sinh', 'Tan', 'TanDegrees', 'Tanh'])"""
    column_selector: str = None
    """ColumnPicker"""
    output_mode: _AzuremlApplyMathOperationOutputModeEnum = _AzuremlApplyMathOperationOutputModeEnum.append
    """enum (enum: ['Append', 'Inplace', 'ResultOnly'])"""


class _AzuremlApplyMathOperationOutput:
    result_dataset: Output = None
    """DataFrameDirectory"""


class _AzuremlApplyMathOperationComponent(Component):
    inputs: _AzuremlApplyMathOperationInput
    outputs: _AzuremlApplyMathOperationOutput
    runsettings: _CommandComponentRunsetting


_azureml_apply_math_operation = None


def azureml_apply_math_operation(
    input: Path = None,
    category: _AzuremlApplyMathOperationCategoryEnum = _AzuremlApplyMathOperationCategoryEnum.basic,
    basic_func: _AzuremlApplyMathOperationBasicFuncEnum = _AzuremlApplyMathOperationBasicFuncEnum.abs,
    basic_arg_type: _AzuremlApplyMathOperationBasicArgTypeEnum = _AzuremlApplyMathOperationBasicArgTypeEnum.constant,
    basic_constant: float = 1,
    basic_column_selector: str = None,
    compare_func: _AzuremlApplyMathOperationCompareFuncEnum = _AzuremlApplyMathOperationCompareFuncEnum.equalto,
    compare_arg_type: _AzuremlApplyMathOperationCompareArgTypeEnum = _AzuremlApplyMathOperationCompareArgTypeEnum.constant,
    compare_constant: float = 1,
    compare_column_selector: str = None,
    operations_func: _AzuremlApplyMathOperationOperationsFuncEnum = _AzuremlApplyMathOperationOperationsFuncEnum.add,
    operations_arg_type: _AzuremlApplyMathOperationOperationsArgTypeEnum = _AzuremlApplyMathOperationOperationsArgTypeEnum.constant,
    operations_constant: float = 1,
    operations_column_selector: str = None,
    rounding_func: _AzuremlApplyMathOperationRoundingFuncEnum = _AzuremlApplyMathOperationRoundingFuncEnum.ceiling,
    rounding_arg_type: _AzuremlApplyMathOperationRoundingArgTypeEnum = _AzuremlApplyMathOperationRoundingArgTypeEnum.constant,
    rounding_constant: float = 1,
    rounding_column_selector: str = None,
    special_func: _AzuremlApplyMathOperationSpecialFuncEnum = _AzuremlApplyMathOperationSpecialFuncEnum.beta,
    special_arg_type: _AzuremlApplyMathOperationSpecialArgTypeEnum = _AzuremlApplyMathOperationSpecialArgTypeEnum.constant,
    special_constant: float = 1,
    special_column_selector: str = None,
    trigonometric_func: _AzuremlApplyMathOperationTrigonometricFuncEnum = _AzuremlApplyMathOperationTrigonometricFuncEnum.acos,
    column_selector: str = None,
    output_mode: _AzuremlApplyMathOperationOutputModeEnum = _AzuremlApplyMathOperationOutputModeEnum.append,
) -> _AzuremlApplyMathOperationComponent:
    """Applies a mathematical operation to column values.
    
    :param input: DataFrameDirectory
    :type input: Path
    :param category: enum (enum: ['Basic', 'Compare', 'Operations', 'Rounding', 'Special', 'Trigonometric'])
    :type category: _AzuremlApplyMathOperationCategoryEnum
    :param basic_func: enum (optional, enum: ['Abs', 'Atan2', 'Conj', 'Cuberoot', 'DoubleFactorial', 'Eps', 'Exp', 'Exp2', 'ExpMinus1', 'Factorial', 'Hypotenuse', 'ImaginaryPart', 'Ln', 'LnPlus1', 'Log', 'Log10', 'Log2', 'NthRoot', 'Pow', 'RealPart', 'Sqrt', 'SqrtPi', 'Square'])
    :type basic_func: _AzuremlApplyMathOperationBasicFuncEnum
    :param basic_arg_type: enum (optional, enum: ['Constant', 'ColumnSet'])
    :type basic_arg_type: _AzuremlApplyMathOperationBasicArgTypeEnum
    :param basic_constant: float (optional)
    :type basic_constant: float
    :param basic_column_selector: ColumnPicker (optional)
    :type basic_column_selector: str
    :param compare_func: enum (optional, enum: ['EqualTo', 'GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo', 'NotEqualTo', 'PairMax', 'PairMin'])
    :type compare_func: _AzuremlApplyMathOperationCompareFuncEnum
    :param compare_arg_type: enum (optional, enum: ['Constant', 'ColumnSet'])
    :type compare_arg_type: _AzuremlApplyMathOperationCompareArgTypeEnum
    :param compare_constant: float (optional)
    :type compare_constant: float
    :param compare_column_selector: ColumnPicker (optional)
    :type compare_column_selector: str
    :param operations_func: enum (optional, enum: ['Add', 'Divide', 'Multiply', 'Subtract'])
    :type operations_func: _AzuremlApplyMathOperationOperationsFuncEnum
    :param operations_arg_type: enum (optional, enum: ['Constant', 'ColumnSet'])
    :type operations_arg_type: _AzuremlApplyMathOperationOperationsArgTypeEnum
    :param operations_constant: float (optional)
    :type operations_constant: float
    :param operations_column_selector: ColumnPicker (optional)
    :type operations_column_selector: str
    :param rounding_func: enum (optional, enum: ['Ceiling', 'CeilingPower2', 'Floor', 'Mod', 'Quotient', 'Remainder', 'RoundDigits', 'RoundDown', 'RoundUp', 'ToEven', 'ToMultiple', 'ToOdd', 'Truncate'])
    :type rounding_func: _AzuremlApplyMathOperationRoundingFuncEnum
    :param rounding_arg_type: enum (optional, enum: ['Constant', 'ColumnSet'])
    :type rounding_arg_type: _AzuremlApplyMathOperationRoundingArgTypeEnum
    :param rounding_constant: float (optional)
    :type rounding_constant: float
    :param rounding_column_selector: ColumnPicker (optional)
    :type rounding_column_selector: str
    :param special_func: enum (optional, enum: ['Beta', 'BetaLn', 'EllipticIntegralE', 'EllipticIntegralK', 'Erf', 'Erfc', 'ErfcScaled', 'ErfInverse', 'ExponentialIntegralEin', 'Gamma', 'GammaLn', 'GammaRegularizedP', 'GammaRegularizedPInverse', 'GammaRegularizedQ', 'GammaRegularizedQInverse', 'Polygamma'])
    :type special_func: _AzuremlApplyMathOperationSpecialFuncEnum
    :param special_arg_type: enum (optional, enum: ['Constant', 'ColumnSet'])
    :type special_arg_type: _AzuremlApplyMathOperationSpecialArgTypeEnum
    :param special_constant: float (optional)
    :type special_constant: float
    :param special_column_selector: ColumnPicker (optional)
    :type special_column_selector: str
    :param trigonometric_func: enum (optional, enum: ['Acos', 'AcosDegrees', 'Acosh', 'Acot', 'AcotDegrees', 'Acoth', 'Acsc', 'AcscDegrees', 'Acsch', 'Arg', 'Asec', 'AsecDegrees', 'Asech', 'Asin', 'AsinDegrees', 'Asinh', 'Atan', 'AtanDegrees', 'Atanh', 'Cis', 'Cos', 'CosDegrees', 'Cosh', 'Cot', 'CotDegrees', 'Coth', 'Csc', 'CscDegrees', 'Csch', 'DegreesToRadians', 'RadiansToDegrees', 'Sec', 'SecDegrees', 'Sech', 'Sign', 'Sin', 'Sinc', 'SinDegrees', 'Sinh', 'Tan', 'TanDegrees', 'Tanh'])
    :type trigonometric_func: _AzuremlApplyMathOperationTrigonometricFuncEnum
    :param column_selector: ColumnPicker
    :type column_selector: str
    :param output_mode: enum (enum: ['Append', 'Inplace', 'ResultOnly'])
    :type output_mode: _AzuremlApplyMathOperationOutputModeEnum
    :output result_dataset: DataFrameDirectory
    :type: result_dataset: Output
    """
    global _azureml_apply_math_operation
    if _azureml_apply_math_operation is None:
        _azureml_apply_math_operation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Apply Math Operation', version=None, feed='azureml')
    return _azureml_apply_math_operation(
            input=input,
            category=category,
            basic_func=basic_func,
            basic_arg_type=basic_arg_type,
            basic_constant=basic_constant,
            basic_column_selector=basic_column_selector,
            compare_func=compare_func,
            compare_arg_type=compare_arg_type,
            compare_constant=compare_constant,
            compare_column_selector=compare_column_selector,
            operations_func=operations_func,
            operations_arg_type=operations_arg_type,
            operations_constant=operations_constant,
            operations_column_selector=operations_column_selector,
            rounding_func=rounding_func,
            rounding_arg_type=rounding_arg_type,
            rounding_constant=rounding_constant,
            rounding_column_selector=rounding_column_selector,
            special_func=special_func,
            special_arg_type=special_arg_type,
            special_constant=special_constant,
            special_column_selector=special_column_selector,
            trigonometric_func=trigonometric_func,
            column_selector=column_selector,
            output_mode=output_mode,)


class _AzuremlApplySqlTransformationInput:
    t1: Input = None
    """DataFrameDirectory"""
    t2: Input = None
    """DataFrameDirectory(optional)"""
    t3: Input = None
    """DataFrameDirectory(optional)"""
    sqlquery: str = 'select * from t1'
    """Script"""


class _AzuremlApplySqlTransformationOutput:
    result_dataset: Output = None
    """DataFrameDirectory"""


class _AzuremlApplySqlTransformationComponent(Component):
    inputs: _AzuremlApplySqlTransformationInput
    outputs: _AzuremlApplySqlTransformationOutput
    runsettings: _CommandComponentRunsetting


_azureml_apply_sql_transformation = None


def azureml_apply_sql_transformation(
    t1: Path = None,
    t2: Path = None,
    t3: Path = None,
    sqlquery: str = 'select * from t1',
) -> _AzuremlApplySqlTransformationComponent:
    """Runs a SQLite query on input datasets to transform the data.
    
    :param t1: DataFrameDirectory
    :type t1: Path
    :param t2: DataFrameDirectory(optional)
    :type t2: Path
    :param t3: DataFrameDirectory(optional)
    :type t3: Path
    :param sqlquery: Script
    :type sqlquery: str
    :output result_dataset: DataFrameDirectory
    :type: result_dataset: Output
    """
    global _azureml_apply_sql_transformation
    if _azureml_apply_sql_transformation is None:
        _azureml_apply_sql_transformation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Apply SQL Transformation', version=None, feed='azureml')
    return _azureml_apply_sql_transformation(
            t1=t1,
            t2=t2,
            t3=t3,
            sqlquery=sqlquery,)


class _AzuremlApplyTransformationInput:
    transformation: Input = None
    """A unary data transformation"""
    dataset: Input = None
    """Dataset to be transformed"""


class _AzuremlApplyTransformationOutput:
    transformed_dataset: Output = None
    """Transformed dataset"""


class _AzuremlApplyTransformationComponent(Component):
    inputs: _AzuremlApplyTransformationInput
    outputs: _AzuremlApplyTransformationOutput
    runsettings: _CommandComponentRunsetting


_azureml_apply_transformation = None


def azureml_apply_transformation(
    transformation: Path = None,
    dataset: Path = None,
) -> _AzuremlApplyTransformationComponent:
    """Applies a well-specified data transformation to a dataset.
    
    :param transformation: A unary data transformation
    :type transformation: Path
    :param dataset: Dataset to be transformed
    :type dataset: Path
    :output transformed_dataset: Transformed dataset
    :type: transformed_dataset: Output
    """
    global _azureml_apply_transformation
    if _azureml_apply_transformation is None:
        _azureml_apply_transformation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Apply Transformation', version=None, feed='azureml')
    return _azureml_apply_transformation(
            transformation=transformation,
            dataset=dataset,)


class _AzuremlAssignDataToClustersInput:
    trained_model: Input = None
    """Trained clustering model"""
    dataset: Input = None
    """Input data source"""
    check_for_append_or_uncheck_for_result_only: bool = True
    """Whether output dataset must contain input dataset appended by assignments column (Checked) or assignments column only (Unchecked)"""


class _AzuremlAssignDataToClustersOutput:
    results_dataset: Output = None
    """Input dataset appended by data column of assignments or assignments column only"""


class _AzuremlAssignDataToClustersComponent(Component):
    inputs: _AzuremlAssignDataToClustersInput
    outputs: _AzuremlAssignDataToClustersOutput
    runsettings: _CommandComponentRunsetting


_azureml_assign_data_to_clusters = None


def azureml_assign_data_to_clusters(
    trained_model: Path = None,
    dataset: Path = None,
    check_for_append_or_uncheck_for_result_only: bool = True,
) -> _AzuremlAssignDataToClustersComponent:
    """Assign data to clusters using an existing trained clustering model.
    
    :param trained_model: Trained clustering model
    :type trained_model: Path
    :param dataset: Input data source
    :type dataset: Path
    :param check_for_append_or_uncheck_for_result_only: Whether output dataset must contain input dataset appended by assignments column (Checked) or assignments column only (Unchecked)
    :type check_for_append_or_uncheck_for_result_only: bool
    :output results_dataset: Input dataset appended by data column of assignments or assignments column only
    :type: results_dataset: Output
    """
    global _azureml_assign_data_to_clusters
    if _azureml_assign_data_to_clusters is None:
        _azureml_assign_data_to_clusters = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Assign Data to Clusters', version=None, feed='azureml')
    return _azureml_assign_data_to_clusters(
            trained_model=trained_model,
            dataset=dataset,
            check_for_append_or_uncheck_for_result_only=check_for_append_or_uncheck_for_result_only,)


class _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlBoostedDecisionTreeRegressionInput:
    create_trainer_mode: _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum = _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    maximum_number_of_leaves_per_tree: int = 20
    """Specify the maximum number of leaves per tree (optional, min: 2, max: 131072)"""
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10
    """Specify the minimum number of cases required to form a leaf node (optional, min: 1)"""
    the_learning_rate: float = 0.2
    """Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)"""
    total_number_of_trees_constructed: int = 100
    """Specify the maximum number of trees that can be created during training (optional, min: 1)"""
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128'
    """Specify range for the maximum number of leaves allowed per tree (optional)"""
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50'
    """Specify the range for the minimum number of cases required to form a leaf (optional)"""
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4'
    """Specify the range for the initial learning rate (optional)"""
    range_for_total_number_of_trees_constructed: str = '20; 100; 500'
    """Specify the range for the maximum number of trees that can be created during training (optional)"""
    random_number_seed: int = None
    """Provide a seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlBoostedDecisionTreeRegressionOutput:
    untrained_model: Output = None
    """An untrained regression model that can be connected to the Train Generic Model or Cross Validate Model modules"""


class _AzuremlBoostedDecisionTreeRegressionComponent(Component):
    inputs: _AzuremlBoostedDecisionTreeRegressionInput
    outputs: _AzuremlBoostedDecisionTreeRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_boosted_decision_tree_regression = None


def azureml_boosted_decision_tree_regression(
    create_trainer_mode: _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum = _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum.singleparameter,
    maximum_number_of_leaves_per_tree: int = 20,
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10,
    the_learning_rate: float = 0.2,
    total_number_of_trees_constructed: int = 100,
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128',
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50',
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4',
    range_for_total_number_of_trees_constructed: str = '20; 100; 500',
    random_number_seed: int = None,
) -> _AzuremlBoostedDecisionTreeRegressionComponent:
    """Creates a regression model using the Boosted Decision Tree algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlBoostedDecisionTreeRegressionCreateTrainerModeEnum
    :param maximum_number_of_leaves_per_tree: Specify the maximum number of leaves per tree (optional, min: 2, max: 131072)
    :type maximum_number_of_leaves_per_tree: int
    :param minimum_number_of_training_instances_required_to_form_a_leaf: Specify the minimum number of cases required to form a leaf node (optional, min: 1)
    :type minimum_number_of_training_instances_required_to_form_a_leaf: int
    :param the_learning_rate: Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)
    :type the_learning_rate: float
    :param total_number_of_trees_constructed: Specify the maximum number of trees that can be created during training (optional, min: 1)
    :type total_number_of_trees_constructed: int
    :param range_for_maximum_number_of_leaves_per_tree: Specify range for the maximum number of leaves allowed per tree (optional)
    :type range_for_maximum_number_of_leaves_per_tree: str
    :param range_for_minimum_number_of_training_instances_required_to_form_a_leaf: Specify the range for the minimum number of cases required to form a leaf (optional)
    :type range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str
    :param range_for_learning_rate: Specify the range for the initial learning rate (optional)
    :type range_for_learning_rate: str
    :param range_for_total_number_of_trees_constructed: Specify the range for the maximum number of trees that can be created during training (optional)
    :type range_for_total_number_of_trees_constructed: str
    :param random_number_seed: Provide a seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained regression model that can be connected to the Train Generic Model or Cross Validate Model modules
    :type: untrained_model: Output
    """
    global _azureml_boosted_decision_tree_regression
    if _azureml_boosted_decision_tree_regression is None:
        _azureml_boosted_decision_tree_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Boosted Decision Tree Regression', version=None, feed='azureml')
    return _azureml_boosted_decision_tree_regression(
            create_trainer_mode=create_trainer_mode,
            maximum_number_of_leaves_per_tree=maximum_number_of_leaves_per_tree,
            minimum_number_of_training_instances_required_to_form_a_leaf=minimum_number_of_training_instances_required_to_form_a_leaf,
            the_learning_rate=the_learning_rate,
            total_number_of_trees_constructed=total_number_of_trees_constructed,
            range_for_maximum_number_of_leaves_per_tree=range_for_maximum_number_of_leaves_per_tree,
            range_for_minimum_number_of_training_instances_required_to_form_a_leaf=range_for_minimum_number_of_training_instances_required_to_form_a_leaf,
            range_for_learning_rate=range_for_learning_rate,
            range_for_total_number_of_trees_constructed=range_for_total_number_of_trees_constructed,
            random_number_seed=random_number_seed,)


class _AzuremlCleanMissingDataCleaningModeEnum(Enum):
    custom_substitution_value = 'Custom substitution value'
    replace_with_mean = 'Replace with mean'
    replace_with_median = 'Replace with median'
    replace_with_mode = 'Replace with mode'
    remove_entire_row = 'Remove entire row'
    remove_entire_column = 'Remove entire column'


class _AzuremlCleanMissingDataColsWithAllMissingValuesEnum(Enum):
    propagate = 'Propagate'
    remove = 'Remove'


class _AzuremlCleanMissingDataInput:
    dataset: Input = None
    """Dataset to be cleaned"""
    columns_to_be_cleaned: str = None
    """Columns for missing values clean operation"""
    minimum_missing_value_ratio: float = 0.0
    """Clean only column with missing value ratio above specified value, out of set of all selected columns (max: 1.0)"""
    maximum_missing_value_ratio: float = 1.0
    """Clean only columns with missing value ratio below specified value, out of set of all selected columns (max: 1.0)"""
    cleaning_mode: _AzuremlCleanMissingDataCleaningModeEnum = _AzuremlCleanMissingDataCleaningModeEnum.custom_substitution_value
    """Algorithm to clean missing values (enum: ['Custom substitution value', 'Replace with mean', 'Replace with median', 'Replace with mode', 'Remove entire row', 'Remove entire column'])"""
    replacement_value: str = '0'
    """Type the value that takes the place of missing values (optional)"""
    generate_missing_value_indicator_column: bool = False
    """Generate a column that indicates which rows were cleaned (optional)"""
    cols_with_all_missing_values: _AzuremlCleanMissingDataColsWithAllMissingValuesEnum = _AzuremlCleanMissingDataColsWithAllMissingValuesEnum.remove
    """Cols with all missing values (optional, enum: ['Propagate', 'Remove'])"""


class _AzuremlCleanMissingDataOutput:
    cleaned_dataset: Output = None
    """Cleaned dataset"""
    cleaning_transformation: Output = None
    """Transformation to be passed to Apply Transformation module to clean new data"""


class _AzuremlCleanMissingDataComponent(Component):
    inputs: _AzuremlCleanMissingDataInput
    outputs: _AzuremlCleanMissingDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_clean_missing_data = None


def azureml_clean_missing_data(
    dataset: Path = None,
    columns_to_be_cleaned: str = None,
    minimum_missing_value_ratio: float = 0.0,
    maximum_missing_value_ratio: float = 1.0,
    cleaning_mode: _AzuremlCleanMissingDataCleaningModeEnum = _AzuremlCleanMissingDataCleaningModeEnum.custom_substitution_value,
    replacement_value: str = '0',
    generate_missing_value_indicator_column: bool = False,
    cols_with_all_missing_values: _AzuremlCleanMissingDataColsWithAllMissingValuesEnum = _AzuremlCleanMissingDataColsWithAllMissingValuesEnum.remove,
) -> _AzuremlCleanMissingDataComponent:
    """Specifies how to handle the values missing from a dataset.
    
    :param dataset: Dataset to be cleaned
    :type dataset: Path
    :param columns_to_be_cleaned: Columns for missing values clean operation
    :type columns_to_be_cleaned: str
    :param minimum_missing_value_ratio: Clean only column with missing value ratio above specified value, out of set of all selected columns (max: 1.0)
    :type minimum_missing_value_ratio: float
    :param maximum_missing_value_ratio: Clean only columns with missing value ratio below specified value, out of set of all selected columns (max: 1.0)
    :type maximum_missing_value_ratio: float
    :param cleaning_mode: Algorithm to clean missing values (enum: ['Custom substitution value', 'Replace with mean', 'Replace with median', 'Replace with mode', 'Remove entire row', 'Remove entire column'])
    :type cleaning_mode: _AzuremlCleanMissingDataCleaningModeEnum
    :param replacement_value: Type the value that takes the place of missing values (optional)
    :type replacement_value: str
    :param generate_missing_value_indicator_column: Generate a column that indicates which rows were cleaned (optional)
    :type generate_missing_value_indicator_column: bool
    :param cols_with_all_missing_values: Cols with all missing values (optional, enum: ['Propagate', 'Remove'])
    :type cols_with_all_missing_values: _AzuremlCleanMissingDataColsWithAllMissingValuesEnum
    :output cleaned_dataset: Cleaned dataset
    :type: cleaned_dataset: Output
    :output cleaning_transformation: Transformation to be passed to Apply Transformation module to clean new data
    :type: cleaning_transformation: Output
    """
    global _azureml_clean_missing_data
    if _azureml_clean_missing_data is None:
        _azureml_clean_missing_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Clean Missing Data', version=None, feed='azureml')
    return _azureml_clean_missing_data(
            dataset=dataset,
            columns_to_be_cleaned=columns_to_be_cleaned,
            minimum_missing_value_ratio=minimum_missing_value_ratio,
            maximum_missing_value_ratio=maximum_missing_value_ratio,
            cleaning_mode=cleaning_mode,
            replacement_value=replacement_value,
            generate_missing_value_indicator_column=generate_missing_value_indicator_column,
            cols_with_all_missing_values=cols_with_all_missing_values,)


class _AzuremlClipValuesClipmodeEnum(Enum):
    clippeaks = 'ClipPeaks'
    clipsubpeaks = 'ClipSubPeaks'
    clippeaksandsubpeaks = 'ClipPeaksAndSubpeaks'


class _AzuremlClipValuesUpperthresholdEnum(Enum):
    constant = 'Constant'
    percentile = 'Percentile'


class _AzuremlClipValuesModeuppersubstituteEnum(Enum):
    threshold = 'Threshold'
    mean = 'Mean'
    median = 'Median'
    missing = 'Missing'


class _AzuremlClipValuesLowerthresholdEnum(Enum):
    constant = 'Constant'
    percentile = 'Percentile'


class _AzuremlClipValuesModeowersubstituteEnum(Enum):
    threshold = 'Threshold'
    mean = 'Mean'
    median = 'Median'
    missing = 'Missing'


class _AzuremlClipValuesLowerupperthresholdEnum(Enum):
    constant = 'Constant'
    percentile = 'Percentile'


class _AzuremlClipValuesModeusubstituteEnum(Enum):
    threshold = 'Threshold'
    mean = 'Mean'
    median = 'Median'
    missing = 'Missing'


class _AzuremlClipValuesModelsubstituteEnum(Enum):
    threshold = 'Threshold'
    mean = 'Mean'
    median = 'Median'
    missing = 'Missing'


class _AzuremlClipValuesInput:
    input: Input = None
    """DataFrameDirectory"""
    clipmode: _AzuremlClipValuesClipmodeEnum = _AzuremlClipValuesClipmodeEnum.clippeaks
    """enum (enum: ['ClipPeaks', 'ClipSubPeaks', 'ClipPeaksAndSubpeaks'])"""
    upperthreshold: _AzuremlClipValuesUpperthresholdEnum = _AzuremlClipValuesUpperthresholdEnum.constant
    """enum (optional, enum: ['Constant', 'Percentile'])"""
    constantupperthreshold: float = 99
    """float (optional)"""
    percentileupperthreshold: float = 99
    """float (optional)"""
    modeuppersubstitute: _AzuremlClipValuesModeuppersubstituteEnum = _AzuremlClipValuesModeuppersubstituteEnum.threshold
    """enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])"""
    lowerthreshold: _AzuremlClipValuesLowerthresholdEnum = _AzuremlClipValuesLowerthresholdEnum.constant
    """enum (optional, enum: ['Constant', 'Percentile'])"""
    constantlowerthreshold: float = 1
    """float (optional)"""
    percentilelowerthreshold: float = 1
    """float (optional)"""
    modeowersubstitute: _AzuremlClipValuesModeowersubstituteEnum = _AzuremlClipValuesModeowersubstituteEnum.threshold
    """enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])"""
    lowerupperthreshold: _AzuremlClipValuesLowerupperthresholdEnum = _AzuremlClipValuesLowerupperthresholdEnum.constant
    """enum (optional, enum: ['Constant', 'Percentile'])"""
    constantuthreshold: float = 99
    """float (optional)"""
    constantlthreshold: float = 1
    """float (optional)"""
    percentileuthreshold: float = 99
    """float (optional)"""
    percentilelthreshold: float = 1
    """float (optional)"""
    modeusubstitute: _AzuremlClipValuesModeusubstituteEnum = _AzuremlClipValuesModeusubstituteEnum.threshold
    """enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])"""
    modelsubstitute: _AzuremlClipValuesModelsubstituteEnum = _AzuremlClipValuesModelsubstituteEnum.threshold
    """enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])"""
    column_selector: str = None
    """ColumnPicker"""
    inplace_flag: bool = True
    """boolean"""
    indicator_flag: bool = False
    """boolean"""


class _AzuremlClipValuesOutput:
    result_dataset: Output = None
    """DataFrameDirectory"""


class _AzuremlClipValuesComponent(Component):
    inputs: _AzuremlClipValuesInput
    outputs: _AzuremlClipValuesOutput
    runsettings: _CommandComponentRunsetting


_azureml_clip_values = None


def azureml_clip_values(
    input: Path = None,
    clipmode: _AzuremlClipValuesClipmodeEnum = _AzuremlClipValuesClipmodeEnum.clippeaks,
    upperthreshold: _AzuremlClipValuesUpperthresholdEnum = _AzuremlClipValuesUpperthresholdEnum.constant,
    constantupperthreshold: float = 99,
    percentileupperthreshold: float = 99,
    modeuppersubstitute: _AzuremlClipValuesModeuppersubstituteEnum = _AzuremlClipValuesModeuppersubstituteEnum.threshold,
    lowerthreshold: _AzuremlClipValuesLowerthresholdEnum = _AzuremlClipValuesLowerthresholdEnum.constant,
    constantlowerthreshold: float = 1,
    percentilelowerthreshold: float = 1,
    modeowersubstitute: _AzuremlClipValuesModeowersubstituteEnum = _AzuremlClipValuesModeowersubstituteEnum.threshold,
    lowerupperthreshold: _AzuremlClipValuesLowerupperthresholdEnum = _AzuremlClipValuesLowerupperthresholdEnum.constant,
    constantuthreshold: float = 99,
    constantlthreshold: float = 1,
    percentileuthreshold: float = 99,
    percentilelthreshold: float = 1,
    modeusubstitute: _AzuremlClipValuesModeusubstituteEnum = _AzuremlClipValuesModeusubstituteEnum.threshold,
    modelsubstitute: _AzuremlClipValuesModelsubstituteEnum = _AzuremlClipValuesModelsubstituteEnum.threshold,
    column_selector: str = None,
    inplace_flag: bool = True,
    indicator_flag: bool = False,
) -> _AzuremlClipValuesComponent:
    """Detects outliers and clips or replaces their values.
    
    :param input: DataFrameDirectory
    :type input: Path
    :param clipmode: enum (enum: ['ClipPeaks', 'ClipSubPeaks', 'ClipPeaksAndSubpeaks'])
    :type clipmode: _AzuremlClipValuesClipmodeEnum
    :param upperthreshold: enum (optional, enum: ['Constant', 'Percentile'])
    :type upperthreshold: _AzuremlClipValuesUpperthresholdEnum
    :param constantupperthreshold: float (optional)
    :type constantupperthreshold: float
    :param percentileupperthreshold: float (optional)
    :type percentileupperthreshold: float
    :param modeuppersubstitute: enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])
    :type modeuppersubstitute: _AzuremlClipValuesModeuppersubstituteEnum
    :param lowerthreshold: enum (optional, enum: ['Constant', 'Percentile'])
    :type lowerthreshold: _AzuremlClipValuesLowerthresholdEnum
    :param constantlowerthreshold: float (optional)
    :type constantlowerthreshold: float
    :param percentilelowerthreshold: float (optional)
    :type percentilelowerthreshold: float
    :param modeowersubstitute: enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])
    :type modeowersubstitute: _AzuremlClipValuesModeowersubstituteEnum
    :param lowerupperthreshold: enum (optional, enum: ['Constant', 'Percentile'])
    :type lowerupperthreshold: _AzuremlClipValuesLowerupperthresholdEnum
    :param constantuthreshold: float (optional)
    :type constantuthreshold: float
    :param constantlthreshold: float (optional)
    :type constantlthreshold: float
    :param percentileuthreshold: float (optional)
    :type percentileuthreshold: float
    :param percentilelthreshold: float (optional)
    :type percentilelthreshold: float
    :param modeusubstitute: enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])
    :type modeusubstitute: _AzuremlClipValuesModeusubstituteEnum
    :param modelsubstitute: enum (optional, enum: ['Threshold', 'Mean', 'Median', 'Missing'])
    :type modelsubstitute: _AzuremlClipValuesModelsubstituteEnum
    :param column_selector: ColumnPicker
    :type column_selector: str
    :param inplace_flag: boolean
    :type inplace_flag: bool
    :param indicator_flag: boolean
    :type indicator_flag: bool
    :output result_dataset: DataFrameDirectory
    :type: result_dataset: Output
    """
    global _azureml_clip_values
    if _azureml_clip_values is None:
        _azureml_clip_values = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Clip Values', version=None, feed='azureml')
    return _azureml_clip_values(
            input=input,
            clipmode=clipmode,
            upperthreshold=upperthreshold,
            constantupperthreshold=constantupperthreshold,
            percentileupperthreshold=percentileupperthreshold,
            modeuppersubstitute=modeuppersubstitute,
            lowerthreshold=lowerthreshold,
            constantlowerthreshold=constantlowerthreshold,
            percentilelowerthreshold=percentilelowerthreshold,
            modeowersubstitute=modeowersubstitute,
            lowerupperthreshold=lowerupperthreshold,
            constantuthreshold=constantuthreshold,
            constantlthreshold=constantlthreshold,
            percentileuthreshold=percentileuthreshold,
            percentilelthreshold=percentilelthreshold,
            modeusubstitute=modeusubstitute,
            modelsubstitute=modelsubstitute,
            column_selector=column_selector,
            inplace_flag=inplace_flag,
            indicator_flag=indicator_flag,)


class _AzuremlConvertWordToVectorWord2VecStrategyEnum(Enum):
    glove_pretrained_english_model = 'GloVe pretrained English Model'
    gensim_word2vec = 'Gensim Word2Vec'
    gensim_fasttext = 'Gensim FastText'


class _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum(Enum):
    skip_gram = 'Skip_gram'
    cbow = 'CBOW'


class _AzuremlConvertWordToVectorInput:
    dataset: Input = None
    """Input data"""
    target_column: str = None
    """Select one target column whose vocabulary embeddings will be generated"""
    word2vec_strategy: _AzuremlConvertWordToVectorWord2VecStrategyEnum = _AzuremlConvertWordToVectorWord2VecStrategyEnum.gensim_word2vec
    """Select the strategy for computing word embedding (enum: ['GloVe pretrained English Model', 'Gensim Word2Vec', 'Gensim FastText'])"""
    word2vec_training_algorithm: _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum = _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum.skip_gram
    """Select the training algorithm for training Word2Vec model (optional, enum: ['Skip_gram', 'CBOW'])"""
    length_of_word_embedding: int = 100
    """Specify the length of the word embedding/vector (optional, min: 10, max: 2000)"""
    context_window_size: int = 5
    """Specify the maximum distance between the word being predicted and the current word (optional, min: 1, max: 100)"""
    number_of_epochs: int = 5
    """Specify the number of epochs (iterations) over the corpus (optional, min: 1, max: 1024)"""
    maximum_vocabulary_size: int = 10000
    """Specify the maximum number of the words in vocabulary (min: 10, max: 2147483647)"""
    minimum_word_count: int = 5
    """Ignores all words that have a frequency lower than this value (min: 1, max: 100)"""


class _AzuremlConvertWordToVectorOutput:
    vocabulary_with_embeddings: Output = None
    """Vocabulary with embeddings"""


class _AzuremlConvertWordToVectorComponent(Component):
    inputs: _AzuremlConvertWordToVectorInput
    outputs: _AzuremlConvertWordToVectorOutput
    runsettings: _CommandComponentRunsetting


_azureml_convert_word_to_vector = None


def azureml_convert_word_to_vector(
    dataset: Path = None,
    target_column: str = None,
    word2vec_strategy: _AzuremlConvertWordToVectorWord2VecStrategyEnum = _AzuremlConvertWordToVectorWord2VecStrategyEnum.gensim_word2vec,
    word2vec_training_algorithm: _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum = _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum.skip_gram,
    length_of_word_embedding: int = 100,
    context_window_size: int = 5,
    number_of_epochs: int = 5,
    maximum_vocabulary_size: int = 10000,
    minimum_word_count: int = 5,
) -> _AzuremlConvertWordToVectorComponent:
    """Convert word to vector.
    
    :param dataset: Input data
    :type dataset: Path
    :param target_column: Select one target column whose vocabulary embeddings will be generated
    :type target_column: str
    :param word2vec_strategy: Select the strategy for computing word embedding (enum: ['GloVe pretrained English Model', 'Gensim Word2Vec', 'Gensim FastText'])
    :type word2vec_strategy: _AzuremlConvertWordToVectorWord2VecStrategyEnum
    :param word2vec_training_algorithm: Select the training algorithm for training Word2Vec model (optional, enum: ['Skip_gram', 'CBOW'])
    :type word2vec_training_algorithm: _AzuremlConvertWordToVectorWord2VecTrainingAlgorithmEnum
    :param length_of_word_embedding: Specify the length of the word embedding/vector (optional, min: 10, max: 2000)
    :type length_of_word_embedding: int
    :param context_window_size: Specify the maximum distance between the word being predicted and the current word (optional, min: 1, max: 100)
    :type context_window_size: int
    :param number_of_epochs: Specify the number of epochs (iterations) over the corpus (optional, min: 1, max: 1024)
    :type number_of_epochs: int
    :param maximum_vocabulary_size: Specify the maximum number of the words in vocabulary (min: 10, max: 2147483647)
    :type maximum_vocabulary_size: int
    :param minimum_word_count: Ignores all words that have a frequency lower than this value (min: 1, max: 100)
    :type minimum_word_count: int
    :output vocabulary_with_embeddings: Vocabulary with embeddings
    :type: vocabulary_with_embeddings: Output
    """
    global _azureml_convert_word_to_vector
    if _azureml_convert_word_to_vector is None:
        _azureml_convert_word_to_vector = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Convert Word to Vector', version=None, feed='azureml')
    return _azureml_convert_word_to_vector(
            dataset=dataset,
            target_column=target_column,
            word2vec_strategy=word2vec_strategy,
            word2vec_training_algorithm=word2vec_training_algorithm,
            length_of_word_embedding=length_of_word_embedding,
            context_window_size=context_window_size,
            number_of_epochs=number_of_epochs,
            maximum_vocabulary_size=maximum_vocabulary_size,
            minimum_word_count=minimum_word_count,)


class _AzuremlConvertToCsvInput:
    dataset: Input = None
    """Input dataset"""


class _AzuremlConvertToCsvOutput:
    results_dataset: Output = None
    """Output dataset"""


class _AzuremlConvertToCsvComponent(Component):
    inputs: _AzuremlConvertToCsvInput
    outputs: _AzuremlConvertToCsvOutput
    runsettings: _CommandComponentRunsetting


_azureml_convert_to_csv = None


def azureml_convert_to_csv(
    dataset: Path = None,
) -> _AzuremlConvertToCsvComponent:
    """Converts data input to a comma-separated values format.
    
    :param dataset: Input dataset
    :type dataset: Path
    :output results_dataset: Output dataset
    :type: results_dataset: Output
    """
    global _azureml_convert_to_csv
    if _azureml_convert_to_csv is None:
        _azureml_convert_to_csv = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Convert to CSV', version=None, feed='azureml')
    return _azureml_convert_to_csv(
            dataset=dataset,)


class _AzuremlConvertToDatasetActionEnum(Enum):
    none = 'None'
    setmissingvalues = 'SetMissingValues'
    replacevalues = 'ReplaceValues'


class _AzuremlConvertToDatasetReplaceEnum(Enum):
    missing = 'Missing'
    custom = 'Custom'


class _AzuremlConvertToDatasetInput:
    dataset: Input = None
    """Input dataset"""
    action: _AzuremlConvertToDatasetActionEnum = _AzuremlConvertToDatasetActionEnum.none
    """Action to apply to input dataset (enum: ['None', 'SetMissingValues', 'ReplaceValues'])"""
    custom_missing_value: str = '?'
    """Value indicating missing value token (optional)"""
    replace: _AzuremlConvertToDatasetReplaceEnum = _AzuremlConvertToDatasetReplaceEnum.missing
    """Specifies type of replacement for values (optional, enum: ['Missing', 'Custom'])"""
    custom_value: str = 'obs'
    """Value to be replaced (optional)"""
    new_value: str = '0'
    """Replacement value (optional)"""


class _AzuremlConvertToDatasetOutput:
    results_dataset: Output = None
    """Output dataset"""


class _AzuremlConvertToDatasetComponent(Component):
    inputs: _AzuremlConvertToDatasetInput
    outputs: _AzuremlConvertToDatasetOutput
    runsettings: _CommandComponentRunsetting


_azureml_convert_to_dataset = None


def azureml_convert_to_dataset(
    dataset: Path = None,
    action: _AzuremlConvertToDatasetActionEnum = _AzuremlConvertToDatasetActionEnum.none,
    custom_missing_value: str = '?',
    replace: _AzuremlConvertToDatasetReplaceEnum = _AzuremlConvertToDatasetReplaceEnum.missing,
    custom_value: str = 'obs',
    new_value: str = '0',
) -> _AzuremlConvertToDatasetComponent:
    """Converts data input to the internal Dataset format used by Azure Machine Learning designer.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param action: Action to apply to input dataset (enum: ['None', 'SetMissingValues', 'ReplaceValues'])
    :type action: _AzuremlConvertToDatasetActionEnum
    :param custom_missing_value: Value indicating missing value token (optional)
    :type custom_missing_value: str
    :param replace: Specifies type of replacement for values (optional, enum: ['Missing', 'Custom'])
    :type replace: _AzuremlConvertToDatasetReplaceEnum
    :param custom_value: Value to be replaced (optional)
    :type custom_value: str
    :param new_value: Replacement value (optional)
    :type new_value: str
    :output results_dataset: Output dataset
    :type: results_dataset: Output
    """
    global _azureml_convert_to_dataset
    if _azureml_convert_to_dataset is None:
        _azureml_convert_to_dataset = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Convert to Dataset', version=None, feed='azureml')
    return _azureml_convert_to_dataset(
            dataset=dataset,
            action=action,
            custom_missing_value=custom_missing_value,
            replace=replace,
            custom_value=custom_value,
            new_value=new_value,)


class _AzuremlConvertToImageDirectoryInput:
    input_dataset: Input = None
    """Input dataset"""


class _AzuremlConvertToImageDirectoryOutput:
    output_image_directory: Output = None
    """Output image directory."""


class _AzuremlConvertToImageDirectoryComponent(Component):
    inputs: _AzuremlConvertToImageDirectoryInput
    outputs: _AzuremlConvertToImageDirectoryOutput
    runsettings: _CommandComponentRunsetting


_azureml_convert_to_image_directory = None


def azureml_convert_to_image_directory(
    input_dataset: Path = None,
) -> _AzuremlConvertToImageDirectoryComponent:
    """Convert dataset to image directory format.
    
    :param input_dataset: Input dataset
    :type input_dataset: Path
    :output output_image_directory: Output image directory.
    :type: output_image_directory: Output
    """
    global _azureml_convert_to_image_directory
    if _azureml_convert_to_image_directory is None:
        _azureml_convert_to_image_directory = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Convert to Image Directory', version=None, feed='azureml')
    return _azureml_convert_to_image_directory(
            input_dataset=input_dataset,)


class _AzuremlConvertToIndicatorValuesInput:
    dataset: Input = None
    """Dataset with categorical columns"""
    categorical_columns_to_convert: str = None
    """Select categorical columns to convert to indicator matrices."""
    overwrite_categorical_columns: bool = False
    """If True, overwrite the selected categorical columns, otherwise append the resulting indicator matrices to the dataset (optional)"""


class _AzuremlConvertToIndicatorValuesOutput:
    results_dataset: Output = None
    """Dataset with categorical columns converted to indicator matrices."""
    indicator_values_transformation: Output = None
    """Transformation to be passed to Apply Transformation module to convert indicator values for new data"""


class _AzuremlConvertToIndicatorValuesComponent(Component):
    inputs: _AzuremlConvertToIndicatorValuesInput
    outputs: _AzuremlConvertToIndicatorValuesOutput
    runsettings: _CommandComponentRunsetting


_azureml_convert_to_indicator_values = None


def azureml_convert_to_indicator_values(
    dataset: Path = None,
    categorical_columns_to_convert: str = None,
    overwrite_categorical_columns: bool = False,
) -> _AzuremlConvertToIndicatorValuesComponent:
    """Converts categorical values in columns to indicator values.
    
    :param dataset: Dataset with categorical columns
    :type dataset: Path
    :param categorical_columns_to_convert: Select categorical columns to convert to indicator matrices.
    :type categorical_columns_to_convert: str
    :param overwrite_categorical_columns: If True, overwrite the selected categorical columns, otherwise append the resulting indicator matrices to the dataset (optional)
    :type overwrite_categorical_columns: bool
    :output results_dataset: Dataset with categorical columns converted to indicator matrices.
    :type: results_dataset: Output
    :output indicator_values_transformation: Transformation to be passed to Apply Transformation module to convert indicator values for new data
    :type: indicator_values_transformation: Output
    """
    global _azureml_convert_to_indicator_values
    if _azureml_convert_to_indicator_values is None:
        _azureml_convert_to_indicator_values = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Convert to Indicator Values', version=None, feed='azureml')
    return _azureml_convert_to_indicator_values(
            dataset=dataset,
            categorical_columns_to_convert=categorical_columns_to_convert,
            overwrite_categorical_columns=overwrite_categorical_columns,)


class _AzuremlCreatePythonModelInput:
    python_script: str = '\n# The script MUST define a class named AzureMLModel.\n# This class MUST at least define the following three methods: "__init__", "train" and "predict".\n# The signatures (method and argument names) of all these methods MUST be exactly the same as the following example.\n\n# Please do not install extra packages such as "pip install xgboost" in this script,\n# otherwise errors will be raised when reading models in down-stream modules.\n\nimport pandas as pd\nfrom sklearn.linear_model import LogisticRegression\n\n\nclass AzureMLModel:\n    # The __init__ method is only invoked in module "Create Python Model",\n    # and will not be invoked again in the following modules "Train Model" and "Score Model".\n    # The attributes defined in the __init__ method are preserved and usable in the train and predict method.\n    def __init__(self):\n        # self.model must be assigned\n        self.model = LogisticRegression()\n        self.feature_column_names = list()\n\n    # Train model\n    #   Param<df_train>: a pandas.DataFrame\n    #   Param<df_label>: a pandas.Series\n    def train(self, df_train, df_label):\n        # self.feature_column_names records the column names used for training.\n        # It is recommended to set this attribute before training so that the\n        # feature columns used in predict and train methods have the same names.\n        self.feature_column_names = df_train.columns.tolist()\n        self.model.fit(df_train, df_label)\n\n    # Predict results\n    #   Param<df>: a pandas.DataFrame\n    #   Must return a pandas.DataFrame\n    def predict(self, df):\n        # The feature columns used for prediction MUST have the same names as the ones for training.\n        # The name of score column ("Scored Labels" in this case) MUST be different from any other\n        # columns in input data.\n        return pd.DataFrame({\'Scored Labels\': self.model.predict(df[self.feature_column_names])})\n'
    """The Python script to execute"""


class _AzuremlCreatePythonModelOutput:
    untrained_model: Output = None
    """A untrained custom python model"""


class _AzuremlCreatePythonModelComponent(Component):
    inputs: _AzuremlCreatePythonModelInput
    outputs: _AzuremlCreatePythonModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_create_python_model = None


def azureml_create_python_model(
    python_script: str = '\n# The script MUST define a class named AzureMLModel.\n# This class MUST at least define the following three methods: "__init__", "train" and "predict".\n# The signatures (method and argument names) of all these methods MUST be exactly the same as the following example.\n\n# Please do not install extra packages such as "pip install xgboost" in this script,\n# otherwise errors will be raised when reading models in down-stream modules.\n\nimport pandas as pd\nfrom sklearn.linear_model import LogisticRegression\n\n\nclass AzureMLModel:\n    # The __init__ method is only invoked in module "Create Python Model",\n    # and will not be invoked again in the following modules "Train Model" and "Score Model".\n    # The attributes defined in the __init__ method are preserved and usable in the train and predict method.\n    def __init__(self):\n        # self.model must be assigned\n        self.model = LogisticRegression()\n        self.feature_column_names = list()\n\n    # Train model\n    #   Param<df_train>: a pandas.DataFrame\n    #   Param<df_label>: a pandas.Series\n    def train(self, df_train, df_label):\n        # self.feature_column_names records the column names used for training.\n        # It is recommended to set this attribute before training so that the\n        # feature columns used in predict and train methods have the same names.\n        self.feature_column_names = df_train.columns.tolist()\n        self.model.fit(df_train, df_label)\n\n    # Predict results\n    #   Param<df>: a pandas.DataFrame\n    #   Must return a pandas.DataFrame\n    def predict(self, df):\n        # The feature columns used for prediction MUST have the same names as the ones for training.\n        # The name of score column ("Scored Labels" in this case) MUST be different from any other\n        # columns in input data.\n        return pd.DataFrame({\'Scored Labels\': self.model.predict(df[self.feature_column_names])})\n',
) -> _AzuremlCreatePythonModelComponent:
    """Creates Python model using custom script.
    
    :param python_script: The Python script to execute
    :type python_script: str
    :output untrained_model: A untrained custom python model
    :type: untrained_model: Output
    """
    global _azureml_create_python_model
    if _azureml_create_python_model is None:
        _azureml_create_python_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Create Python Model', version=None, feed='azureml')
    return _azureml_create_python_model(
            python_script=python_script,)


class _AzuremlCrossValidateModelInput:
    untrained_model: Input = None
    """Untrained learner"""
    dataset: Input = None
    """Training data"""
    name_or_numerical_index_of_the_label_column: str = None
    """Select the column that contains the label or outcome column"""
    random_seed: int = 0
    """Specify a numeric seed to use for random number generation.  (max: 4294967295)"""


class _AzuremlCrossValidateModelOutput:
    scored_results: Output = None
    """Data scored results"""
    evaluation_results_by_fold: Output = None
    """Data evaluation results by fold"""


class _AzuremlCrossValidateModelComponent(Component):
    inputs: _AzuremlCrossValidateModelInput
    outputs: _AzuremlCrossValidateModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_cross_validate_model = None


def azureml_cross_validate_model(
    untrained_model: Path = None,
    dataset: Path = None,
    name_or_numerical_index_of_the_label_column: str = None,
    random_seed: int = 0,
) -> _AzuremlCrossValidateModelComponent:
    """Cross Validate a classification or regression model with standard metrics.
    
    :param untrained_model: Untrained learner
    :type untrained_model: Path
    :param dataset: Training data
    :type dataset: Path
    :param name_or_numerical_index_of_the_label_column: Select the column that contains the label or outcome column
    :type name_or_numerical_index_of_the_label_column: str
    :param random_seed: Specify a numeric seed to use for random number generation.  (max: 4294967295)
    :type random_seed: int
    :output scored_results: Data scored results
    :type: scored_results: Output
    :output evaluation_results_by_fold: Data evaluation results by fold
    :type: evaluation_results_by_fold: Output
    """
    global _azureml_cross_validate_model
    if _azureml_cross_validate_model is None:
        _azureml_cross_validate_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Cross Validate Model', version=None, feed='azureml')
    return _azureml_cross_validate_model(
            untrained_model=untrained_model,
            dataset=dataset,
            name_or_numerical_index_of_the_label_column=name_or_numerical_index_of_the_label_column,
            random_seed=random_seed,)


class _AzuremlDecisionForestRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlDecisionForestRegressionResamplingMethodEnum(Enum):
    bagging_resampling = 'Bagging Resampling'
    replicate_resampling = 'Replicate Resampling'


class _AzuremlDecisionForestRegressionInput:
    create_trainer_mode: _AzuremlDecisionForestRegressionCreateTrainerModeEnum = _AzuremlDecisionForestRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    number_of_decision_trees: int = 8
    """Specify the number of decision trees to create in the ensemble (optional, min: 1)"""
    maximum_depth_of_the_decision_trees: int = 32
    """Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)"""
    minimum_number_of_samples_per_leaf_node: int = 1
    """Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)"""
    range_for_number_of_decision_trees: str = '1; 8; 32'
    """Specify range for the number of decision trees to create in the ensemble (optional)"""
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64'
    """Specify range for the maximum depth of the decision trees (optional)"""
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16'
    """Specify range for the minimum number of samples per leaf node (optional)"""
    resampling_method: _AzuremlDecisionForestRegressionResamplingMethodEnum = _AzuremlDecisionForestRegressionResamplingMethodEnum.bagging_resampling
    """Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])"""


class _AzuremlDecisionForestRegressionOutput:
    untrained_model: Output = None
    """An untrained regression model"""


class _AzuremlDecisionForestRegressionComponent(Component):
    inputs: _AzuremlDecisionForestRegressionInput
    outputs: _AzuremlDecisionForestRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_decision_forest_regression = None


def azureml_decision_forest_regression(
    create_trainer_mode: _AzuremlDecisionForestRegressionCreateTrainerModeEnum = _AzuremlDecisionForestRegressionCreateTrainerModeEnum.singleparameter,
    number_of_decision_trees: int = 8,
    maximum_depth_of_the_decision_trees: int = 32,
    minimum_number_of_samples_per_leaf_node: int = 1,
    range_for_number_of_decision_trees: str = '1; 8; 32',
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64',
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16',
    resampling_method: _AzuremlDecisionForestRegressionResamplingMethodEnum = _AzuremlDecisionForestRegressionResamplingMethodEnum.bagging_resampling,
) -> _AzuremlDecisionForestRegressionComponent:
    """Creates a regression model using the decision forest algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlDecisionForestRegressionCreateTrainerModeEnum
    :param number_of_decision_trees: Specify the number of decision trees to create in the ensemble (optional, min: 1)
    :type number_of_decision_trees: int
    :param maximum_depth_of_the_decision_trees: Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)
    :type maximum_depth_of_the_decision_trees: int
    :param minimum_number_of_samples_per_leaf_node: Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)
    :type minimum_number_of_samples_per_leaf_node: int
    :param range_for_number_of_decision_trees: Specify range for the number of decision trees to create in the ensemble (optional)
    :type range_for_number_of_decision_trees: str
    :param range_for_the_maximum_depth_of_the_decision_trees: Specify range for the maximum depth of the decision trees (optional)
    :type range_for_the_maximum_depth_of_the_decision_trees: str
    :param range_for_the_minimum_number_of_samples_per_leaf_node: Specify range for the minimum number of samples per leaf node (optional)
    :type range_for_the_minimum_number_of_samples_per_leaf_node: str
    :param resampling_method: Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])
    :type resampling_method: _AzuremlDecisionForestRegressionResamplingMethodEnum
    :output untrained_model: An untrained regression model
    :type: untrained_model: Output
    """
    global _azureml_decision_forest_regression
    if _azureml_decision_forest_regression is None:
        _azureml_decision_forest_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Decision Forest Regression', version=None, feed='azureml')
    return _azureml_decision_forest_regression(
            create_trainer_mode=create_trainer_mode,
            number_of_decision_trees=number_of_decision_trees,
            maximum_depth_of_the_decision_trees=maximum_depth_of_the_decision_trees,
            minimum_number_of_samples_per_leaf_node=minimum_number_of_samples_per_leaf_node,
            range_for_number_of_decision_trees=range_for_number_of_decision_trees,
            range_for_the_maximum_depth_of_the_decision_trees=range_for_the_maximum_depth_of_the_decision_trees,
            range_for_the_minimum_number_of_samples_per_leaf_node=range_for_the_minimum_number_of_samples_per_leaf_node,
            resampling_method=resampling_method,)


class _AzuremlDensenetModelNameEnum(Enum):
    densenet121 = 'densenet121'
    densenet161 = 'densenet161'
    densenet169 = 'densenet169'
    densenet201 = 'densenet201'


class _AzuremlDensenetInput:
    model_name: _AzuremlDensenetModelNameEnum = _AzuremlDensenetModelNameEnum.densenet201
    """Name of a certain densenet structure (enum: ['densenet121', 'densenet161', 'densenet169', 'densenet201'])"""
    pretrained: bool = True
    """Indicate whether to use a model pre-trained on ImageNet"""
    memory_efficient: bool = False
    """Indicate whether to use checkpointing, which is much more memory efficient but slower"""


class _AzuremlDensenetOutput:
    untrained_model: Output = None
    """Untrained densenet model path"""


class _AzuremlDensenetComponent(Component):
    inputs: _AzuremlDensenetInput
    outputs: _AzuremlDensenetOutput
    runsettings: _CommandComponentRunsetting


_azureml_densenet = None


def azureml_densenet(
    model_name: _AzuremlDensenetModelNameEnum = _AzuremlDensenetModelNameEnum.densenet201,
    pretrained: bool = True,
    memory_efficient: bool = False,
) -> _AzuremlDensenetComponent:
    """Creates a image classification model using the densenet algorithm.
    
    :param model_name: Name of a certain densenet structure (enum: ['densenet121', 'densenet161', 'densenet169', 'densenet201'])
    :type model_name: _AzuremlDensenetModelNameEnum
    :param pretrained: Indicate whether to use a model pre-trained on ImageNet
    :type pretrained: bool
    :param memory_efficient: Indicate whether to use checkpointing, which is much more memory efficient but slower
    :type memory_efficient: bool
    :output untrained_model: Untrained densenet model path
    :type: untrained_model: Output
    """
    global _azureml_densenet
    if _azureml_densenet is None:
        _azureml_densenet = _assets.load_component(
            _workspace.from_config(),
            name='azureml://DenseNet', version=None, feed='azureml')
    return _azureml_densenet(
            model_name=model_name,
            pretrained=pretrained,
            memory_efficient=memory_efficient,)


class _AzuremlEditMetadataDataTypeEnum(Enum):
    unchanged = 'Unchanged'
    string = 'String'
    integer = 'Integer'
    double = 'Double'
    boolean = 'Boolean'
    datetime = 'DateTime'


class _AzuremlEditMetadataCategoricalEnum(Enum):
    unchanged = 'Unchanged'
    categorical = 'Categorical'
    noncategorical = 'NonCategorical'


class _AzuremlEditMetadataFieldsEnum(Enum):
    unchanged = 'Unchanged'
    features = 'Features'
    labels = 'Labels'
    clearfeatures = 'ClearFeatures'
    clearlabels = 'ClearLabels'
    clearscores = 'ClearScores'


class _AzuremlEditMetadataInput:
    dataset: Input = None
    """Input dataset"""
    column: str = None
    """Choose the columns to which your changes should apply"""
    data_type: _AzuremlEditMetadataDataTypeEnum = _AzuremlEditMetadataDataTypeEnum.unchanged
    """Specify the new data type of the column (enum: ['Unchanged', 'String', 'Integer', 'Double', 'Boolean', 'DateTime'])"""
    date_and_time_format: str = None
    """Specify custom format string for parsing DateTime, refer to Python standard library datetime.strftime() for detailed documentation. Leave empty for default permissive parsing (optional)"""
    categorical: _AzuremlEditMetadataCategoricalEnum = _AzuremlEditMetadataCategoricalEnum.unchanged
    """Indicate whether the column should be flagged as categorical (enum: ['Unchanged', 'Categorical', 'NonCategorical'])"""
    fields: _AzuremlEditMetadataFieldsEnum = _AzuremlEditMetadataFieldsEnum.unchanged
    """Specify whether the column should be considered a feature or label by learning algorithms (enum: ['Unchanged', 'Features', 'Labels', 'ClearFeatures', 'ClearLabels', 'ClearScores'])"""
    new_column_name: str = None
    """Type the new names of the columns (optional)"""


class _AzuremlEditMetadataOutput:
    results_dataset: Output = None
    """Dataset with changed metadata"""


class _AzuremlEditMetadataComponent(Component):
    inputs: _AzuremlEditMetadataInput
    outputs: _AzuremlEditMetadataOutput
    runsettings: _CommandComponentRunsetting


_azureml_edit_metadata = None


def azureml_edit_metadata(
    dataset: Path = None,
    column: str = None,
    data_type: _AzuremlEditMetadataDataTypeEnum = _AzuremlEditMetadataDataTypeEnum.unchanged,
    date_and_time_format: str = None,
    categorical: _AzuremlEditMetadataCategoricalEnum = _AzuremlEditMetadataCategoricalEnum.unchanged,
    fields: _AzuremlEditMetadataFieldsEnum = _AzuremlEditMetadataFieldsEnum.unchanged,
    new_column_name: str = None,
) -> _AzuremlEditMetadataComponent:
    """Edits metadata associated with columns in a dataset.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param column: Choose the columns to which your changes should apply
    :type column: str
    :param data_type: Specify the new data type of the column (enum: ['Unchanged', 'String', 'Integer', 'Double', 'Boolean', 'DateTime'])
    :type data_type: _AzuremlEditMetadataDataTypeEnum
    :param date_and_time_format: Specify custom format string for parsing DateTime, refer to Python standard library datetime.strftime() for detailed documentation. Leave empty for default permissive parsing (optional)
    :type date_and_time_format: str
    :param categorical: Indicate whether the column should be flagged as categorical (enum: ['Unchanged', 'Categorical', 'NonCategorical'])
    :type categorical: _AzuremlEditMetadataCategoricalEnum
    :param fields: Specify whether the column should be considered a feature or label by learning algorithms (enum: ['Unchanged', 'Features', 'Labels', 'ClearFeatures', 'ClearLabels', 'ClearScores'])
    :type fields: _AzuremlEditMetadataFieldsEnum
    :param new_column_name: Type the new names of the columns (optional)
    :type new_column_name: str
    :output results_dataset: Dataset with changed metadata
    :type: results_dataset: Output
    """
    global _azureml_edit_metadata
    if _azureml_edit_metadata is None:
        _azureml_edit_metadata = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Edit Metadata', version=None, feed='azureml')
    return _azureml_edit_metadata(
            dataset=dataset,
            column=column,
            data_type=data_type,
            date_and_time_format=date_and_time_format,
            categorical=categorical,
            fields=fields,
            new_column_name=new_column_name,)


class _AzuremlEnterDataManuallyDataformatEnum(Enum):
    arff = 'ARFF'
    csv = 'CSV'
    svmlight = 'SvmLight'
    tsv = 'TSV'


class _AzuremlEnterDataManuallyInput:
    dataformat: _AzuremlEnterDataManuallyDataformatEnum = _AzuremlEnterDataManuallyDataformatEnum.csv
    """Select which format data will be entered (enum: ['ARFF', 'CSV', 'SvmLight', 'TSV'])"""
    hasheader: bool = True
    """CSV or TSV file has a header (optional)"""
    data: str = None
    """Text to output as DataTable"""


class _AzuremlEnterDataManuallyOutput:
    dataset: Output = None
    """Entered data"""


class _AzuremlEnterDataManuallyComponent(Component):
    inputs: _AzuremlEnterDataManuallyInput
    outputs: _AzuremlEnterDataManuallyOutput
    runsettings: _CommandComponentRunsetting


_azureml_enter_data_manually = None


def azureml_enter_data_manually(
    dataformat: _AzuremlEnterDataManuallyDataformatEnum = _AzuremlEnterDataManuallyDataformatEnum.csv,
    hasheader: bool = True,
    data: str = None,
) -> _AzuremlEnterDataManuallyComponent:
    """Enables entering and editing small datasets by typing values.
    
    :param dataformat: Select which format data will be entered (enum: ['ARFF', 'CSV', 'SvmLight', 'TSV'])
    :type dataformat: _AzuremlEnterDataManuallyDataformatEnum
    :param hasheader: CSV or TSV file has a header (optional)
    :type hasheader: bool
    :param data: Text to output as DataTable
    :type data: str
    :output dataset: Entered data
    :type: dataset: Output
    """
    global _azureml_enter_data_manually
    if _azureml_enter_data_manually is None:
        _azureml_enter_data_manually = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Enter Data Manually', version=None, feed='azureml')
    return _azureml_enter_data_manually(
            dataformat=dataformat,
            hasheader=hasheader,
            data=data,)


class _AzuremlEvaluateModelInput:
    scored_dataset: Input = None
    """Scored dataset"""
    scored_dataset_to_compare: Input = None
    """Scored dataset to compare (optional)(optional)"""


class _AzuremlEvaluateModelOutput:
    evaluation_results: Output = None
    """Data evaluation result"""


class _AzuremlEvaluateModelComponent(Component):
    inputs: _AzuremlEvaluateModelInput
    outputs: _AzuremlEvaluateModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_evaluate_model = None


def azureml_evaluate_model(
    scored_dataset: Path = None,
    scored_dataset_to_compare: Path = None,
) -> _AzuremlEvaluateModelComponent:
    """Evaluates the results of a classification or regression model with standard metrics.
    
    :param scored_dataset: Scored dataset
    :type scored_dataset: Path
    :param scored_dataset_to_compare: Scored dataset to compare (optional)(optional)
    :type scored_dataset_to_compare: Path
    :output evaluation_results: Data evaluation result
    :type: evaluation_results: Output
    """
    global _azureml_evaluate_model
    if _azureml_evaluate_model is None:
        _azureml_evaluate_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Evaluate Model', version=None, feed='azureml')
    return _azureml_evaluate_model(
            scored_dataset=scored_dataset,
            scored_dataset_to_compare=scored_dataset_to_compare,)


class _AzuremlEvaluateRecommenderInput:
    test_dataset: Input = None
    """Test dataset"""
    scored_dataset: Input = None
    """Scored dataset"""


class _AzuremlEvaluateRecommenderOutput:
    metric: Output = None
    """A table of evaluation metrics"""


class _AzuremlEvaluateRecommenderComponent(Component):
    inputs: _AzuremlEvaluateRecommenderInput
    outputs: _AzuremlEvaluateRecommenderOutput
    runsettings: _CommandComponentRunsetting


_azureml_evaluate_recommender = None


def azureml_evaluate_recommender(
    test_dataset: Path = None,
    scored_dataset: Path = None,
) -> _AzuremlEvaluateRecommenderComponent:
    """Evaluate a recommendation model.
    
    :param test_dataset: Test dataset
    :type test_dataset: Path
    :param scored_dataset: Scored dataset
    :type scored_dataset: Path
    :output metric: A table of evaluation metrics
    :type: metric: Output
    """
    global _azureml_evaluate_recommender
    if _azureml_evaluate_recommender is None:
        _azureml_evaluate_recommender = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Evaluate Recommender', version=None, feed='azureml')
    return _azureml_evaluate_recommender(
            test_dataset=test_dataset,
            scored_dataset=scored_dataset,)


class _AzuremlExecutePythonScriptInput:
    dataset1: Input = None
    """Input dataset 1(optional)"""
    dataset2: Input = None
    """Input dataset 2(optional)"""
    script_bundle: Input = None
    """Zip file containing custom resources(optional)"""
    python_script: str = '\n# The script MUST contain a function named azureml_main\n# which is the entry point for this module.\n\n# imports up here can be used to\nimport pandas as pd\n\n# The entry point function MUST have two input arguments.\n# If the input port is not connected, the corresponding\n# dataframe argument will be None.\n#   Param<dataframe1>: a pandas.DataFrame\n#   Param<dataframe2>: a pandas.DataFrame\ndef azureml_main(dataframe1 = None, dataframe2 = None):\n\n    # Execution logic goes here\n    print(f\'Input pandas.DataFrame #1: {dataframe1}\')\n\n    # If a zip file is connected to the third input port,\n    # it is unzipped under "./Script Bundle". This directory is added\n    # to sys.path. Therefore, if your zip file contains a Python file\n    # mymodule.py you can import it using:\n    # import mymodule\n\n    # Return value must be of a sequence of pandas.DataFrame\n    # E.g.\n    #   -  Single return value: return dataframe1,\n    #   -  Two return values: return dataframe1, dataframe2\n    return dataframe1,\n\n'
    """The Python script to execute"""


class _AzuremlExecutePythonScriptOutput:
    result_dataset: Output = None
    """Output Dataset"""
    python_device: Output = None
    """Output Dataset2"""


class _AzuremlExecutePythonScriptComponent(Component):
    inputs: _AzuremlExecutePythonScriptInput
    outputs: _AzuremlExecutePythonScriptOutput
    runsettings: _CommandComponentRunsetting


_azureml_execute_python_script = None


def azureml_execute_python_script(
    dataset1: Path = None,
    dataset2: Path = None,
    script_bundle: Path = None,
    python_script: str = '\n# The script MUST contain a function named azureml_main\n# which is the entry point for this module.\n\n# imports up here can be used to\nimport pandas as pd\n\n# The entry point function MUST have two input arguments.\n# If the input port is not connected, the corresponding\n# dataframe argument will be None.\n#   Param<dataframe1>: a pandas.DataFrame\n#   Param<dataframe2>: a pandas.DataFrame\ndef azureml_main(dataframe1 = None, dataframe2 = None):\n\n    # Execution logic goes here\n    print(f\'Input pandas.DataFrame #1: {dataframe1}\')\n\n    # If a zip file is connected to the third input port,\n    # it is unzipped under "./Script Bundle". This directory is added\n    # to sys.path. Therefore, if your zip file contains a Python file\n    # mymodule.py you can import it using:\n    # import mymodule\n\n    # Return value must be of a sequence of pandas.DataFrame\n    # E.g.\n    #   -  Single return value: return dataframe1,\n    #   -  Two return values: return dataframe1, dataframe2\n    return dataframe1,\n\n',
) -> _AzuremlExecutePythonScriptComponent:
    """Executes a Python script from an Azure Machine Learning designer pipeline.
    
    :param dataset1: Input dataset 1(optional)
    :type dataset1: Path
    :param dataset2: Input dataset 2(optional)
    :type dataset2: Path
    :param script_bundle: Zip file containing custom resources(optional)
    :type script_bundle: Path
    :param python_script: The Python script to execute
    :type python_script: str
    :output result_dataset: Output Dataset
    :type: result_dataset: Output
    :output python_device: Output Dataset2
    :type: python_device: Output
    """
    global _azureml_execute_python_script
    if _azureml_execute_python_script is None:
        _azureml_execute_python_script = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Execute Python Script', version=None, feed='azureml')
    return _azureml_execute_python_script(
            dataset1=dataset1,
            dataset2=dataset2,
            script_bundle=script_bundle,
            python_script=python_script,)


class _AzuremlExecuteRScriptInput:
    dataset1: Input = None
    """Input dataset 1(optional)"""
    dataset2: Input = None
    """Input dataset 2(optional)"""
    script_bundle: Input = None
    """Set of R sources(optional)"""
    r_script: str = '\n# R version: 3.5.1\n# The script MUST contain a function named azureml_main\n# which is the entry point for this module.\n\n# Please note that functions dependant on X11 library\n# such as "View" are not supported because X11 library\n# is not pre-installed.\n\n# The entry point function MUST have two input arguments.\n# If the input port is not connected, the corresponding\n# dataframe argument will be null.\n#   Param<dataframe1>: a R DataFrame\n#   Param<dataframe2>: a R DataFrame\nazureml_main <- function(dataframe1, dataframe2){\n  print("R script run.")\n\n  # If a zip file is connected to the third input port, it is\n  # unzipped under "./Script Bundle". This directory is added\n  # to sys.path.\n\n  # Return datasets as a Named List\n  return(list(dataset1=dataframe1, dataset2=dataframe2))\n}\n\n'
    """Specify a StreamReader pointing to the R script sources"""
    random_seed: int = None
    """Define a random seed value for use inside the R environment. Calls \"set.seed(value)\"  (optional)"""


class _AzuremlExecuteRScriptOutput:
    result_dataset: Output = None
    """Output Dataset"""
    r_device: Output = None
    """Output Dataset2"""


class _AzuremlExecuteRScriptComponent(Component):
    inputs: _AzuremlExecuteRScriptInput
    outputs: _AzuremlExecuteRScriptOutput
    runsettings: _CommandComponentRunsetting


_azureml_execute_r_script = None


def azureml_execute_r_script(
    dataset1: Path = None,
    dataset2: Path = None,
    script_bundle: Path = None,
    r_script: str = '\n# R version: 3.5.1\n# The script MUST contain a function named azureml_main\n# which is the entry point for this module.\n\n# Please note that functions dependant on X11 library\n# such as "View" are not supported because X11 library\n# is not pre-installed.\n\n# The entry point function MUST have two input arguments.\n# If the input port is not connected, the corresponding\n# dataframe argument will be null.\n#   Param<dataframe1>: a R DataFrame\n#   Param<dataframe2>: a R DataFrame\nazureml_main <- function(dataframe1, dataframe2){\n  print("R script run.")\n\n  # If a zip file is connected to the third input port, it is\n  # unzipped under "./Script Bundle". This directory is added\n  # to sys.path.\n\n  # Return datasets as a Named List\n  return(list(dataset1=dataframe1, dataset2=dataframe2))\n}\n\n',
    random_seed: int = None,
) -> _AzuremlExecuteRScriptComponent:
    """Executes an R script from an Azure Machine Learning designer pipeline.
    
    :param dataset1: Input dataset 1(optional)
    :type dataset1: Path
    :param dataset2: Input dataset 2(optional)
    :type dataset2: Path
    :param script_bundle: Set of R sources(optional)
    :type script_bundle: Path
    :param r_script: Specify a StreamReader pointing to the R script sources
    :type r_script: str
    :param random_seed: Define a random seed value for use inside the R environment. Calls \"set.seed(value)\"  (optional)
    :type random_seed: int
    :output result_dataset: Output Dataset
    :type: result_dataset: Output
    :output r_device: Output Dataset2
    :type: r_device: Output
    """
    global _azureml_execute_r_script
    if _azureml_execute_r_script is None:
        _azureml_execute_r_script = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Execute R Script', version=None, feed='azureml')
    return _azureml_execute_r_script(
            dataset1=dataset1,
            dataset2=dataset2,
            script_bundle=script_bundle,
            r_script=r_script,
            random_seed=random_seed,)


class _AzuremlExportDataInput:
    input_path: Input = None
    """export data"""
    datastore_type: str = None
    """datastore type (optional)"""
    output_data_store: str = None
    """the location of output data store"""
    output_path: str = None
    """the relative output path in the data store (optional)"""
    output_file_type: str = None
    """the file type to be outputted (optional)"""
    datatable_name: str = None
    """export data table name (optional)"""
    column_list_to_be_saved: str = None
    """selected column(s) to be exported (optional)"""
    column_list_datatable_columns: str = None
    """column names in export data table (optional)"""
    number_rows_per_operation: int = 50
    """number of rows per operation (optional)"""


class _AzuremlExportDataOutput:
    pass


class _AzuremlExportDataComponent(Component):
    inputs: _AzuremlExportDataInput
    outputs: _AzuremlExportDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_export_data = None


def azureml_export_data(
    input_path: Path = None,
    datastore_type: str = None,
    output_data_store: str = None,
    output_path: str = None,
    output_file_type: str = None,
    datatable_name: str = None,
    column_list_to_be_saved: str = None,
    column_list_datatable_columns: str = None,
    number_rows_per_operation: int = 50,
) -> _AzuremlExportDataComponent:
    """Writes a dataset to cloud-based storage in Azure, such as Azure blob storage, Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2.
    
    :param input_path: export data
    :type input_path: Path
    :param datastore_type: datastore type (optional)
    :type datastore_type: str
    :param output_data_store: the location of output data store
    :type output_data_store: str
    :param output_path: the relative output path in the data store (optional)
    :type output_path: str
    :param output_file_type: the file type to be outputted (optional)
    :type output_file_type: str
    :param datatable_name: export data table name (optional)
    :type datatable_name: str
    :param column_list_to_be_saved: selected column(s) to be exported (optional)
    :type column_list_to_be_saved: str
    :param column_list_datatable_columns: column names in export data table (optional)
    :type column_list_datatable_columns: str
    :param number_rows_per_operation: number of rows per operation (optional)
    :type number_rows_per_operation: int
    """
    global _azureml_export_data
    if _azureml_export_data is None:
        _azureml_export_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Export Data', version=None, feed='azureml')
    return _azureml_export_data(
            input_path=input_path,
            datastore_type=datastore_type,
            output_data_store=output_data_store,
            output_path=output_path,
            output_file_type=output_file_type,
            datatable_name=datatable_name,
            column_list_to_be_saved=column_list_to_be_saved,
            column_list_datatable_columns=column_list_datatable_columns,
            number_rows_per_operation=number_rows_per_operation,)


class _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum(Enum):
    create = 'Create'
    readonly = 'ReadOnly'


class _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum(Enum):
    binary_weight = 'Binary Weight'
    tf_weight = 'TF Weight'
    idf_weight = 'IDF Weight'
    tf_idf_weight = 'TF-IDF Weight'


class _AzuremlExtractNGramFeaturesFromTextInput:
    dataset: Input = None
    """Input data"""
    input_vocabulary: Input = None
    """Input vocabulary(optional)"""
    text_column: str = None
    """Name or index (one-based) of text column"""
    vocabulary_mode: _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum = _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum.create
    """Specify how the n-gram vocabulary should be created from the corpus (enum: ['Create', 'ReadOnly'])"""
    n_grams_size: int = 1
    """Indicate the maximum size of n-grams to create (min: 1)"""
    weighting_function: _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum = _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum.binary_weight
    """Choose the weighting function to apply to each n-gram value (enum: ['Binary Weight', 'TF Weight', 'IDF Weight', 'TF-IDF Weight'])"""
    minimum_word_length: int = 3
    """Specify the minimum length of words to include in n-grams (min: 1)"""
    maximum_word_length: int = 25
    """Specify the maximum length of words to include in n-grams (min: 2)"""
    minimum_n_gram_document_absolute_frequency: float = 5
    """Minimum n-gram document absolute frequency (min: 1.0)"""
    maximum_n_gram_document_ratio: float = 1
    """Maximum n-gram document ratio (min: 0.0001)"""
    normalize_n_gram_feature_vectors: bool = False
    """Normalize n-gram feature vectors.  If true, then the n-gram feature vector is divided by its L2 norm."""


class _AzuremlExtractNGramFeaturesFromTextOutput:
    results_dataset: Output = None
    """Extracted features"""
    result_vocabulary: Output = None
    """Result vocabulary"""


class _AzuremlExtractNGramFeaturesFromTextComponent(Component):
    inputs: _AzuremlExtractNGramFeaturesFromTextInput
    outputs: _AzuremlExtractNGramFeaturesFromTextOutput
    runsettings: _CommandComponentRunsetting


_azureml_extract_n_gram_features_from_text = None


def azureml_extract_n_gram_features_from_text(
    dataset: Path = None,
    input_vocabulary: Path = None,
    text_column: str = None,
    vocabulary_mode: _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum = _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum.create,
    n_grams_size: int = 1,
    weighting_function: _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum = _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum.binary_weight,
    minimum_word_length: int = 3,
    maximum_word_length: int = 25,
    minimum_n_gram_document_absolute_frequency: float = 5,
    maximum_n_gram_document_ratio: float = 1,
    normalize_n_gram_feature_vectors: bool = False,
) -> _AzuremlExtractNGramFeaturesFromTextComponent:
    """Creates N-Gram dictionary features and does feature selection on them.
    
    :param dataset: Input data
    :type dataset: Path
    :param input_vocabulary: Input vocabulary(optional)
    :type input_vocabulary: Path
    :param text_column: Name or index (one-based) of text column
    :type text_column: str
    :param vocabulary_mode: Specify how the n-gram vocabulary should be created from the corpus (enum: ['Create', 'ReadOnly'])
    :type vocabulary_mode: _AzuremlExtractNGramFeaturesFromTextVocabularyModeEnum
    :param n_grams_size: Indicate the maximum size of n-grams to create (min: 1)
    :type n_grams_size: int
    :param weighting_function: Choose the weighting function to apply to each n-gram value (enum: ['Binary Weight', 'TF Weight', 'IDF Weight', 'TF-IDF Weight'])
    :type weighting_function: _AzuremlExtractNGramFeaturesFromTextWeightingFunctionEnum
    :param minimum_word_length: Specify the minimum length of words to include in n-grams (min: 1)
    :type minimum_word_length: int
    :param maximum_word_length: Specify the maximum length of words to include in n-grams (min: 2)
    :type maximum_word_length: int
    :param minimum_n_gram_document_absolute_frequency: Minimum n-gram document absolute frequency (min: 1.0)
    :type minimum_n_gram_document_absolute_frequency: float
    :param maximum_n_gram_document_ratio: Maximum n-gram document ratio (min: 0.0001)
    :type maximum_n_gram_document_ratio: float
    :param normalize_n_gram_feature_vectors: Normalize n-gram feature vectors.  If true, then the n-gram feature vector is divided by its L2 norm.
    :type normalize_n_gram_feature_vectors: bool
    :output results_dataset: Extracted features
    :type: results_dataset: Output
    :output result_vocabulary: Result vocabulary
    :type: result_vocabulary: Output
    """
    global _azureml_extract_n_gram_features_from_text
    if _azureml_extract_n_gram_features_from_text is None:
        _azureml_extract_n_gram_features_from_text = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Extract N-Gram Features from Text', version=None, feed='azureml')
    return _azureml_extract_n_gram_features_from_text(
            dataset=dataset,
            input_vocabulary=input_vocabulary,
            text_column=text_column,
            vocabulary_mode=vocabulary_mode,
            n_grams_size=n_grams_size,
            weighting_function=weighting_function,
            minimum_word_length=minimum_word_length,
            maximum_word_length=maximum_word_length,
            minimum_n_gram_document_absolute_frequency=minimum_n_gram_document_absolute_frequency,
            maximum_n_gram_document_ratio=maximum_n_gram_document_ratio,
            normalize_n_gram_feature_vectors=normalize_n_gram_feature_vectors,)


class _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlFastForestQuantileRegressionInput:
    create_trainer_mode: _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum = _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    number_of_trees: int = 100
    """Specifies the number of trees to be constructed (optional)"""
    number_of_leaves: int = 20
    """Specifies the maximum number of leaves per tree. The default number is 20 (optional, min: 2)"""
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10
    """Indicates the minimum number of training instances requried to form a leaf (optional)"""
    bagging_fraction: float = 0.7
    """Specifies the fraction of training data to use for each tree (optional)"""
    split_fraction: float = 0.7
    """Specifies the fraction of features (chosen randomly) to use for each split (optional)"""
    quantiles_to_be_estimated: str = '0.25; 0.5; 0.75'
    """Specifies the quantile to be estimated (optional)"""
    range_for_total_number_of_trees_constructed: str = '16; 32; 64'
    """Specify the range for the maximum number of trees that can be created during training (optional)"""
    range_for_maximum_number_of_leaves_per_tree: str = '16; 32; 64'
    """Specify range for the maximum number of leaves allowed per tree (optional)"""
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 5; 10'
    """Specify the range for the minimum number of cases required to form a leaf (optional)"""
    range_for_bagging_fraction: str = '0.25; 0.5; 0.75'
    """Specifies the range for fraction of training data to use for each tree (optional)"""
    range_for_split_fraction: str = '0.25; 0.5; 0.75'
    """Specifies the range for fraction of features (chosen randomly) to use for each split (optional)"""
    required_quantile_values: str = '0.25; 0.5; 0.75'
    """Required quantile value used during parameter sweep (optional)"""
    random_number_seed: int = None
    """Provide a seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlFastForestQuantileRegressionOutput:
    untrained_model: Output = None
    """An untrained quantile regression model that can be connected to the Train Generic Model or Cross Validate Model modules."""


class _AzuremlFastForestQuantileRegressionComponent(Component):
    inputs: _AzuremlFastForestQuantileRegressionInput
    outputs: _AzuremlFastForestQuantileRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_fast_forest_quantile_regression = None


def azureml_fast_forest_quantile_regression(
    create_trainer_mode: _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum = _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum.singleparameter,
    number_of_trees: int = 100,
    number_of_leaves: int = 20,
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10,
    bagging_fraction: float = 0.7,
    split_fraction: float = 0.7,
    quantiles_to_be_estimated: str = '0.25; 0.5; 0.75',
    range_for_total_number_of_trees_constructed: str = '16; 32; 64',
    range_for_maximum_number_of_leaves_per_tree: str = '16; 32; 64',
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 5; 10',
    range_for_bagging_fraction: str = '0.25; 0.5; 0.75',
    range_for_split_fraction: str = '0.25; 0.5; 0.75',
    required_quantile_values: str = '0.25; 0.5; 0.75',
    random_number_seed: int = None,
) -> _AzuremlFastForestQuantileRegressionComponent:
    """Creates a quantile regression model
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlFastForestQuantileRegressionCreateTrainerModeEnum
    :param number_of_trees: Specifies the number of trees to be constructed (optional)
    :type number_of_trees: int
    :param number_of_leaves: Specifies the maximum number of leaves per tree. The default number is 20 (optional, min: 2)
    :type number_of_leaves: int
    :param minimum_number_of_training_instances_required_to_form_a_leaf: Indicates the minimum number of training instances requried to form a leaf (optional)
    :type minimum_number_of_training_instances_required_to_form_a_leaf: int
    :param bagging_fraction: Specifies the fraction of training data to use for each tree (optional)
    :type bagging_fraction: float
    :param split_fraction: Specifies the fraction of features (chosen randomly) to use for each split (optional)
    :type split_fraction: float
    :param quantiles_to_be_estimated: Specifies the quantile to be estimated (optional)
    :type quantiles_to_be_estimated: str
    :param range_for_total_number_of_trees_constructed: Specify the range for the maximum number of trees that can be created during training (optional)
    :type range_for_total_number_of_trees_constructed: str
    :param range_for_maximum_number_of_leaves_per_tree: Specify range for the maximum number of leaves allowed per tree (optional)
    :type range_for_maximum_number_of_leaves_per_tree: str
    :param range_for_minimum_number_of_training_instances_required_to_form_a_leaf: Specify the range for the minimum number of cases required to form a leaf (optional)
    :type range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str
    :param range_for_bagging_fraction: Specifies the range for fraction of training data to use for each tree (optional)
    :type range_for_bagging_fraction: str
    :param range_for_split_fraction: Specifies the range for fraction of features (chosen randomly) to use for each split (optional)
    :type range_for_split_fraction: str
    :param required_quantile_values: Required quantile value used during parameter sweep (optional)
    :type required_quantile_values: str
    :param random_number_seed: Provide a seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained quantile regression model that can be connected to the Train Generic Model or Cross Validate Model modules.
    :type: untrained_model: Output
    """
    global _azureml_fast_forest_quantile_regression
    if _azureml_fast_forest_quantile_regression is None:
        _azureml_fast_forest_quantile_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Fast Forest Quantile Regression', version=None, feed='azureml')
    return _azureml_fast_forest_quantile_regression(
            create_trainer_mode=create_trainer_mode,
            number_of_trees=number_of_trees,
            number_of_leaves=number_of_leaves,
            minimum_number_of_training_instances_required_to_form_a_leaf=minimum_number_of_training_instances_required_to_form_a_leaf,
            bagging_fraction=bagging_fraction,
            split_fraction=split_fraction,
            quantiles_to_be_estimated=quantiles_to_be_estimated,
            range_for_total_number_of_trees_constructed=range_for_total_number_of_trees_constructed,
            range_for_maximum_number_of_leaves_per_tree=range_for_maximum_number_of_leaves_per_tree,
            range_for_minimum_number_of_training_instances_required_to_form_a_leaf=range_for_minimum_number_of_training_instances_required_to_form_a_leaf,
            range_for_bagging_fraction=range_for_bagging_fraction,
            range_for_split_fraction=range_for_split_fraction,
            required_quantile_values=required_quantile_values,
            random_number_seed=random_number_seed,)


class _AzuremlFeatureHashingInput:
    dataset: Input = None
    """Input dataset"""
    target_column: str = None
    """Choose the columns to which hashing will be applied"""
    hashing_bitsize: int = 10
    """Type the number of bits used to hash the selected columns (min: 1, max: 31)"""
    n_grams: int = 2
    """Specify the number of N-grams generated during hashing (max: 10)"""


class _AzuremlFeatureHashingOutput:
    transformed_dataset: Output = None
    """Output dataset with hashed columns,the number of feature columns generated is related to the parameters(Hashing bitsize)."""


class _AzuremlFeatureHashingComponent(Component):
    inputs: _AzuremlFeatureHashingInput
    outputs: _AzuremlFeatureHashingOutput
    runsettings: _CommandComponentRunsetting


_azureml_feature_hashing = None


def azureml_feature_hashing(
    dataset: Path = None,
    target_column: str = None,
    hashing_bitsize: int = 10,
    n_grams: int = 2,
) -> _AzuremlFeatureHashingComponent:
    """Convert text data to numeric features using the nimbusml.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param target_column: Choose the columns to which hashing will be applied
    :type target_column: str
    :param hashing_bitsize: Type the number of bits used to hash the selected columns (min: 1, max: 31)
    :type hashing_bitsize: int
    :param n_grams: Specify the number of N-grams generated during hashing (max: 10)
    :type n_grams: int
    :output transformed_dataset: Output dataset with hashed columns,the number of feature columns generated is related to the parameters(Hashing bitsize).
    :type: transformed_dataset: Output
    """
    global _azureml_feature_hashing
    if _azureml_feature_hashing is None:
        _azureml_feature_hashing = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Feature Hashing', version=None, feed='azureml')
    return _azureml_feature_hashing(
            dataset=dataset,
            target_column=target_column,
            hashing_bitsize=hashing_bitsize,
            n_grams=n_grams,)


class _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum(Enum):
    pearsoncorrelation = 'PearsonCorrelation'
    chisquared = 'ChiSquared'


class _AzuremlFilterBasedFeatureSelectionInput:
    input_dataset: Input = None
    """Input dataset"""
    operate_on_feature_columns_only: bool = True
    """Indicate whether to use only feature columns in the scoring process (optional)"""
    target_column: str = None
    """Specify the target column"""
    number_of_desired_features: int = 1
    """Specify the number of features to output in results"""
    feature_scoring_method: _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum = _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum.pearsoncorrelation
    """Choose the method to use for scoring (enum: ['PearsonCorrelation', 'ChiSquared'])"""


class _AzuremlFilterBasedFeatureSelectionOutput:
    filtered_dataset: Output = None
    """Filtered dataset"""
    features: Output = None
    """Names of output columns and feature selection scores"""


class _AzuremlFilterBasedFeatureSelectionComponent(Component):
    inputs: _AzuremlFilterBasedFeatureSelectionInput
    outputs: _AzuremlFilterBasedFeatureSelectionOutput
    runsettings: _CommandComponentRunsetting


_azureml_filter_based_feature_selection = None


def azureml_filter_based_feature_selection(
    input_dataset: Path = None,
    operate_on_feature_columns_only: bool = True,
    target_column: str = None,
    number_of_desired_features: int = 1,
    feature_scoring_method: _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum = _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum.pearsoncorrelation,
) -> _AzuremlFilterBasedFeatureSelectionComponent:
    """Identifies the features in a dataset with the greatest predictive power.
    
    :param input_dataset: Input dataset
    :type input_dataset: Path
    :param operate_on_feature_columns_only: Indicate whether to use only feature columns in the scoring process (optional)
    :type operate_on_feature_columns_only: bool
    :param target_column: Specify the target column
    :type target_column: str
    :param number_of_desired_features: Specify the number of features to output in results
    :type number_of_desired_features: int
    :param feature_scoring_method: Choose the method to use for scoring (enum: ['PearsonCorrelation', 'ChiSquared'])
    :type feature_scoring_method: _AzuremlFilterBasedFeatureSelectionFeatureScoringMethodEnum
    :output filtered_dataset: Filtered dataset
    :type: filtered_dataset: Output
    :output features: Names of output columns and feature selection scores
    :type: features: Output
    """
    global _azureml_filter_based_feature_selection
    if _azureml_filter_based_feature_selection is None:
        _azureml_filter_based_feature_selection = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Filter Based Feature Selection', version=None, feed='azureml')
    return _azureml_filter_based_feature_selection(
            input_dataset=input_dataset,
            operate_on_feature_columns_only=operate_on_feature_columns_only,
            target_column=target_column,
            number_of_desired_features=number_of_desired_features,
            feature_scoring_method=feature_scoring_method,)


class _AzuremlGroupDataIntoBinsBinningModeEnum(Enum):
    quantiles = 'Quantiles'
    equal_width = 'Equal Width'
    custom_edges = 'Custom Edges'


class _AzuremlGroupDataIntoBinsQuantileNormalizationEnum(Enum):
    percent = 'Percent'
    pquantile = 'PQuantile'
    quantile_index = 'Quantile Index'


class _AzuremlGroupDataIntoBinsOutputModeEnum(Enum):
    append = 'Append'
    inplace = 'Inplace'
    result_only = 'Result Only'


class _AzuremlGroupDataIntoBinsInput:
    dataset: Input = None
    """Dataset to be analyzed"""
    binning_mode: _AzuremlGroupDataIntoBinsBinningModeEnum = _AzuremlGroupDataIntoBinsBinningModeEnum.quantiles
    """Choose a binning method (enum: ['Quantiles', 'Equal Width', 'Custom Edges'])"""
    number_of_bins: int = 10
    """Specify the desired number of bins (optional, min: 1)"""
    quantile_normalization: _AzuremlGroupDataIntoBinsQuantileNormalizationEnum = _AzuremlGroupDataIntoBinsQuantileNormalizationEnum.percent
    """Choose the method for normalizing quantiles (optional, enum: ['Percent', 'PQuantile', 'Quantile Index'])"""
    comma_separated_list_of_bin_edges: str = None
    """Type a comma-separated list of numbers to use as bin edges (optional)"""
    columns_to_bin: str = None
    """Choose columns for quantization"""
    output_mode: _AzuremlGroupDataIntoBinsOutputModeEnum = _AzuremlGroupDataIntoBinsOutputModeEnum.append
    """Indicate how quantized columns should be output (enum: ['Append', 'Inplace', 'Result Only'])"""
    tag_columns_as_categorical: bool = True
    """Indicate whether output columns should be tagged as categorical"""


class _AzuremlGroupDataIntoBinsOutput:
    quantized_dataset: Output = None
    """Dataset with quantized columns"""
    binning_transformation: Output = None
    """Transformation that applies quantization to the dataset"""


class _AzuremlGroupDataIntoBinsComponent(Component):
    inputs: _AzuremlGroupDataIntoBinsInput
    outputs: _AzuremlGroupDataIntoBinsOutput
    runsettings: _CommandComponentRunsetting


_azureml_group_data_into_bins = None


def azureml_group_data_into_bins(
    dataset: Path = None,
    binning_mode: _AzuremlGroupDataIntoBinsBinningModeEnum = _AzuremlGroupDataIntoBinsBinningModeEnum.quantiles,
    number_of_bins: int = 10,
    quantile_normalization: _AzuremlGroupDataIntoBinsQuantileNormalizationEnum = _AzuremlGroupDataIntoBinsQuantileNormalizationEnum.percent,
    comma_separated_list_of_bin_edges: str = None,
    columns_to_bin: str = None,
    output_mode: _AzuremlGroupDataIntoBinsOutputModeEnum = _AzuremlGroupDataIntoBinsOutputModeEnum.append,
    tag_columns_as_categorical: bool = True,
) -> _AzuremlGroupDataIntoBinsComponent:
    """Map input values to a smaller number of bins using a quantization function.
    
    :param dataset: Dataset to be analyzed
    :type dataset: Path
    :param binning_mode: Choose a binning method (enum: ['Quantiles', 'Equal Width', 'Custom Edges'])
    :type binning_mode: _AzuremlGroupDataIntoBinsBinningModeEnum
    :param number_of_bins: Specify the desired number of bins (optional, min: 1)
    :type number_of_bins: int
    :param quantile_normalization: Choose the method for normalizing quantiles (optional, enum: ['Percent', 'PQuantile', 'Quantile Index'])
    :type quantile_normalization: _AzuremlGroupDataIntoBinsQuantileNormalizationEnum
    :param comma_separated_list_of_bin_edges: Type a comma-separated list of numbers to use as bin edges (optional)
    :type comma_separated_list_of_bin_edges: str
    :param columns_to_bin: Choose columns for quantization
    :type columns_to_bin: str
    :param output_mode: Indicate how quantized columns should be output (enum: ['Append', 'Inplace', 'Result Only'])
    :type output_mode: _AzuremlGroupDataIntoBinsOutputModeEnum
    :param tag_columns_as_categorical: Indicate whether output columns should be tagged as categorical
    :type tag_columns_as_categorical: bool
    :output quantized_dataset: Dataset with quantized columns
    :type: quantized_dataset: Output
    :output binning_transformation: Transformation that applies quantization to the dataset
    :type: binning_transformation: Output
    """
    global _azureml_group_data_into_bins
    if _azureml_group_data_into_bins is None:
        _azureml_group_data_into_bins = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Group Data into Bins', version=None, feed='azureml')
    return _azureml_group_data_into_bins(
            dataset=dataset,
            binning_mode=binning_mode,
            number_of_bins=number_of_bins,
            quantile_normalization=quantile_normalization,
            comma_separated_list_of_bin_edges=comma_separated_list_of_bin_edges,
            columns_to_bin=columns_to_bin,
            output_mode=output_mode,
            tag_columns_as_categorical=tag_columns_as_categorical,)


class _AzuremlImportDataInput:
    input_dataset_request_dto: str = None
    """input dataset Id/Object"""
    data_store_type: str = None
    """data store type (optional)"""
    override_data_store_name: str = None
    """string (optional)"""
    override_data_path: str = None
    """string (optional)"""


class _AzuremlImportDataOutput:
    output_data: Output = None
    """DataFrameDirectory"""


class _AzuremlImportDataComponent(Component):
    inputs: _AzuremlImportDataInput
    outputs: _AzuremlImportDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_import_data = None


def azureml_import_data(
    input_dataset_request_dto: str = None,
    data_store_type: str = None,
    override_data_store_name: str = None,
    override_data_path: str = None,
) -> _AzuremlImportDataComponent:
    """Load data from web URLs or from various cloud-based storage in Azure, such as Azure SQL database, Azure blob storage,  Azure Data Lake Storage Gen1, Azure Data Lake Storage Gen2.
    
    :param input_dataset_request_dto: input dataset Id/Object
    :type input_dataset_request_dto: str
    :param data_store_type: data store type (optional)
    :type data_store_type: str
    :param override_data_store_name: string (optional)
    :type override_data_store_name: str
    :param override_data_path: string (optional)
    :type override_data_path: str
    :output output_data: DataFrameDirectory
    :type: output_data: Output
    """
    global _azureml_import_data
    if _azureml_import_data is None:
        _azureml_import_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Import Data', version=None, feed='azureml')
    return _azureml_import_data(
            input_dataset_request_dto=input_dataset_request_dto,
            data_store_type=data_store_type,
            override_data_store_name=override_data_store_name,
            override_data_path=override_data_path,)


class _AzuremlInitImageTransformationResizeEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationCenterCropEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationPadEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationRandomResizedCropEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationRandomCropEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationRandomRotationEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationRandomAffineEnum(Enum):
    false = 'False'
    true = 'True'


class _AzuremlInitImageTransformationInput:
    resize: _AzuremlInitImageTransformationResizeEnum = _AzuremlInitImageTransformationResizeEnum.true
    """Resize the input PIL Image to the given size (enum: ['False', 'True'])"""
    size: int = 256
    """Desired output size (optional, min: 1)"""
    center_crop: _AzuremlInitImageTransformationCenterCropEnum = _AzuremlInitImageTransformationCenterCropEnum.true
    """Crops the given PIL Image at the center (enum: ['False', 'True'])"""
    crop_size: int = 224
    """Desired output size of the crop (optional, min: 1)"""
    pad: _AzuremlInitImageTransformationPadEnum = _AzuremlInitImageTransformationPadEnum.false
    """Pad the given PIL Image on all sides with the given \"pad\" value (enum: ['False', 'True'])"""
    padding: int = 0
    """Padding on each border (optional)"""
    color_jitter: bool = False
    """Randomly change the brightness, contrast and saturation of an image"""
    grayscale: bool = False
    """Convert image to grayscale"""
    random_resized_crop: _AzuremlInitImageTransformationRandomResizedCropEnum = _AzuremlInitImageTransformationRandomResizedCropEnum.false
    """Crop the given PIL Image to random size and aspect ratio (enum: ['False', 'True'])"""
    random_resized_crop_size: int = 256
    """Expected output size of each edge (optional, min: 1)"""
    random_crop: _AzuremlInitImageTransformationRandomCropEnum = _AzuremlInitImageTransformationRandomCropEnum.false
    """Crop the given PIL Image at a random location (enum: ['False', 'True'])"""
    random_crop_size: int = 224
    """Desired output size of the crop (optional, min: 1)"""
    random_horizontal_flip: bool = True
    """Horizontally flip the given PIL Image randomly with a given probability"""
    random_vertical_flip: bool = False
    """Vertically flip the given PIL Image randomly with a given probability"""
    random_rotation: _AzuremlInitImageTransformationRandomRotationEnum = _AzuremlInitImageTransformationRandomRotationEnum.false
    """Rotate the image by angle (enum: ['False', 'True'])"""
    random_rotation_degrees: int = 0
    """Range of degrees to select from (optional, max: 180)"""
    random_affine: _AzuremlInitImageTransformationRandomAffineEnum = _AzuremlInitImageTransformationRandomAffineEnum.false
    """Random affine transformation of the image keeping center invariant (enum: ['False', 'True'])"""
    random_affine_degrees: int = 0
    """Range of degrees to select from (optional, max: 180)"""
    random_grayscale: bool = False
    """Randomly convert image to grayscale with a probability of p (default 0.1)"""
    random_perspective: bool = False
    """Performs Perspective transformation of the given PIL Image randomly with a given probability"""


class _AzuremlInitImageTransformationOutput:
    output_image_transformation: Output = None
    """Output image transformation"""


class _AzuremlInitImageTransformationComponent(Component):
    inputs: _AzuremlInitImageTransformationInput
    outputs: _AzuremlInitImageTransformationOutput
    runsettings: _CommandComponentRunsetting


_azureml_init_image_transformation = None


def azureml_init_image_transformation(
    resize: _AzuremlInitImageTransformationResizeEnum = _AzuremlInitImageTransformationResizeEnum.true,
    size: int = 256,
    center_crop: _AzuremlInitImageTransformationCenterCropEnum = _AzuremlInitImageTransformationCenterCropEnum.true,
    crop_size: int = 224,
    pad: _AzuremlInitImageTransformationPadEnum = _AzuremlInitImageTransformationPadEnum.false,
    padding: int = 0,
    color_jitter: bool = False,
    grayscale: bool = False,
    random_resized_crop: _AzuremlInitImageTransformationRandomResizedCropEnum = _AzuremlInitImageTransformationRandomResizedCropEnum.false,
    random_resized_crop_size: int = 256,
    random_crop: _AzuremlInitImageTransformationRandomCropEnum = _AzuremlInitImageTransformationRandomCropEnum.false,
    random_crop_size: int = 224,
    random_horizontal_flip: bool = True,
    random_vertical_flip: bool = False,
    random_rotation: _AzuremlInitImageTransformationRandomRotationEnum = _AzuremlInitImageTransformationRandomRotationEnum.false,
    random_rotation_degrees: int = 0,
    random_affine: _AzuremlInitImageTransformationRandomAffineEnum = _AzuremlInitImageTransformationRandomAffineEnum.false,
    random_affine_degrees: int = 0,
    random_grayscale: bool = False,
    random_perspective: bool = False,
) -> _AzuremlInitImageTransformationComponent:
    """Initialize image transformation.
    
    :param resize: Resize the input PIL Image to the given size (enum: ['False', 'True'])
    :type resize: _AzuremlInitImageTransformationResizeEnum
    :param size: Desired output size (optional, min: 1)
    :type size: int
    :param center_crop: Crops the given PIL Image at the center (enum: ['False', 'True'])
    :type center_crop: _AzuremlInitImageTransformationCenterCropEnum
    :param crop_size: Desired output size of the crop (optional, min: 1)
    :type crop_size: int
    :param pad: Pad the given PIL Image on all sides with the given \"pad\" value (enum: ['False', 'True'])
    :type pad: _AzuremlInitImageTransformationPadEnum
    :param padding: Padding on each border (optional)
    :type padding: int
    :param color_jitter: Randomly change the brightness, contrast and saturation of an image
    :type color_jitter: bool
    :param grayscale: Convert image to grayscale
    :type grayscale: bool
    :param random_resized_crop: Crop the given PIL Image to random size and aspect ratio (enum: ['False', 'True'])
    :type random_resized_crop: _AzuremlInitImageTransformationRandomResizedCropEnum
    :param random_resized_crop_size: Expected output size of each edge (optional, min: 1)
    :type random_resized_crop_size: int
    :param random_crop: Crop the given PIL Image at a random location (enum: ['False', 'True'])
    :type random_crop: _AzuremlInitImageTransformationRandomCropEnum
    :param random_crop_size: Desired output size of the crop (optional, min: 1)
    :type random_crop_size: int
    :param random_horizontal_flip: Horizontally flip the given PIL Image randomly with a given probability
    :type random_horizontal_flip: bool
    :param random_vertical_flip: Vertically flip the given PIL Image randomly with a given probability
    :type random_vertical_flip: bool
    :param random_rotation: Rotate the image by angle (enum: ['False', 'True'])
    :type random_rotation: _AzuremlInitImageTransformationRandomRotationEnum
    :param random_rotation_degrees: Range of degrees to select from (optional, max: 180)
    :type random_rotation_degrees: int
    :param random_affine: Random affine transformation of the image keeping center invariant (enum: ['False', 'True'])
    :type random_affine: _AzuremlInitImageTransformationRandomAffineEnum
    :param random_affine_degrees: Range of degrees to select from (optional, max: 180)
    :type random_affine_degrees: int
    :param random_grayscale: Randomly convert image to grayscale with a probability of p (default 0.1)
    :type random_grayscale: bool
    :param random_perspective: Performs Perspective transformation of the given PIL Image randomly with a given probability
    :type random_perspective: bool
    :output output_image_transformation: Output image transformation
    :type: output_image_transformation: Output
    """
    global _azureml_init_image_transformation
    if _azureml_init_image_transformation is None:
        _azureml_init_image_transformation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Init Image Transformation', version=None, feed='azureml')
    return _azureml_init_image_transformation(
            resize=resize,
            size=size,
            center_crop=center_crop,
            crop_size=crop_size,
            pad=pad,
            padding=padding,
            color_jitter=color_jitter,
            grayscale=grayscale,
            random_resized_crop=random_resized_crop,
            random_resized_crop_size=random_resized_crop_size,
            random_crop=random_crop,
            random_crop_size=random_crop_size,
            random_horizontal_flip=random_horizontal_flip,
            random_vertical_flip=random_vertical_flip,
            random_rotation=random_rotation,
            random_rotation_degrees=random_rotation_degrees,
            random_affine=random_affine,
            random_affine_degrees=random_affine_degrees,
            random_grayscale=random_grayscale,
            random_perspective=random_perspective,)


class _AzuremlJoinDataJoinTypeEnum(Enum):
    inner_join = 'Inner Join'
    left_outer_join = 'Left Outer Join'
    full_outer_join = 'Full Outer Join'
    left_semi_join = 'Left Semi-Join'


class _AzuremlJoinDataInput:
    left_dataset: Input = None
    """First dataset to join"""
    right_dataset: Input = None
    """Second dataset to join"""
    comma_separated_case_sensitive_names_of_join_key_columns_for_l: str = None
    """Select the join key columns for the first dataset"""
    comma_separated_case_sensitive_names_of_join_key_columns_for_r: str = None
    """Select the join key columns for the second dataset"""
    match_case: bool = True
    """Indicate whether a case-sensitive comparison is allowed on key columns"""
    join_type: _AzuremlJoinDataJoinTypeEnum = _AzuremlJoinDataJoinTypeEnum.inner_join
    """Choose a join type (enum: ['Inner Join', 'Left Outer Join', 'Full Outer Join', 'Left Semi-Join'])"""
    keep_right_key_columns_in_joined_table: bool = True
    """Indicate whether to keep key columns from the second dataset in the joined dataset (optional)"""


class _AzuremlJoinDataOutput:
    results_dataset: Output = None
    """Result of join operation"""


class _AzuremlJoinDataComponent(Component):
    inputs: _AzuremlJoinDataInput
    outputs: _AzuremlJoinDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_join_data = None


def azureml_join_data(
    left_dataset: Path = None,
    right_dataset: Path = None,
    comma_separated_case_sensitive_names_of_join_key_columns_for_l: str = None,
    comma_separated_case_sensitive_names_of_join_key_columns_for_r: str = None,
    match_case: bool = True,
    join_type: _AzuremlJoinDataJoinTypeEnum = _AzuremlJoinDataJoinTypeEnum.inner_join,
    keep_right_key_columns_in_joined_table: bool = True,
) -> _AzuremlJoinDataComponent:
    """Joins two datasets on selected key columns.
    
    :param left_dataset: First dataset to join
    :type left_dataset: Path
    :param right_dataset: Second dataset to join
    :type right_dataset: Path
    :param comma_separated_case_sensitive_names_of_join_key_columns_for_l: Select the join key columns for the first dataset
    :type comma_separated_case_sensitive_names_of_join_key_columns_for_l: str
    :param comma_separated_case_sensitive_names_of_join_key_columns_for_r: Select the join key columns for the second dataset
    :type comma_separated_case_sensitive_names_of_join_key_columns_for_r: str
    :param match_case: Indicate whether a case-sensitive comparison is allowed on key columns
    :type match_case: bool
    :param join_type: Choose a join type (enum: ['Inner Join', 'Left Outer Join', 'Full Outer Join', 'Left Semi-Join'])
    :type join_type: _AzuremlJoinDataJoinTypeEnum
    :param keep_right_key_columns_in_joined_table: Indicate whether to keep key columns from the second dataset in the joined dataset (optional)
    :type keep_right_key_columns_in_joined_table: bool
    :output results_dataset: Result of join operation
    :type: results_dataset: Output
    """
    global _azureml_join_data
    if _azureml_join_data is None:
        _azureml_join_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Join Data', version=None, feed='azureml')
    return _azureml_join_data(
            left_dataset=left_dataset,
            right_dataset=right_dataset,
            comma_separated_case_sensitive_names_of_join_key_columns_for_l=comma_separated_case_sensitive_names_of_join_key_columns_for_l,
            comma_separated_case_sensitive_names_of_join_key_columns_for_r=comma_separated_case_sensitive_names_of_join_key_columns_for_r,
            match_case=match_case,
            join_type=join_type,
            keep_right_key_columns_in_joined_table=keep_right_key_columns_in_joined_table,)


class _AzuremlKMeansClusteringCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'


class _AzuremlKMeansClusteringInitializationEnum(Enum):
    random = 'Random'
    k_means = 'K-Means++'
    default = 'Default'


class _AzuremlKMeansClusteringMetricEnum(Enum):
    euclidean = 'Euclidean'


class _AzuremlKMeansClusteringAssignLabelModeEnum(Enum):
    ignore_label_column = 'Ignore label column'
    fill_missing_values = 'Fill missing values'
    overwrite_from_closest_to_center = 'Overwrite from closest to center'


class _AzuremlKMeansClusteringInput:
    create_trainer_mode: _AzuremlKMeansClusteringCreateTrainerModeEnum = _AzuremlKMeansClusteringCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter'])"""
    number_of_centroids: int = 2
    """Number of Centroids (optional, min: 2)"""
    initialization: _AzuremlKMeansClusteringInitializationEnum = _AzuremlKMeansClusteringInitializationEnum.k_means
    """Initialization algorithm (optional, enum: ['Random', 'K-Means++', 'Default'])"""
    random_number_seed: int = None
    """Type a value to seed the random number for centroid generator used by the training model. Leave blank to have value randomly choosen at first train. (optional, max: 4294967295)"""
    metric: _AzuremlKMeansClusteringMetricEnum = _AzuremlKMeansClusteringMetricEnum.euclidean
    """Selected metric (enum: ['Euclidean'])"""
    should_input_instances_be_normalized: bool = True
    """Indicate whether instances should be normalized"""
    iterations: int = 100
    """Number of iterations (min: 1)"""
    assign_label_mode: _AzuremlKMeansClusteringAssignLabelModeEnum = _AzuremlKMeansClusteringAssignLabelModeEnum.ignore_label_column
    """Mode of value assignment to the labeled column (enum: ['Ignore label column', 'Fill missing values', 'Overwrite from closest to center'])"""


class _AzuremlKMeansClusteringOutput:
    untrained_model: Output = None
    """Untrained K-Means clustering model"""


class _AzuremlKMeansClusteringComponent(Component):
    inputs: _AzuremlKMeansClusteringInput
    outputs: _AzuremlKMeansClusteringOutput
    runsettings: _CommandComponentRunsetting


_azureml_k_means_clustering = None


def azureml_k_means_clustering(
    create_trainer_mode: _AzuremlKMeansClusteringCreateTrainerModeEnum = _AzuremlKMeansClusteringCreateTrainerModeEnum.singleparameter,
    number_of_centroids: int = 2,
    initialization: _AzuremlKMeansClusteringInitializationEnum = _AzuremlKMeansClusteringInitializationEnum.k_means,
    random_number_seed: int = None,
    metric: _AzuremlKMeansClusteringMetricEnum = _AzuremlKMeansClusteringMetricEnum.euclidean,
    should_input_instances_be_normalized: bool = True,
    iterations: int = 100,
    assign_label_mode: _AzuremlKMeansClusteringAssignLabelModeEnum = _AzuremlKMeansClusteringAssignLabelModeEnum.ignore_label_column,
) -> _AzuremlKMeansClusteringComponent:
    """Initialize K-Means clustering model.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter'])
    :type create_trainer_mode: _AzuremlKMeansClusteringCreateTrainerModeEnum
    :param number_of_centroids: Number of Centroids (optional, min: 2)
    :type number_of_centroids: int
    :param initialization: Initialization algorithm (optional, enum: ['Random', 'K-Means++', 'Default'])
    :type initialization: _AzuremlKMeansClusteringInitializationEnum
    :param random_number_seed: Type a value to seed the random number for centroid generator used by the training model. Leave blank to have value randomly choosen at first train. (optional, max: 4294967295)
    :type random_number_seed: int
    :param metric: Selected metric (enum: ['Euclidean'])
    :type metric: _AzuremlKMeansClusteringMetricEnum
    :param should_input_instances_be_normalized: Indicate whether instances should be normalized
    :type should_input_instances_be_normalized: bool
    :param iterations: Number of iterations (min: 1)
    :type iterations: int
    :param assign_label_mode: Mode of value assignment to the labeled column (enum: ['Ignore label column', 'Fill missing values', 'Overwrite from closest to center'])
    :type assign_label_mode: _AzuremlKMeansClusteringAssignLabelModeEnum
    :output untrained_model: Untrained K-Means clustering model
    :type: untrained_model: Output
    """
    global _azureml_k_means_clustering
    if _azureml_k_means_clustering is None:
        _azureml_k_means_clustering = _assets.load_component(
            _workspace.from_config(),
            name='azureml://K-Means Clustering', version=None, feed='azureml')
    return _azureml_k_means_clustering(
            create_trainer_mode=create_trainer_mode,
            number_of_centroids=number_of_centroids,
            initialization=initialization,
            random_number_seed=random_number_seed,
            metric=metric,
            should_input_instances_be_normalized=should_input_instances_be_normalized,
            iterations=iterations,
            assign_label_mode=assign_label_mode,)


class _AzuremlLatentDirichletAllocationShowAllOptionsEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlLatentDirichletAllocationInput:
    dataset: Input = None
    """Input dataset"""
    target_columns: str = None
    """Target column name or index"""
    number_of_topics_to_model: int = 5
    """Model the document distribution against N topics (min: 1, max: 1000)"""
    n_grams: int = 2
    """Order of N-grams generated during hashing (min: 1, max: 10)"""
    normalize: bool = True
    """Normalize output to probabilities. The feature topic matrix will be P(word|topic)."""
    show_all_options: _AzuremlLatentDirichletAllocationShowAllOptionsEnum = _AzuremlLatentDirichletAllocationShowAllOptionsEnum.false
    """Presents additional parameters specific to Skleaarn online LDA (enum: ['True', 'False'])"""
    rho_parameter: float = 0.01
    """Rho parameter (optional, min: 2.220446049250313e-16, max: 1.0)"""
    alpha_parameter: float = 0.01
    """Alpha parameter (optional, min: 2.220446049250313e-16, max: 1.0)"""
    estimated_number_of_documents: int = 1000
    """Estimated number of documents (optional, min: 1, max: 2147483647)"""
    size_of_the_batch: int = 32
    """Size of the batch (optional, min: 1, max: 1024)"""
    initial_value_of_iteration_count: int = 10
    """Initial value of iteration count used in learning rate update schedule (optional, min: 1, max: 2147483647)"""
    power_applied_to_the_iteration_during_updates: float = 0.5
    """Power applied to the iteration count during online updates (optional, min: 0.5, max: 1.0)"""
    passes: int = 25
    """Number of training iterations (optional, min: 1, max: 1024)"""
    build_dictionary_of_ngrams_prior_to_lda: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum = _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum.true
    """Builds a dictionary of ngrams prior to LDA. Useful for model inspection and interpretation (optional, enum: ['True', 'False'])"""
    maximum_number_of_ngrams_in_dictionary: int = 20000
    """Maximum size of the dictionary. If number of tokens in the input exceed this size, collisions may occur (optional, min: 1, max: 2147483647)"""
    hash_bits: int = 12
    """Number of bits to use for feature hashing (optional, min: 1, max: 31)"""
    build_dictionary_of_ngrams: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum = _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum.true
    """Builds a dictionary of ngrams prior to computing LDA. Useful for model inspection and interpretation (optional, enum: ['True', 'False'])"""
    maximum_size_of_ngram_dictionary: int = 20000
    """Maximum size of the ngrams dictionary. If number of tokens in the input exceed this size, collisions may occur (optional, min: 1, max: 2147483647)"""
    number_of_hash_bits: int = 12
    """Number of bits to use during feature hashing (optional, min: 1, max: 31)"""


class _AzuremlLatentDirichletAllocationOutput:
    transformed_dataset: Output = None
    """Output dataset"""
    feature_topic_matrix: Output = None
    """Feature topic matrix produced by LDA"""
    lda_transformation: Output = None
    """Transformation that applies LDA to the dataset"""


class _AzuremlLatentDirichletAllocationComponent(Component):
    inputs: _AzuremlLatentDirichletAllocationInput
    outputs: _AzuremlLatentDirichletAllocationOutput
    runsettings: _CommandComponentRunsetting


_azureml_latent_dirichlet_allocation = None


def azureml_latent_dirichlet_allocation(
    dataset: Path = None,
    target_columns: str = None,
    number_of_topics_to_model: int = 5,
    n_grams: int = 2,
    normalize: bool = True,
    show_all_options: _AzuremlLatentDirichletAllocationShowAllOptionsEnum = _AzuremlLatentDirichletAllocationShowAllOptionsEnum.false,
    rho_parameter: float = 0.01,
    alpha_parameter: float = 0.01,
    estimated_number_of_documents: int = 1000,
    size_of_the_batch: int = 32,
    initial_value_of_iteration_count: int = 10,
    power_applied_to_the_iteration_during_updates: float = 0.5,
    passes: int = 25,
    build_dictionary_of_ngrams_prior_to_lda: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum = _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum.true,
    maximum_number_of_ngrams_in_dictionary: int = 20000,
    hash_bits: int = 12,
    build_dictionary_of_ngrams: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum = _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum.true,
    maximum_size_of_ngram_dictionary: int = 20000,
    number_of_hash_bits: int = 12,
) -> _AzuremlLatentDirichletAllocationComponent:
    """Topic Modeling: Latent Dirichlet Allocation.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param target_columns: Target column name or index
    :type target_columns: str
    :param number_of_topics_to_model: Model the document distribution against N topics (min: 1, max: 1000)
    :type number_of_topics_to_model: int
    :param n_grams: Order of N-grams generated during hashing (min: 1, max: 10)
    :type n_grams: int
    :param normalize: Normalize output to probabilities. The feature topic matrix will be P(word|topic).
    :type normalize: bool
    :param show_all_options: Presents additional parameters specific to Skleaarn online LDA (enum: ['True', 'False'])
    :type show_all_options: _AzuremlLatentDirichletAllocationShowAllOptionsEnum
    :param rho_parameter: Rho parameter (optional, min: 2.220446049250313e-16, max: 1.0)
    :type rho_parameter: float
    :param alpha_parameter: Alpha parameter (optional, min: 2.220446049250313e-16, max: 1.0)
    :type alpha_parameter: float
    :param estimated_number_of_documents: Estimated number of documents (optional, min: 1, max: 2147483647)
    :type estimated_number_of_documents: int
    :param size_of_the_batch: Size of the batch (optional, min: 1, max: 1024)
    :type size_of_the_batch: int
    :param initial_value_of_iteration_count: Initial value of iteration count used in learning rate update schedule (optional, min: 1, max: 2147483647)
    :type initial_value_of_iteration_count: int
    :param power_applied_to_the_iteration_during_updates: Power applied to the iteration count during online updates (optional, min: 0.5, max: 1.0)
    :type power_applied_to_the_iteration_during_updates: float
    :param passes: Number of training iterations (optional, min: 1, max: 1024)
    :type passes: int
    :param build_dictionary_of_ngrams_prior_to_lda: Builds a dictionary of ngrams prior to LDA. Useful for model inspection and interpretation (optional, enum: ['True', 'False'])
    :type build_dictionary_of_ngrams_prior_to_lda: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsPriorToLdaEnum
    :param maximum_number_of_ngrams_in_dictionary: Maximum size of the dictionary. If number of tokens in the input exceed this size, collisions may occur (optional, min: 1, max: 2147483647)
    :type maximum_number_of_ngrams_in_dictionary: int
    :param hash_bits: Number of bits to use for feature hashing (optional, min: 1, max: 31)
    :type hash_bits: int
    :param build_dictionary_of_ngrams: Builds a dictionary of ngrams prior to computing LDA. Useful for model inspection and interpretation (optional, enum: ['True', 'False'])
    :type build_dictionary_of_ngrams: _AzuremlLatentDirichletAllocationBuildDictionaryOfNgramsEnum
    :param maximum_size_of_ngram_dictionary: Maximum size of the ngrams dictionary. If number of tokens in the input exceed this size, collisions may occur (optional, min: 1, max: 2147483647)
    :type maximum_size_of_ngram_dictionary: int
    :param number_of_hash_bits: Number of bits to use during feature hashing (optional, min: 1, max: 31)
    :type number_of_hash_bits: int
    :output transformed_dataset: Output dataset
    :type: transformed_dataset: Output
    :output feature_topic_matrix: Feature topic matrix produced by LDA
    :type: feature_topic_matrix: Output
    :output lda_transformation: Transformation that applies LDA to the dataset
    :type: lda_transformation: Output
    """
    global _azureml_latent_dirichlet_allocation
    if _azureml_latent_dirichlet_allocation is None:
        _azureml_latent_dirichlet_allocation = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Latent Dirichlet Allocation', version=None, feed='azureml')
    return _azureml_latent_dirichlet_allocation(
            dataset=dataset,
            target_columns=target_columns,
            number_of_topics_to_model=number_of_topics_to_model,
            n_grams=n_grams,
            normalize=normalize,
            show_all_options=show_all_options,
            rho_parameter=rho_parameter,
            alpha_parameter=alpha_parameter,
            estimated_number_of_documents=estimated_number_of_documents,
            size_of_the_batch=size_of_the_batch,
            initial_value_of_iteration_count=initial_value_of_iteration_count,
            power_applied_to_the_iteration_during_updates=power_applied_to_the_iteration_during_updates,
            passes=passes,
            build_dictionary_of_ngrams_prior_to_lda=build_dictionary_of_ngrams_prior_to_lda,
            maximum_number_of_ngrams_in_dictionary=maximum_number_of_ngrams_in_dictionary,
            hash_bits=hash_bits,
            build_dictionary_of_ngrams=build_dictionary_of_ngrams,
            maximum_size_of_ngram_dictionary=maximum_size_of_ngram_dictionary,
            number_of_hash_bits=number_of_hash_bits,)


class _AzuremlLinearRegressionSolutionMethodEnum(Enum):
    online_gradient_descent = 'Online Gradient Descent'
    ordinary_least_squares = 'Ordinary Least Squares'


class _AzuremlLinearRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlLinearRegressionInput:
    solution_method: _AzuremlLinearRegressionSolutionMethodEnum = _AzuremlLinearRegressionSolutionMethodEnum.ordinary_least_squares
    """Choose an optimization method (enum: ['Online Gradient Descent', 'Ordinary Least Squares'])"""
    create_trainer_mode: _AzuremlLinearRegressionCreateTrainerModeEnum = _AzuremlLinearRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (optional, enum: ['SingleParameter', 'ParameterRange'])"""
    learning_rate: float = 0.1
    """Specify the initial learning rate for the stochastic gradient descent optimizer (optional, min: 2.220446049250313e-16)"""
    number_of_epochs_over_which_algorithm_iterates_through_examples: int = 10
    """Specify how many times the algorithm should iterate through examples. For datasets with a small number of examples, this number should be large to reach convergence. (optional)"""
    l2_regularization_term_weight: float = 0.001
    """Specify the weight for L2 regularization. Use a non-zero value to avoid overfitting. (optional)"""
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2'
    """Specify the range for the initial learning rate for the stochastic gradient descent optimizer (optional)"""
    range_for_number_of_epochs_over_which_algorithm_iterates_through_examples: str = '1; 10; 100'
    """Specify range for how many times the algorithm should iterate through examples. For datasets with a small number of examples, this number should be large to reach convergence. (optional)"""
    range_for_l2_regularization_term_weight: str = '0.001; 0.01; 0.1'
    """Specify the range for the weight for L2 regularization. Use a non-zero value to avoid overfitting. (optional)"""
    should_input_instances_be_normalized: bool = True
    """Indicate whether instances should be normalized (optional)"""
    decrease_learning_rate_as_iterations_progress: bool = True
    """Indicate whether the learning rate should decrease as iterations progress (optional)"""
    l2_regularization_weight: float = 0.001
    """Specify the weight for the L2 regularization. Use a non-zero value to avoid overfitting. (optional)"""
    include_intercept_term: bool = True
    """Indicate whether an additional term should be added for the intercept (optional)"""
    random_number_seed: int = None
    """Specify a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlLinearRegressionOutput:
    untrained_model: Output = None
    """An untrained regression model"""


class _AzuremlLinearRegressionComponent(Component):
    inputs: _AzuremlLinearRegressionInput
    outputs: _AzuremlLinearRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_linear_regression = None


def azureml_linear_regression(
    solution_method: _AzuremlLinearRegressionSolutionMethodEnum = _AzuremlLinearRegressionSolutionMethodEnum.ordinary_least_squares,
    create_trainer_mode: _AzuremlLinearRegressionCreateTrainerModeEnum = _AzuremlLinearRegressionCreateTrainerModeEnum.singleparameter,
    learning_rate: float = 0.1,
    number_of_epochs_over_which_algorithm_iterates_through_examples: int = 10,
    l2_regularization_term_weight: float = 0.001,
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2',
    range_for_number_of_epochs_over_which_algorithm_iterates_through_examples: str = '1; 10; 100',
    range_for_l2_regularization_term_weight: str = '0.001; 0.01; 0.1',
    should_input_instances_be_normalized: bool = True,
    decrease_learning_rate_as_iterations_progress: bool = True,
    l2_regularization_weight: float = 0.001,
    include_intercept_term: bool = True,
    random_number_seed: int = None,
) -> _AzuremlLinearRegressionComponent:
    """Creates a linear regression model.
    
    :param solution_method: Choose an optimization method (enum: ['Online Gradient Descent', 'Ordinary Least Squares'])
    :type solution_method: _AzuremlLinearRegressionSolutionMethodEnum
    :param create_trainer_mode: Create advanced learner options (optional, enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlLinearRegressionCreateTrainerModeEnum
    :param learning_rate: Specify the initial learning rate for the stochastic gradient descent optimizer (optional, min: 2.220446049250313e-16)
    :type learning_rate: float
    :param number_of_epochs_over_which_algorithm_iterates_through_examples: Specify how many times the algorithm should iterate through examples. For datasets with a small number of examples, this number should be large to reach convergence. (optional)
    :type number_of_epochs_over_which_algorithm_iterates_through_examples: int
    :param l2_regularization_term_weight: Specify the weight for L2 regularization. Use a non-zero value to avoid overfitting. (optional)
    :type l2_regularization_term_weight: float
    :param range_for_learning_rate: Specify the range for the initial learning rate for the stochastic gradient descent optimizer (optional)
    :type range_for_learning_rate: str
    :param range_for_number_of_epochs_over_which_algorithm_iterates_through_examples: Specify range for how many times the algorithm should iterate through examples. For datasets with a small number of examples, this number should be large to reach convergence. (optional)
    :type range_for_number_of_epochs_over_which_algorithm_iterates_through_examples: str
    :param range_for_l2_regularization_term_weight: Specify the range for the weight for L2 regularization. Use a non-zero value to avoid overfitting. (optional)
    :type range_for_l2_regularization_term_weight: str
    :param should_input_instances_be_normalized: Indicate whether instances should be normalized (optional)
    :type should_input_instances_be_normalized: bool
    :param decrease_learning_rate_as_iterations_progress: Indicate whether the learning rate should decrease as iterations progress (optional)
    :type decrease_learning_rate_as_iterations_progress: bool
    :param l2_regularization_weight: Specify the weight for the L2 regularization. Use a non-zero value to avoid overfitting. (optional)
    :type l2_regularization_weight: float
    :param include_intercept_term: Indicate whether an additional term should be added for the intercept (optional)
    :type include_intercept_term: bool
    :param random_number_seed: Specify a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained regression model
    :type: untrained_model: Output
    """
    global _azureml_linear_regression
    if _azureml_linear_regression is None:
        _azureml_linear_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Linear Regression', version=None, feed='azureml')
    return _azureml_linear_regression(
            solution_method=solution_method,
            create_trainer_mode=create_trainer_mode,
            learning_rate=learning_rate,
            number_of_epochs_over_which_algorithm_iterates_through_examples=number_of_epochs_over_which_algorithm_iterates_through_examples,
            l2_regularization_term_weight=l2_regularization_term_weight,
            range_for_learning_rate=range_for_learning_rate,
            range_for_number_of_epochs_over_which_algorithm_iterates_through_examples=range_for_number_of_epochs_over_which_algorithm_iterates_through_examples,
            range_for_l2_regularization_term_weight=range_for_l2_regularization_term_weight,
            should_input_instances_be_normalized=should_input_instances_be_normalized,
            decrease_learning_rate_as_iterations_progress=decrease_learning_rate_as_iterations_progress,
            l2_regularization_weight=l2_regularization_weight,
            include_intercept_term=include_intercept_term,
            random_number_seed=random_number_seed,)


class _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlMulticlassBoostedDecisionTreeInput:
    create_trainer_mode: _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum = _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    maximum_number_of_leaves_per_tree: int = 20
    """Specify the maximum number of leaves allowed per tree (optional, min: 2, max: 131072)"""
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10
    """Specify the minimum number of cases required to form a leaf (optional, min: 1)"""
    the_learning_rate: float = 0.2
    """Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)"""
    total_number_of_trees_constructed: int = 100
    """Specify the maximum number of trees that can be created during training (optional, min: 1)"""
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128'
    """Specify range for the maximum number of leaves allowed per tree (optional)"""
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50'
    """Specify the range for the minimum number of cases required to form a leaf (optional)"""
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4'
    """Specify the range for the initial learning rate (optional)"""
    range_for_total_number_of_trees_constructed: str = '20; 100; 500'
    """Specify the range for the maximum number of trees that can be created during training (optional)"""
    random_number_seed: int = None
    """Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlMulticlassBoostedDecisionTreeOutput:
    untrained_model: Output = None
    """An untrained multiclass classification model"""


class _AzuremlMulticlassBoostedDecisionTreeComponent(Component):
    inputs: _AzuremlMulticlassBoostedDecisionTreeInput
    outputs: _AzuremlMulticlassBoostedDecisionTreeOutput
    runsettings: _CommandComponentRunsetting


_azureml_multiclass_boosted_decision_tree = None


def azureml_multiclass_boosted_decision_tree(
    create_trainer_mode: _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum = _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum.singleparameter,
    maximum_number_of_leaves_per_tree: int = 20,
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10,
    the_learning_rate: float = 0.2,
    total_number_of_trees_constructed: int = 100,
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128',
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50',
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4',
    range_for_total_number_of_trees_constructed: str = '20; 100; 500',
    random_number_seed: int = None,
) -> _AzuremlMulticlassBoostedDecisionTreeComponent:
    """Creates a multiclass classifier using a boosted decision tree algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlMulticlassBoostedDecisionTreeCreateTrainerModeEnum
    :param maximum_number_of_leaves_per_tree: Specify the maximum number of leaves allowed per tree (optional, min: 2, max: 131072)
    :type maximum_number_of_leaves_per_tree: int
    :param minimum_number_of_training_instances_required_to_form_a_leaf: Specify the minimum number of cases required to form a leaf (optional, min: 1)
    :type minimum_number_of_training_instances_required_to_form_a_leaf: int
    :param the_learning_rate: Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)
    :type the_learning_rate: float
    :param total_number_of_trees_constructed: Specify the maximum number of trees that can be created during training (optional, min: 1)
    :type total_number_of_trees_constructed: int
    :param range_for_maximum_number_of_leaves_per_tree: Specify range for the maximum number of leaves allowed per tree (optional)
    :type range_for_maximum_number_of_leaves_per_tree: str
    :param range_for_minimum_number_of_training_instances_required_to_form_a_leaf: Specify the range for the minimum number of cases required to form a leaf (optional)
    :type range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str
    :param range_for_learning_rate: Specify the range for the initial learning rate (optional)
    :type range_for_learning_rate: str
    :param range_for_total_number_of_trees_constructed: Specify the range for the maximum number of trees that can be created during training (optional)
    :type range_for_total_number_of_trees_constructed: str
    :param random_number_seed: Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained multiclass classification model
    :type: untrained_model: Output
    """
    global _azureml_multiclass_boosted_decision_tree
    if _azureml_multiclass_boosted_decision_tree is None:
        _azureml_multiclass_boosted_decision_tree = _assets.load_component(
            _workspace.from_config(),
            name='azureml://MultiClass Boosted Decision Tree', version=None, feed='azureml')
    return _azureml_multiclass_boosted_decision_tree(
            create_trainer_mode=create_trainer_mode,
            maximum_number_of_leaves_per_tree=maximum_number_of_leaves_per_tree,
            minimum_number_of_training_instances_required_to_form_a_leaf=minimum_number_of_training_instances_required_to_form_a_leaf,
            the_learning_rate=the_learning_rate,
            total_number_of_trees_constructed=total_number_of_trees_constructed,
            range_for_maximum_number_of_leaves_per_tree=range_for_maximum_number_of_leaves_per_tree,
            range_for_minimum_number_of_training_instances_required_to_form_a_leaf=range_for_minimum_number_of_training_instances_required_to_form_a_leaf,
            range_for_learning_rate=range_for_learning_rate,
            range_for_total_number_of_trees_constructed=range_for_total_number_of_trees_constructed,
            random_number_seed=random_number_seed,)


class _AzuremlMulticlassDecisionForestCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlMulticlassDecisionForestResamplingMethodEnum(Enum):
    bagging_resampling = 'Bagging Resampling'
    replicate_resampling = 'Replicate Resampling'


class _AzuremlMulticlassDecisionForestInput:
    create_trainer_mode: _AzuremlMulticlassDecisionForestCreateTrainerModeEnum = _AzuremlMulticlassDecisionForestCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    number_of_decision_trees: int = 8
    """Specify the number of decision trees to create in the ensemble (optional, min: 1)"""
    maximum_depth_of_the_decision_trees: int = 32
    """Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)"""
    minimum_number_of_samples_per_leaf_node: int = 1
    """Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)"""
    range_for_number_of_decision_trees: str = '1; 8; 32'
    """Specify range for the number of decision trees to create in the ensemble (optional)"""
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64'
    """Specify range for the maximum depth of the decision trees (optional)"""
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16'
    """Specify range for the minimum number of samples per leaf node (optional)"""
    resampling_method: _AzuremlMulticlassDecisionForestResamplingMethodEnum = _AzuremlMulticlassDecisionForestResamplingMethodEnum.bagging_resampling
    """Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])"""


class _AzuremlMulticlassDecisionForestOutput:
    untrained_model: Output = None
    """An untrained multiclass classification model"""


class _AzuremlMulticlassDecisionForestComponent(Component):
    inputs: _AzuremlMulticlassDecisionForestInput
    outputs: _AzuremlMulticlassDecisionForestOutput
    runsettings: _CommandComponentRunsetting


_azureml_multiclass_decision_forest = None


def azureml_multiclass_decision_forest(
    create_trainer_mode: _AzuremlMulticlassDecisionForestCreateTrainerModeEnum = _AzuremlMulticlassDecisionForestCreateTrainerModeEnum.singleparameter,
    number_of_decision_trees: int = 8,
    maximum_depth_of_the_decision_trees: int = 32,
    minimum_number_of_samples_per_leaf_node: int = 1,
    range_for_number_of_decision_trees: str = '1; 8; 32',
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64',
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16',
    resampling_method: _AzuremlMulticlassDecisionForestResamplingMethodEnum = _AzuremlMulticlassDecisionForestResamplingMethodEnum.bagging_resampling,
) -> _AzuremlMulticlassDecisionForestComponent:
    """Creates a multiclass classification model using the decision forest algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlMulticlassDecisionForestCreateTrainerModeEnum
    :param number_of_decision_trees: Specify the number of decision trees to create in the ensemble (optional, min: 1)
    :type number_of_decision_trees: int
    :param maximum_depth_of_the_decision_trees: Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)
    :type maximum_depth_of_the_decision_trees: int
    :param minimum_number_of_samples_per_leaf_node: Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)
    :type minimum_number_of_samples_per_leaf_node: int
    :param range_for_number_of_decision_trees: Specify range for the number of decision trees to create in the ensemble (optional)
    :type range_for_number_of_decision_trees: str
    :param range_for_the_maximum_depth_of_the_decision_trees: Specify range for the maximum depth of the decision trees (optional)
    :type range_for_the_maximum_depth_of_the_decision_trees: str
    :param range_for_the_minimum_number_of_samples_per_leaf_node: Specify range for the minimum number of samples per leaf node (optional)
    :type range_for_the_minimum_number_of_samples_per_leaf_node: str
    :param resampling_method: Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])
    :type resampling_method: _AzuremlMulticlassDecisionForestResamplingMethodEnum
    :output untrained_model: An untrained multiclass classification model
    :type: untrained_model: Output
    """
    global _azureml_multiclass_decision_forest
    if _azureml_multiclass_decision_forest is None:
        _azureml_multiclass_decision_forest = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Multiclass Decision Forest', version=None, feed='azureml')
    return _azureml_multiclass_decision_forest(
            create_trainer_mode=create_trainer_mode,
            number_of_decision_trees=number_of_decision_trees,
            maximum_depth_of_the_decision_trees=maximum_depth_of_the_decision_trees,
            minimum_number_of_samples_per_leaf_node=minimum_number_of_samples_per_leaf_node,
            range_for_number_of_decision_trees=range_for_number_of_decision_trees,
            range_for_the_maximum_depth_of_the_decision_trees=range_for_the_maximum_depth_of_the_decision_trees,
            range_for_the_minimum_number_of_samples_per_leaf_node=range_for_the_minimum_number_of_samples_per_leaf_node,
            resampling_method=resampling_method,)


class _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlMulticlassLogisticRegressionInput:
    create_trainer_mode: _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum = _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    optimization_tolerance: float = 1e-07
    """Specify a tolerance value for the L-BFGS optimizer (optional, min: 2.220446049250313e-16)"""
    l2_regularizaton_weight: float = 1.0
    """Specify the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    range_for_optimization_tolerance: str = '0.00001; 0.00000001'
    """Specify a range for the tolerance value for the L-BFGS optimizer (optional)"""
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0'
    """Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    random_number_seed: int = None
    """Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlMulticlassLogisticRegressionOutput:
    untrained_model: Output = None
    """An untrained classificaiton model"""


class _AzuremlMulticlassLogisticRegressionComponent(Component):
    inputs: _AzuremlMulticlassLogisticRegressionInput
    outputs: _AzuremlMulticlassLogisticRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_multiclass_logistic_regression = None


def azureml_multiclass_logistic_regression(
    create_trainer_mode: _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum = _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum.singleparameter,
    optimization_tolerance: float = 1e-07,
    l2_regularizaton_weight: float = 1.0,
    range_for_optimization_tolerance: str = '0.00001; 0.00000001',
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0',
    random_number_seed: int = None,
) -> _AzuremlMulticlassLogisticRegressionComponent:
    """Creates a multiclass logistic regression classification model.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlMulticlassLogisticRegressionCreateTrainerModeEnum
    :param optimization_tolerance: Specify a tolerance value for the L-BFGS optimizer (optional, min: 2.220446049250313e-16)
    :type optimization_tolerance: float
    :param l2_regularizaton_weight: Specify the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type l2_regularizaton_weight: float
    :param range_for_optimization_tolerance: Specify a range for the tolerance value for the L-BFGS optimizer (optional)
    :type range_for_optimization_tolerance: str
    :param range_for_l2_regularization_weight: Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type range_for_l2_regularization_weight: str
    :param random_number_seed: Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained classificaiton model
    :type: untrained_model: Output
    """
    global _azureml_multiclass_logistic_regression
    if _azureml_multiclass_logistic_regression is None:
        _azureml_multiclass_logistic_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Multiclass Logistic Regression', version=None, feed='azureml')
    return _azureml_multiclass_logistic_regression(
            create_trainer_mode=create_trainer_mode,
            optimization_tolerance=optimization_tolerance,
            l2_regularizaton_weight=l2_regularizaton_weight,
            range_for_optimization_tolerance=range_for_optimization_tolerance,
            range_for_l2_regularization_weight=range_for_l2_regularization_weight,
            random_number_seed=random_number_seed,)


class _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlMulticlassNeuralNetworkInput:
    create_trainer_mode: _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum = _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    hidden_layer_specification: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum = _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum.fully_connected_case
    """Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes: str = '100'
    """Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)"""
    the_learning_rate: float = 0.1
    """Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)"""
    number_of_learning_iterations: int = 100
    """Specify the number of iterations while learning (optional, min: 1)"""
    hidden_layer_specification1: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum = _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum.fully_connected_case
    """Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes1: str = '100'
    """Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)"""
    range_for_learning_rate: str = '0.1; 0.2; 0.4'
    """Specify the range for the size of each step in the learning process (optional)"""
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160'
    """Specify the range for the number of iterations while learning (optional)"""
    the_momentum: float = 0
    """Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)"""
    shuffle_examples: bool = True
    """Select this option to change the order of instances between learning iterations"""
    random_number_seed: int = None
    """Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)"""


class _AzuremlMulticlassNeuralNetworkOutput:
    untrained_model: Output = None
    """An untrained multiclass classification model"""


class _AzuremlMulticlassNeuralNetworkComponent(Component):
    inputs: _AzuremlMulticlassNeuralNetworkInput
    outputs: _AzuremlMulticlassNeuralNetworkOutput
    runsettings: _CommandComponentRunsetting


_azureml_multiclass_neural_network = None


def azureml_multiclass_neural_network(
    create_trainer_mode: _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum = _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum.singleparameter,
    hidden_layer_specification: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum = _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum.fully_connected_case,
    number_of_hidden_nodes: str = '100',
    the_learning_rate: float = 0.1,
    number_of_learning_iterations: int = 100,
    hidden_layer_specification1: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum = _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum.fully_connected_case,
    number_of_hidden_nodes1: str = '100',
    range_for_learning_rate: str = '0.1; 0.2; 0.4',
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160',
    the_momentum: float = 0,
    shuffle_examples: bool = True,
    random_number_seed: int = None,
) -> _AzuremlMulticlassNeuralNetworkComponent:
    """Creates a multiclass classification model using a neural network algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlMulticlassNeuralNetworkCreateTrainerModeEnum
    :param hidden_layer_specification: Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecificationEnum
    :param number_of_hidden_nodes: Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes: str
    :param the_learning_rate: Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)
    :type the_learning_rate: float
    :param number_of_learning_iterations: Specify the number of iterations while learning (optional, min: 1)
    :type number_of_learning_iterations: int
    :param hidden_layer_specification1: Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification1: _AzuremlMulticlassNeuralNetworkHiddenLayerSpecification1Enum
    :param number_of_hidden_nodes1: Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes1: str
    :param range_for_learning_rate: Specify the range for the size of each step in the learning process (optional)
    :type range_for_learning_rate: str
    :param range_for_number_of_learning_iterations: Specify the range for the number of iterations while learning (optional)
    :type range_for_number_of_learning_iterations: str
    :param the_momentum: Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)
    :type the_momentum: float
    :param shuffle_examples: Select this option to change the order of instances between learning iterations
    :type shuffle_examples: bool
    :param random_number_seed: Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained multiclass classification model
    :type: untrained_model: Output
    """
    global _azureml_multiclass_neural_network
    if _azureml_multiclass_neural_network is None:
        _azureml_multiclass_neural_network = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Multiclass Neural Network', version=None, feed='azureml')
    return _azureml_multiclass_neural_network(
            create_trainer_mode=create_trainer_mode,
            hidden_layer_specification=hidden_layer_specification,
            number_of_hidden_nodes=number_of_hidden_nodes,
            the_learning_rate=the_learning_rate,
            number_of_learning_iterations=number_of_learning_iterations,
            hidden_layer_specification1=hidden_layer_specification1,
            number_of_hidden_nodes1=number_of_hidden_nodes1,
            range_for_learning_rate=range_for_learning_rate,
            range_for_number_of_learning_iterations=range_for_number_of_learning_iterations,
            the_momentum=the_momentum,
            shuffle_examples=shuffle_examples,
            random_number_seed=random_number_seed,)


class _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlNeuralNetworkRegressionInput:
    create_trainer_mode: _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum = _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    hidden_layer_specification: _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum = _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum.fully_connected_case
    """Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes: str = '100'
    """Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)"""
    the_learning_rate: float = 0.1
    """Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)"""
    number_of_learning_iterations: int = 100
    """Specify the number of iterations while learning (optional, min: 1)"""
    hidden_layer_specification1: _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum = _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum.fully_connected_case
    """Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes1: str = '100'
    """Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)"""
    range_for_learning_rate: str = '0.1; 0.2; 0.4'
    """Specify the range for the size of each step in the learning process (optional)"""
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160'
    """Specify the range for the number of iterations while learning (optional)"""
    the_momentum: float = 0
    """Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)"""
    shuffle_examples: bool = True
    """Select this option to change the order of instances between learning iterations"""
    random_number_seed: int = None
    """Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)"""


class _AzuremlNeuralNetworkRegressionOutput:
    untrained_model: Output = None
    """An untrained regression model"""


class _AzuremlNeuralNetworkRegressionComponent(Component):
    inputs: _AzuremlNeuralNetworkRegressionInput
    outputs: _AzuremlNeuralNetworkRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_neural_network_regression = None


def azureml_neural_network_regression(
    create_trainer_mode: _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum = _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum.singleparameter,
    hidden_layer_specification: _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum = _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum.fully_connected_case,
    number_of_hidden_nodes: str = '100',
    the_learning_rate: float = 0.1,
    number_of_learning_iterations: int = 100,
    hidden_layer_specification1: _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum = _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum.fully_connected_case,
    number_of_hidden_nodes1: str = '100',
    range_for_learning_rate: str = '0.1; 0.2; 0.4',
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160',
    the_momentum: float = 0,
    shuffle_examples: bool = True,
    random_number_seed: int = None,
) -> _AzuremlNeuralNetworkRegressionComponent:
    """Creates a regression model using a neural network algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlNeuralNetworkRegressionCreateTrainerModeEnum
    :param hidden_layer_specification: Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification: _AzuremlNeuralNetworkRegressionHiddenLayerSpecificationEnum
    :param number_of_hidden_nodes: Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes: str
    :param the_learning_rate: Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)
    :type the_learning_rate: float
    :param number_of_learning_iterations: Specify the number of iterations while learning (optional, min: 1)
    :type number_of_learning_iterations: int
    :param hidden_layer_specification1: Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification1: _AzuremlNeuralNetworkRegressionHiddenLayerSpecification1Enum
    :param number_of_hidden_nodes1: Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes1: str
    :param range_for_learning_rate: Specify the range for the size of each step in the learning process (optional)
    :type range_for_learning_rate: str
    :param range_for_number_of_learning_iterations: Specify the range for the number of iterations while learning (optional)
    :type range_for_number_of_learning_iterations: str
    :param the_momentum: Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)
    :type the_momentum: float
    :param shuffle_examples: Select this option to change the order of instances between learning iterations
    :type shuffle_examples: bool
    :param random_number_seed: Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained regression model
    :type: untrained_model: Output
    """
    global _azureml_neural_network_regression
    if _azureml_neural_network_regression is None:
        _azureml_neural_network_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Neural Network Regression', version=None, feed='azureml')
    return _azureml_neural_network_regression(
            create_trainer_mode=create_trainer_mode,
            hidden_layer_specification=hidden_layer_specification,
            number_of_hidden_nodes=number_of_hidden_nodes,
            the_learning_rate=the_learning_rate,
            number_of_learning_iterations=number_of_learning_iterations,
            hidden_layer_specification1=hidden_layer_specification1,
            number_of_hidden_nodes1=number_of_hidden_nodes1,
            range_for_learning_rate=range_for_learning_rate,
            range_for_number_of_learning_iterations=range_for_number_of_learning_iterations,
            the_momentum=the_momentum,
            shuffle_examples=shuffle_examples,
            random_number_seed=random_number_seed,)


class _AzuremlNormalizeDataTransformationMethodEnum(Enum):
    zscore = 'ZScore'
    minmax = 'MinMax'
    logistic = 'Logistic'
    lognormal = 'LogNormal'
    tanh = 'Tanh'


class _AzuremlNormalizeDataInput:
    dataset: Input = None
    """Input dataset"""
    transformation_method: _AzuremlNormalizeDataTransformationMethodEnum = _AzuremlNormalizeDataTransformationMethodEnum.zscore
    """Choose the mathematical method used for scaling (enum: ['ZScore', 'MinMax', 'Logistic', 'LogNormal', 'Tanh'])"""
    use_0_for_constant_columns_when_checked: bool = True
    """Use NaN for constant columns when unchecked or 0 when checked  (optional)"""
    columns_to_transform: str = None
    """Select all columns to which the selected transformation should be applied"""


class _AzuremlNormalizeDataOutput:
    transformed_dataset: Output = None
    """Transformed dataset"""
    transformation_function: Output = None
    """Definition of the transformation function, which can be applied to other datasets"""


class _AzuremlNormalizeDataComponent(Component):
    inputs: _AzuremlNormalizeDataInput
    outputs: _AzuremlNormalizeDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_normalize_data = None


def azureml_normalize_data(
    dataset: Path = None,
    transformation_method: _AzuremlNormalizeDataTransformationMethodEnum = _AzuremlNormalizeDataTransformationMethodEnum.zscore,
    use_0_for_constant_columns_when_checked: bool = True,
    columns_to_transform: str = None,
) -> _AzuremlNormalizeDataComponent:
    """Rescales numeric data to constrain dataset values to a standard range.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param transformation_method: Choose the mathematical method used for scaling (enum: ['ZScore', 'MinMax', 'Logistic', 'LogNormal', 'Tanh'])
    :type transformation_method: _AzuremlNormalizeDataTransformationMethodEnum
    :param use_0_for_constant_columns_when_checked: Use NaN for constant columns when unchecked or 0 when checked  (optional)
    :type use_0_for_constant_columns_when_checked: bool
    :param columns_to_transform: Select all columns to which the selected transformation should be applied
    :type columns_to_transform: str
    :output transformed_dataset: Transformed dataset
    :type: transformed_dataset: Output
    :output transformation_function: Definition of the transformation function, which can be applied to other datasets
    :type: transformation_function: Output
    """
    global _azureml_normalize_data
    if _azureml_normalize_data is None:
        _azureml_normalize_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Normalize Data', version=None, feed='azureml')
    return _azureml_normalize_data(
            dataset=dataset,
            transformation_method=transformation_method,
            use_0_for_constant_columns_when_checked=use_0_for_constant_columns_when_checked,
            columns_to_transform=columns_to_transform,)


class _AzuremlOneVsAllMulticlassInput:
    untrained_binary_classification_model: Input = None
    """An untrained binary classification model"""


class _AzuremlOneVsAllMulticlassOutput:
    untrained_model: Output = None
    """An untrained multi-class classification"""


class _AzuremlOneVsAllMulticlassComponent(Component):
    inputs: _AzuremlOneVsAllMulticlassInput
    outputs: _AzuremlOneVsAllMulticlassOutput
    runsettings: _CommandComponentRunsetting


_azureml_one_vs_all_multiclass = None


def azureml_one_vs_all_multiclass(
    untrained_binary_classification_model: Path = None,
) -> _AzuremlOneVsAllMulticlassComponent:
    """Creates a one-vs-all multiclass classification model from an ensemble of binary classification models.
    
    :param untrained_binary_classification_model: An untrained binary classification model
    :type untrained_binary_classification_model: Path
    :output untrained_model: An untrained multi-class classification
    :type: untrained_model: Output
    """
    global _azureml_one_vs_all_multiclass
    if _azureml_one_vs_all_multiclass is None:
        _azureml_one_vs_all_multiclass = _assets.load_component(
            _workspace.from_config(),
            name='azureml://One-vs-All Multiclass', version=None, feed='azureml')
    return _azureml_one_vs_all_multiclass(
            untrained_binary_classification_model=untrained_binary_classification_model,)


class _AzuremlOneVsOneMulticlassInput:
    untrained_binary_classification_model: Input = None
    """An untrained binary classification model"""


class _AzuremlOneVsOneMulticlassOutput:
    untrained_model: Output = None
    """An untrained multi-class classification"""


class _AzuremlOneVsOneMulticlassComponent(Component):
    inputs: _AzuremlOneVsOneMulticlassInput
    outputs: _AzuremlOneVsOneMulticlassOutput
    runsettings: _CommandComponentRunsetting


_azureml_one_vs_one_multiclass = None


def azureml_one_vs_one_multiclass(
    untrained_binary_classification_model: Path = None,
) -> _AzuremlOneVsOneMulticlassComponent:
    """Creates a one-vs-one multiclass classification model from an ensemble of binary classification models.
    
    :param untrained_binary_classification_model: An untrained binary classification model
    :type untrained_binary_classification_model: Path
    :output untrained_model: An untrained multi-class classification
    :type: untrained_model: Output
    """
    global _azureml_one_vs_one_multiclass
    if _azureml_one_vs_one_multiclass is None:
        _azureml_one_vs_one_multiclass = _assets.load_component(
            _workspace.from_config(),
            name='azureml://One-vs-One Multiclass', version=None, feed='azureml')
    return _azureml_one_vs_one_multiclass(
            untrained_binary_classification_model=untrained_binary_classification_model,)


class _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum(Enum):
    singleparameter = 'SingleParameter'


class _AzuremlPcaBasedAnomalyDetectionInput:
    training_mode: _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum = _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum.singleparameter
    """Specify learner options. Use 'SingleParameter' to manually specify all values. Use 'ParameterRange' to sweep over tunable parameters. (enum: ['SingleParameter'])"""
    number_of_components_to_use_in_pca: int = 2
    """Specify the number of components to use in PCA. (optional, min: 1)"""
    oversampling_parameter_for_randomized_pca: int = 2
    """Specify the accuracy parameter for randomized PCA training. (optional)"""
    enable_input_feature_mean_normalization: bool = False
    """Specify if the input data is normalized to have zero mean. """


class _AzuremlPcaBasedAnomalyDetectionOutput:
    untrained_model: Output = None
    """An untrained PCA-based anomaly detection model."""


class _AzuremlPcaBasedAnomalyDetectionComponent(Component):
    inputs: _AzuremlPcaBasedAnomalyDetectionInput
    outputs: _AzuremlPcaBasedAnomalyDetectionOutput
    runsettings: _CommandComponentRunsetting


_azureml_pca_based_anomaly_detection = None


def azureml_pca_based_anomaly_detection(
    training_mode: _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum = _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum.singleparameter,
    number_of_components_to_use_in_pca: int = 2,
    oversampling_parameter_for_randomized_pca: int = 2,
    enable_input_feature_mean_normalization: bool = False,
) -> _AzuremlPcaBasedAnomalyDetectionComponent:
    """Create a PCA-based anomaly detection model.
    
    :param training_mode: Specify learner options. Use 'SingleParameter' to manually specify all values. Use 'ParameterRange' to sweep over tunable parameters. (enum: ['SingleParameter'])
    :type training_mode: _AzuremlPcaBasedAnomalyDetectionTrainingModeEnum
    :param number_of_components_to_use_in_pca: Specify the number of components to use in PCA. (optional, min: 1)
    :type number_of_components_to_use_in_pca: int
    :param oversampling_parameter_for_randomized_pca: Specify the accuracy parameter for randomized PCA training. (optional)
    :type oversampling_parameter_for_randomized_pca: int
    :param enable_input_feature_mean_normalization: Specify if the input data is normalized to have zero mean. 
    :type enable_input_feature_mean_normalization: bool
    :output untrained_model: An untrained PCA-based anomaly detection model.
    :type: untrained_model: Output
    """
    global _azureml_pca_based_anomaly_detection
    if _azureml_pca_based_anomaly_detection is None:
        _azureml_pca_based_anomaly_detection = _assets.load_component(
            _workspace.from_config(),
            name='azureml://PCA-Based Anomaly Detection', version=None, feed='azureml')
    return _azureml_pca_based_anomaly_detection(
            training_mode=training_mode,
            number_of_components_to_use_in_pca=number_of_components_to_use_in_pca,
            oversampling_parameter_for_randomized_pca=oversampling_parameter_for_randomized_pca,
            enable_input_feature_mean_normalization=enable_input_feature_mean_normalization,)


class _AzuremlPartitionAndSamplePartitionOrSampleModeEnum(Enum):
    assign_to_folds = 'Assign to Folds'
    pick_fold = 'Pick Fold'
    sampling = 'Sampling'
    head = 'Head'


class _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum(Enum):
    partition_evenly = 'Partition evenly'
    partition_with_customized_proportions = 'Partition with customized proportions'


class _AzuremlPartitionAndSampleStratifiedSplitEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlPartitionAndSampleInput:
    dataset: Input = None
    """Dataset to be split"""
    partition_or_sample_mode: _AzuremlPartitionAndSamplePartitionOrSampleModeEnum = _AzuremlPartitionAndSamplePartitionOrSampleModeEnum.sampling
    """Select the partition or sampling mode (enum: ['Assign to Folds', 'Pick Fold', 'Sampling', 'Head'])"""
    use_replacement_in_the_partitioning: bool = False
    """Indicate whether the dataset should be replaced when split, or split without replacement (optional)"""
    randomized_split: bool = True
    """Indicates whether split is random or not (optional)"""
    random_seed: int = 0
    """Specify a seed for the random number generator (optional, max: 4294967295)"""
    specify_the_partitioner_method: _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum = _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum.partition_evenly
    """EvenSize where you specify number of folds, or ShapeInPct where you specify a list of percentage numbers (optional, enum: ['Partition evenly', 'Partition with customized proportions'])"""
    specify_how_many_folds_do_you_want_to_split_evenly_into: int = 5
    """Number of even partitions to be evenly split into (optional, min: 1)"""
    stratified_split: _AzuremlPartitionAndSampleStratifiedSplitEnum = _AzuremlPartitionAndSampleStratifiedSplitEnum.false
    """Indicates whether the split is stratified or not (optional, enum: ['True', 'False'])"""
    stratification_key_column: str = None
    """Column containing stratification key (optional)"""
    proportion_list_of_customized_folds_separated_by_comma: str = None
    """List of proportions separated by comma (optional)"""
    stratified_split_for_customized_fold_assignment: _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum = _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum.false
    """Indicates whether the split is stratified or not for customized fold assignments (optional, enum: ['True', 'False'])"""
    stratification_key_column_for_customized_fold_assignment: str = None
    """Column containing stratification key for customized fold assignments (optional)"""
    specify_which_fold_to_be_sampled_from: int = 1
    """Index of the partitioned fold to be sampled from (optional, min: 1)"""
    pick_complement_of_the_selected_fold: bool = False
    """Complement of the logic fold (optional)"""
    rate_of_sampling: float = 0.01
    """Sampling rate (optional)"""
    random_seed_for_sampling: int = 0
    """Random number generator seed for sampling (optional, max: 4294967295)"""
    stratified_split_for_sampling: _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum = _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum.false
    """Indicates whether the split is stratified or not for sampling (optional, enum: ['True', 'False'])"""
    stratification_key_column_for_sampling: str = None
    """Column containing stratification key for sampling (optional)"""
    number_of_rows_to_select: int = 10
    """Maximum number of records that will be allowed to pass through to the next module (optional)"""


class _AzuremlPartitionAndSampleOutput:
    odataset: Output = None
    """Dataset resulting from the split"""


class _AzuremlPartitionAndSampleComponent(Component):
    inputs: _AzuremlPartitionAndSampleInput
    outputs: _AzuremlPartitionAndSampleOutput
    runsettings: _CommandComponentRunsetting


_azureml_partition_and_sample = None


def azureml_partition_and_sample(
    dataset: Path = None,
    partition_or_sample_mode: _AzuremlPartitionAndSamplePartitionOrSampleModeEnum = _AzuremlPartitionAndSamplePartitionOrSampleModeEnum.sampling,
    use_replacement_in_the_partitioning: bool = False,
    randomized_split: bool = True,
    random_seed: int = 0,
    specify_the_partitioner_method: _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum = _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum.partition_evenly,
    specify_how_many_folds_do_you_want_to_split_evenly_into: int = 5,
    stratified_split: _AzuremlPartitionAndSampleStratifiedSplitEnum = _AzuremlPartitionAndSampleStratifiedSplitEnum.false,
    stratification_key_column: str = None,
    proportion_list_of_customized_folds_separated_by_comma: str = None,
    stratified_split_for_customized_fold_assignment: _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum = _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum.false,
    stratification_key_column_for_customized_fold_assignment: str = None,
    specify_which_fold_to_be_sampled_from: int = 1,
    pick_complement_of_the_selected_fold: bool = False,
    rate_of_sampling: float = 0.01,
    random_seed_for_sampling: int = 0,
    stratified_split_for_sampling: _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum = _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum.false,
    stratification_key_column_for_sampling: str = None,
    number_of_rows_to_select: int = 10,
) -> _AzuremlPartitionAndSampleComponent:
    """Creates multiple partitions of a dataset based on sampling.
    
    :param dataset: Dataset to be split
    :type dataset: Path
    :param partition_or_sample_mode: Select the partition or sampling mode (enum: ['Assign to Folds', 'Pick Fold', 'Sampling', 'Head'])
    :type partition_or_sample_mode: _AzuremlPartitionAndSamplePartitionOrSampleModeEnum
    :param use_replacement_in_the_partitioning: Indicate whether the dataset should be replaced when split, or split without replacement (optional)
    :type use_replacement_in_the_partitioning: bool
    :param randomized_split: Indicates whether split is random or not (optional)
    :type randomized_split: bool
    :param random_seed: Specify a seed for the random number generator (optional, max: 4294967295)
    :type random_seed: int
    :param specify_the_partitioner_method: EvenSize where you specify number of folds, or ShapeInPct where you specify a list of percentage numbers (optional, enum: ['Partition evenly', 'Partition with customized proportions'])
    :type specify_the_partitioner_method: _AzuremlPartitionAndSampleSpecifyThePartitionerMethodEnum
    :param specify_how_many_folds_do_you_want_to_split_evenly_into: Number of even partitions to be evenly split into (optional, min: 1)
    :type specify_how_many_folds_do_you_want_to_split_evenly_into: int
    :param stratified_split: Indicates whether the split is stratified or not (optional, enum: ['True', 'False'])
    :type stratified_split: _AzuremlPartitionAndSampleStratifiedSplitEnum
    :param stratification_key_column: Column containing stratification key (optional)
    :type stratification_key_column: str
    :param proportion_list_of_customized_folds_separated_by_comma: List of proportions separated by comma (optional)
    :type proportion_list_of_customized_folds_separated_by_comma: str
    :param stratified_split_for_customized_fold_assignment: Indicates whether the split is stratified or not for customized fold assignments (optional, enum: ['True', 'False'])
    :type stratified_split_for_customized_fold_assignment: _AzuremlPartitionAndSampleStratifiedSplitForCustomizedFoldAssignmentEnum
    :param stratification_key_column_for_customized_fold_assignment: Column containing stratification key for customized fold assignments (optional)
    :type stratification_key_column_for_customized_fold_assignment: str
    :param specify_which_fold_to_be_sampled_from: Index of the partitioned fold to be sampled from (optional, min: 1)
    :type specify_which_fold_to_be_sampled_from: int
    :param pick_complement_of_the_selected_fold: Complement of the logic fold (optional)
    :type pick_complement_of_the_selected_fold: bool
    :param rate_of_sampling: Sampling rate (optional)
    :type rate_of_sampling: float
    :param random_seed_for_sampling: Random number generator seed for sampling (optional, max: 4294967295)
    :type random_seed_for_sampling: int
    :param stratified_split_for_sampling: Indicates whether the split is stratified or not for sampling (optional, enum: ['True', 'False'])
    :type stratified_split_for_sampling: _AzuremlPartitionAndSampleStratifiedSplitForSamplingEnum
    :param stratification_key_column_for_sampling: Column containing stratification key for sampling (optional)
    :type stratification_key_column_for_sampling: str
    :param number_of_rows_to_select: Maximum number of records that will be allowed to pass through to the next module (optional)
    :type number_of_rows_to_select: int
    :output odataset: Dataset resulting from the split
    :type: odataset: Output
    """
    global _azureml_partition_and_sample
    if _azureml_partition_and_sample is None:
        _azureml_partition_and_sample = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Partition and Sample', version=None, feed='azureml')
    return _azureml_partition_and_sample(
            dataset=dataset,
            partition_or_sample_mode=partition_or_sample_mode,
            use_replacement_in_the_partitioning=use_replacement_in_the_partitioning,
            randomized_split=randomized_split,
            random_seed=random_seed,
            specify_the_partitioner_method=specify_the_partitioner_method,
            specify_how_many_folds_do_you_want_to_split_evenly_into=specify_how_many_folds_do_you_want_to_split_evenly_into,
            stratified_split=stratified_split,
            stratification_key_column=stratification_key_column,
            proportion_list_of_customized_folds_separated_by_comma=proportion_list_of_customized_folds_separated_by_comma,
            stratified_split_for_customized_fold_assignment=stratified_split_for_customized_fold_assignment,
            stratification_key_column_for_customized_fold_assignment=stratification_key_column_for_customized_fold_assignment,
            specify_which_fold_to_be_sampled_from=specify_which_fold_to_be_sampled_from,
            pick_complement_of_the_selected_fold=pick_complement_of_the_selected_fold,
            rate_of_sampling=rate_of_sampling,
            random_seed_for_sampling=random_seed_for_sampling,
            stratified_split_for_sampling=stratified_split_for_sampling,
            stratification_key_column_for_sampling=stratification_key_column_for_sampling,
            number_of_rows_to_select=number_of_rows_to_select,)


class _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum(Enum):
    accuracy = 'Accuracy'
    precision = 'Precision'
    recall = 'Recall'
    mean_absolute_error = 'Mean Absolute Error'
    root_mean_squared_error = 'Root Mean Squared Error'
    relative_absolute_error = 'Relative Absolute Error'
    relative_squared_error = 'Relative Squared Error'
    coefficient_of_determination = 'Coefficient of Determination'


class _AzuremlPermutationFeatureImportanceInput:
    trained_model: Input = None
    """Trained model to be used for scoring"""
    test_data: Input = None
    """Test dataset for scoring and evaluating a model after permutation of feature values"""
    random_seed: int = 0
    """Random number generator seed value (max: 4294967295)"""
    metric_for_measuring_performance: _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum = _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum.accuracy
    """Evaluation metric (enum: ['Accuracy', 'Precision', 'Recall', 'Mean Absolute Error', 'Root Mean Squared Error', 'Relative Absolute Error', 'Relative Squared Error', 'Coefficient of Determination'])"""


class _AzuremlPermutationFeatureImportanceOutput:
    feature_importance: Output = None
    """Feature importance results"""


class _AzuremlPermutationFeatureImportanceComponent(Component):
    inputs: _AzuremlPermutationFeatureImportanceInput
    outputs: _AzuremlPermutationFeatureImportanceOutput
    runsettings: _CommandComponentRunsetting


_azureml_permutation_feature_importance = None


def azureml_permutation_feature_importance(
    trained_model: Path = None,
    test_data: Path = None,
    random_seed: int = 0,
    metric_for_measuring_performance: _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum = _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum.accuracy,
) -> _AzuremlPermutationFeatureImportanceComponent:
    """Computes the permutation feature importance scores of feature variables given a trained model and a test dataset.
    
    :param trained_model: Trained model to be used for scoring
    :type trained_model: Path
    :param test_data: Test dataset for scoring and evaluating a model after permutation of feature values
    :type test_data: Path
    :param random_seed: Random number generator seed value (max: 4294967295)
    :type random_seed: int
    :param metric_for_measuring_performance: Evaluation metric (enum: ['Accuracy', 'Precision', 'Recall', 'Mean Absolute Error', 'Root Mean Squared Error', 'Relative Absolute Error', 'Relative Squared Error', 'Coefficient of Determination'])
    :type metric_for_measuring_performance: _AzuremlPermutationFeatureImportanceMetricForMeasuringPerformanceEnum
    :output feature_importance: Feature importance results
    :type: feature_importance: Output
    """
    global _azureml_permutation_feature_importance
    if _azureml_permutation_feature_importance is None:
        _azureml_permutation_feature_importance = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Permutation Feature Importance', version=None, feed='azureml')
    return _azureml_permutation_feature_importance(
            trained_model=trained_model,
            test_data=test_data,
            random_seed=random_seed,
            metric_for_measuring_performance=metric_for_measuring_performance,)


class _AzuremlPoissonRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlPoissonRegressionInput:
    create_trainer_mode: _AzuremlPoissonRegressionCreateTrainerModeEnum = _AzuremlPoissonRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting: float = 1e-07
    """Specify a tolerance value for optimization convergence. The lower the value, the slower and more accurate the fitting. (optional, min: 2.220446049250313e-16)"""
    l1_regularization_weight: float = 1.0
    """Specify the L1 regularization weight. Use a non-zero value to avoid overfitting the model. (optional)"""
    l2_regularization_weight: float = 1.0
    """Specify the L2 regularization weight. Use a non-zero value to avoid overfitting the model. (optional)"""
    memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: int = 20
    """Indicate how much memory (in MB) to use for the L-BFGS optimizer. With less memory, training is faster but less accurate the training. (optional, min: 1)"""
    range_for_optimization_tolerance: str = '0.00001; 0.00000001'
    """Specify a range for the tolerance value for the L-BFGS optimizer (optional)"""
    range_for_l1_regularization_weight: str = '0.0; 0.01; 0.1; 1.0'
    """Specify the range for the L1 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0'
    """Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: str = '5; 20; 50'
    """Specify the range for the amount of memory (in MB) to use for the L-BFGS optimizer. The lower the value, the faster and less accurate the training. (optional)"""


class _AzuremlPoissonRegressionOutput:
    untrained_model: Output = None
    """An untrained Poisson regression model"""


class _AzuremlPoissonRegressionComponent(Component):
    inputs: _AzuremlPoissonRegressionInput
    outputs: _AzuremlPoissonRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_poisson_regression = None


def azureml_poisson_regression(
    create_trainer_mode: _AzuremlPoissonRegressionCreateTrainerModeEnum = _AzuremlPoissonRegressionCreateTrainerModeEnum.singleparameter,
    tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting: float = 1e-07,
    l1_regularization_weight: float = 1.0,
    l2_regularization_weight: float = 1.0,
    memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: int = 20,
    range_for_optimization_tolerance: str = '0.00001; 0.00000001',
    range_for_l1_regularization_weight: str = '0.0; 0.01; 0.1; 1.0',
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0',
    range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: str = '5; 20; 50',
) -> _AzuremlPoissonRegressionComponent:
    """Creates a regression model that assumes data has a Poisson distribution
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlPoissonRegressionCreateTrainerModeEnum
    :param tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting: Specify a tolerance value for optimization convergence. The lower the value, the slower and more accurate the fitting. (optional, min: 2.220446049250313e-16)
    :type tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting: float
    :param l1_regularization_weight: Specify the L1 regularization weight. Use a non-zero value to avoid overfitting the model. (optional)
    :type l1_regularization_weight: float
    :param l2_regularization_weight: Specify the L2 regularization weight. Use a non-zero value to avoid overfitting the model. (optional)
    :type l2_regularization_weight: float
    :param memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: Indicate how much memory (in MB) to use for the L-BFGS optimizer. With less memory, training is faster but less accurate the training. (optional, min: 1)
    :type memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: int
    :param range_for_optimization_tolerance: Specify a range for the tolerance value for the L-BFGS optimizer (optional)
    :type range_for_optimization_tolerance: str
    :param range_for_l1_regularization_weight: Specify the range for the L1 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type range_for_l1_regularization_weight: str
    :param range_for_l2_regularization_weight: Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type range_for_l2_regularization_weight: str
    :param range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: Specify the range for the amount of memory (in MB) to use for the L-BFGS optimizer. The lower the value, the faster and less accurate the training. (optional)
    :type range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training: str
    :output untrained_model: An untrained Poisson regression model
    :type: untrained_model: Output
    """
    global _azureml_poisson_regression
    if _azureml_poisson_regression is None:
        _azureml_poisson_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Poisson Regression', version=None, feed='azureml')
    return _azureml_poisson_regression(
            create_trainer_mode=create_trainer_mode,
            tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting=tolerance_parameter_for_optimization_convergence_the_lower_the_value_the_slower_and_more_accurate_the_fitting,
            l1_regularization_weight=l1_regularization_weight,
            l2_regularization_weight=l2_regularization_weight,
            memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training=memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training,
            range_for_optimization_tolerance=range_for_optimization_tolerance,
            range_for_l1_regularization_weight=range_for_l1_regularization_weight,
            range_for_l2_regularization_weight=range_for_l2_regularization_weight,
            range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training=range_for_memory_size_for_l_bfgs_the_lower_the_value_the_faster_and_less_accurate_the_training,)


class _AzuremlPreprocessTextLanguageEnum(Enum):
    english = 'English'


class _AzuremlPreprocessTextInput:
    dataset: Input = None
    """Input data"""
    stop_words: Input = None
    """Optional custom list of stop words to remove(optional)"""
    language: _AzuremlPreprocessTextLanguageEnum = _AzuremlPreprocessTextLanguageEnum.english
    """Select the language to preprocess (enum: ['English'])"""
    expand_verb_contractions: bool = True
    """Expand verb contractions (English only) (optional)"""
    text_column_to_clean: str = None
    """Select the text column to clean"""
    remove_stop_words: bool = True
    """Remove stop words"""
    use_lemmatization: bool = True
    """Use lemmatization"""
    detect_sentences: bool = True
    """Detect sentences by adding a sentence terminator \"|||\" that can be used by the n-gram features extractor module"""
    normalize_case_to_lowercase: bool = True
    """Normalize case to lowercase"""
    remove_numbers: bool = True
    """Remove numbers"""
    remove_special_characters: bool = True
    """Remove non-alphanumeric special characters and replace them with \"|\" character"""
    remove_duplicate_characters: bool = True
    """Remove duplicate characters"""
    remove_email_addresses: bool = True
    """Remove email addresses"""
    remove_urls: bool = True
    """Remove URLs"""
    normalize_backslashes_to_slashes: bool = True
    """Normalize backslashes to slashes"""
    split_tokens_on_special_characters: bool = True
    """Split tokens on special characters"""
    custom_regular_expression: str = None
    """Specify the custom regular expression (optional)"""
    custom_replacement_string: str = None
    """Specify the custom replacement string for the custom regular expression (optional)"""


class _AzuremlPreprocessTextOutput:
    results_dataset: Output = None
    """Results dataset"""


class _AzuremlPreprocessTextComponent(Component):
    inputs: _AzuremlPreprocessTextInput
    outputs: _AzuremlPreprocessTextOutput
    runsettings: _CommandComponentRunsetting


_azureml_preprocess_text = None


def azureml_preprocess_text(
    dataset: Path = None,
    stop_words: Path = None,
    language: _AzuremlPreprocessTextLanguageEnum = _AzuremlPreprocessTextLanguageEnum.english,
    expand_verb_contractions: bool = True,
    text_column_to_clean: str = None,
    remove_stop_words: bool = True,
    use_lemmatization: bool = True,
    detect_sentences: bool = True,
    normalize_case_to_lowercase: bool = True,
    remove_numbers: bool = True,
    remove_special_characters: bool = True,
    remove_duplicate_characters: bool = True,
    remove_email_addresses: bool = True,
    remove_urls: bool = True,
    normalize_backslashes_to_slashes: bool = True,
    split_tokens_on_special_characters: bool = True,
    custom_regular_expression: str = None,
    custom_replacement_string: str = None,
) -> _AzuremlPreprocessTextComponent:
    """Performs cleaning operations on text.
    
    :param dataset: Input data
    :type dataset: Path
    :param stop_words: Optional custom list of stop words to remove(optional)
    :type stop_words: Path
    :param language: Select the language to preprocess (enum: ['English'])
    :type language: _AzuremlPreprocessTextLanguageEnum
    :param expand_verb_contractions: Expand verb contractions (English only) (optional)
    :type expand_verb_contractions: bool
    :param text_column_to_clean: Select the text column to clean
    :type text_column_to_clean: str
    :param remove_stop_words: Remove stop words
    :type remove_stop_words: bool
    :param use_lemmatization: Use lemmatization
    :type use_lemmatization: bool
    :param detect_sentences: Detect sentences by adding a sentence terminator \"|||\" that can be used by the n-gram features extractor module
    :type detect_sentences: bool
    :param normalize_case_to_lowercase: Normalize case to lowercase
    :type normalize_case_to_lowercase: bool
    :param remove_numbers: Remove numbers
    :type remove_numbers: bool
    :param remove_special_characters: Remove non-alphanumeric special characters and replace them with \"|\" character
    :type remove_special_characters: bool
    :param remove_duplicate_characters: Remove duplicate characters
    :type remove_duplicate_characters: bool
    :param remove_email_addresses: Remove email addresses
    :type remove_email_addresses: bool
    :param remove_urls: Remove URLs
    :type remove_urls: bool
    :param normalize_backslashes_to_slashes: Normalize backslashes to slashes
    :type normalize_backslashes_to_slashes: bool
    :param split_tokens_on_special_characters: Split tokens on special characters
    :type split_tokens_on_special_characters: bool
    :param custom_regular_expression: Specify the custom regular expression (optional)
    :type custom_regular_expression: str
    :param custom_replacement_string: Specify the custom replacement string for the custom regular expression (optional)
    :type custom_replacement_string: str
    :output results_dataset: Results dataset
    :type: results_dataset: Output
    """
    global _azureml_preprocess_text
    if _azureml_preprocess_text is None:
        _azureml_preprocess_text = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Preprocess Text', version=None, feed='azureml')
    return _azureml_preprocess_text(
            dataset=dataset,
            stop_words=stop_words,
            language=language,
            expand_verb_contractions=expand_verb_contractions,
            text_column_to_clean=text_column_to_clean,
            remove_stop_words=remove_stop_words,
            use_lemmatization=use_lemmatization,
            detect_sentences=detect_sentences,
            normalize_case_to_lowercase=normalize_case_to_lowercase,
            remove_numbers=remove_numbers,
            remove_special_characters=remove_special_characters,
            remove_duplicate_characters=remove_duplicate_characters,
            remove_email_addresses=remove_email_addresses,
            remove_urls=remove_urls,
            normalize_backslashes_to_slashes=normalize_backslashes_to_slashes,
            split_tokens_on_special_characters=split_tokens_on_special_characters,
            custom_regular_expression=custom_regular_expression,
            custom_replacement_string=custom_replacement_string,)


class _AzuremlRemoveDuplicateRowsInput:
    dataset: Input = None
    """Input dataset"""
    key_column_selection_filter_expression: str = None
    """Choose the key columns to use when searching for duplicates"""
    retain_first_duplicate_row: bool = True
    """indicate whether to keep the first row of a set of duplicates and discard others. if false, the last duplicate row encountered will be kept."""


class _AzuremlRemoveDuplicateRowsOutput:
    results_dataset: Output = None
    """Filtered dataset"""


class _AzuremlRemoveDuplicateRowsComponent(Component):
    inputs: _AzuremlRemoveDuplicateRowsInput
    outputs: _AzuremlRemoveDuplicateRowsOutput
    runsettings: _CommandComponentRunsetting


_azureml_remove_duplicate_rows = None


def azureml_remove_duplicate_rows(
    dataset: Path = None,
    key_column_selection_filter_expression: str = None,
    retain_first_duplicate_row: bool = True,
) -> _AzuremlRemoveDuplicateRowsComponent:
    """Removes the duplicate rows from a dataset.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param key_column_selection_filter_expression: Choose the key columns to use when searching for duplicates
    :type key_column_selection_filter_expression: str
    :param retain_first_duplicate_row: indicate whether to keep the first row of a set of duplicates and discard others. if false, the last duplicate row encountered will be kept.
    :type retain_first_duplicate_row: bool
    :output results_dataset: Filtered dataset
    :type: results_dataset: Output
    """
    global _azureml_remove_duplicate_rows
    if _azureml_remove_duplicate_rows is None:
        _azureml_remove_duplicate_rows = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Remove Duplicate Rows', version=None, feed='azureml')
    return _azureml_remove_duplicate_rows(
            dataset=dataset,
            key_column_selection_filter_expression=key_column_selection_filter_expression,
            retain_first_duplicate_row=retain_first_duplicate_row,)


class _AzuremlResnetModelNameEnum(Enum):
    resnet18 = 'resnet18'
    resnet34 = 'resnet34'
    resnet50 = 'resnet50'
    resnet101 = 'resnet101'
    resnet152 = 'resnet152'
    resnext50_32x4d = 'resnext50_32x4d'
    resnext101_32x8d = 'resnext101_32x8d'
    wide_resnet50_2 = 'wide_resnet50_2'
    wide_resnet101_2 = 'wide_resnet101_2'


class _AzuremlResnetInput:
    model_name: _AzuremlResnetModelNameEnum = _AzuremlResnetModelNameEnum.resnext101_32x8d
    """Name of a certain resnet structure (enum: ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50_32x4d', 'resnext101_32x8d', 'wide_resnet50_2', 'wide_resnet101_2'])"""
    pretrained: bool = True
    """Indicate whether to use a model pre-trained on ImageNet"""
    zero_init_residual: bool = False
    """Zero-initialize the last BN in each residual branch. (optional)"""


class _AzuremlResnetOutput:
    untrained_model: Output = None
    """Untrained resnet model path"""


class _AzuremlResnetComponent(Component):
    inputs: _AzuremlResnetInput
    outputs: _AzuremlResnetOutput
    runsettings: _CommandComponentRunsetting


_azureml_resnet = None


def azureml_resnet(
    model_name: _AzuremlResnetModelNameEnum = _AzuremlResnetModelNameEnum.resnext101_32x8d,
    pretrained: bool = True,
    zero_init_residual: bool = False,
) -> _AzuremlResnetComponent:
    """Creates a image classification model using the resnet algorithm.
    
    :param model_name: Name of a certain resnet structure (enum: ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'resnext50_32x4d', 'resnext101_32x8d', 'wide_resnet50_2', 'wide_resnet101_2'])
    :type model_name: _AzuremlResnetModelNameEnum
    :param pretrained: Indicate whether to use a model pre-trained on ImageNet
    :type pretrained: bool
    :param zero_init_residual: Zero-initialize the last BN in each residual branch. (optional)
    :type zero_init_residual: bool
    :output untrained_model: Untrained resnet model path
    :type: untrained_model: Output
    """
    global _azureml_resnet
    if _azureml_resnet is None:
        _azureml_resnet = _assets.load_component(
            _workspace.from_config(),
            name='azureml://ResNet', version=None, feed='azureml')
    return _azureml_resnet(
            model_name=model_name,
            pretrained=pretrained,
            zero_init_residual=zero_init_residual,)


class _AzuremlSmoteInput:
    samples: Input = None
    """A DataTable of samples"""
    label_column: str = None
    """Select the column that contains the label or outcome column"""
    smote_percentage: int = 100
    """Amount of oversampling.If not in integral multiples of 100, the minority class will be randomized and downsampled from the next integral multiple of 100."""
    number_of_nearest_neighbors: int = 1
    """The number of nearest neighbors (min: 1)"""
    random_seed: int = 0
    """Random number generator seed (max: 4294967295)"""


class _AzuremlSmoteOutput:
    table: Output = None
    """A DataTable containing original samples plus an additional synthetic minority class samples, where T is the number of minority class samples"""


class _AzuremlSmoteComponent(Component):
    inputs: _AzuremlSmoteInput
    outputs: _AzuremlSmoteOutput
    runsettings: _CommandComponentRunsetting


_azureml_smote = None


def azureml_smote(
    samples: Path = None,
    label_column: str = None,
    smote_percentage: int = 100,
    number_of_nearest_neighbors: int = 1,
    random_seed: int = 0,
) -> _AzuremlSmoteComponent:
    """Increases the number of low incidence examples in a dataset.
    
    :param samples: A DataTable of samples
    :type samples: Path
    :param label_column: Select the column that contains the label or outcome column
    :type label_column: str
    :param smote_percentage: Amount of oversampling.If not in integral multiples of 100, the minority class will be randomized and downsampled from the next integral multiple of 100.
    :type smote_percentage: int
    :param number_of_nearest_neighbors: The number of nearest neighbors (min: 1)
    :type number_of_nearest_neighbors: int
    :param random_seed: Random number generator seed (max: 4294967295)
    :type random_seed: int
    :output table: A DataTable containing original samples plus an additional synthetic minority class samples, where T is the number of minority class samples
    :type: table: Output
    """
    global _azureml_smote
    if _azureml_smote is None:
        _azureml_smote = _assets.load_component(
            _workspace.from_config(),
            name='azureml://SMOTE', version=None, feed='azureml')
    return _azureml_smote(
            samples=samples,
            label_column=label_column,
            smote_percentage=smote_percentage,
            number_of_nearest_neighbors=number_of_nearest_neighbors,
            random_seed=random_seed,)


class _AzuremlScoreImageModelInput:
    trained_model: Input = None
    """Trained predictive model"""
    dataset: Input = None
    """Input data to score"""


class _AzuremlScoreImageModelOutput:
    scored_dataset: Output = None
    """Dataset with obtained scores"""


class _AzuremlScoreImageModelComponent(Component):
    inputs: _AzuremlScoreImageModelInput
    outputs: _AzuremlScoreImageModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_score_image_model = None


def azureml_score_image_model(
    trained_model: Path = None,
    dataset: Path = None,
) -> _AzuremlScoreImageModelComponent:
    """Scores predictions for a trained image model.
    
    :param trained_model: Trained predictive model
    :type trained_model: Path
    :param dataset: Input data to score
    :type dataset: Path
    :output scored_dataset: Dataset with obtained scores
    :type: scored_dataset: Output
    """
    global _azureml_score_image_model
    if _azureml_score_image_model is None:
        _azureml_score_image_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Score Image Model', version=None, feed='azureml')
    return _azureml_score_image_model(
            trained_model=trained_model,
            dataset=dataset,)


class _AzuremlScoreModelInput:
    trained_model: Input = None
    """Trained predictive model"""
    dataset: Input = None
    """Input test dataset"""
    append_score_columns_to_output: bool = True
    """If checked, append score columns to the result dataset, otherwise only return the scores and true labels if available."""


class _AzuremlScoreModelOutput:
    scored_dataset: Output = None
    """Dataset with obtained scores"""


class _AzuremlScoreModelComponent(Component):
    inputs: _AzuremlScoreModelInput
    outputs: _AzuremlScoreModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_score_model = None


def azureml_score_model(
    trained_model: Path = None,
    dataset: Path = None,
    append_score_columns_to_output: bool = True,
) -> _AzuremlScoreModelComponent:
    """Scores predictions for a trained classification or regression model.
    
    :param trained_model: Trained predictive model
    :type trained_model: Path
    :param dataset: Input test dataset
    :type dataset: Path
    :param append_score_columns_to_output: If checked, append score columns to the result dataset, otherwise only return the scores and true labels if available.
    :type append_score_columns_to_output: bool
    :output scored_dataset: Dataset with obtained scores
    :type: scored_dataset: Output
    """
    global _azureml_score_model
    if _azureml_score_model is None:
        _azureml_score_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Score Model', version=None, feed='azureml')
    return _azureml_score_model(
            trained_model=trained_model,
            dataset=dataset,
            append_score_columns_to_output=append_score_columns_to_output,)


class _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum(Enum):
    rating_prediction = 'Rating Prediction'
    item_recommendation = 'Item Recommendation'


class _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum(Enum):
    from_all_items = 'From All Items'
    from_rated_items_for_model_evaluation = 'From Rated Items (for model evaluation)'
    from_unrated_items_to_suggest_new_items_to_users = 'From Unrated Items (to suggest new items to users)'


class _AzuremlScoreSvdRecommenderInput:
    trained_svd_recommendation: Input = None
    """Trained SVD recommendation"""
    dataset_to_score: Input = None
    """Dataset to score"""
    training_data: Input = None
    """Dataset containing the training data. (Used to filter out already rated items from prediction)(optional)"""
    recommender_prediction_kind: _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum = _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum.item_recommendation
    """Specify the type of prediction the recommendation should output (enum: ['Rating Prediction', 'Item Recommendation'])"""
    recommended_item_selection: _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum = _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum.from_rated_items_for_model_evaluation
    """Select the set of items to make recommendations from (optional, enum: ['From All Items', 'From Rated Items (for model evaluation)', 'From Unrated Items (to suggest new items to users)'])"""
    minimum_size_of_the_recommendation_pool_for_a_single_user: int = 2
    """Specify the minimum size of the recommendation pool for each user (optional, min: 1)"""
    maximum_number_of_items_to_recommend_to_a_user: int = 5
    """Specify the maximum number of items to recommend to a user (optional, min: 1)"""
    whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool = False
    """Specify whether to return the predicted ratings of the items along with the labels (optional)"""


class _AzuremlScoreSvdRecommenderOutput:
    scored_dataset: Output = None
    """Scored dataset"""


class _AzuremlScoreSvdRecommenderComponent(Component):
    inputs: _AzuremlScoreSvdRecommenderInput
    outputs: _AzuremlScoreSvdRecommenderOutput
    runsettings: _CommandComponentRunsetting


_azureml_score_svd_recommender = None


def azureml_score_svd_recommender(
    trained_svd_recommendation: Path = None,
    dataset_to_score: Path = None,
    training_data: Path = None,
    recommender_prediction_kind: _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum = _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum.item_recommendation,
    recommended_item_selection: _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum = _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum.from_rated_items_for_model_evaluation,
    minimum_size_of_the_recommendation_pool_for_a_single_user: int = 2,
    maximum_number_of_items_to_recommend_to_a_user: int = 5,
    whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool = False,
) -> _AzuremlScoreSvdRecommenderComponent:
    """Score a dataset using the SVD recommendation.
    
    :param trained_svd_recommendation: Trained SVD recommendation
    :type trained_svd_recommendation: Path
    :param dataset_to_score: Dataset to score
    :type dataset_to_score: Path
    :param training_data: Dataset containing the training data. (Used to filter out already rated items from prediction)(optional)
    :type training_data: Path
    :param recommender_prediction_kind: Specify the type of prediction the recommendation should output (enum: ['Rating Prediction', 'Item Recommendation'])
    :type recommender_prediction_kind: _AzuremlScoreSvdRecommenderRecommenderPredictionKindEnum
    :param recommended_item_selection: Select the set of items to make recommendations from (optional, enum: ['From All Items', 'From Rated Items (for model evaluation)', 'From Unrated Items (to suggest new items to users)'])
    :type recommended_item_selection: _AzuremlScoreSvdRecommenderRecommendedItemSelectionEnum
    :param minimum_size_of_the_recommendation_pool_for_a_single_user: Specify the minimum size of the recommendation pool for each user (optional, min: 1)
    :type minimum_size_of_the_recommendation_pool_for_a_single_user: int
    :param maximum_number_of_items_to_recommend_to_a_user: Specify the maximum number of items to recommend to a user (optional, min: 1)
    :type maximum_number_of_items_to_recommend_to_a_user: int
    :param whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: Specify whether to return the predicted ratings of the items along with the labels (optional)
    :type whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool
    :output scored_dataset: Scored dataset
    :type: scored_dataset: Output
    """
    global _azureml_score_svd_recommender
    if _azureml_score_svd_recommender is None:
        _azureml_score_svd_recommender = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Score SVD Recommender', version=None, feed='azureml')
    return _azureml_score_svd_recommender(
            trained_svd_recommendation=trained_svd_recommendation,
            dataset_to_score=dataset_to_score,
            training_data=training_data,
            recommender_prediction_kind=recommender_prediction_kind,
            recommended_item_selection=recommended_item_selection,
            minimum_size_of_the_recommendation_pool_for_a_single_user=minimum_size_of_the_recommendation_pool_for_a_single_user,
            maximum_number_of_items_to_recommend_to_a_user=maximum_number_of_items_to_recommend_to_a_user,
            whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels=whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels,)


class _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum(Enum):
    vw = 'VW'
    svmlight = 'SVMLight'


class _AzuremlScoreVowpalWabbitModelInput:
    trained_vowpal_wabbit_model: Input = None
    """Trained Vowpal Wabbit model."""
    test_data: Input = None
    """Test data."""
    vw_arguments: str = None
    """Type vowpal wabbit command line arguments. (optional)"""
    name_of_the_test_data_file: str = None
    """Type name of the test data file. (optional)"""
    specify_file_type: _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum = _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum.vw
    """Please specify file type. (enum: ['VW', 'SVMLight'])"""
    include_an_extra_column_containing_labels: bool = False
    """Whether to include an extra column containing labels in the scored dataset."""
    include_an_extra_column_containing_raw_scores: bool = False
    """Whether to include an extra column containing raw scores in the scored dataset."""


class _AzuremlScoreVowpalWabbitModelOutput:
    scored_dataset: Output = None
    """Scored dataset"""


class _AzuremlScoreVowpalWabbitModelComponent(Component):
    inputs: _AzuremlScoreVowpalWabbitModelInput
    outputs: _AzuremlScoreVowpalWabbitModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_score_vowpal_wabbit_model = None


def azureml_score_vowpal_wabbit_model(
    trained_vowpal_wabbit_model: Path = None,
    test_data: Path = None,
    vw_arguments: str = None,
    name_of_the_test_data_file: str = None,
    specify_file_type: _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum = _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum.vw,
    include_an_extra_column_containing_labels: bool = False,
    include_an_extra_column_containing_raw_scores: bool = False,
) -> _AzuremlScoreVowpalWabbitModelComponent:
    """Score data using Vowpal Wabbit from the command line interface.
    
    :param trained_vowpal_wabbit_model: Trained Vowpal Wabbit model.
    :type trained_vowpal_wabbit_model: Path
    :param test_data: Test data.
    :type test_data: Path
    :param vw_arguments: Type vowpal wabbit command line arguments. (optional)
    :type vw_arguments: str
    :param name_of_the_test_data_file: Type name of the test data file. (optional)
    :type name_of_the_test_data_file: str
    :param specify_file_type: Please specify file type. (enum: ['VW', 'SVMLight'])
    :type specify_file_type: _AzuremlScoreVowpalWabbitModelSpecifyFileTypeEnum
    :param include_an_extra_column_containing_labels: Whether to include an extra column containing labels in the scored dataset.
    :type include_an_extra_column_containing_labels: bool
    :param include_an_extra_column_containing_raw_scores: Whether to include an extra column containing raw scores in the scored dataset.
    :type include_an_extra_column_containing_raw_scores: bool
    :output scored_dataset: Scored dataset
    :type: scored_dataset: Output
    """
    global _azureml_score_vowpal_wabbit_model
    if _azureml_score_vowpal_wabbit_model is None:
        _azureml_score_vowpal_wabbit_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Score Vowpal Wabbit Model', version=None, feed='azureml')
    return _azureml_score_vowpal_wabbit_model(
            trained_vowpal_wabbit_model=trained_vowpal_wabbit_model,
            test_data=test_data,
            vw_arguments=vw_arguments,
            name_of_the_test_data_file=name_of_the_test_data_file,
            specify_file_type=specify_file_type,
            include_an_extra_column_containing_labels=include_an_extra_column_containing_labels,
            include_an_extra_column_containing_raw_scores=include_an_extra_column_containing_raw_scores,)


class _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum(Enum):
    rating_prediction = 'Rating Prediction'
    item_recommendation = 'Item Recommendation'


class _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum(Enum):
    from_all_items = 'From All Items'
    from_rated_items_for_model_evaluation = 'From Rated Items (for model evaluation)'
    from_unrated_items_to_suggest_new_items_to_users = 'From Unrated Items (to suggest new items to users)'


class _AzuremlScoreWideAndDeepRecommenderInput:
    trained_wide_and_deep_recommendation_model: Input = None
    """Trained Wide and Deep recommendation model"""
    dataset_to_score: Input = None
    """Dataset to score"""
    user_features: Input = None
    """User features(optional)"""
    item_features: Input = None
    """Item features(optional)"""
    training_data: Input = None
    """Dataset containing the training data. (Used to filter out already rated items from prediction)(optional)"""
    recommender_prediction_kind: _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum = _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum.item_recommendation
    """Specify the type of prediction the recommendation should output (enum: ['Rating Prediction', 'Item Recommendation'])"""
    recommended_item_selection: _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum = _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum.from_rated_items_for_model_evaluation
    """Select the set of items to make recommendations from (optional, enum: ['From All Items', 'From Rated Items (for model evaluation)', 'From Unrated Items (to suggest new items to users)'])"""
    minimum_size_of_the_recommendation_pool_for_a_single_user: int = 2
    """Specify the minimum size of the recommendation pool for each user (optional, min: 1)"""
    maximum_number_of_items_to_recommend_to_a_user: int = 5
    """Specify the maximum number of items to recommend to a user (optional, min: 1)"""
    whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool = False
    """Specify whether to return the predicted ratings of the items along with the labels (optional)"""


class _AzuremlScoreWideAndDeepRecommenderOutput:
    scored_dataset: Output = None
    """Scored dataset"""


class _AzuremlScoreWideAndDeepRecommenderComponent(Component):
    inputs: _AzuremlScoreWideAndDeepRecommenderInput
    outputs: _AzuremlScoreWideAndDeepRecommenderOutput
    runsettings: _CommandComponentRunsetting


_azureml_score_wide_and_deep_recommender = None


def azureml_score_wide_and_deep_recommender(
    trained_wide_and_deep_recommendation_model: Path = None,
    dataset_to_score: Path = None,
    user_features: Path = None,
    item_features: Path = None,
    training_data: Path = None,
    recommender_prediction_kind: _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum = _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum.item_recommendation,
    recommended_item_selection: _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum = _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum.from_rated_items_for_model_evaluation,
    minimum_size_of_the_recommendation_pool_for_a_single_user: int = 2,
    maximum_number_of_items_to_recommend_to_a_user: int = 5,
    whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool = False,
) -> _AzuremlScoreWideAndDeepRecommenderComponent:
    """Score a dataset using the Wide and Deep recommendation model.
    
    :param trained_wide_and_deep_recommendation_model: Trained Wide and Deep recommendation model
    :type trained_wide_and_deep_recommendation_model: Path
    :param dataset_to_score: Dataset to score
    :type dataset_to_score: Path
    :param user_features: User features(optional)
    :type user_features: Path
    :param item_features: Item features(optional)
    :type item_features: Path
    :param training_data: Dataset containing the training data. (Used to filter out already rated items from prediction)(optional)
    :type training_data: Path
    :param recommender_prediction_kind: Specify the type of prediction the recommendation should output (enum: ['Rating Prediction', 'Item Recommendation'])
    :type recommender_prediction_kind: _AzuremlScoreWideAndDeepRecommenderRecommenderPredictionKindEnum
    :param recommended_item_selection: Select the set of items to make recommendations from (optional, enum: ['From All Items', 'From Rated Items (for model evaluation)', 'From Unrated Items (to suggest new items to users)'])
    :type recommended_item_selection: _AzuremlScoreWideAndDeepRecommenderRecommendedItemSelectionEnum
    :param minimum_size_of_the_recommendation_pool_for_a_single_user: Specify the minimum size of the recommendation pool for each user (optional, min: 1)
    :type minimum_size_of_the_recommendation_pool_for_a_single_user: int
    :param maximum_number_of_items_to_recommend_to_a_user: Specify the maximum number of items to recommend to a user (optional, min: 1)
    :type maximum_number_of_items_to_recommend_to_a_user: int
    :param whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: Specify whether to return the predicted ratings of the items along with the labels (optional)
    :type whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels: bool
    :output scored_dataset: Scored dataset
    :type: scored_dataset: Output
    """
    global _azureml_score_wide_and_deep_recommender
    if _azureml_score_wide_and_deep_recommender is None:
        _azureml_score_wide_and_deep_recommender = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Score Wide and Deep Recommender', version=None, feed='azureml')
    return _azureml_score_wide_and_deep_recommender(
            trained_wide_and_deep_recommendation_model=trained_wide_and_deep_recommendation_model,
            dataset_to_score=dataset_to_score,
            user_features=user_features,
            item_features=item_features,
            training_data=training_data,
            recommender_prediction_kind=recommender_prediction_kind,
            recommended_item_selection=recommended_item_selection,
            minimum_size_of_the_recommendation_pool_for_a_single_user=minimum_size_of_the_recommendation_pool_for_a_single_user,
            maximum_number_of_items_to_recommend_to_a_user=maximum_number_of_items_to_recommend_to_a_user,
            whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels=whether_to_return_the_predicted_ratings_of_the_items_along_with_the_labels,)


class _AzuremlSelectColumnsTransformInput:
    dataset_with_desired_columns: Input = None
    """Dataset containing desired set of columns"""


class _AzuremlSelectColumnsTransformOutput:
    columns_selection_transformation: Output = None
    """Transformation that selects the same subset of columns as in the given dataset."""


class _AzuremlSelectColumnsTransformComponent(Component):
    inputs: _AzuremlSelectColumnsTransformInput
    outputs: _AzuremlSelectColumnsTransformOutput
    runsettings: _CommandComponentRunsetting


_azureml_select_columns_transform = None


def azureml_select_columns_transform(
    dataset_with_desired_columns: Path = None,
) -> _AzuremlSelectColumnsTransformComponent:
    """Create a transformation that selects the same subset of columns as in the given dataset.
    
    :param dataset_with_desired_columns: Dataset containing desired set of columns
    :type dataset_with_desired_columns: Path
    :output columns_selection_transformation: Transformation that selects the same subset of columns as in the given dataset.
    :type: columns_selection_transformation: Output
    """
    global _azureml_select_columns_transform
    if _azureml_select_columns_transform is None:
        _azureml_select_columns_transform = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Select Columns Transform', version=None, feed='azureml')
    return _azureml_select_columns_transform(
            dataset_with_desired_columns=dataset_with_desired_columns,)


class _AzuremlSelectColumnsInDatasetInput:
    dataset: Input = None
    """Input dataset"""
    select_columns: str = None
    """Select columns to keep in the projected dataset"""


class _AzuremlSelectColumnsInDatasetOutput:
    results_dataset: Output = None
    """Output dataset"""


class _AzuremlSelectColumnsInDatasetComponent(Component):
    inputs: _AzuremlSelectColumnsInDatasetInput
    outputs: _AzuremlSelectColumnsInDatasetOutput
    runsettings: _CommandComponentRunsetting


_azureml_select_columns_in_dataset = None


def azureml_select_columns_in_dataset(
    dataset: Path = None,
    select_columns: str = None,
) -> _AzuremlSelectColumnsInDatasetComponent:
    """Selects columns to include or exclude from a dataset in an operation.
    
    :param dataset: Input dataset
    :type dataset: Path
    :param select_columns: Select columns to keep in the projected dataset
    :type select_columns: str
    :output results_dataset: Output dataset
    :type: results_dataset: Output
    """
    global _azureml_select_columns_in_dataset
    if _azureml_select_columns_in_dataset is None:
        _azureml_select_columns_in_dataset = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Select Columns in Dataset', version=None, feed='azureml')
    return _azureml_select_columns_in_dataset(
            dataset=dataset,
            select_columns=select_columns,)


class _AzuremlSplitDataSplittingModeEnum(Enum):
    split_rows = 'Split Rows'
    regular_expression = 'Regular Expression'
    relative_expression = 'Relative Expression'


class _AzuremlSplitDataStratifiedSplitEnum(Enum):
    true = 'True'
    false = 'False'


class _AzuremlSplitDataInput:
    dataset: Input = None
    """Dataset to split"""
    splitting_mode: _AzuremlSplitDataSplittingModeEnum = _AzuremlSplitDataSplittingModeEnum.split_rows
    """Choose the method for splitting the dataset (enum: ['Split Rows', 'Regular Expression', 'Relative Expression'])"""
    fraction_of_rows_in_the_first_output_dataset: float = 0.5
    """Specify a ratio representing the number of rows in the first output dataset over the number of rows in the input dataset (optional, max: 1.0)"""
    randomized_split: bool = True
    """Indicate whether rows should be randomly selected (optional)"""
    random_seed: int = 0
    """Provide a value to see the random number generator seed (optional, max: 4294967295)"""
    stratified_split: _AzuremlSplitDataStratifiedSplitEnum = _AzuremlSplitDataStratifiedSplitEnum.false
    """Indicate whether the rows in each split should be grouped using a strata column (optional, enum: ['True', 'False'])"""
    stratification_key_column: str = None
    """Select the column containing the stratification key (optional)"""
    regular_expression: str = '\"column name" ^start'
    """Type a regular expression to use as criteria when splitting the dataset on a string column (optional)"""
    relational_expression: str = '\"column name" > 3'
    """Type a relational expression to use in splitting the dataset on a numeric column (optional)"""


class _AzuremlSplitDataOutput:
    results_dataset1: Output = None
    """Dataset containing selected rows"""
    results_dataset2: Output = None
    """Dataset containing all other rows"""


class _AzuremlSplitDataComponent(Component):
    inputs: _AzuremlSplitDataInput
    outputs: _AzuremlSplitDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_split_data = None


def azureml_split_data(
    dataset: Path = None,
    splitting_mode: _AzuremlSplitDataSplittingModeEnum = _AzuremlSplitDataSplittingModeEnum.split_rows,
    fraction_of_rows_in_the_first_output_dataset: float = 0.5,
    randomized_split: bool = True,
    random_seed: int = 0,
    stratified_split: _AzuremlSplitDataStratifiedSplitEnum = _AzuremlSplitDataStratifiedSplitEnum.false,
    stratification_key_column: str = None,
    regular_expression: str = '\"column name" ^start',
    relational_expression: str = '\"column name" > 3',
) -> _AzuremlSplitDataComponent:
    """Partitions the rows of a dataset into two distinct sets.
    
    :param dataset: Dataset to split
    :type dataset: Path
    :param splitting_mode: Choose the method for splitting the dataset (enum: ['Split Rows', 'Regular Expression', 'Relative Expression'])
    :type splitting_mode: _AzuremlSplitDataSplittingModeEnum
    :param fraction_of_rows_in_the_first_output_dataset: Specify a ratio representing the number of rows in the first output dataset over the number of rows in the input dataset (optional, max: 1.0)
    :type fraction_of_rows_in_the_first_output_dataset: float
    :param randomized_split: Indicate whether rows should be randomly selected (optional)
    :type randomized_split: bool
    :param random_seed: Provide a value to see the random number generator seed (optional, max: 4294967295)
    :type random_seed: int
    :param stratified_split: Indicate whether the rows in each split should be grouped using a strata column (optional, enum: ['True', 'False'])
    :type stratified_split: _AzuremlSplitDataStratifiedSplitEnum
    :param stratification_key_column: Select the column containing the stratification key (optional)
    :type stratification_key_column: str
    :param regular_expression: Type a regular expression to use as criteria when splitting the dataset on a string column (optional)
    :type regular_expression: str
    :param relational_expression: Type a relational expression to use in splitting the dataset on a numeric column (optional)
    :type relational_expression: str
    :output results_dataset1: Dataset containing selected rows
    :type: results_dataset1: Output
    :output results_dataset2: Dataset containing all other rows
    :type: results_dataset2: Output
    """
    global _azureml_split_data
    if _azureml_split_data is None:
        _azureml_split_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Split Data', version=None, feed='azureml')
    return _azureml_split_data(
            dataset=dataset,
            splitting_mode=splitting_mode,
            fraction_of_rows_in_the_first_output_dataset=fraction_of_rows_in_the_first_output_dataset,
            randomized_split=randomized_split,
            random_seed=random_seed,
            stratified_split=stratified_split,
            stratification_key_column=stratification_key_column,
            regular_expression=regular_expression,
            relational_expression=relational_expression,)


class _AzuremlSplitImageDirectoryInput:
    input_image_directory: Input = None
    """Input image directory"""
    fraction_of_images_in_the_first_output: float = 0.9
    """Fraction of images in the first output (min: 2.220446049250313e-16, max: 0.9999999999999998)"""


class _AzuremlSplitImageDirectoryOutput:
    output_image_directory1: Output = None
    """First output image directory"""
    output_image_directory2: Output = None
    """Second output image directory"""


class _AzuremlSplitImageDirectoryComponent(Component):
    inputs: _AzuremlSplitImageDirectoryInput
    outputs: _AzuremlSplitImageDirectoryOutput
    runsettings: _CommandComponentRunsetting


_azureml_split_image_directory = None


def azureml_split_image_directory(
    input_image_directory: Path = None,
    fraction_of_images_in_the_first_output: float = 0.9,
) -> _AzuremlSplitImageDirectoryComponent:
    """Partitions the images of a image directory into two distinct sets.
    
    :param input_image_directory: Input image directory
    :type input_image_directory: Path
    :param fraction_of_images_in_the_first_output: Fraction of images in the first output (min: 2.220446049250313e-16, max: 0.9999999999999998)
    :type fraction_of_images_in_the_first_output: float
    :output output_image_directory1: First output image directory
    :type: output_image_directory1: Output
    :output output_image_directory2: Second output image directory
    :type: output_image_directory2: Output
    """
    global _azureml_split_image_directory
    if _azureml_split_image_directory is None:
        _azureml_split_image_directory = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Split Image Directory', version=None, feed='azureml')
    return _azureml_split_image_directory(
            input_image_directory=input_image_directory,
            fraction_of_images_in_the_first_output=fraction_of_images_in_the_first_output,)


class _AzuremlSummarizeDataInput:
    input: Input = None
    """DataFrameDirectory"""


class _AzuremlSummarizeDataOutput:
    result_dataset: Output = None
    """DataFrameDirectory"""


class _AzuremlSummarizeDataComponent(Component):
    inputs: _AzuremlSummarizeDataInput
    outputs: _AzuremlSummarizeDataOutput
    runsettings: _CommandComponentRunsetting


_azureml_summarize_data = None


def azureml_summarize_data(
    input: Path = None,
) -> _AzuremlSummarizeDataComponent:
    """Generates a basic descriptive statistics report for the columns in a dataset.
    
    :param input: DataFrameDirectory
    :type input: Path
    :output result_dataset: DataFrameDirectory
    :type: result_dataset: Output
    """
    global _azureml_summarize_data
    if _azureml_summarize_data is None:
        _azureml_summarize_data = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Summarize Data', version=None, feed='azureml')
    return _azureml_summarize_data(
            input=input,)


class _AzuremlTrainAnomalyDetectionModelInput:
    untrained_model: Input = None
    """Untrained learner"""
    dataset: Input = None
    """Input data source"""


class _AzuremlTrainAnomalyDetectionModelOutput:
    trained_model: Output = None
    """Trained anomaly detection model"""


class _AzuremlTrainAnomalyDetectionModelComponent(Component):
    inputs: _AzuremlTrainAnomalyDetectionModelInput
    outputs: _AzuremlTrainAnomalyDetectionModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_anomaly_detection_model = None


def azureml_train_anomaly_detection_model(
    untrained_model: Path = None,
    dataset: Path = None,
) -> _AzuremlTrainAnomalyDetectionModelComponent:
    """Trains an anomaly detector model and labels data from the training set
    
    :param untrained_model: Untrained learner
    :type untrained_model: Path
    :param dataset: Input data source
    :type dataset: Path
    :output trained_model: Trained anomaly detection model
    :type: trained_model: Output
    """
    global _azureml_train_anomaly_detection_model
    if _azureml_train_anomaly_detection_model is None:
        _azureml_train_anomaly_detection_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train Anomaly Detection Model', version=None, feed='azureml')
    return _azureml_train_anomaly_detection_model(
            untrained_model=untrained_model,
            dataset=dataset,)


class _AzuremlTrainClusteringModelInput:
    untrained_model: Input = None
    """Untrained clustering model"""
    dataset: Input = None
    """Input data source"""
    column_set: str = None
    """Column selection pattern"""
    check_for_append_or_uncheck_for_result_only: bool = True
    """Whether output dataset must contain input dataset appended by assignments column (Checked) or assignments column only (Unchecked)"""


class _AzuremlTrainClusteringModelOutput:
    trained_model: Output = None
    """Trained clustering model"""
    results_dataset: Output = None
    """Input dataset appended by data column of assignments or assignments column only"""


class _AzuremlTrainClusteringModelComponent(Component):
    inputs: _AzuremlTrainClusteringModelInput
    outputs: _AzuremlTrainClusteringModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_clustering_model = None


def azureml_train_clustering_model(
    untrained_model: Path = None,
    dataset: Path = None,
    column_set: str = None,
    check_for_append_or_uncheck_for_result_only: bool = True,
) -> _AzuremlTrainClusteringModelComponent:
    """Train clustering model and assign data to clusters.
    
    :param untrained_model: Untrained clustering model
    :type untrained_model: Path
    :param dataset: Input data source
    :type dataset: Path
    :param column_set: Column selection pattern
    :type column_set: str
    :param check_for_append_or_uncheck_for_result_only: Whether output dataset must contain input dataset appended by assignments column (Checked) or assignments column only (Unchecked)
    :type check_for_append_or_uncheck_for_result_only: bool
    :output trained_model: Trained clustering model
    :type: trained_model: Output
    :output results_dataset: Input dataset appended by data column of assignments or assignments column only
    :type: results_dataset: Output
    """
    global _azureml_train_clustering_model
    if _azureml_train_clustering_model is None:
        _azureml_train_clustering_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train Clustering Model', version=None, feed='azureml')
    return _azureml_train_clustering_model(
            untrained_model=untrained_model,
            dataset=dataset,
            column_set=column_set,
            check_for_append_or_uncheck_for_result_only=check_for_append_or_uncheck_for_result_only,)


class _AzuremlTrainModelInput:
    untrained_model: Input = None
    """Untrained learner"""
    dataset: Input = None
    """Training data"""
    label_column: str = None
    """Select the column that contains the label or outcome column"""
    model_explanations: bool = False
    """Whether to generate explanations for the trained model. Default is unchecked to reduce extra compute overhead. (optional)"""


class _AzuremlTrainModelOutput:
    trained_model: Output = None
    """Trained learner"""


class _AzuremlTrainModelComponent(Component):
    inputs: _AzuremlTrainModelInput
    outputs: _AzuremlTrainModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_model = None


def azureml_train_model(
    untrained_model: Path = None,
    dataset: Path = None,
    label_column: str = None,
    model_explanations: bool = False,
) -> _AzuremlTrainModelComponent:
    """Trains a classification or regression model in a supervised manner.
    
    :param untrained_model: Untrained learner
    :type untrained_model: Path
    :param dataset: Training data
    :type dataset: Path
    :param label_column: Select the column that contains the label or outcome column
    :type label_column: str
    :param model_explanations: Whether to generate explanations for the trained model. Default is unchecked to reduce extra compute overhead. (optional)
    :type model_explanations: bool
    :output trained_model: Trained learner
    :type: trained_model: Output
    """
    global _azureml_train_model
    if _azureml_train_model is None:
        _azureml_train_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train Model', version=None, feed='azureml')
    return _azureml_train_model(
            untrained_model=untrained_model,
            dataset=dataset,
            label_column=label_column,
            model_explanations=model_explanations,)


class _AzuremlTrainPytorchModelInput:
    untrained_model: Input = None
    """Untrained model"""
    training_dataset: Input = None
    """Input dataset for training"""
    validation_dataset: Input = None
    """Input dataset for validation"""
    epochs: int = 5
    """Epochs. (min: 1)"""
    batch_size: int = 16
    """Batch size. (min: 1)"""
    warmup_step_number: int = 0
    """Warmup step number (optional)"""
    learning_rate: float = 0.001
    """Learning rate. (min: 2.220446049250313e-16, max: 2.0)"""
    random_seed: int = 1
    """Random seed."""
    patience: int = 3
    """Patience. (min: 1)"""
    print_frequency: int = 10
    """Training log print frequency over iterations in each epoch. (optional, min: 1)"""


class _AzuremlTrainPytorchModelOutput:
    trained_model: Output = None
    """Trained model"""


class _AzuremlTrainPytorchModelComponent(Component):
    inputs: _AzuremlTrainPytorchModelInput
    outputs: _AzuremlTrainPytorchModelOutput
    runsettings: _DistributedComponentRunsetting


_azureml_train_pytorch_model = None


def azureml_train_pytorch_model(
    untrained_model: Path = None,
    training_dataset: Path = None,
    validation_dataset: Path = None,
    epochs: int = 5,
    batch_size: int = 16,
    warmup_step_number: int = 0,
    learning_rate: float = 0.001,
    random_seed: int = 1,
    patience: int = 3,
    print_frequency: int = 10,
) -> _AzuremlTrainPytorchModelComponent:
    """Train pytorch model from scratch or finetune it.
    
    :param untrained_model: Untrained model
    :type untrained_model: Path
    :param training_dataset: Input dataset for training
    :type training_dataset: Path
    :param validation_dataset: Input dataset for validation
    :type validation_dataset: Path
    :param epochs: Epochs. (min: 1)
    :type epochs: int
    :param batch_size: Batch size. (min: 1)
    :type batch_size: int
    :param warmup_step_number: Warmup step number (optional)
    :type warmup_step_number: int
    :param learning_rate: Learning rate. (min: 2.220446049250313e-16, max: 2.0)
    :type learning_rate: float
    :param random_seed: Random seed.
    :type random_seed: int
    :param patience: Patience. (min: 1)
    :type patience: int
    :param print_frequency: Training log print frequency over iterations in each epoch. (optional, min: 1)
    :type print_frequency: int
    :output trained_model: Trained model
    :type: trained_model: Output
    """
    global _azureml_train_pytorch_model
    if _azureml_train_pytorch_model is None:
        _azureml_train_pytorch_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train PyTorch Model', version=None, feed='azureml')
    return _azureml_train_pytorch_model(
            untrained_model=untrained_model,
            training_dataset=training_dataset,
            validation_dataset=validation_dataset,
            epochs=epochs,
            batch_size=batch_size,
            warmup_step_number=warmup_step_number,
            learning_rate=learning_rate,
            random_seed=random_seed,
            patience=patience,
            print_frequency=print_frequency,)


class _AzuremlTrainSvdRecommenderInput:
    training_dataset_of_user_item_rating_triples: Input = None
    """Ratings of items by users, expressed as triple (User, Item, Rating)"""
    number_of_factors: int = 200
    """Specify the number of factors to use with recommendation (min: 1)"""
    number_of_recommendation_algorithm_iterations: int = 30
    """Specify the maximum number of iterations to perform while training the recommendation model (min: 1)"""
    learning_rate: float = 0.005
    """Specify the size of each step in the learning process (min: 2.220446049250313e-16, max: 2.0)"""


class _AzuremlTrainSvdRecommenderOutput:
    trained_svd_recommendation: Output = None
    """Trained SVD recommendation"""


class _AzuremlTrainSvdRecommenderComponent(Component):
    inputs: _AzuremlTrainSvdRecommenderInput
    outputs: _AzuremlTrainSvdRecommenderOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_svd_recommender = None


def azureml_train_svd_recommender(
    training_dataset_of_user_item_rating_triples: Path = None,
    number_of_factors: int = 200,
    number_of_recommendation_algorithm_iterations: int = 30,
    learning_rate: float = 0.005,
) -> _AzuremlTrainSvdRecommenderComponent:
    """Train a collaborative filtering recommendation using SVD algorithm.
    
    :param training_dataset_of_user_item_rating_triples: Ratings of items by users, expressed as triple (User, Item, Rating)
    :type training_dataset_of_user_item_rating_triples: Path
    :param number_of_factors: Specify the number of factors to use with recommendation (min: 1)
    :type number_of_factors: int
    :param number_of_recommendation_algorithm_iterations: Specify the maximum number of iterations to perform while training the recommendation model (min: 1)
    :type number_of_recommendation_algorithm_iterations: int
    :param learning_rate: Specify the size of each step in the learning process (min: 2.220446049250313e-16, max: 2.0)
    :type learning_rate: float
    :output trained_svd_recommendation: Trained SVD recommendation
    :type: trained_svd_recommendation: Output
    """
    global _azureml_train_svd_recommender
    if _azureml_train_svd_recommender is None:
        _azureml_train_svd_recommender = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train SVD Recommender', version=None, feed='azureml')
    return _azureml_train_svd_recommender(
            training_dataset_of_user_item_rating_triples=training_dataset_of_user_item_rating_triples,
            number_of_factors=number_of_factors,
            number_of_recommendation_algorithm_iterations=number_of_recommendation_algorithm_iterations,
            learning_rate=learning_rate,)


class _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum(Enum):
    vw = 'VW'
    svmlight = 'SVMLight'


class _AzuremlTrainVowpalWabbitModelInput:
    pre_trained_vowpal_wabbit_model: Input = None
    """Trained Vowpal Wabbit model.(optional)"""
    training_data: Input = None
    """Training data."""
    vw_arguments: str = None
    """Type vowpal wabbit command line arguments. (optional)"""
    name_of_the_training_data_file: str = None
    """Type name of the training data file. (optional)"""
    specify_file_type: _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum = _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum.vw
    """Please specify file type. (enum: ['VW', 'SVMLight'])"""
    output_readable_model_file: bool = False
    """Output readable model (--readable_model) file."""
    output_inverted_hash_file: bool = False
    """Output inverted hash (--invert_hash) file."""


class _AzuremlTrainVowpalWabbitModelOutput:
    trained_vowpal_wabbit_model: Output = None
    """Trained Vowpal Wabbit model"""


class _AzuremlTrainVowpalWabbitModelComponent(Component):
    inputs: _AzuremlTrainVowpalWabbitModelInput
    outputs: _AzuremlTrainVowpalWabbitModelOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_vowpal_wabbit_model = None


def azureml_train_vowpal_wabbit_model(
    pre_trained_vowpal_wabbit_model: Path = None,
    training_data: Path = None,
    vw_arguments: str = None,
    name_of_the_training_data_file: str = None,
    specify_file_type: _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum = _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum.vw,
    output_readable_model_file: bool = False,
    output_inverted_hash_file: bool = False,
) -> _AzuremlTrainVowpalWabbitModelComponent:
    """Train a Vowpal Wabbit model using the command line interface.
    
    :param pre_trained_vowpal_wabbit_model: Trained Vowpal Wabbit model.(optional)
    :type pre_trained_vowpal_wabbit_model: Path
    :param training_data: Training data.
    :type training_data: Path
    :param vw_arguments: Type vowpal wabbit command line arguments. (optional)
    :type vw_arguments: str
    :param name_of_the_training_data_file: Type name of the training data file. (optional)
    :type name_of_the_training_data_file: str
    :param specify_file_type: Please specify file type. (enum: ['VW', 'SVMLight'])
    :type specify_file_type: _AzuremlTrainVowpalWabbitModelSpecifyFileTypeEnum
    :param output_readable_model_file: Output readable model (--readable_model) file.
    :type output_readable_model_file: bool
    :param output_inverted_hash_file: Output inverted hash (--invert_hash) file.
    :type output_inverted_hash_file: bool
    :output trained_vowpal_wabbit_model: Trained Vowpal Wabbit model
    :type: trained_vowpal_wabbit_model: Output
    """
    global _azureml_train_vowpal_wabbit_model
    if _azureml_train_vowpal_wabbit_model is None:
        _azureml_train_vowpal_wabbit_model = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train Vowpal Wabbit Model', version=None, feed='azureml')
    return _azureml_train_vowpal_wabbit_model(
            pre_trained_vowpal_wabbit_model=pre_trained_vowpal_wabbit_model,
            training_data=training_data,
            vw_arguments=vw_arguments,
            name_of_the_training_data_file=name_of_the_training_data_file,
            specify_file_type=specify_file_type,
            output_readable_model_file=output_readable_model_file,
            output_inverted_hash_file=output_inverted_hash_file,)


class _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum(Enum):
    adagrad = 'Adagrad'
    adam = 'Adam'
    ftrl = 'Ftrl'
    rmsprop = 'RMSProp'
    sgd = 'SGD'
    adadelta = 'Adadelta'


class _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum(Enum):
    adagrad = 'Adagrad'
    adam = 'Adam'
    ftrl = 'Ftrl'
    rmsprop = 'RMSProp'
    sgd = 'SGD'
    adadelta = 'Adadelta'


class _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum(Enum):
    relu = 'ReLU'
    sigmoid = 'Sigmoid'
    tanh = 'Tanh'
    linear = 'Linear'
    leakyrelu = 'LeakyReLU'


class _AzuremlTrainWideAndDeepRecommenderInput:
    training_dataset_of_user_item_rating_triples: Input = None
    """Ratings of items by users, expressed as triple (User, Item, Rating)"""
    user_features: Input = None
    """User features(optional)"""
    item_features: Input = None
    """Item features(optional)"""
    epochs: int = 15
    """Maximum number of epochs to perform while training (min: 1)"""
    batch_size: int = 64
    """Number of consecutive samples to combine in a single batch (min: 1)"""
    wide_part_optimizer: _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum = _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum.adagrad
    """Optimizer used to apply gradients to the wide part of the model (enum: ['Adagrad', 'Adam', 'Ftrl', 'RMSProp', 'SGD', 'Adadelta'])"""
    wide_optimizer_learning_rate: float = 0.1
    """Size of each step in the learning process for wide part of the model (min: 2.220446049250313e-16, max: 2.0)"""
    crossed_feature_dimension: int = 1000
    """Crossed feature dimension for wide part model (min: 1)"""
    deep_part_optimizer: _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum = _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum.adagrad
    """Optimizer used to apply gradients to the deep part of the model (enum: ['Adagrad', 'Adam', 'Ftrl', 'RMSProp', 'SGD', 'Adadelta'])"""
    deep_optimizer_learning_rate: float = 0.1
    """Size of each step in the learning process for deep part of the model (min: 2.220446049250313e-16, max: 2.0)"""
    user_embedding_dimension: int = 16
    """User embedding dimension for deep part model (min: 1)"""
    item_embedding_dimension: int = 16
    """Item embedding dimension for deep part model (min: 1)"""
    categorical_features_embedding_dimension: int = 4
    """Categorical features embedding dimension for deep part model (min: 1)"""
    hidden_units: str = '256,128'
    """Hidden units per layer for deep part model"""
    activation_function: _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum = _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum.relu
    """Activation function applied to each layer in deep part model (enum: ['ReLU', 'Sigmoid', 'Tanh', 'Linear', 'LeakyReLU'])"""
    dropout: float = 0.8
    """Probability that each element is dropped in deep part model (max: 1.0)"""
    batch_normalization: bool = True
    """Whether to use batch normalization after each hidden layer"""


class _AzuremlTrainWideAndDeepRecommenderOutput:
    trained_wide_and_deep_recommendation_model: Output = None
    """Trained Wide and Deep recommendation model"""


class _AzuremlTrainWideAndDeepRecommenderComponent(Component):
    inputs: _AzuremlTrainWideAndDeepRecommenderInput
    outputs: _AzuremlTrainWideAndDeepRecommenderOutput
    runsettings: _CommandComponentRunsetting


_azureml_train_wide_and_deep_recommender = None


def azureml_train_wide_and_deep_recommender(
    training_dataset_of_user_item_rating_triples: Path = None,
    user_features: Path = None,
    item_features: Path = None,
    epochs: int = 15,
    batch_size: int = 64,
    wide_part_optimizer: _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum = _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum.adagrad,
    wide_optimizer_learning_rate: float = 0.1,
    crossed_feature_dimension: int = 1000,
    deep_part_optimizer: _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum = _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum.adagrad,
    deep_optimizer_learning_rate: float = 0.1,
    user_embedding_dimension: int = 16,
    item_embedding_dimension: int = 16,
    categorical_features_embedding_dimension: int = 4,
    hidden_units: str = '256,128',
    activation_function: _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum = _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum.relu,
    dropout: float = 0.8,
    batch_normalization: bool = True,
) -> _AzuremlTrainWideAndDeepRecommenderComponent:
    """Train a recommender based on Wide & Deep model.
    
    :param training_dataset_of_user_item_rating_triples: Ratings of items by users, expressed as triple (User, Item, Rating)
    :type training_dataset_of_user_item_rating_triples: Path
    :param user_features: User features(optional)
    :type user_features: Path
    :param item_features: Item features(optional)
    :type item_features: Path
    :param epochs: Maximum number of epochs to perform while training (min: 1)
    :type epochs: int
    :param batch_size: Number of consecutive samples to combine in a single batch (min: 1)
    :type batch_size: int
    :param wide_part_optimizer: Optimizer used to apply gradients to the wide part of the model (enum: ['Adagrad', 'Adam', 'Ftrl', 'RMSProp', 'SGD', 'Adadelta'])
    :type wide_part_optimizer: _AzuremlTrainWideAndDeepRecommenderWidePartOptimizerEnum
    :param wide_optimizer_learning_rate: Size of each step in the learning process for wide part of the model (min: 2.220446049250313e-16, max: 2.0)
    :type wide_optimizer_learning_rate: float
    :param crossed_feature_dimension: Crossed feature dimension for wide part model (min: 1)
    :type crossed_feature_dimension: int
    :param deep_part_optimizer: Optimizer used to apply gradients to the deep part of the model (enum: ['Adagrad', 'Adam', 'Ftrl', 'RMSProp', 'SGD', 'Adadelta'])
    :type deep_part_optimizer: _AzuremlTrainWideAndDeepRecommenderDeepPartOptimizerEnum
    :param deep_optimizer_learning_rate: Size of each step in the learning process for deep part of the model (min: 2.220446049250313e-16, max: 2.0)
    :type deep_optimizer_learning_rate: float
    :param user_embedding_dimension: User embedding dimension for deep part model (min: 1)
    :type user_embedding_dimension: int
    :param item_embedding_dimension: Item embedding dimension for deep part model (min: 1)
    :type item_embedding_dimension: int
    :param categorical_features_embedding_dimension: Categorical features embedding dimension for deep part model (min: 1)
    :type categorical_features_embedding_dimension: int
    :param hidden_units: Hidden units per layer for deep part model
    :type hidden_units: str
    :param activation_function: Activation function applied to each layer in deep part model (enum: ['ReLU', 'Sigmoid', 'Tanh', 'Linear', 'LeakyReLU'])
    :type activation_function: _AzuremlTrainWideAndDeepRecommenderActivationFunctionEnum
    :param dropout: Probability that each element is dropped in deep part model (max: 1.0)
    :type dropout: float
    :param batch_normalization: Whether to use batch normalization after each hidden layer
    :type batch_normalization: bool
    :output trained_wide_and_deep_recommendation_model: Trained Wide and Deep recommendation model
    :type: trained_wide_and_deep_recommendation_model: Output
    """
    global _azureml_train_wide_and_deep_recommender
    if _azureml_train_wide_and_deep_recommender is None:
        _azureml_train_wide_and_deep_recommender = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Train Wide and Deep Recommender', version=None, feed='azureml')
    return _azureml_train_wide_and_deep_recommender(
            training_dataset_of_user_item_rating_triples=training_dataset_of_user_item_rating_triples,
            user_features=user_features,
            item_features=item_features,
            epochs=epochs,
            batch_size=batch_size,
            wide_part_optimizer=wide_part_optimizer,
            wide_optimizer_learning_rate=wide_optimizer_learning_rate,
            crossed_feature_dimension=crossed_feature_dimension,
            deep_part_optimizer=deep_part_optimizer,
            deep_optimizer_learning_rate=deep_optimizer_learning_rate,
            user_embedding_dimension=user_embedding_dimension,
            item_embedding_dimension=item_embedding_dimension,
            categorical_features_embedding_dimension=categorical_features_embedding_dimension,
            hidden_units=hidden_units,
            activation_function=activation_function,
            dropout=dropout,
            batch_normalization=batch_normalization,)


class _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum(Enum):
    entire_grid = 'Entire grid'
    random_sweep = 'Random sweep'


class _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum(Enum):
    accuracy = 'Accuracy'
    precision = 'Precision'
    recall = 'Recall'
    f_score = 'F-score'
    auc = 'AUC'
    average_log_loss = 'Average Log Loss'


class _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum(Enum):
    mean_absolute_error = 'Mean absolute error'
    root_of_mean_squared_error = 'Root of mean squared error'
    relative_absolute_error = 'Relative absolute error'
    relative_squared_error = 'Relative squared error'
    coefficient_of_determination = 'Coefficient of determination'


class _AzuremlTuneModelHyperparametersInput:
    untrained_model: Input = None
    """Untrained model for parameter sweep"""
    training_dataset: Input = None
    """Input dataset for training"""
    optional_validation_dataset: Input = None
    """Input dataset for validation (for Train/Test validation mode)(optional)"""
    specify_parameter_sweeping_mode: _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum = _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum.random_sweep
    """Sweep entire grid on parameter space, or sweep with using a limited number of sample runs (enum: ['Entire grid', 'Random sweep'])"""
    maximum_number_of_runs_on_random_sweep: int = 5
    """Execute maximum number of runs using random sweep (optional, min: 1, max: 10000)"""
    random_seed: int = 0
    """Provide a value to seed the random number generator (optional, max: 4294967295)"""
    name_or_numerical_index_of_the_label_column: str = None
    """Label column"""
    metric_for_measuring_performance_for_classification: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum = _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum.accuracy
    """Select the metric used for evaluating classification models (enum: ['Accuracy', 'Precision', 'Recall', 'F-score', 'AUC', 'Average Log Loss'])"""
    metric_for_measuring_performance_for_regression: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum = _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum.mean_absolute_error
    """Select the metric used for evaluating regression models (enum: ['Mean absolute error', 'Root of mean squared error', 'Relative absolute error', 'Relative squared error', 'Coefficient of determination'])"""


class _AzuremlTuneModelHyperparametersOutput:
    sweep_results: Output = None
    """Results metric for parameter sweep runs"""
    trained_best_model: Output = None
    """Model with best performance on the training dataset"""


class _AzuremlTuneModelHyperparametersComponent(Component):
    inputs: _AzuremlTuneModelHyperparametersInput
    outputs: _AzuremlTuneModelHyperparametersOutput
    runsettings: _CommandComponentRunsetting


_azureml_tune_model_hyperparameters = None


def azureml_tune_model_hyperparameters(
    untrained_model: Path = None,
    training_dataset: Path = None,
    optional_validation_dataset: Path = None,
    specify_parameter_sweeping_mode: _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum = _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum.random_sweep,
    maximum_number_of_runs_on_random_sweep: int = 5,
    random_seed: int = 0,
    name_or_numerical_index_of_the_label_column: str = None,
    metric_for_measuring_performance_for_classification: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum = _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum.accuracy,
    metric_for_measuring_performance_for_regression: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum = _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum.mean_absolute_error,
) -> _AzuremlTuneModelHyperparametersComponent:
    """Perform a parameter sweep on the model to determine the optimum parameter settings.
    
    :param untrained_model: Untrained model for parameter sweep
    :type untrained_model: Path
    :param training_dataset: Input dataset for training
    :type training_dataset: Path
    :param optional_validation_dataset: Input dataset for validation (for Train/Test validation mode)(optional)
    :type optional_validation_dataset: Path
    :param specify_parameter_sweeping_mode: Sweep entire grid on parameter space, or sweep with using a limited number of sample runs (enum: ['Entire grid', 'Random sweep'])
    :type specify_parameter_sweeping_mode: _AzuremlTuneModelHyperparametersSpecifyParameterSweepingModeEnum
    :param maximum_number_of_runs_on_random_sweep: Execute maximum number of runs using random sweep (optional, min: 1, max: 10000)
    :type maximum_number_of_runs_on_random_sweep: int
    :param random_seed: Provide a value to seed the random number generator (optional, max: 4294967295)
    :type random_seed: int
    :param name_or_numerical_index_of_the_label_column: Label column
    :type name_or_numerical_index_of_the_label_column: str
    :param metric_for_measuring_performance_for_classification: Select the metric used for evaluating classification models (enum: ['Accuracy', 'Precision', 'Recall', 'F-score', 'AUC', 'Average Log Loss'])
    :type metric_for_measuring_performance_for_classification: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForClassificationEnum
    :param metric_for_measuring_performance_for_regression: Select the metric used for evaluating regression models (enum: ['Mean absolute error', 'Root of mean squared error', 'Relative absolute error', 'Relative squared error', 'Coefficient of determination'])
    :type metric_for_measuring_performance_for_regression: _AzuremlTuneModelHyperparametersMetricForMeasuringPerformanceForRegressionEnum
    :output sweep_results: Results metric for parameter sweep runs
    :type: sweep_results: Output
    :output trained_best_model: Model with best performance on the training dataset
    :type: trained_best_model: Output
    """
    global _azureml_tune_model_hyperparameters
    if _azureml_tune_model_hyperparameters is None:
        _azureml_tune_model_hyperparameters = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Tune Model Hyperparameters', version=None, feed='azureml')
    return _azureml_tune_model_hyperparameters(
            untrained_model=untrained_model,
            training_dataset=training_dataset,
            optional_validation_dataset=optional_validation_dataset,
            specify_parameter_sweeping_mode=specify_parameter_sweeping_mode,
            maximum_number_of_runs_on_random_sweep=maximum_number_of_runs_on_random_sweep,
            random_seed=random_seed,
            name_or_numerical_index_of_the_label_column=name_or_numerical_index_of_the_label_column,
            metric_for_measuring_performance_for_classification=metric_for_measuring_performance_for_classification,
            metric_for_measuring_performance_for_regression=metric_for_measuring_performance_for_regression,)


class _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassAveragedPerceptronInput:
    create_trainer_mode: _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum = _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    initial_learning_rate: float = 1.0
    """The initial learning rate for the Stochastic Gradient Descent optimizer.  (optional, min: 2.220446049250313e-16)"""
    maximum_number_of_iterations: int = 10
    """The number of Stochastic Gradient Descent iterations to be performed over the training dataset.  (optional, min: 1)"""
    range_for_initial_learning_rate: str = '0.1; 0.5; 1.0'
    """Range for initial learning rate for the Stochastic Gradient Descent optimizer.  (optional)"""
    range_for_maximum_number_of_iterations: str = '1; 10'
    """Range for the number of Stochastic Gradient Descent iterations to be performed over the training dataset.  (optional)"""
    random_number_seed: int = None
    """The seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlTwoClassAveragedPerceptronOutput:
    untrained_model: Output = None
    """An untrained binary classification model that can be connected to the Create One-vs-All Multi-class Classifier or Train Generic Model or Cross Validate Model modules."""


class _AzuremlTwoClassAveragedPerceptronComponent(Component):
    inputs: _AzuremlTwoClassAveragedPerceptronInput
    outputs: _AzuremlTwoClassAveragedPerceptronOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_averaged_perceptron = None


def azureml_two_class_averaged_perceptron(
    create_trainer_mode: _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum = _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum.singleparameter,
    initial_learning_rate: float = 1.0,
    maximum_number_of_iterations: int = 10,
    range_for_initial_learning_rate: str = '0.1; 0.5; 1.0',
    range_for_maximum_number_of_iterations: str = '1; 10',
    random_number_seed: int = None,
) -> _AzuremlTwoClassAveragedPerceptronComponent:
    """Creates an averaged perceptron binary classification model.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassAveragedPerceptronCreateTrainerModeEnum
    :param initial_learning_rate: The initial learning rate for the Stochastic Gradient Descent optimizer.  (optional, min: 2.220446049250313e-16)
    :type initial_learning_rate: float
    :param maximum_number_of_iterations: The number of Stochastic Gradient Descent iterations to be performed over the training dataset.  (optional, min: 1)
    :type maximum_number_of_iterations: int
    :param range_for_initial_learning_rate: Range for initial learning rate for the Stochastic Gradient Descent optimizer.  (optional)
    :type range_for_initial_learning_rate: str
    :param range_for_maximum_number_of_iterations: Range for the number of Stochastic Gradient Descent iterations to be performed over the training dataset.  (optional)
    :type range_for_maximum_number_of_iterations: str
    :param random_number_seed: The seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained binary classification model that can be connected to the Create One-vs-All Multi-class Classifier or Train Generic Model or Cross Validate Model modules.
    :type: untrained_model: Output
    """
    global _azureml_two_class_averaged_perceptron
    if _azureml_two_class_averaged_perceptron is None:
        _azureml_two_class_averaged_perceptron = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Averaged Perceptron', version=None, feed='azureml')
    return _azureml_two_class_averaged_perceptron(
            create_trainer_mode=create_trainer_mode,
            initial_learning_rate=initial_learning_rate,
            maximum_number_of_iterations=maximum_number_of_iterations,
            range_for_initial_learning_rate=range_for_initial_learning_rate,
            range_for_maximum_number_of_iterations=range_for_maximum_number_of_iterations,
            random_number_seed=random_number_seed,)


class _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassBoostedDecisionTreeInput:
    create_trainer_mode: _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum = _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    maximum_number_of_leaves_per_tree: int = 20
    """Specify the maximum number of leaves allowed per tree (optional, min: 2, max: 131072)"""
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10
    """Specify the minimum number of cases required to form a leaf (optional, min: 1)"""
    the_learning_rate: float = 0.2
    """Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)"""
    total_number_of_trees_constructed: int = 100
    """Specify the maximum number of trees that can be created during training (optional, min: 1)"""
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128'
    """Specify range for the maximum number of leaves allowed per tree (optional)"""
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50'
    """Specify the range for the minimum number of cases required to form a leaf (optional)"""
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4'
    """Specify the range for the initial learning rate (optional)"""
    range_for_total_number_of_trees_constructed: str = '20; 100; 500'
    """Specify the range for the maximum number of trees that can be created during training (optional)"""
    random_number_seed: int = None
    """Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlTwoClassBoostedDecisionTreeOutput:
    untrained_model: Output = None
    """An untrained binary classification model"""


class _AzuremlTwoClassBoostedDecisionTreeComponent(Component):
    inputs: _AzuremlTwoClassBoostedDecisionTreeInput
    outputs: _AzuremlTwoClassBoostedDecisionTreeOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_boosted_decision_tree = None


def azureml_two_class_boosted_decision_tree(
    create_trainer_mode: _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum = _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum.singleparameter,
    maximum_number_of_leaves_per_tree: int = 20,
    minimum_number_of_training_instances_required_to_form_a_leaf: int = 10,
    the_learning_rate: float = 0.2,
    total_number_of_trees_constructed: int = 100,
    range_for_maximum_number_of_leaves_per_tree: str = '2; 8; 32; 128',
    range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str = '1; 10; 50',
    range_for_learning_rate: str = '0.025; 0.05; 0.1; 0.2; 0.4',
    range_for_total_number_of_trees_constructed: str = '20; 100; 500',
    random_number_seed: int = None,
) -> _AzuremlTwoClassBoostedDecisionTreeComponent:
    """Creates a binary classifier using a boosted decision tree algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassBoostedDecisionTreeCreateTrainerModeEnum
    :param maximum_number_of_leaves_per_tree: Specify the maximum number of leaves allowed per tree (optional, min: 2, max: 131072)
    :type maximum_number_of_leaves_per_tree: int
    :param minimum_number_of_training_instances_required_to_form_a_leaf: Specify the minimum number of cases required to form a leaf (optional, min: 1)
    :type minimum_number_of_training_instances_required_to_form_a_leaf: int
    :param the_learning_rate: Specify the initial learning rate (optional, min: 2.220446049250313e-16, max: 1.0)
    :type the_learning_rate: float
    :param total_number_of_trees_constructed: Specify the maximum number of trees that can be created during training (optional, min: 1)
    :type total_number_of_trees_constructed: int
    :param range_for_maximum_number_of_leaves_per_tree: Specify range for the maximum number of leaves allowed per tree (optional)
    :type range_for_maximum_number_of_leaves_per_tree: str
    :param range_for_minimum_number_of_training_instances_required_to_form_a_leaf: Specify the range for the minimum number of cases required to form a leaf (optional)
    :type range_for_minimum_number_of_training_instances_required_to_form_a_leaf: str
    :param range_for_learning_rate: Specify the range for the initial learning rate (optional)
    :type range_for_learning_rate: str
    :param range_for_total_number_of_trees_constructed: Specify the range for the maximum number of trees that can be created during training (optional)
    :type range_for_total_number_of_trees_constructed: str
    :param random_number_seed: Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained binary classification model
    :type: untrained_model: Output
    """
    global _azureml_two_class_boosted_decision_tree
    if _azureml_two_class_boosted_decision_tree is None:
        _azureml_two_class_boosted_decision_tree = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Boosted Decision Tree', version=None, feed='azureml')
    return _azureml_two_class_boosted_decision_tree(
            create_trainer_mode=create_trainer_mode,
            maximum_number_of_leaves_per_tree=maximum_number_of_leaves_per_tree,
            minimum_number_of_training_instances_required_to_form_a_leaf=minimum_number_of_training_instances_required_to_form_a_leaf,
            the_learning_rate=the_learning_rate,
            total_number_of_trees_constructed=total_number_of_trees_constructed,
            range_for_maximum_number_of_leaves_per_tree=range_for_maximum_number_of_leaves_per_tree,
            range_for_minimum_number_of_training_instances_required_to_form_a_leaf=range_for_minimum_number_of_training_instances_required_to_form_a_leaf,
            range_for_learning_rate=range_for_learning_rate,
            range_for_total_number_of_trees_constructed=range_for_total_number_of_trees_constructed,
            random_number_seed=random_number_seed,)


class _AzuremlTwoClassDecisionForestCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassDecisionForestResamplingMethodEnum(Enum):
    bagging_resampling = 'Bagging Resampling'
    replicate_resampling = 'Replicate Resampling'


class _AzuremlTwoClassDecisionForestInput:
    create_trainer_mode: _AzuremlTwoClassDecisionForestCreateTrainerModeEnum = _AzuremlTwoClassDecisionForestCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    number_of_decision_trees: int = 8
    """Specify the number of decision trees to create in the ensemble (optional, min: 1)"""
    maximum_depth_of_the_decision_trees: int = 32
    """Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)"""
    minimum_number_of_samples_per_leaf_node: int = 1
    """Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)"""
    range_for_number_of_decision_trees: str = '1; 8; 32'
    """Specify range for the number of decision trees to create in the ensemble (optional)"""
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64'
    """Specify range for the maximum depth of the decision trees (optional)"""
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16'
    """Specify range for the minimum number of samples per leaf node (optional)"""
    resampling_method: _AzuremlTwoClassDecisionForestResamplingMethodEnum = _AzuremlTwoClassDecisionForestResamplingMethodEnum.bagging_resampling
    """Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])"""


class _AzuremlTwoClassDecisionForestOutput:
    untrained_model: Output = None
    """An untrained binary classification model"""


class _AzuremlTwoClassDecisionForestComponent(Component):
    inputs: _AzuremlTwoClassDecisionForestInput
    outputs: _AzuremlTwoClassDecisionForestOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_decision_forest = None


def azureml_two_class_decision_forest(
    create_trainer_mode: _AzuremlTwoClassDecisionForestCreateTrainerModeEnum = _AzuremlTwoClassDecisionForestCreateTrainerModeEnum.singleparameter,
    number_of_decision_trees: int = 8,
    maximum_depth_of_the_decision_trees: int = 32,
    minimum_number_of_samples_per_leaf_node: int = 1,
    range_for_number_of_decision_trees: str = '1; 8; 32',
    range_for_the_maximum_depth_of_the_decision_trees: str = '1; 16; 64',
    range_for_the_minimum_number_of_samples_per_leaf_node: str = '1; 4; 16',
    resampling_method: _AzuremlTwoClassDecisionForestResamplingMethodEnum = _AzuremlTwoClassDecisionForestResamplingMethodEnum.bagging_resampling,
) -> _AzuremlTwoClassDecisionForestComponent:
    """Creates a two-class classification model using the decision forest algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassDecisionForestCreateTrainerModeEnum
    :param number_of_decision_trees: Specify the number of decision trees to create in the ensemble (optional, min: 1)
    :type number_of_decision_trees: int
    :param maximum_depth_of_the_decision_trees: Specify the maximum depth of any decision tree that can be created in the ensemble (optional, min: 1)
    :type maximum_depth_of_the_decision_trees: int
    :param minimum_number_of_samples_per_leaf_node: Specify the minimum number of training samples required to generate a leaf node (optional, min: 1)
    :type minimum_number_of_samples_per_leaf_node: int
    :param range_for_number_of_decision_trees: Specify range for the number of decision trees to create in the ensemble (optional)
    :type range_for_number_of_decision_trees: str
    :param range_for_the_maximum_depth_of_the_decision_trees: Specify range for the maximum depth of the decision trees (optional)
    :type range_for_the_maximum_depth_of_the_decision_trees: str
    :param range_for_the_minimum_number_of_samples_per_leaf_node: Specify range for the minimum number of samples per leaf node (optional)
    :type range_for_the_minimum_number_of_samples_per_leaf_node: str
    :param resampling_method: Choose a resampling method (enum: ['Bagging Resampling', 'Replicate Resampling'])
    :type resampling_method: _AzuremlTwoClassDecisionForestResamplingMethodEnum
    :output untrained_model: An untrained binary classification model
    :type: untrained_model: Output
    """
    global _azureml_two_class_decision_forest
    if _azureml_two_class_decision_forest is None:
        _azureml_two_class_decision_forest = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Decision Forest', version=None, feed='azureml')
    return _azureml_two_class_decision_forest(
            create_trainer_mode=create_trainer_mode,
            number_of_decision_trees=number_of_decision_trees,
            maximum_depth_of_the_decision_trees=maximum_depth_of_the_decision_trees,
            minimum_number_of_samples_per_leaf_node=minimum_number_of_samples_per_leaf_node,
            range_for_number_of_decision_trees=range_for_number_of_decision_trees,
            range_for_the_maximum_depth_of_the_decision_trees=range_for_the_maximum_depth_of_the_decision_trees,
            range_for_the_minimum_number_of_samples_per_leaf_node=range_for_the_minimum_number_of_samples_per_leaf_node,
            resampling_method=resampling_method,)


class _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassLogisticRegressionInput:
    create_trainer_mode: _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum = _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    optimization_tolerance: float = 1e-07
    """Specify a tolerance value for the L-BFGS optimizer (optional, min: 2.220446049250313e-16)"""
    l2_regularizaton_weight: float = 1.0
    """Specify the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    range_for_optimization_tolerance: str = '0.00001; 0.00000001'
    """Specify a range for the tolerance value for the L-BFGS optimizer (optional)"""
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0'
    """Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)"""
    random_number_seed: int = None
    """Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlTwoClassLogisticRegressionOutput:
    untrained_model: Output = None
    """An untrained classification model"""


class _AzuremlTwoClassLogisticRegressionComponent(Component):
    inputs: _AzuremlTwoClassLogisticRegressionInput
    outputs: _AzuremlTwoClassLogisticRegressionOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_logistic_regression = None


def azureml_two_class_logistic_regression(
    create_trainer_mode: _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum = _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum.singleparameter,
    optimization_tolerance: float = 1e-07,
    l2_regularizaton_weight: float = 1.0,
    range_for_optimization_tolerance: str = '0.00001; 0.00000001',
    range_for_l2_regularization_weight: str = '0.01; 0.1; 1.0',
    random_number_seed: int = None,
) -> _AzuremlTwoClassLogisticRegressionComponent:
    """Creates a two-class logistic regression model.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassLogisticRegressionCreateTrainerModeEnum
    :param optimization_tolerance: Specify a tolerance value for the L-BFGS optimizer (optional, min: 2.220446049250313e-16)
    :type optimization_tolerance: float
    :param l2_regularizaton_weight: Specify the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type l2_regularizaton_weight: float
    :param range_for_optimization_tolerance: Specify a range for the tolerance value for the L-BFGS optimizer (optional)
    :type range_for_optimization_tolerance: str
    :param range_for_l2_regularization_weight: Specify the range for the L2 regularization weight. Use a non-zero value to avoid overfitting. (optional)
    :type range_for_l2_regularization_weight: str
    :param random_number_seed: Type a value to seed the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained classification model
    :type: untrained_model: Output
    """
    global _azureml_two_class_logistic_regression
    if _azureml_two_class_logistic_regression is None:
        _azureml_two_class_logistic_regression = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Logistic Regression', version=None, feed='azureml')
    return _azureml_two_class_logistic_regression(
            create_trainer_mode=create_trainer_mode,
            optimization_tolerance=optimization_tolerance,
            l2_regularizaton_weight=l2_regularizaton_weight,
            range_for_optimization_tolerance=range_for_optimization_tolerance,
            range_for_l2_regularization_weight=range_for_l2_regularization_weight,
            random_number_seed=random_number_seed,)


class _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum(Enum):
    fully_connected_case = 'Fully-connected case'


class _AzuremlTwoClassNeuralNetworkInput:
    create_trainer_mode: _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum = _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    hidden_layer_specification: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum = _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum.fully_connected_case
    """Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes: str = '100'
    """Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)"""
    the_learning_rate: float = 0.1
    """Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)"""
    number_of_learning_iterations: int = 100
    """Specify the number of iterations while learning (optional, min: 1)"""
    hidden_layer_specification1: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum = _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum.fully_connected_case
    """Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])"""
    number_of_hidden_nodes1: str = '100'
    """Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)"""
    range_for_learning_rate: str = '0.1; 0.2; 0.4'
    """Specify the range for the size of each step in the learning process (optional)"""
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160'
    """Specify the range for the number of iterations while learning (optional)"""
    the_momentum: float = 0
    """Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)"""
    shuffle_examples: bool = True
    """Select this option to change the order of instances between learning iterations"""
    random_number_seed: int = None
    """Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)"""


class _AzuremlTwoClassNeuralNetworkOutput:
    untrained_model: Output = None
    """An untrained binary classification model"""


class _AzuremlTwoClassNeuralNetworkComponent(Component):
    inputs: _AzuremlTwoClassNeuralNetworkInput
    outputs: _AzuremlTwoClassNeuralNetworkOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_neural_network = None


def azureml_two_class_neural_network(
    create_trainer_mode: _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum = _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum.singleparameter,
    hidden_layer_specification: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum = _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum.fully_connected_case,
    number_of_hidden_nodes: str = '100',
    the_learning_rate: float = 0.1,
    number_of_learning_iterations: int = 100,
    hidden_layer_specification1: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum = _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum.fully_connected_case,
    number_of_hidden_nodes1: str = '100',
    range_for_learning_rate: str = '0.1; 0.2; 0.4',
    range_for_number_of_learning_iterations: str = '20; 40; 80; 160',
    the_momentum: float = 0,
    shuffle_examples: bool = True,
    random_number_seed: int = None,
) -> _AzuremlTwoClassNeuralNetworkComponent:
    """Creates a binary classifier using a neural network algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassNeuralNetworkCreateTrainerModeEnum
    :param hidden_layer_specification: Specify the architecture of the hidden layer or layers (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecificationEnum
    :param number_of_hidden_nodes: Type the number of nodes in the hidden layer. For multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes: str
    :param the_learning_rate: Specify the size of each step in the learning process (optional, min: 2.220446049250313e-16, max: 2.0)
    :type the_learning_rate: float
    :param number_of_learning_iterations: Specify the number of iterations while learning (optional, min: 1)
    :type number_of_learning_iterations: int
    :param hidden_layer_specification1: Specify the architecture of the hidden layer or layers for range (optional, enum: ['Fully-connected case'])
    :type hidden_layer_specification1: _AzuremlTwoClassNeuralNetworkHiddenLayerSpecification1Enum
    :param number_of_hidden_nodes1: Type the number of nodes in the hidden layer, or for multiple hidden layers, type a comma-separated list. (optional)
    :type number_of_hidden_nodes1: str
    :param range_for_learning_rate: Specify the range for the size of each step in the learning process (optional)
    :type range_for_learning_rate: str
    :param range_for_number_of_learning_iterations: Specify the range for the number of iterations while learning (optional)
    :type range_for_number_of_learning_iterations: str
    :param the_momentum: Specify a weight to apply during learning to nodes from previous iterations (max: 1.0)
    :type the_momentum: float
    :param shuffle_examples: Select this option to change the order of instances between learning iterations
    :type shuffle_examples: bool
    :param random_number_seed: Specify a numeric seed to use for random number generation. Leave blank to use the default seed. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained binary classification model
    :type: untrained_model: Output
    """
    global _azureml_two_class_neural_network
    if _azureml_two_class_neural_network is None:
        _azureml_two_class_neural_network = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Neural Network', version=None, feed='azureml')
    return _azureml_two_class_neural_network(
            create_trainer_mode=create_trainer_mode,
            hidden_layer_specification=hidden_layer_specification,
            number_of_hidden_nodes=number_of_hidden_nodes,
            the_learning_rate=the_learning_rate,
            number_of_learning_iterations=number_of_learning_iterations,
            hidden_layer_specification1=hidden_layer_specification1,
            number_of_hidden_nodes1=number_of_hidden_nodes1,
            range_for_learning_rate=range_for_learning_rate,
            range_for_number_of_learning_iterations=range_for_number_of_learning_iterations,
            the_momentum=the_momentum,
            shuffle_examples=shuffle_examples,
            random_number_seed=random_number_seed,)


class _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum(Enum):
    singleparameter = 'SingleParameter'
    parameterrange = 'ParameterRange'


class _AzuremlTwoClassSupportVectorMachineInput:
    create_trainer_mode: _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum = _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum.singleparameter
    """Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])"""
    number_of_iterations: int = 10
    """The number of iterations. (optional, min: 1)"""
    the_value_lambda: float = 0.001
    """Weight for L1 regularization. Using a non-zero value avoids overfitting the model to the training dataset. (optional, min: 2.220446049250313e-16)"""
    range_for_number_of_iterations: str = '1; 10; 100'
    """The range for the number of iterations. (optional)"""
    range_for_lambda: str = '0.00001; 0.0001; 0.001; 0.01; 0.1'
    """Weight range for the for L1 regularization. Using a non-zero value avoids overfitting the model to the training dataset. (optional)"""
    normalize_the_features: bool = True
    """If true normalize the features."""
    random_number_seed: int = None
    """The seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)"""


class _AzuremlTwoClassSupportVectorMachineOutput:
    untrained_model: Output = None
    """An untrained binary classification model that can be connected to the Create One-vs-All Multiclass Classification Model or Train Generic Model or Cross Validate Model modules."""


class _AzuremlTwoClassSupportVectorMachineComponent(Component):
    inputs: _AzuremlTwoClassSupportVectorMachineInput
    outputs: _AzuremlTwoClassSupportVectorMachineOutput
    runsettings: _CommandComponentRunsetting


_azureml_two_class_support_vector_machine = None


def azureml_two_class_support_vector_machine(
    create_trainer_mode: _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum = _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum.singleparameter,
    number_of_iterations: int = 10,
    the_value_lambda: float = 0.001,
    range_for_number_of_iterations: str = '1; 10; 100',
    range_for_lambda: str = '0.00001; 0.0001; 0.001; 0.01; 0.1',
    normalize_the_features: bool = True,
    random_number_seed: int = None,
) -> _AzuremlTwoClassSupportVectorMachineComponent:
    """Creates a binary classification model using the Support Vector Machine algorithm.
    
    :param create_trainer_mode: Create advanced learner options (enum: ['SingleParameter', 'ParameterRange'])
    :type create_trainer_mode: _AzuremlTwoClassSupportVectorMachineCreateTrainerModeEnum
    :param number_of_iterations: The number of iterations. (optional, min: 1)
    :type number_of_iterations: int
    :param the_value_lambda: Weight for L1 regularization. Using a non-zero value avoids overfitting the model to the training dataset. (optional, min: 2.220446049250313e-16)
    :type the_value_lambda: float
    :param range_for_number_of_iterations: The range for the number of iterations. (optional)
    :type range_for_number_of_iterations: str
    :param range_for_lambda: Weight range for the for L1 regularization. Using a non-zero value avoids overfitting the model to the training dataset. (optional)
    :type range_for_lambda: str
    :param normalize_the_features: If true normalize the features.
    :type normalize_the_features: bool
    :param random_number_seed: The seed for the random number generator used by the model. Leave blank for default. (optional, max: 4294967295)
    :type random_number_seed: int
    :output untrained_model: An untrained binary classification model that can be connected to the Create One-vs-All Multiclass Classification Model or Train Generic Model or Cross Validate Model modules.
    :type: untrained_model: Output
    """
    global _azureml_two_class_support_vector_machine
    if _azureml_two_class_support_vector_machine is None:
        _azureml_two_class_support_vector_machine = _assets.load_component(
            _workspace.from_config(),
            name='azureml://Two-Class Support Vector Machine', version=None, feed='azureml')
    return _azureml_two_class_support_vector_machine(
            create_trainer_mode=create_trainer_mode,
            number_of_iterations=number_of_iterations,
            the_value_lambda=the_value_lambda,
            range_for_number_of_iterations=range_for_number_of_iterations,
            range_for_lambda=range_for_lambda,
            normalize_the_features=normalize_the_features,
            random_number_seed=random_number_seed,)


class _FineTuneForHuggingfaceTextClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = 128
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = 5e-05
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _FineTuneForHuggingfaceTextClassificationOutput:
    output_model: Output = None
    """path"""


class _FineTuneForHuggingfaceTextClassificationComponent(Component):
    inputs: _FineTuneForHuggingfaceTextClassificationInput
    outputs: _FineTuneForHuggingfaceTextClassificationOutput
    runsettings: _CommandComponentRunsetting


_fine_tune_for_huggingface_text_classification = None


def fine_tune_for_huggingface_text_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = 128,
    per_device_train_batch_size: int = 8,
    learning_rate: float = 5e-05,
    num_train_epochs: int = 1,
) -> _FineTuneForHuggingfaceTextClassificationComponent:
    """fine_tune_for_huggingface_text_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _fine_tune_for_huggingface_text_classification
    if _fine_tune_for_huggingface_text_classification is None:
        _fine_tune_for_huggingface_text_classification = _assets.load_component(
            _workspace.from_config(),
            name='fine_tune_for_huggingface_text_classification', version='0.0.1', feed='huggingface')
    return _fine_tune_for_huggingface_text_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


class _FineTuneForHuggingfaceTextGenerationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = 5e-05
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _FineTuneForHuggingfaceTextGenerationOutput:
    output_model: Output = None
    """path"""


class _FineTuneForHuggingfaceTextGenerationComponent(Component):
    inputs: _FineTuneForHuggingfaceTextGenerationInput
    outputs: _FineTuneForHuggingfaceTextGenerationOutput
    runsettings: _CommandComponentRunsetting


_fine_tune_for_huggingface_text_generation = None


def fine_tune_for_huggingface_text_generation(
    model: Path = None,
    dataset: Path = None,
    per_device_train_batch_size: int = 8,
    learning_rate: float = 5e-05,
    num_train_epochs: int = 1,
) -> _FineTuneForHuggingfaceTextGenerationComponent:
    """fine_tune_for_huggingface_text_generation
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _fine_tune_for_huggingface_text_generation
    if _fine_tune_for_huggingface_text_generation is None:
        _fine_tune_for_huggingface_text_generation = _assets.load_component(
            _workspace.from_config(),
            name='fine_tune_for_huggingface_text_generation', version='0.0.1', feed='huggingface')
    return _fine_tune_for_huggingface_text_generation(
            model=model,
            dataset=dataset,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


class _FineTuneForHuggingfaceTokenClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = 128
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = 5e-05
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _FineTuneForHuggingfaceTokenClassificationOutput:
    output_model: Output = None
    """path"""


class _FineTuneForHuggingfaceTokenClassificationComponent(Component):
    inputs: _FineTuneForHuggingfaceTokenClassificationInput
    outputs: _FineTuneForHuggingfaceTokenClassificationOutput
    runsettings: _CommandComponentRunsetting


_fine_tune_for_huggingface_token_classification = None


def fine_tune_for_huggingface_token_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = 128,
    per_device_train_batch_size: int = 8,
    learning_rate: float = 5e-05,
    num_train_epochs: int = 1,
) -> _FineTuneForHuggingfaceTokenClassificationComponent:
    """fine_tune_for_huggingface_token_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _fine_tune_for_huggingface_token_classification
    if _fine_tune_for_huggingface_token_classification is None:
        _fine_tune_for_huggingface_token_classification = _assets.load_component(
            _workspace.from_config(),
            name='fine_tune_for_huggingface_token_classification', version='0.0.1', feed='huggingface')
    return _fine_tune_for_huggingface_token_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


class _ScoreForHuggingfaceTextClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = 128
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""


class _ScoreForHuggingfaceTextClassificationOutput:
    output_dir: Output = None
    """path"""


class _ScoreForHuggingfaceTextClassificationComponent(Component):
    inputs: _ScoreForHuggingfaceTextClassificationInput
    outputs: _ScoreForHuggingfaceTextClassificationOutput
    runsettings: _CommandComponentRunsetting


_score_for_huggingface_text_classification = None


def score_for_huggingface_text_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = 128,
) -> _ScoreForHuggingfaceTextClassificationComponent:
    """score_for_huggingface_text_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :output output_dir: path
    :type: output_dir: Output
    """
    global _score_for_huggingface_text_classification
    if _score_for_huggingface_text_classification is None:
        _score_for_huggingface_text_classification = _assets.load_component(
            _workspace.from_config(),
            name='score_for_huggingface_text_classification', version='0.0.1', feed='huggingface')
    return _score_for_huggingface_text_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,)


class _ScoreForHuggingfaceTextGenerationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""


class _ScoreForHuggingfaceTextGenerationOutput:
    output_dir: Output = None
    """path"""


class _ScoreForHuggingfaceTextGenerationComponent(Component):
    inputs: _ScoreForHuggingfaceTextGenerationInput
    outputs: _ScoreForHuggingfaceTextGenerationOutput
    runsettings: _CommandComponentRunsetting


_score_for_huggingface_text_generation = None


def score_for_huggingface_text_generation(
    model: Path = None,
    dataset: Path = None,
) -> _ScoreForHuggingfaceTextGenerationComponent:
    """score_for_huggingface_text_generation
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :output output_dir: path
    :type: output_dir: Output
    """
    global _score_for_huggingface_text_generation
    if _score_for_huggingface_text_generation is None:
        _score_for_huggingface_text_generation = _assets.load_component(
            _workspace.from_config(),
            name='score_for_huggingface_text_generation', version='0.0.1', feed='huggingface')
    return _score_for_huggingface_text_generation(
            model=model,
            dataset=dataset,)


class _ScoreForHuggingfaceTokenClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = 128
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""


class _ScoreForHuggingfaceTokenClassificationOutput:
    output_dir: Output = None
    """path"""


class _ScoreForHuggingfaceTokenClassificationComponent(Component):
    inputs: _ScoreForHuggingfaceTokenClassificationInput
    outputs: _ScoreForHuggingfaceTokenClassificationOutput
    runsettings: _CommandComponentRunsetting


_score_for_huggingface_token_classification = None


def score_for_huggingface_token_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = 128,
) -> _ScoreForHuggingfaceTokenClassificationComponent:
    """score_for_huggingface_token_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :output output_dir: path
    :type: output_dir: Output
    """
    global _score_for_huggingface_token_classification
    if _score_for_huggingface_token_classification is None:
        _score_for_huggingface_token_classification = _assets.load_component(
            _workspace.from_config(),
            name='score_for_huggingface_token_classification', version='0.0.1', feed='huggingface')
    return _score_for_huggingface_token_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,)


class _SweepForHuggingfaceTextClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = None
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = None
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _SweepForHuggingfaceTextClassificationOutput:
    output_model: Output = None
    """path"""


class _SweepForHuggingfaceTextClassificationComponent(Component):
    inputs: _SweepForHuggingfaceTextClassificationInput
    outputs: _SweepForHuggingfaceTextClassificationOutput
    runsettings: _SweepComponentRunsetting


_sweep_for_huggingface_text_classification = None


def sweep_for_huggingface_text_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = None,
    per_device_train_batch_size: int = 8,
    learning_rate: float = None,
    num_train_epochs: int = 1,
) -> _SweepForHuggingfaceTextClassificationComponent:
    """sweep_for_huggingface_text_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _sweep_for_huggingface_text_classification
    if _sweep_for_huggingface_text_classification is None:
        _sweep_for_huggingface_text_classification = _assets.load_component(
            _workspace.from_config(),
            name='sweep_for_huggingface_text_classification', version='0.0.1', feed='huggingface')
    return _sweep_for_huggingface_text_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


class _SweepForHuggingfaceTextGenerationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = None
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _SweepForHuggingfaceTextGenerationOutput:
    output_model: Output = None
    """path"""


class _SweepForHuggingfaceTextGenerationComponent(Component):
    inputs: _SweepForHuggingfaceTextGenerationInput
    outputs: _SweepForHuggingfaceTextGenerationOutput
    runsettings: _SweepComponentRunsetting


_sweep_for_huggingface_text_generation = None


def sweep_for_huggingface_text_generation(
    model: Path = None,
    dataset: Path = None,
    per_device_train_batch_size: int = 8,
    learning_rate: float = None,
    num_train_epochs: int = 1,
) -> _SweepForHuggingfaceTextGenerationComponent:
    """sweep_for_huggingface_text_generation
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _sweep_for_huggingface_text_generation
    if _sweep_for_huggingface_text_generation is None:
        _sweep_for_huggingface_text_generation = _assets.load_component(
            _workspace.from_config(),
            name='sweep_for_huggingface_text_generation', version='0.0.1', feed='huggingface')
    return _sweep_for_huggingface_text_generation(
            model=model,
            dataset=dataset,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


class _SweepForHuggingfaceTokenClassificationInput:
    model: Input = None
    """path"""
    dataset: Input = None
    """path"""
    max_seq_length: int = None
    """The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)"""
    per_device_train_batch_size: int = 8
    """Batch size per GPU/TPU core/CPU for training. (optional)"""
    learning_rate: float = None
    """The initial learning rate for AdamW. (optional)"""
    num_train_epochs: int = 1
    """Total number of training epochs to perform. (optional)"""


class _SweepForHuggingfaceTokenClassificationOutput:
    output_model: Output = None
    """path"""


class _SweepForHuggingfaceTokenClassificationComponent(Component):
    inputs: _SweepForHuggingfaceTokenClassificationInput
    outputs: _SweepForHuggingfaceTokenClassificationOutput
    runsettings: _SweepComponentRunsetting


_sweep_for_huggingface_token_classification = None


def sweep_for_huggingface_token_classification(
    model: Path = None,
    dataset: Path = None,
    max_seq_length: int = None,
    per_device_train_batch_size: int = 8,
    learning_rate: float = None,
    num_train_epochs: int = 1,
) -> _SweepForHuggingfaceTokenClassificationComponent:
    """sweep_for_huggingface_token_classification
    
    :param model: path
    :type model: Path
    :param dataset: path
    :type dataset: Path
    :param max_seq_length: The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded. (optional)
    :type max_seq_length: int
    :param per_device_train_batch_size: Batch size per GPU/TPU core/CPU for training. (optional)
    :type per_device_train_batch_size: int
    :param learning_rate: The initial learning rate for AdamW. (optional)
    :type learning_rate: float
    :param num_train_epochs: Total number of training epochs to perform. (optional)
    :type num_train_epochs: int
    :output output_model: path
    :type: output_model: Output
    """
    global _sweep_for_huggingface_token_classification
    if _sweep_for_huggingface_token_classification is None:
        _sweep_for_huggingface_token_classification = _assets.load_component(
            _workspace.from_config(),
            name='sweep_for_huggingface_token_classification', version='0.0.1', feed='huggingface')
    return _sweep_for_huggingface_token_classification(
            model=model,
            dataset=dataset,
            max_seq_length=max_seq_length,
            per_device_train_batch_size=per_device_train_batch_size,
            learning_rate=learning_rate,
            num_train_epochs=num_train_epochs,)


# +===================================================+
#                    datasets
# +===================================================+


class Datasets:

    @property
    @lru_cache(maxsize=1)
    def adult_census_income_binary_classification_dataset(self):
        """Census Income dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Adult Census Income Binary Classification dataset', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def automobile_price_data_raw(self):
        """Clean missing data module required. Prices of various automobiles against make, model and technical specifications"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Automobile price data (Raw)', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def crm_appetency_labels_shared(self):
        """CRM Appetency Labels"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='CRM Appetency Labels Shared', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def crm_churn_labels_shared(self):
        """CRM Churn Labels"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='CRM Churn Labels Shared', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def crm_dataset_shared(self):
        """CRM Dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='CRM Dataset Shared', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def crm_upselling_labels_shared(self):
        """CRM Upselling Labels"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='CRM Upselling Labels Shared', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def flight_delays_data(self):
        """Flight Delays Data"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Flight Delays Data', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def german_credit_card_uci_dataset(self):
        """German Credit Card UCI dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='German Credit Card UCI dataset', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def imdb_movie_titles(self):
        """IMDB Movie Titles"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='IMDB Movie Titles', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def movie_ratings(self):
        """Movie Ratings"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Movie Ratings', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def weather_dataset(self):
        """Weather Dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Weather Dataset', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def wikipedia_sp_500_dataset(self):
        """Wikipedia SP 500 Dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Wikipedia SP 500 Dataset', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def animal_images_dataset(self):
        """This sample dataset is derived from Open Image Dataset and includes 3 animal categories (cat, dog, frog). Each category contains 10 images."""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Animal Images Dataset', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def restaurant_feature_data(self):
        """Contains restaurant features, such as name, address and dress_code."""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Restaurant Feature Data', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def restaurant_ratings(self):
        """Contains ratings given by customers to restaurants on scale from 0 to 2."""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Restaurant Ratings', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def restaurant_customer_data(self):
        """Contains customer features, such as drink_level, dress_preference and marital_status."""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='Restaurant Customer Data', version=None, feed='azureml')

    @property
    @lru_cache(maxsize=1)
    def acronym_identification_default(self):
        """Huggingface acronym_identification-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='acronym_identification-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ade_corpus_v2_ade_corpus_v2_classification(self):
        """Huggingface ade_corpus_v2-Ade_corpus_v2_classification dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ade_corpus_v2-Ade_corpus_v2_classification', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ade_corpus_v2_ade_corpus_v2_drug_ade_relation(self):
        """Huggingface ade_corpus_v2-Ade_corpus_v2_drug_ade_relation dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ade_corpus_v2-Ade_corpus_v2_drug_ade_relation', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ade_corpus_v2_ade_corpus_v2_drug_dosage_relation(self):
        """Huggingface ade_corpus_v2-Ade_corpus_v2_drug_dosage_relation dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ade_corpus_v2-Ade_corpus_v2_drug_dosage_relation', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def adversarial_qa_adversarialqa(self):
        """Huggingface adversarial_qa-adversarialQA dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='adversarial_qa-adversarialQA', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def adversarial_qa_dbert(self):
        """Huggingface adversarial_qa-dbert dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='adversarial_qa-dbert', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def adversarial_qa_dbidaf(self):
        """Huggingface adversarial_qa-dbidaf dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='adversarial_qa-dbidaf', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def adversarial_qa_droberta(self):
        """Huggingface adversarial_qa-droberta dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='adversarial_qa-droberta', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def aeslc_default(self):
        """Huggingface aeslc-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='aeslc-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def afrikaans_ner_corpus_afrikaans_ner_corpus(self):
        """Huggingface afrikaans_ner_corpus-afrikaans_ner_corpus dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='afrikaans_ner_corpus-afrikaans_ner_corpus', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ag_news_default(self):
        """Huggingface ag_news-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ag_news-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ai2_arc_arc_challenge(self):
        """Huggingface ai2_arc-ARC-Challenge dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ai2_arc-ARC-Challenge', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ai2_arc_arc_easy(self):
        """Huggingface ai2_arc-ARC-Easy dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ai2_arc-ARC-Easy', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def air_dialogue_air_dialogue_data(self):
        """Huggingface air_dialogue-air_dialogue_data dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='air_dialogue-air_dialogue_data', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def air_dialogue_air_dialogue_kb(self):
        """Huggingface air_dialogue-air_dialogue_kb dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='air_dialogue-air_dialogue_kb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def allegro_reviews_default(self):
        """Huggingface allegro_reviews-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='allegro_reviews-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def allocine_allocine(self):
        """Huggingface allocine-allocine dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='allocine-allocine', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alt_alt_km(self):
        """Huggingface alt-alt-km dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='alt-alt-km', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alt_alt_my(self):
        """Huggingface alt-alt-my dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='alt-alt-my', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alt_alt_my_transliteration(self):
        """Huggingface alt-alt-my-transliteration dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='alt-alt-my-transliteration', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alt_alt_my_west_transliteration(self):
        """Huggingface alt-alt-my-west-transliteration dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='alt-alt-my-west-transliteration', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alt_alt_parallel(self):
        """Huggingface alt-alt-parallel dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='alt-alt-parallel', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_polarity_amazon_polarity(self):
        """Huggingface amazon_polarity-amazon_polarity dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_polarity-amazon_polarity', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_all_languages(self):
        """Huggingface amazon_reviews_multi-all_languages dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-all_languages', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_de(self):
        """Huggingface amazon_reviews_multi-de dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-de', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_en(self):
        """Huggingface amazon_reviews_multi-en dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-en', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_es(self):
        """Huggingface amazon_reviews_multi-es dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-es', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_fr(self):
        """Huggingface amazon_reviews_multi-fr dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-fr', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_ja(self):
        """Huggingface amazon_reviews_multi-ja dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-ja', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amazon_reviews_multi_zh(self):
        """Huggingface amazon_reviews_multi-zh dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amazon_reviews_multi-zh', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ambig_qa_full(self):
        """Huggingface ambig_qa-full dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ambig_qa-full', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ambig_qa_light(self):
        """Huggingface ambig_qa-light dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ambig_qa-light', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def amttl_amttl(self):
        """Huggingface amttl-amttl dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='amttl-amttl', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def anli_plain_text(self):
        """Huggingface anli-plain_text dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='anli-plain_text', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def app_reviews_default(self):
        """Huggingface app_reviews-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='app_reviews-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def aqua_rat_raw(self):
        """Huggingface aqua_rat-raw dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='aqua_rat-raw', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def aqua_rat_tokenized(self):
        """Huggingface aqua_rat-tokenized dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='aqua_rat-tokenized', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ar_res_reviews_default(self):
        """Huggingface ar_res_reviews-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='ar_res_reviews-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def arcd_plain_text(self):
        """Huggingface arcd-plain_text dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='arcd-plain_text', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def arsentd_lev_default(self):
        """Huggingface arsentd_lev-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='arsentd_lev-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def art_anli(self):
        """Huggingface art-anli dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='art-anli', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def aslg_pc12_default(self):
        """Huggingface aslg_pc12-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='aslg_pc12-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def asset_ratings(self):
        """Huggingface asset-ratings dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='asset-ratings', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def asset_simplification(self):
        """Huggingface asset-simplification dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='asset-simplification', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def assin2_default(self):
        """Huggingface assin2-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='assin2-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def assin_full(self):
        """Huggingface assin-full dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='assin-full', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def assin_ptbr(self):
        """Huggingface assin-ptbr dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='assin-ptbr', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def assin_ptpt(self):
        """Huggingface assin-ptpt dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='assin-ptpt', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def atomic_atomic(self):
        """Huggingface atomic-atomic dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='atomic-atomic', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def autshumato_autshumato_en_tn(self):
        """Huggingface autshumato-autshumato-en-tn dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='autshumato-autshumato-en-tn', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def autshumato_autshumato_en_ts(self):
        """Huggingface autshumato-autshumato-en-ts dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='autshumato-autshumato-en-ts', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def autshumato_autshumato_en_ts_manual(self):
        """Huggingface autshumato-autshumato-en-ts-manual dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='autshumato-autshumato-en-ts-manual', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def autshumato_autshumato_en_zu(self):
        """Huggingface autshumato-autshumato-en-zu dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='autshumato-autshumato-en-zu', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def bsc_tecla_tecla(self):
        """Huggingface bsc/tecla-tecla dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='bsc.tecla-tecla', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_ax(self):
        """Huggingface glue-ax dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-ax', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_cola(self):
        """Huggingface glue-cola dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-cola', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_mnli(self):
        """Huggingface glue-mnli dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-mnli', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_mnli_matched(self):
        """Huggingface glue-mnli_matched dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-mnli_matched', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_mnli_mismatched(self):
        """Huggingface glue-mnli_mismatched dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-mnli_mismatched', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_mrpc(self):
        """Huggingface glue-mrpc dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-mrpc', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_qnli(self):
        """Huggingface glue-qnli dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-qnli', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_qqp(self):
        """Huggingface glue-qqp dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-qqp', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_rte(self):
        """Huggingface glue-rte dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-rte', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_sst2(self):
        """Huggingface glue-sst2 dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-sst2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_stsb(self):
        """Huggingface glue-stsb dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-stsb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def glue_wnli(self):
        """Huggingface glue-wnli dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='glue-wnli', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def imdb_plain_text(self):
        """Huggingface imdb-plain_text dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='imdb-plain_text', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_plain_text(self):
        """Huggingface squad-plain_text dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad-plain_text', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_adversarial_addonesent(self):
        """Huggingface squad_adversarial-AddOneSent dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_adversarial-AddOneSent', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_adversarial_addsent(self):
        """Huggingface squad_adversarial-AddSent dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_adversarial-AddSent', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_es_v1_1_0(self):
        """Huggingface squad_es-v1.1.0 dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_es-v1.1.0', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_it_default(self):
        """Huggingface squad_it-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_it-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_v1_pt_default(self):
        """Huggingface squad_v1_pt-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_v1_pt-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squad_v2_squad_v2(self):
        """Huggingface squad_v2-squad_v2 dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squad_v2-squad_v2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squadshifts_amazon(self):
        """Huggingface squadshifts-amazon dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squadshifts-amazon', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squadshifts_new_wiki(self):
        """Huggingface squadshifts-new_wiki dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squadshifts-new_wiki', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squadshifts_nyt(self):
        """Huggingface squadshifts-nyt dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squadshifts-nyt', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def squadshifts_reddit(self):
        """Huggingface squadshifts-reddit dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='squadshifts-reddit', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_axb(self):
        """Huggingface super_glue-axb dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-axb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_axg(self):
        """Huggingface super_glue-axg dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-axg', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_boolq(self):
        """Huggingface super_glue-boolq dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-boolq', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_cb(self):
        """Huggingface super_glue-cb dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-cb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_copa(self):
        """Huggingface super_glue-copa dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-copa', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_multirc(self):
        """Huggingface super_glue-multirc dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-multirc', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_record(self):
        """Huggingface super_glue-record dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-record', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_rte(self):
        """Huggingface super_glue-rte dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-rte', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_wic(self):
        """Huggingface super_glue-wic dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-wic', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_wsc(self):
        """Huggingface super_glue-wsc dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-wsc', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def super_glue_wsc_fixed(self):
        """Huggingface super_glue-wsc.fixed dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='super_glue-wsc.fixed', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swag_full(self):
        """Huggingface swag-full dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swag-full', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swag_regular(self):
        """Huggingface swag-regular dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swag-regular', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swahili_swahili(self):
        """Huggingface swahili-swahili dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swahili-swahili', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swahili_news_swahili_news(self):
        """Huggingface swahili_news-swahili_news dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swahili_news-swahili_news', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swda_default(self):
        """Huggingface swda-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swda-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swedish_ner_corpus_default(self):
        """Huggingface swedish_ner_corpus-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swedish_ner_corpus-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def swedish_reviews_plain_text(self):
        """Huggingface swedish_reviews-plain_text dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='swedish_reviews-plain_text', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tab_fact_blind_test(self):
        """Huggingface tab_fact-blind_test dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tab_fact-blind_test', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tab_fact_tab_fact(self):
        """Huggingface tab_fact-tab_fact dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tab_fact-tab_fact', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tamilmixsentiment_default(self):
        """Huggingface tamilmixsentiment-default dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tamilmixsentiment-default', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tanzil_bg_en(self):
        """Huggingface tanzil-bg-en dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tanzil-bg-en', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tanzil_bn_hi(self):
        """Huggingface tanzil-bn-hi dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tanzil-bn-hi', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tanzil_en_tr(self):
        """Huggingface tanzil-en-tr dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tanzil-en-tr', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tanzil_fa_sv(self):
        """Huggingface tanzil-fa-sv dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tanzil-fa-sv', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tanzil_ru_zh(self):
        """Huggingface tanzil-ru-zh dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tanzil-ru-zh', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_en(self):
        """Huggingface tapaco-en dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-en', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_eo(self):
        """Huggingface tapaco-eo dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-eo', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_es(self):
        """Huggingface tapaco-es dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-es', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_et(self):
        """Huggingface tapaco-et dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-et', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_eu(self):
        """Huggingface tapaco-eu dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-eu', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_fi(self):
        """Huggingface tapaco-fi dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-fi', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_fr(self):
        """Huggingface tapaco-fr dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-fr', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_gl(self):
        """Huggingface tapaco-gl dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-gl', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def tapaco_gos(self):
        """Huggingface tapaco-gos dataset"""
        return _assets.load_dataset(
            _workspace.from_config(),
            name='tapaco-gos', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def capreolus_bert_base_msmarco(self):
        """Huggingface Capreolus/bert-base-msmarco model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='Capreolus.bert-base-msmarco', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ferch423_gpt2_small_portuguese_wikipediabio(self):
        """Huggingface Ferch423/gpt2-small-portuguese-wikipediabio model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='Ferch423.gpt2-small-portuguese-wikipediabio', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def gronlp_gpt2_small_italian(self):
        """Huggingface GroNLP/gpt2-small-italian model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='GroNLP.gpt2-small-italian', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def lilaboualili_bert_vanilla(self):
        """Huggingface LilaBoualili/bert-vanilla model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='LilaBoualili.bert-vanilla', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def myx4567_distilgpt2_finetuned_wikitext2(self):
        """Huggingface MYX4567/distilgpt2-finetuned-wikitext2 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='MYX4567.distilgpt2-finetuned-wikitext2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def maltehb_l_ctra_danish_electra_small_uncased_ner_dane(self):
        """Huggingface Maltehb/-l-ctra-danish-electra-small-uncased-ner-dane model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='Maltehb.-l-ctra-danish-electra-small-uncased-ner-dane', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def media1129_recipe_tag_model(self):
        """Huggingface Media1129/recipe-tag-model model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='Media1129.recipe-tag-model', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def narsil_tiny_distilbert_sequence_classification(self):
        """Huggingface Narsil/tiny-distilbert-sequence-classification model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='Narsil.tiny-distilbert-sequence-classification', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def prosusai_finbert(self):
        """Huggingface ProsusAI/finbert model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ProsusAI.finbert', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def recordedfuture_swedish_ner(self):
        """Huggingface RecordedFuture/Swedish-NER model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='RecordedFuture.Swedish-NER', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def akhooli_gpt2_small_arabic(self):
        """Huggingface akhooli/gpt2-small-arabic model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='akhooli.gpt2-small-arabic', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def akhooli_gpt2_small_arabic_poetry(self):
        """Huggingface akhooli/gpt2-small-arabic-poetry model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='akhooli.gpt2-small-arabic-poetry', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alvaroalon2_biobert_chemical_ner(self):
        """Huggingface alvaroalon2/biobert_chemical_ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='alvaroalon2.biobert_chemical_ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def alvaroalon2_biobert_diseases_ner(self):
        """Huggingface alvaroalon2/biobert_diseases_ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='alvaroalon2.biobert_diseases_ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def asi_gpt_fr_cased_small(self):
        """Huggingface asi/gpt-fr-cased-small model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='asi.gpt-fr-cased-small', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def avichr_hebert_sentiment_analysis(self):
        """Huggingface avichr/heBERT_sentiment_analysis model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='avichr.heBERT_sentiment_analysis', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def bert_base_uncased(self):
        """Huggingface bert-base-uncased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='bert-base-uncased', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def bertin_project_bertin_base_ner_conll2002_es(self):
        """Huggingface bertin-project/bertin-base-ner-conll2002-es model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='bertin-project.bertin-base-ner-conll2002-es', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def cahya_gpt2_small_indonesian_522m(self):
        """Huggingface cahya/gpt2-small-indonesian-522M model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='cahya.gpt2-small-indonesian-522M', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def cahya_gpt2_small_indonesian_story(self):
        """Huggingface cahya/gpt2-small-indonesian-story model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='cahya.gpt2-small-indonesian-story', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def cardiffnlp_twitter_roberta_base_emotion(self):
        """Huggingface cardiffnlp/twitter-roberta-base-emotion model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='cardiffnlp.twitter-roberta-base-emotion', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def chambliss_distilbert_for_food_extraction(self):
        """Huggingface chambliss/distilbert-for-food-extraction model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='chambliss.distilbert-for-food-extraction', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_albert_base_chinese_ner(self):
        """Huggingface ckiplab/albert-base-chinese-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.albert-base-chinese-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_albert_base_chinese_pos(self):
        """Huggingface ckiplab/albert-base-chinese-pos model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.albert-base-chinese-pos', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_albert_base_chinese_ws(self):
        """Huggingface ckiplab/albert-base-chinese-ws model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.albert-base-chinese-ws', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_albert_tiny_chinese_ws(self):
        """Huggingface ckiplab/albert-tiny-chinese-ws model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.albert-tiny-chinese-ws', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_bert_base_chinese_ner(self):
        """Huggingface ckiplab/bert-base-chinese-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.bert-base-chinese-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_bert_base_chinese_pos(self):
        """Huggingface ckiplab/bert-base-chinese-pos model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.bert-base-chinese-pos', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ckiplab_bert_base_chinese_ws(self):
        """Huggingface ckiplab/bert-base-chinese-ws model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ckiplab.bert-base-chinese-ws', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def colorfulscoop_gpt2_small_ja(self):
        """Huggingface colorfulscoop/gpt2-small-ja model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='colorfulscoop.gpt2-small-ja', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def cross_encoder_ms_marco_electra_base(self):
        """Huggingface cross-encoder/ms-marco-electra-base model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='cross-encoder.ms-marco-electra-base', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def cross_encoder_stsb_tinybert_l_4(self):
        """Huggingface cross-encoder/stsb-TinyBERT-L-4 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='cross-encoder.stsb-TinyBERT-L-4', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def datificate_gpt2_small_spanish(self):
        """Huggingface datificate/gpt2-small-spanish model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='datificate.gpt2-small-spanish', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def dbmdz_bert_base_cased_finetuned_conll03_english(self):
        """Huggingface dbmdz/bert-base-cased-finetuned-conll03-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='dbmdz.bert-base-cased-finetuned-conll03-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def distilbert_base_uncased_finetuned_sst_2_english(self):
        """Huggingface distilbert-base-uncased-finetuned-sst-2-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='distilbert-base-uncased-finetuned-sst-2-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def dslim_bert_base_ner(self):
        """Huggingface dslim/bert-base-NER model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='dslim.bert-base-NER', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def dslim_bert_base_ner_uncased(self):
        """Huggingface dslim/bert-base-NER-uncased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='dslim.bert-base-NER-uncased', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def elastic_distilbert_base_cased_finetuned_conll03_english(self):
        """Huggingface elastic/distilbert-base-cased-finetuned-conll03-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='elastic.distilbert-base-cased-finetuned-conll03-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def elastic_distilbert_base_uncased_finetuned_conll03_english(self):
        """Huggingface elastic/distilbert-base-uncased-finetuned-conll03-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='elastic.distilbert-base-uncased-finetuned-conll03-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ethanyt_guwen_ner(self):
        """Huggingface ethanyt/guwen-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ethanyt.guwen-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def ethanyt_guwen_punc(self):
        """Huggingface ethanyt/guwen-punc model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='ethanyt.guwen-punc', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def finiteautomata_bertweet_base_sentiment_analysis(self):
        """Huggingface finiteautomata/bertweet-base-sentiment-analysis model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='finiteautomata.bertweet-base-sentiment-analysis', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def finiteautomata_beto_sentiment_analysis(self):
        """Huggingface finiteautomata/beto-sentiment-analysis model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='finiteautomata.beto-sentiment-analysis', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def gilf_french_camembert_postag_model(self):
        """Huggingface gilf/french-camembert-postag-model model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='gilf.french-camembert-postag-model', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def gunghio_distilbert_base_multilingual_cased_finetuned_conll2003_ner(self):
        """Huggingface gunghio/distilbert-base-multilingual-cased-finetuned-conll2003-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='gunghio.distilbert-base-multilingual-cased-finetuned-conll2003-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def hf_internal_testing_tiny_xlm_roberta(self):
        """Huggingface hf-internal-testing/tiny-xlm-roberta model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='hf-internal-testing.tiny-xlm-roberta', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def jsfoon_slogan_generator(self):
        """Huggingface jsfoon/slogan-generator model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='jsfoon.slogan-generator', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def lordtt13_emo_mobilebert(self):
        """Huggingface lordtt13/emo-mobilebert model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='lordtt13.emo-mobilebert', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def microsoft_codegpt_small_py(self):
        """Huggingface microsoft/CodeGPT-small-py model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='microsoft.CodeGPT-small-py', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def microsoft_codegpt_small_py_adaptedgpt2(self):
        """Huggingface microsoft/CodeGPT-small-py-adaptedGPT2 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='microsoft.CodeGPT-small-py-adaptedGPT2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def microsoft_minilm_l12_h384_uncased(self):
        """Huggingface microsoft/MiniLM-L12-H384-uncased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='microsoft.MiniLM-L12-H384-uncased', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def mrm8488_bert_spanish_cased_finetuned_ner(self):
        """Huggingface mrm8488/bert-spanish-cased-finetuned-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='mrm8488.bert-spanish-cased-finetuned-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def mrm8488_bert_tiny_finetuned_sms_spam_detection(self):
        """Huggingface mrm8488/bert-tiny-finetuned-sms-spam-detection model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='mrm8488.bert-tiny-finetuned-sms-spam-detection', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def mrm8488_codebert_base_finetuned_stackoverflow_ner(self):
        """Huggingface mrm8488/codebert-base-finetuned-stackoverflow-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='mrm8488.codebert-base-finetuned-stackoverflow-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def mrm8488_mobilebert_finetuned_ner(self):
        """Huggingface mrm8488/mobilebert-finetuned-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='mrm8488.mobilebert-finetuned-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def mrm8488_mobilebert_finetuned_pos(self):
        """Huggingface mrm8488/mobilebert-finetuned-pos model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='mrm8488.mobilebert-finetuned-pos', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def nateraw_bert_base_uncased_emotion(self):
        """Huggingface nateraw/bert-base-uncased-emotion model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='nateraw.bert-base-uncased-emotion', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def oliverguhr_german_sentiment_bert(self):
        """Huggingface oliverguhr/german-sentiment-bert model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='oliverguhr.german-sentiment-bert', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def philschmid_distilroberta_base_ner_conll2003(self):
        """Huggingface philschmid/distilroberta-base-ner-conll2003 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='philschmid.distilroberta-base-ner-conll2003', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def pierreguillou_gpt2_small_portuguese(self):
        """Huggingface pierreguillou/gpt2-small-portuguese model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='pierreguillou.gpt2-small-portuguese', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def pierrerappolt_disease_extraction(self):
        """Huggingface pierrerappolt/disease-extraction model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='pierrerappolt.disease-extraction', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def pranavpsv_gpt2_genre_story_generator(self):
        """Huggingface pranavpsv/gpt2-genre-story-generator model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='pranavpsv.gpt2-genre-story-generator', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def proycon_bert_ner_cased_sonar1_nld(self):
        """Huggingface proycon/bert-ner-cased-sonar1-nld model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='proycon.bert-ner-cased-sonar1-nld', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sgugger_tiny_distilbert_classification(self):
        """Huggingface sgugger/tiny-distilbert-classification model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sgugger.tiny-distilbert-classification', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_ctrl(self):
        """Huggingface sshleifer/tiny-ctrl model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-ctrl', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_dbmdz_bert_large_cased_finetuned_conll03_english(self):
        """Huggingface sshleifer/tiny-dbmdz-bert-large-cased-finetuned-conll03-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-dbmdz-bert-large-cased-finetuned-conll03-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_distilbert_base_cased(self):
        """Huggingface sshleifer/tiny-distilbert-base-cased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-distilbert-base-cased', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_distilbert_base_uncased_finetuned_sst_2_english(self):
        """Huggingface sshleifer/tiny-distilbert-base-uncased-finetuned-sst-2-english model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-distilbert-base-uncased-finetuned-sst-2-english', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_gpt2(self):
        """Huggingface sshleifer/tiny-gpt2 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-gpt2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def sshleifer_tiny_xlnet_base_cased(self):
        """Huggingface sshleifer/tiny-xlnet-base-cased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='sshleifer.tiny-xlnet-base-cased', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_bert_base_uncased_cola(self):
        """Huggingface textattack/bert-base-uncased-CoLA model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.bert-base-uncased-CoLA', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_bert_base_uncased_mnli(self):
        """Huggingface textattack/bert-base-uncased-MNLI model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.bert-base-uncased-MNLI', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_bert_base_uncased_sst_2(self):
        """Huggingface textattack/bert-base-uncased-SST-2 model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.bert-base-uncased-SST-2', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_bert_base_uncased_imdb(self):
        """Huggingface textattack/bert-base-uncased-imdb model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.bert-base-uncased-imdb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_bert_base_uncased_snli(self):
        """Huggingface textattack/bert-base-uncased-snli model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.bert-base-uncased-snli', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_distilbert_base_uncased_imdb(self):
        """Huggingface textattack/distilbert-base-uncased-imdb model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.distilbert-base-uncased-imdb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_distilbert_base_uncased_rotten_tomatoes(self):
        """Huggingface textattack/distilbert-base-uncased-rotten-tomatoes model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.distilbert-base-uncased-rotten-tomatoes', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_roberta_base_imdb(self):
        """Huggingface textattack/roberta-base-imdb model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.roberta-base-imdb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def textattack_xlnet_base_cased_imdb(self):
        """Huggingface textattack/xlnet-base-cased-imdb model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='textattack.xlnet-base-cased-imdb', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def transformersbook_codepage_small(self):
        """Huggingface transformersbook/codepage-small model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='transformersbook.codepage-small', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def uer_gpt2_chinese_poem(self):
        """Huggingface uer/gpt2-chinese-poem model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='uer.gpt2-chinese-poem', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def uer_roberta_base_finetuned_cluener2020_chinese(self):
        """Huggingface uer/roberta-base-finetuned-cluener2020-chinese model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='uer.roberta-base-finetuned-cluener2020-chinese', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def unitary_toxic_bert(self):
        """Huggingface unitary/toxic-bert model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='unitary.toxic-bert', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def vblagoje_bert_english_uncased_finetuned_pos(self):
        """Huggingface vblagoje/bert-english-uncased-finetuned-pos model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='vblagoje.bert-english-uncased-finetuned-pos', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def vishnun_distilgpt2_finetuned_distilgpt2_med_articles(self):
        """Huggingface vishnun/distilgpt2-finetuned-distilgpt2-med_articles model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='vishnun.distilgpt2-finetuned-distilgpt2-med_articles', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def vishnun_distilgpt2_finetuned_tamilmixsentiment(self):
        """Huggingface vishnun/distilgpt2-finetuned-tamilmixsentiment model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='vishnun.distilgpt2-finetuned-tamilmixsentiment', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def wietsedv_bert_base_multilingual_cased_finetuned_conll2002_ner(self):
        """Huggingface wietsedv/bert-base-multilingual-cased-finetuned-conll2002-ner model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='wietsedv.bert-base-multilingual-cased-finetuned-conll2002-ner', version='1', feed='huggingface')

    @property
    @lru_cache(maxsize=1)
    def xlnet_base_cased(self):
        """Huggingface xlnet-base-cased model"""
        return _assets.load_model(
            _workspace.from_config(),
            name='xlnet-base-cased', version='1', feed='huggingface')


datasets = Datasets()
