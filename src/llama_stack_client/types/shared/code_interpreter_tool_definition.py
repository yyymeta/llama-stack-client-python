# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..rest_api_execution_config_param import RestAPIExecutionConfigParam

__all__ = ["CodeInterpreterToolDefinition"]


class CodeInterpreterToolDefinition(BaseModel):
    enable_inline_code_execution: bool

    type: Literal["code_interpreter"]

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    remote_execution: Optional[RestAPIExecutionConfigParam] = None
