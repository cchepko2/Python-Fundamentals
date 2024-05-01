card1 = '''
=======
|     |
|  A  |
|     |
=======
'''
card2 = '''
=======
|     |
|  X  |
|     |
=======
'''

def print_cards(card_str_lst, sep_str):
    prt_lst = []
    for card in card_str_lst:
        lines = card.split('\n')
        height = len(lines)
        prt_lst.append(lines)
    #print(prt_lst)
    for h in range(height):
        for card in prt_lst:
            print(card[h], end=sep_str)
        print()

print_cards([card1, card2], ' \t ')


#for i in range(len(card1_lines)):
#    print(card1_lines[i], card2_lines[i])