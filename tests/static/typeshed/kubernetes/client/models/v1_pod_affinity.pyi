# Stubs for kubernetes.client.models.v1_pod_affinity (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1PodAffinity:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    preferred_during_scheduling_ignored_during_execution: Any = ...
    required_during_scheduling_ignored_during_execution: Any = ...
    def __init__(self, preferred_during_scheduling_ignored_during_execution: Optional[Any] = ..., required_during_scheduling_ignored_during_execution: Optional[Any] = ...) -> None: ...
    @property
    def preferred_during_scheduling_ignored_during_execution(self): ...
    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution: Any) -> None: ...
    @property
    def required_during_scheduling_ignored_during_execution(self): ...
    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...