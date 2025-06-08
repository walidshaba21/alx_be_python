def perform_operation(num1, num2, operation):
    operation = operation.lower()
    
    if(operation == "add" or "+" ):
        return num1 + num2
    elif(operation == "subtract" or "-"):
        return num1 - num2 
    elif(operation == "multiply" or "*" or "x"):
        return num1 * num2
    elif(operation == "divide" or "/"):
        if(num2 == 0):
            return num1 / num2
        return "The divided can't be 0, check the numbers and try again."
    else:
        return  "Invalid operator entered"      
