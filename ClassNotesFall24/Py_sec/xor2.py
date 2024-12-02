import base64
from Crypto.Util.number import *

KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG_KEY1_KEY3_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
ans = bytes.fromhex(KEY1)
ans2_3 = bytes.fromhex(KEY2_KEY3)

ans_lst = []
for byte in ans:
    ans_lst.append(byte)

ans_lst2_3 = []
for byte in ans2_3:
    ans_lst2_3.append(byte)

or_list = []
for i in range(len(ans)):
    or_list.append(ans_lst[i] ^ ans2_3[i])

all_or_list = []
for byte in bytes.fromhex(FLAG_KEY1_KEY3_KEY2):
    all_or_list.append(byte)

sol_lst = []
for i in range(len(all_or_list)):
    sol_lst.append(chr(all_or_list[i] ^ or_list[i]))

print(''.join(sol_lst))





