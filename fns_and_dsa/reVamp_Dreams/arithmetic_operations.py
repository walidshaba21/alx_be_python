def perform_operation(num1, num2,operations):
    
    if operations == 'add':
         return num1 + num2
    elif operations == 'subtract':
         return num1 - num2
    elif operations == 'multiply':
         return num1 * num2
    elif operations == "divide":
        if num2 == 0:
             return "Division by Zero isn't allowed"
        else:
             return num1/num2
    else:
        return "Improper operation type entered" 
