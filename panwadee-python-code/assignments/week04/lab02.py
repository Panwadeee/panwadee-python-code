"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
    # Your code here
        number = int(input("Insert number[" + str(i) + "]: "))
        number.append(number)
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []# Your code here
    odd_numbers = []# [Your code here
    
    #Calculate average
    average = sum(numbers)/10.0
    
    
    # Numbers greater than average
    above_average = []# Your code here

    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else :
            odd_numbers.append(numbers[i])
        
        if numbers[i] > average:
            above_average.append(numbers[i])
        
    
    # Display results
    # Your code here
    print("Even Number List: ",even_numbers)
    print("Odd Number list: ",odd_numbers)
    print("Above Averagre List: ",above_average)
    print("Sum: ",sum(numbers))
    print("Averge: ", average)
    print("Min: ",min(numbers))
    print("max: ",max(numbers))

if __name__ == "__main__":
    number_operations()

