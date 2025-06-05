from ...shared_libraries import constants
from . import prompt
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
import json

def recommend_transformations(input_data: str) -> dict:
    """Recommend transformations for a list of column mappings in JSON

    Args:
        input_data (str): The input JSON, passed from the classifier agent, containing column mappings

    Returns:
        dict: JSON array of recommend transformation per column mapping
    """
    
    if input_data is not None:
        json_data = json.loads(input_data)

        for column_mapping in json_data:
            print(column_mapping)
            reco_xforms = []
            # if source is a string, let's recommend string cleansings
            if column_mapping.get('Raw-data-type', '').lower() == 'string':
                # if source is a string, let's recommend trimming
                reco_xforms.append('trim_leading_trailing_spaces')

            # if we can tell it's an ID, and it's a string, let's recommend standardization of the data
            if 'id' in column_mapping.get('user_column_name', '').lower() and column_mapping.get('Raw-data-type', '').lower() == 'string':
                reco_xforms.append('standardize_id_structure')

            # if we can tell it's a name, and it's a string, let's recommend title casing
            if 'name' in column_mapping.get('user_column_name', '').lower() and column_mapping.get('Raw-data-type', '').lower() == 'string':
                reco_xforms.append('standardize_to_title_case')

            # if we can tell it's a phone, and it's a string, let's recommend phone standardization
            if 'phone' in column_mapping.get('user_column_name', '').lower() and column_mapping.get('Raw-data-type', '').lower() == 'string':
                reco_xforms.append('standardize_to_phone_number')

            # if we can tell it's a state, and it's a string, let's recommend standardizing the state acronym
            if 'state' in column_mapping.get('user_column_name', '').lower() and column_mapping.get('Raw-data-type', '').lower() == 'string':
                reco_xforms.append('standardize_to_state_abbreviations')

            # if we can tell it's an email, and it's a string, let's recommend standardizing formatting
            if 'email' in column_mapping.get('user_column_name', '').lower() and column_mapping.get('Raw-data-type', '').lower() == 'string':
                reco_xforms.append('standardize_to_email_format')

            # if we are converting to a date, let's recommend standardizing to date
            if column_mapping.get('Raw-data-type', '').lower() != column_mapping.get('target-data-type', '').lower() and column_mapping.get('target-data-type', '').lower() == 'date':
                reco_xforms.append('convert_to_standard_date')

            # if we are converting to a datetime, let's recommend standardizing to datetime
            if column_mapping.get('Raw-data-type', '').lower() != column_mapping.get('target-data-type', '').lower() and column_mapping.get('target-data-type', '').lower() == 'datetime':
                reco_xforms.append('convert_to_standard_datetime')

            # if we are converting to a decimal, let's recommend standardizing to decimal
            if column_mapping.get('Raw-data-type', '').lower() != column_mapping.get('target-data-type', '').lower() and column_mapping.get('target-data-type', '').lower() == 'decimal':
                reco_xforms.append('convert_to_standard_decimal')

            column_mapping['recommended_transforms'] = reco_xforms

        open('transformation_agent_output.json', 'w', encoding='UTF-8').write(json.dumps(json_data))
        return {
            "status": "success",
            "recommendations": json_data
        }
    else:
        return {
            "status": "error",
            "error_message": "Error generating recommended transformations for input data.",
        }


transformation_agent = Agent(
    name="transformation_agent",
    model=constants.MODEL,
    description=(
        "Agent to recommend transformations for a given array of column mappings."
    ),
    instruction=prompt.TRANSFORMATION_AGENT_PROMPT,
    tools=[recommend_transformations],
    output_key="transformation_agent_response"
)