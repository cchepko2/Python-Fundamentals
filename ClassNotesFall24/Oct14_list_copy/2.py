import copy

unsorted_names = ["Zorin", "Lizz", "Xander", "Aerg"]

sorted_names = unsorted_names.copy()  # makes a copy, works fine 
                # with a list without an inner list

sorted_names = copy.deepcopy(unsorted_names)  # makes a deep copy,  
                # always works, better to use to be safe

print("Unsorted: ", unsorted_names)
print("Sorted: ", sorted_names)

sorted_names.sort() # sorts names, sort happens in place...modifies itself

print("Unsorted: ", unsorted_names) # both have been sorted
print("Sorted: ", sorted_names)