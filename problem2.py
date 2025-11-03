# def remove_outliers(data, min_val, max_val):
#     for item in data:
#         if item < min_val or item > max_val:
#             data.remove(item)

def remove_outliers(data, min_val, max_val):
    i = 0
    finish = False
    while True:
        if data[i] == data[-1]:
                finish = True
        if data[i] < min_val or data[i] > max_val:
            data.remove(data[i])
            if finish:
                break
            
        else:
            if finish:
                break
            else:
                i += 1
            
# def remove_outliers(data, min_val, max_val):
#     return [x for x in data if min_val <= x <= max_val]   I learned this from ChatGPT

measurements = [8, 5, 12, 1, 9, 20, 15]
print(f"\n\nOriginal measurements: {measurements}")
remove_outliers(measurements, 5, 15)
print(f"Cleaned measurements:  {measurements}")
print("--------------------")

temps = [-5, 10, 0, 35, 15, 40, 20]
print(f"Original temps: {temps}")
remove_outliers(temps, 0, 30)
print(f"Cleaned temps:  {temps}")
print(f"--------------------")

edge_case = [100, 1, 101, 2, 102]
print(f"Original edge case: {edge_case}")
remove_outliers(edge_case, 0, 10)
print(f"Cleaned edge case:  {edge_case}\n\n")


