def calculate_moving_average(data, window_size):
   new_list_of_averages = []
   sum_of_windows = 0
   average = 0
   if window_size > len(data):
      return []
   elif window_size <= 0:
      return []
   else:
       # [1, 2, 4, 5, 4, 2, 5, 6] 3
       for i in range(len(data) - window_size + 1):
          for j in range(window_size):
             sum_of_windows += data[i+j]
             if j == window_size-1:
                average = round(sum_of_windows/window_size, 1)
                new_list_of_averages.append(average)
                sum_of_windows = 0
       return new_list_of_averages 

print()

data = [10, 20, 30, 40, 50]
window_size = 3
new_list = calculate_moving_average(data, window_size)
print(f"Moving average (window {window_size}) of {data}: {new_list}")

data = [1, 2, 3, 4, 5]
window_size = 2
new_list = calculate_moving_average(data, window_size)
print(f"Moving average (window {window_size}) of {data}: {new_list}")

data = [5, 10, 15]
window_size = 5
new_list = calculate_moving_average(data, window_size)
print(f"Moving average (window {window_size}{" - too big" if window_size > len(data) else ''}{" - too small" if window_size <= 0 else ''}) of {data}: {new_list}")

# data = [5, 10, 15]
# window_size = 0
# new_list = calculate_moving_average(data, window_size)
# print(f"Moving average (window {window_size}{" - too big" if window_size > len(data) else ''}{" - too small" if window_size <= 0 else ''}) of {data}: {new_list}")

# data = [5, 10, 15]
# window_size = -5
# new_list = calculate_moving_average(data, window_size)
# print(f"Moving average (window {window_size}{" - too big" if window_size > len(data) else ''}{" - too small" if window_size <= 0 else ''}) of {data}: {new_list}")

# data = [8, 12]
# window_size = 1
# new_list = calculate_moving_average(data, window_size)
# print(f"Moving average (window {window_size}{" - too big" if window_size > len(data) else ''}{" - too small" if window_size <= 0 else ''}) of {data}: {new_list}")

print()