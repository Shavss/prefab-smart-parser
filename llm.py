from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from preprocess import extract_text_from_pdf, split_into_sentences, create_overlapping_chunks

import PyPDF2

building_system = [
          "Wall",
          "Balcony",
          "Pod",
          "Frame",
          "Facade",
          "Floors",
          "Modules",
          "Plants",
          "Roofs",
          "Stairs"
        ]
product_category = [
          "Boarding",
          "Solid Wall Panels",
          "Closed Wall Panels",
          "Twinwall",
          "Open Wall Panels",
          "Structural Insulated Panels (SIPs)",
          "Insulated Concrete Panels",
          "Prefabricated Balcony",
          "Pod",
          "Whole Building System",
          "Structural Frame",
          "Facade System",
          "Hollowcore Floor",
          "Concrete Lattice Floor",
          "Floor Cassettes",
          "Solid Floor Panels",
          "Volumetric module",
          "Prefabricated Plant",
          "Roof Panel",
          "Roof Truss",
          "Prefabricated Stairs"
        ]
material = [
              "Timber",
              "Steel",
              "Concrete",
              "Hybrid",
              "Other"
            ]

load_dotenv()

def define_model():
    llm = ChatOpenAI(temperature=0)
    return llm


# # Define your desired data structure.
# class Joke(BaseModel):
#     individual_related: str = Field(description="Just write individual related information like university name etc")
#     #punchline: str = Field(description="answer to resolve the joke")

# Define your desired data structure.
class ChooseType(BaseModel):
    #element: str = Field(description="The name of the identified element.")
    building_system: str = Field(description="What kind of building system category that element might be belong to.")
    product_category: str = Field(description="What kind of product category that element might be belong to.")
    explanation: str = Field(description="The reason why did you chose this specific product category")
    material: str = Field(description="What kind of material that element was built up?")
    maximum_height: str = Field(description="What is the maximum height of the element")
    minimum_height: str = Field(description="What is the minimum height of the element")
    max_width: str = Field(description="What is the maximum width of the element")
    min_width: str = Field(description="What is the minimum width of the element")
    max_length: str = Field(description="What is the maximum length of the element")
    min_length: str = Field(description="What is the minimum length of the element")

# Set up a parser + inject instructions into the prompt template.


def llm_stack(model, chunk):

    building_system = [
            "Wall",
            "Balcony",
            "Pod",
            "Frame",
            "Facade",
            "Floors",
            "Modules",
            "Plants",
            "Roofs",
            "Stairs"
            ]
    product_category = [
            "Boarding",
            "Solid Wall Panels",
            "Closed Wall Panels",
            "Twinwall",
            "Open Wall Panels",
            "Structural Insulated Panels (SIPs)",
            "Insulated Concrete Panels",
            "Prefabricated Balcony",
            "Pod",
            "Whole Building System",
            "Structural Frame",
            "Facade System",
            "Hollowcore Floor",
            "Concrete Lattice Floor",
            "Floor Cassettes",
            "Solid Floor Panels",
            "Volumetric module",
            "Prefabricated Plant",
            "Roof Panel",
            "Roof Truss",
            "Prefabricated Stairs"
            ]
    material = [
                "Timber",
                "Steel",
                "Concrete",
                "Hybrid",
                "Other"
                ]

    parser = JsonOutputParser(pydantic_object=ChooseType)
    template = """
        You are an assistant that reads the given text and identifies elements related to the building domain. Here is a sample workflow that you can follow:
        1. Identify the elements.  
        2. Extract the metadata about the element. And decide which one of these features fits best with the element.
        Please consider synonyms in the given text like width could be also mentioned as thickness.
        If there is no data about these features, just type "None" for non-existing data.

        Features: 
        - Types of building system:  {building_system},
        - Types of product system: {product_category},
        - materials: {material}

        - Given text: {chunk}

        - Output format: {format_instructions}

        An example output:
        {{
            "element": "Wall 01",
            "building_system": "Wall",
            "product_category": "twinwall",
            "explanation": "there is a direct information about the product is a twinwall",
            "material": "Concrete",
            "maximum height": "10 meter",
            "minimum height": "1 meter",
            "maximum width": "200 centimers",
            "minimum width": "25 centimeters",
            "maximum length": "150 centimetrs",
            "minimum length": "10 centimers"
            
        }}
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["building_system","product_category","material","chunk"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | model | parser

    result = chain.invoke({"building_system": building_system,"product_category": product_category,"material": material, "chunk": chunk})

    print("Result of the LLM invoke: ", result)

    return result

if __name__ == "__main__":
    pdf_file_path = "Data/PDFs/bele_doppelwand_2015.pdf"
    pdf_text = extract_text_from_pdf(pdf_file_path)
    sentences_list = split_into_sentences(pdf_text)
    chunks = create_overlapping_chunks(sentences_list)

    model =define_model()

    for index, chunk in enumerate(chunks):
        print(f"Chunk {index}: {chunk}")

    for chunk in chunks:
        llm_response = llm_stack(model, chunk)
        print ("llm response: ", llm_response)
        ### TO DO
        # Generate a UUID

        
