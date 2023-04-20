
'''
Empty List: If the input list is empty, there are no buildings to see, so the output should also be an empty list.
List with a single building: If the input list contains only one building, you will be able to see that building, so the output should be a list containing that building.
List with all negative buildings: If all the buildings in the input list have a negative height, none of them will be visible as they will be hidden behind each other. In this case, the output should be an empty list.
List with all same height buildings: If all the buildings in the input list have the same height, only the first building will be visible as the others will be hidden behind it. In this case, the output should be a list containing only the first building.
List with decreasing heights: If the heights of the buildings in the input list are decreasing, you will be able to see all the buildings as they will not hide each other. In this case, the output should be the list containing all the buildings.
List with increasing heights: If the heights of the buildings in the input list are increasing, only the last building will be visible as it will hide all the other buildings behind it. In this case, the output should be a list containing only the last building.
'''
def skyline(building_list):
    if not isinstance(building_list, list) or not all(
        isinstance(x, int) for x in building_list):
        return None
    temp = 0
    new_list = []
    for item in building_list:
        if item > temp:
            temp = item
            new_list.append(item)
    return new_list


assert skyline([]) == []
assert skyline([10, 9, 3, 2, 1, 0]) == [10]
assert skyline([-1, -3, -3, -7, -7, -3]) == []
assert skyline([3]) == [3]
assert skyline(["a", "b", "c"]) == None
print("All Tests PASS!!!")
