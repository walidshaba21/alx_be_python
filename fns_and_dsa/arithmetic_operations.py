def perform_operation(num1, num2, operation):
    operation = operation.lower()
    
    if operation in ("add", "+" ):
        return num1 + num2
    elif operation in ("subtract", "-"):
        return num1 - num2 
    elif operation in ("multiply", "*", "x"):
        return num1 * num2
    elif operation in ("divide", "/"):
        if(num2 == 0):
            return "The divided can't be 0, chack the numbers and try again"
        return num1 / num2
    else:
        return  "Invalid operator entered"      
