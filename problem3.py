def zigzag_merge(list1, list2):
    new_list = []
    if len(list1) >= len(list2):
        for i in range(len(list1)):
            new_list.append(list1[i])
            if i < len(list2):
                new_list.append(list2[i])
    else: 
        for i in range(len(list2)):
            if i < len(list1):
                 new_list.append(list1[i])
            new_list.append(list2[i])
            
    return new_list

list_a = [1, 2, 3]
list_b = ['A', 'B', 'C']
print(f"\n\nMerged equal lists: {zigzag_merge(list_a, list_b)}")

list_c = [1, 2]
list_d = ['A', 'B', 'C', 'D']
print(f"Merged with longer second list: {zigzag_merge(list_c, list_d)}")

list_e = [1, 2, 3, 4, 5]
list_f = ['A']
print(f"Merged with longer first list: {zigzag_merge(list_e, list_f)}\n\n")
