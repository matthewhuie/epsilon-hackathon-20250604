from google.adk.agents import Agent

from ...shared_libraries import constants
from . import prompt

import json
import os


classifier_agent = Agent(
    model=constants.MODEL,
    name="classifier_agent",
    description="A helpful agent to classify columns",
    instruction=prompt.CLASSIFIER_AGENT_PROMPT,
    output_key="classifier_agent_response"
)