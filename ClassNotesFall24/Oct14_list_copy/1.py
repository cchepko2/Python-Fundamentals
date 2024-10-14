unsorted_names = ["Zorin", "Lizz", "Xander", "Aerg"]

sorted_names = unsorted_names  # does not make a copy, 
                # just makes one list reference the other
                # they are the same object... 
                # what happens to one happens to the other

print(unsorted_names)
print(sorted_names)

sorted_names.sort() # sorts names, sort happens in place...modifies itself

print(unsorted_names) # both have been sorted
print(sorted_names)