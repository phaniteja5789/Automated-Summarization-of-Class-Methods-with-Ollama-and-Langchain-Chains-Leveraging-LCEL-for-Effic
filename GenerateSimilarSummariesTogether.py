from langchain.prompts.prompt import PromptTemplate
from langchain.llms.ollama import Ollama
from langchain.prompts.few_shot import FewShotPromptTemplate

llm = Ollama(model="llama3",temperature=0.1)


def generate_grouped_summaries(input_summary_data,llm):
    
    examples = [
        {
            "input" : "This method calculates the sum of two numbers",
            "output" : "Addition of two numbers"
        },
        {
            "input" : "Adds two numbers and returns the sum",
            "output" : "Addition of two numbers"
        },
        {
            "input" : "This method calculates the product of two numbers",
            "output" : "Multiplication of two numbers"
        },
        {
            "input" : "Multiplies two numbers and returns the product",
            "output" : "Multiplication of two numbers"
        }
    ]

    example_prompt = PromptTemplate(
    input_variables=["input", "output"], 
    template='''
                Summary of the core functionality of a method {input} \n 
                the group that the method needs to fit in {output}"
                '''
    )

    prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix= '''Based on the values present in the list {input_summary_data} that is given as an argument. 
               group the similar summaries into a single group and name the group with the task that it performs. 
               given some of the examples for your reference. Use those examples for grouping the summaries.
               group the summaries to the bottom most level of the hierarchy. instead of generalizing the summaries.''',
    input_variables=["input_summary_data"],
    )


    chain = prompt | llm
    response = chain.invoke(input_summary_data)

    return response

def grouping_of_summaries(method_summaries):

    summaries = method_summaries.values()
    grouped_summary_response = generate_grouped_summaries(summaries,llm)
    return grouped_summary_response
