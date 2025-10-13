'''
Find the 2nd instance of 'the', 
and slice out the next 10 characters
'''

phrase = "The world is the most wonderful place!"
phrase_c = phrase.lower()

if('the' in phrase.lower()):
    found_index = phrase_c.find('the')
    # the first 'the' starts at index found_index
    print(f"{found_index=}")

    found_index = phrase_c.find('the', found_index+1)
    print(f"{found_index=}")

    print(phrase[found_index+3:found_index+3+10])
