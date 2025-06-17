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

OUTPUT_AGENT_PROMPT = """
    You are an output generator agent. Save the input JSON data to file, from the previous two outputs from classifier and transformation steps.

    **Classifier JSON:**
    {classifier_agent_response}

    **Transformation JSON:**
    {transformation_agent_response}
"""