class GenericCalculations:
    def add(self, *args):
        """
        Adds all the numbers in the given list of arguments.
        """
        return sum(args)

    def multiply(self, *args):
        """
        Multiplies all the numbers in the given list of arguments.
        """
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, *args):
        """
        Divides the first number in the list of arguments by the rest of the numbers.
        """
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    def power(self, *args):
        """
        Raises the first number in the list of arguments to the power of the rest of the numbers.
        """
        result = args[0]
        for num in args[1:]:
            result **= num
        return result

    def concatenate(self, *args):
        """
        Concatenates all the elements in the given list of arguments as strings.
        """
        return ''.join(str(arg) for arg in args)