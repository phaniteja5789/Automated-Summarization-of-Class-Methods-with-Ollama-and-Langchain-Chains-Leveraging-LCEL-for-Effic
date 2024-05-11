import IdentificationOfMethodsFromClass as identification
import GenerateSummaryFromEachMethod as summaryclass
import GenerateSimilarSummariesTogether as similar_summaries
import os

# Directory containing Python files
directory_path = os.getcwd() + "\\codes\\"
user_defined_methods,user_defined_methods_with_str_representation = identification.get_user_defined_methods_from_directory(directory_path)

# Returns the methods present in each class
print("***********************Methods present in each class from the directory*********************************************")
for class_name, methods in user_defined_methods.items():
    print(class_name + ": " + ", ".join(methods))


# Iterate through each method in each class and generate the summary of the method
summary_responses = {}
for class_method_name,str_representation in user_defined_methods_with_str_representation.items():
    summary_response = summaryclass.iteration_through_each_method(str_representation)
    summary_responses[class_method_name] = summary_response

# print the summary associated with each method in each class
print("***********************Summary of each method from the directory*********************************************")
print(summary_responses)


# Grouping the similar summaries together

grouped_summaries = similar_summaries.grouping_of_summaries(summary_responses)

print(grouped_summaries)