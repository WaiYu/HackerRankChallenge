def get_elements(rock):
    elements = []
    ele_count = len(rock)
    while ele_count:
        ele_count -= 1
        elements.append(rock[ele_count])
    return elements

rock_count = int(input()) - 1
common_elements = get_elements(input())
while rock_count:
    new_rock = input()
    new_element = get_elements(new_rock)
    common_elements = list(set(common_elements) & set(new_element))
    rock_count -= 1
print (len(common_elements))
