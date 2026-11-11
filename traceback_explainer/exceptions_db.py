
EXCEPTIONS = {
    "NameError": {
        "description": "Raised when Python tries to access a name that is not defined.",
        "causes": [
            "Using an undefined variable",
            "Accessing a variable outside its scope",
            "Misspelling a variable name"
        ],
        "suggestions": [
            "Define the variable before using it",
            "Check the spelling of the variable",
            "Check whether the variable is accessible"
        ],
        "example": "print(username)"
    },

    "TypeError": {
        "description": "Raised when an operation is applied to an inappropriate data type.",
        "causes": [
            "Adding incompatible data types",
            "Passing the wrong argument type"
        ],
        "suggestions": [
            "Check the data types being used",
            "Convert values to the correct type"
        ],
        "example": "5 + 'hello'"
    },

    "ValueError": {
        "description": "Raised when a function receives an inappropriate value.",
        "causes": [
            "Converting invalid text to a number",
            "Providing an unacceptable value"
        ],
        "suggestions": [
            "Check the value being supplied",
            "Validate input before processing"
        ],
        "example": "int('hello')"
    },

    "IndexError": {
        "description": "Raised when trying to access a sequence position that does not exist.",
        "causes": [
            "Using an index outside a list's range",
            "Accessing an empty list"
        ],
        "suggestions": [
            "Check the length of the list",
            "Make sure the index is within range"
        ],
        "example": "numbers = [1, 2]; print(numbers[5])"
    },

    "KeyError": {
        "description": "Raised when trying to access a dictionary key that does not exist.",
        "causes": [
            "Using a dictionary key that is missing"
        ],
        "suggestions": [
            "Check whether the key exists",
            "Use dict.get() when a key might be missing"
        ],
        "example": "person = {}; print(person['name'])"
    }
}
