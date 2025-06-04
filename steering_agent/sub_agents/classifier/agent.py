from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.artifacts import InMemoryArtifactService # Or GcsArtifactService
from google.adk.sessions import InMemorySessionService


from ...shared_libraries import constants
from . import prompt

import json
import os


classifier_agent = Agent(
    model=constants.MODEL,
    name="classifier_agent",
    description="A helpful agent to classify columns",
    instruction=prompt.CLASSIFIER_AGENT_PROMPT,
    output_key="classifier_agent_response" # Stores output in state['generated_code']
)