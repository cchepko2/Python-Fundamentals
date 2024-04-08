import sys

def solution(lines):
    ans = ''
    for i in range(5):
        if 'FBI' in lines[i]:
            ans = ans+f'{i+1} '
    if(ans == ''):
        ans = "HE GOT AWAY!"
    return ans

def test():
    assert solution(['FBI1','NOTCIA','NOTFBI','STUFF','MORESTUFF']) == '1 3 '
    assert solution(['','','','','']) == 'HE GOT AWAY!'
    assert solution(['BALLOON','NOTCIAFBI','NOTFBI','STUFF','MOREFBISTUFF']) == '2 3 5 '
    print("All tests passed!", file=sys.stderr)


def main():
    lines = []
    for _ in range(5):
        line = input()
        lines.append(line)
    
    ans=solution(lines)
    print(ans)

if __name__ == '__main__':
    test()
    main()
