"""Prompt schema definition."""
from __future__ import annotations

from string import Formatter
from typing import Any, Dict, List
from abc import ABC


class PromptTemplate(ABC):
    """A simple yet sufficient prompt schema with a placeholder for f-string.

    Example:
        .. code-block:: python

            from gentopia import PromptTemplate
            prompt = PromptTemplate(input_variables=["foo"], template="Say {foo}")
    """
    def __init__(self, input_variables: List[str], template: str, validate_template: bool = True,
                 skip_on_failure: bool = True) -> None:
        super().__init__()
        self.input_variables = input_variables
        self.template = template
        self.validate_template = validate_template
        self.skip_on_failure = skip_on_failure

    def format(self, **kwargs: Any) -> str:
        return self.template.format(**kwargs)

    def template_is_valid(cls, values: Dict) -> Dict:
        """Check that template and input variables are consistent."""
        if values["validate_template"]:
            try:
                dummy_input = {var: "" for var in values["input_variables"]}
                Formatter().format(values["template"], **dummy_input)
            except KeyError as e:
                raise ValueError(
                    "Invalid prompt schema; check for mismatched or missing input parameters. "
                    + str(e)
                )
        return values
