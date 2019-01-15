#def remove_ch(s):
   # res = ''
   # punc = '#!;)/{}'
  #  for character in s:

       # if character not in punc:
           # res = res + character
   # return res

#a = '#csc280!isfun;)/{}'
#print(remove_ch(a))



#def amendthesentence(s):
    #x = ''
    #for i in s:
       # if i.isupper():
       #     x += ' {}'.format(i.lower())
      #  else:
      #      x += i
    #return x.strip()
#print(amendthesentence("CodeSignalIsAwesome"))



def lowerupper(l):
    x = ''
    for i in l:
        if i.isupper():
            x += (i.lower())
        else:

            if i.lower():
                x += (i.upper())
    return x.strip()
print(lowerupper("cscIS"))