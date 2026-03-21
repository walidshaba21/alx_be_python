from class_static_methods_demo import Calculator

def main:
    # Using the static method
    sum_result = Calculator.add10, 5
    printf"The sum is: {sum_result}"

    # Using the class method
    product_result = Calculator.multiply10, 5
    printf"The product is: {product_result}"

if __name__ == "__main__":
    main
