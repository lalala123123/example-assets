# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
from azureml.core import Workspace


_default_workspace_from_config = None


def from_config():
    global _default_workspace_from_config
    if _default_workspace_from_config is None:
        _default_workspace_from_config = Workspace.from_config()
    return _default_workspace_from_config
