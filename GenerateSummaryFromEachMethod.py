from langchain.prompts.prompt import PromptTemplate
from langchain.llms.ollama import Ollama

llm = Ollama(model="llama3",temperature=0.1)

def generate_summary_response(method, llm):
    
    prompt = PromptTemplate(
        template='''
        Generate the summary for the method that is passed as an argument in a string format which should only describe the core logic of the method
        and shouldn't worry about the input arguments or the return type or the method name or any example for the below method and it needs
        to return only the summary of the core logic not like "The summary of the method" like that:
        \n\n {method}''',
        
        input_variables=["method"]
    )

    chain = prompt | llm

    response = chain.invoke(method)

    return response


def iteration_through_each_method(method):

    response = generate_summary_response(method, llm)
    return response
