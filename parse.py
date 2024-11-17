from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = (
    "You are tasked with extracting specific information from the following text {dom_content}. "
    "Please follow the instructions carefully and provide the requested information. \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_ollama(dom_chunks, parse_desc):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    for i,ch in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": ch, "parse_description": parse_desc})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
    
    pass