import json
from typing import Optional
import openai
from mod_dlm_schema import PrefabElement  # Importing schema
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from mod_dlm_schema import PrefabElement  # Your custom schema
from pydantic import ValidationError
import json
import os

os.environ["OPENAI_API_KEY"] = "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"
# Step 1: Set up OpenAI API key
openai.api_key = "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"

# Step 2: Use ChatOpenAI with OpenAI API
def fill_schema_with_openai(schema: str, markdown: str) -> dict:
    """Use OpenAI GPT-4 to populate the schema."""
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
    )

    # Define the prompt template
    prompt = PromptTemplate(
        template="""
    You are given the following schema:
    {schema}

    From the provided markdown content:
        {markdown}

    Fill out the schema fields based on the markdown information. If any fields are missing, infer them logically, keeping the schema constraints in mind. Output the result strictly in JSON format matching the schema and leave blank if there is no information found.
    """,
        input_variables=["schema", "markdown"],
    )

    # Use RunnableSequence to chain the prompt and LLM
    sequence = prompt | llm

    # Generate the result
    result = sequence.invoke({"schema": schema, "markdown": markdown})
    return json.loads(result.content)  # Ensure the result is deserialized into a dictionary


# Step 3: Read Markdown File
markdown_file = "markup.md"
with open(markdown_file, "r") as f:
    markdown_content = f.read()

# Step 4: Validate and Populate Schema
def populate_and_validate_schema(markdown_content: str):
    # Convert the PrefabElement schema to JSON for GPT-4
    prefab_schema = json.dumps(PrefabElement.model_json_schema())

    # Fill missing schema data using GPT-4
    try:
        populated_data = fill_schema_with_openai(prefab_schema, markdown_content)

        #print("\n\n\n",populated_data,"\n\n\n")

        # Validate data against the PrefabElement schema
        validated_data = PrefabElement(**populated_data)

        # Return validated data
        return validated_data.dict()
    except ValidationError as e:
        print("Validation Error:", e.json())
        raise e
    except Exception as e:
        print("Error during GPT-4 processing:", e)
        raise e

# Step 5: Populate the Schema and Save Output
output_file = "output.json"

try:
    final_data = populate_and_validate_schema(markdown_content)

    # Save the final JSON output
    with open(output_file, "w") as f:
        json.dump(final_data, f, indent=2)
    print(f"Schema populated and saved to {output_file}")
except Exception as e:
    print(f"Failed to populate schema: {e}")

if __name__ == "__main__":
    pass