def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 3, 67, 32)")

def get_user_input():
    num1 = float(input("Enter value of num1: "))
    num2 = float(input("Enter value of num2: "))
    num3 = float(input("Enter value of num3: "))
    num4 = float(input("Enter value of num4: "))  

    return num1, num2, num3, num4

def calc_average(num1, num2, num3, num4):
    average = (num1 + num2 + num3 + num4) / 4
    print("The average =", average)
    return average
    
def find_min_max(num1, num2, num3, num4):
    min_num = min(num1, num2, num3, num4)
    max_num = max(num1, num2, num3, num4)
    print("Minimum number is:", min_num)
    print("Maximum number is:", max_num)
    return min_num, max_num

def sort_temperature(temperatures):
    temperatures.sort()
    print("Sorted temperatures:", temperatures)
    return temperatures

def calc_median_temperature(temperatures):
    sorted_temperatures = sort_temperature(temperatures)
    n = len(sorted_temperatures)
    if n % 2 == 0:
        median = (sorted_temperatures[n//2 - 1] + sorted_temperatures[n//2]) / 2
    else:
        median = sorted_temperatures[n//2]
    print("Median temperature:", median)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temperatures = get_user_input()
    calc_average_result = calc_average(*temperatures)
    min_num, max_num = find_min_max(*temperatures)
    sorted_temperatures = sort_temperature(list(temperatures))  # Convert temperatures to a list before sorting
    calc_median_temperature(sorted_temperatures)
    
if __name__ == "__main__":
    main()