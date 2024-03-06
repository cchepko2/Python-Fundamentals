fname = "Corin"
lname = "Chepko"
grade = 74.5656

something = "{:>10}{:<15}{:^10.1f}".format(fname, lname, grade)

art0 = '''
     |\_/|          	*****************************    	   (\_/)
    /  @  @ \      	*                   ASCII Lab   *  	      (='.'=)
'''
art1 = '''
    >>x<<        	*                     CSCI 110              *
   /   O  \       	*****************************
   '''
art_name = '''( >   0  <   )       *{:^29}* 	( " )_( " )'''
art_name_left = '''( >   0  <   )       *{:<29}* 	( " )_( " )'''.format(fname+' '+lname)
art_name_right = '''( >   0  <   )       *{:>29}* 	( " )_( " )'''.format(fname+' '+lname)

art_name_f = f'''( >   0  <   )       *{fname:^29}* 	( " )_( " )'''

print(something)

print(art0)#, art1, sep='\n')
print(art_name.format(fname+' '+lname))
print(art_name_f)
print(art_name_left)
print(art_name_right)
print(art1)

pali = input("Give me a word to check if it's a palindrome.")

if(pali.lower() == pali[::-1].lower()):
    print("It's a palindrome!")
else:
    print("Not a palindrome")