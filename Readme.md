This repository details out on the usage of Ollama and Langchain

Problem Statement

	Generate the summary of the function definition, group the similar summaries together

sourcecode.py ==> This is the entry point for the application to run, which imports other code files and perform the necessary operations and displays the final output of the application.

This projects mainly has 3 phases

	phase-1

		In the phase-1, identify the list of methods from each class that is present in the directory "/codes"
		
		After completion of phase-1, for each class it will list out list of methods present in the same class
		

		The entire code for the phase-1 is present in the IdentificationOfMethodsFromClass.py
		
		List of Modules used are os,importlib.util,inspect ==> in order to identify the methods present in the class
		
		
	phase-2
	
		In the phase-2, generate the summary for each method from the class.
		
		List of Modules used are langchain
		
		classes used are 
		
			langchain.prompts.prompt import PromptTemplate ==> Using this, created a Prompt that can be sent to the LLM
			langchain.llms.ollama import Ollama ==> Using this, I used the quantized model in my local machine locally.
			
		
		Used the LCEL(Langchain Expression Language), so that I created a chain that with prompt | llm
		
		
		After completion of phase-2, for every method there exists a summary generated using LLM
		
		
		The LLM used is "llama3"
		
		
	phase-3
	
		In the phase-3, group the summaries together based on their functionality
		
		List of Modules used are langchain
		
		classes used are 
		
			langchain.prompts.prompt import PromptTemplate ==> using this, created a prompt that can be sent as input to the LLM
			
			langchain.llms.ollama import Ollama ==> using this, I used the quantized model in my local machine locally
			
			langchain.prompts.few_shot import FewShotPromptTemplate ==> using this, I can create an examples and send to the LLM so that the response generated from LLM will be accurate
			
		Used the LCEL(Langchain Expression Language), so that I created a chain that with prompt | llm
		
		
		After completion of phase-3, there is a group generated which groups the similar functionalities together
		
		
		The LLM used is "llama3"
		
Output of the project is as below and present in the Output.png

<img width="751" alt="Output" src="https://github.com/phaniteja5789/CodeSummarization/assets/36558484/92f6d211-157a-4855-ba2e-5b8366e24818">
