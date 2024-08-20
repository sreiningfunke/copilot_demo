# Find common elements in two lists:
def find_common_elements(list1, list2):
    common_elements = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_elements.append(item1)
    return common_elements

# Find common elements in three lists:


