#####workedwithLauren
########Problem1

s_word = 'exercise'

def letter_extractor():
    index = len(s_word) - 1
    while index >= 0:
        letter = s_word[index]
        print(letter)

        index = index - 2

letter_extractor()  #make sure to call the function


########Problem2

inp = input('Input the text you want to encrypt:\n')
inp = inp.lower()

key = int(input('Input the key you want to use from 1 to 26:\n'))
def encrypt(input,key): #Function to code a text with caeser cypher.
    if key > 25:
        key = 25
    elif key < 2:
        key = 2
    finaltext = ''
    for letter in input:
        if letter.isalpha():
            num = ord(letter)
            if (num + key) > 122:
                x = (num + key) - 122
                finaltext += chr(x + ord('a') - 1)
            elif((num + key <= 122)):
                finaltext += chr(num + key)
        else:
            finaltext += letter
    print(finaltext)


encrypt(inp,key)


#######Problem3

import collections

freq = collections.Counter("abcb")
for k in freq:
    if freq[k] > 1:
        print(k) # prints "a"
        break
print(-1)


#######Problem4

#use the above line when you are using NON ASCII characters..
s_word = 'https:// www.a©meri can.edu/ ® trademark/€'

s_word = list(s_word)
index = len(s_word) - 1
while index >= 0:
    #letter = s_word[index]
    #print s_word[index]
    if 0 <= ord(s_word[index]) <= 127:
        pass
        #print 'test2'
    else:
        #print 'test'
        s_word[index] = '%C3'
        #s_word[index] = ''.join(s_word[index])
        # print s_word[index]
        #print s_word
    if s_word[index] == ' ':
        #print s_word[index]
        s_word[index] = '+'
        #s_word[index] = ''.join(s_word[index])
    else:
        pass
    # print letter
    index = index - 1

#print s_word
print(''.join(s_word))
#print(s_word)


#########Problem5

string = input("Please enter your own String : ")
flag = 0

length = len(string)
for i in range(length):
    if(string[i] != string[length - i - 1]):
        flag = 1
        break

if(flag == 0):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")


#########Problem6
print('{:12}{:12}{:^12}{:^15}'.format('Name', 'Lastname', 'ID Number', 'Balance'))
print('{:12}{:12}{:^12}{:>12}'.format('Andreas', 'Lokovic', '12345678901', '120456.79'))
print('{:12}{:12}{:^12}{:>12}'.format('Alexandre', 'Whitewash', '456732', '34045.45'))
print('{:12}{:12}{:^12}{:>12}'.format('Montgomery', 'Zappaterra', '23', '3051.34'))


#########Problem7

phrase = ("Please Enter A Phrase: ")
p_replaced = phrase.replace(" ", "_")
print (p_replaced)
phrase = ("Please Enter A Phrase: ")
cap_phrase = phrase.title()
p_replaced = cap_phrase.replace(" ", "_")
print (p_replaced)


#########Problem8

def digitstrip():

    numLen= 4
    stringdigit= ['em1234', 'me4567', 'gr5678', 'bf4567']
    for i in stringdigit:
        print(i[:-numLen])

digitstrip()