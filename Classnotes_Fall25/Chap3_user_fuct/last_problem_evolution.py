import sys

def test():
    # This will not affect your program if they work
    ans = solution("Corin")
    expected = "Thank you, Corin, and farewell!"

    assert ans == expected, f"Expected: {expected}, Actual Output: {ans}"
    assert solution("") == "Thank you, , and farewell!"
    assert solution("Ally") == "Thank you, Ally, and farewell!"
    print("All test passed!", file=sys.stderr)

def main():
    
    test()   # Run my test function
    name_main = input_name()
    answer = solution(name_main)

    print(answer)

def input_name():
    name = input()
    return name


def solution(name : str) -> str:
    '''
    Inputs a string, return a string in a phrase
    '''
    ans = f"Thank you, {name}, and farewell!"
    return ans  # passes the answer back onto the calling function, in this case
                # our global main program


if __name__ == "__main__":  # if I am the main file being run, run my main function
                            # otherwise my functions are open for import
    main()



'''
print("Enter a name: ", file=sys.stderr) # Ignored by Kattis, for user use
name = input()
print(f'Thank you, {name}, and farewell!')
'''
'''name_main = input()
answer = solution(name_main)
print(answer)''' # This stuff is now in our main() function