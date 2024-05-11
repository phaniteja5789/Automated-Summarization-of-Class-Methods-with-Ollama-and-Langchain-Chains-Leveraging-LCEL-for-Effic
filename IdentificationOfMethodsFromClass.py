import os
import importlib.util
import inspect

def get_user_defined_methods_from_directory(directory):
    user_defined_methods = {}
    user_defined_methods_with_str_representation = {}

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".py"):  # Consider only Python files
            module_name = filename[:-3]  # Remove the '.py' extension

            # Import the module dynamically
            module_path = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Iterate through objects in the module
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    class_name = name
                    methods = []
                    # Get user-defined methods from the class
                    for method_name, method in inspect.getmembers(obj):
                        # Exclude methods inherited from base classes
                        if inspect.isfunction(method) and method.__qualname__.startswith(class_name):
                            methods.append(method_name)
                            user_defined_methods_with_str_representation[class_name+"."+method_name] = inspect.getsource(method)
                    user_defined_methods[class_name] = methods

    return (user_defined_methods,user_defined_methods_with_str_representation)

