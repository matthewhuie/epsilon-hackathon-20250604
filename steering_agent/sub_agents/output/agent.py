# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from ...shared_libraries import constants
from . import prompt
import json
import os
import time

def save_json_to_file(input_data: str) -> dict:
    """Takes in input JSON data and saves it to a local file

    Args:
        input_data (str): The input JSON data that will be saved to a local file

    Returns:
        dict: Status of local file saving
    """
    # Define the default directory and filename
    DEFAULT_DIRECTORY = "."
    DEFAULT_FILENAME = "output-" + str(time.time_ns()) + ".json"
    file_path = os.path.join(DEFAULT_DIRECTORY, DEFAULT_FILENAME)

    try:
        # Ensure the default directory exists before attempting to write the file
        if not os.path.exists(DEFAULT_DIRECTORY):
            os.makedirs(DEFAULT_DIRECTORY, exist_ok=True) # Create directory if it doesn't exist

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return {
            "status": "success",
            "message": "Successfully saved JSON data to" + file_path
        }

    except Exception as e:
        return {
            "status": "error",
            "message": "Error saving JSON data to a local file",
        }

output_agent = Agent(
    model=constants.MODEL,
    name="output_agent",
    description="Agent to save JSON data to a local file",
    instruction=prompt.OUTPUT_AGENT_PROMPT,
    tools=[save_json_to_file],
)
