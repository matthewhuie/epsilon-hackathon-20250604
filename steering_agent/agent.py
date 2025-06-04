from google.adk.agents import SequentialAgent

from .shared_libraries import constants

from .sub_agents.classifier.agent import classifier_agent
from .sub_agents.transformation.agent import transformation_agent
from .sub_agents.output.agent import output_agent

from . import prompt

from google.adk.runners import Runner
from google.adk.artifacts import InMemoryArtifactService # Or GcsArtifactService
from google.adk.sessions import InMemorySessionService
from steering_agent.tools.memory import _load_file


root_agent = SequentialAgent(
    name=constants.AGENT_NAME,
    description=constants.DESCRIPTION,
    sub_agents=[
        classifier_agent,
        transformation_agent,
        # output_agent,
    ],
    before_agent_callback=_load_file
)