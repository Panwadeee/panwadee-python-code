"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
    
def get_temperatures():
    x = [32,30,31,33,30,31,34]
    return x

def analyze_temp(temp_list):
    average_temp = 0
    sum = 0
    for temp in temp_list:
        sum = sum + temp
        average_temp = sum / 7
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    return (average_temp,max_temp,min_temp)

def display_analysis(avg,high,low):
    print("Temperature Analysis for the Week:")
    print("average: %f C" % (avg))
    print(f"Highest:{high} c")
    print("lowest: %d c" % (low))

temp_list = get_temperatures()
result = analyze_temp(temp_list)
display_analysis(result[0],result[1],result[2])