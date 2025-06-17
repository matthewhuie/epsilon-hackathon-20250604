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

TRANSFORMATION_AGENT_PROMPT = """Given the below JSON array of column mappings, always use 'recommend_transformations' tool for the array of column mappings.

    **JSON array of column mappings:**
    {classifier_agent_response}

    Also, consider the below mapping of input data to target fields. Input will be in the following JSON format.

    **JSON format of the input column mappings:**
    [
        {
        "user_column_name": "CustomerID",
        "data_obj_column_name": "profileId",
        "data_object_name": "Profile",
        "Raw-data-type": "String",
        "target-data-type": "String"
        }
    ]
    
    "user_column_name" is the name of the column from the input data file
    "data_obj_column_name" is the "fieldTitle" from the identified target data object
    "data_object_name" is the name of the identified target data object
    "Raw-data-type" is the data type of the data in the input file for the particular column
    "target-data-type" is the data type of the fieldTitle in the identified target data object
"""