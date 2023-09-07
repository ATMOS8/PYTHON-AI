#proj1.py
Learned to write any sample string and print it by skipping vovels by five ways
1) if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" :
       a+=x
   using the above statement as many number of times as many strings used and then        printing the new string
2) for x in s :
   using the above for statement and then using the if statement in the 1st way
3) using "if x not in "aeiouAEIOU":" statement in the above "for" statement
4) a = "".join([x for x in s if x != "a" and x != "e" and x != "i" and x != "o" and x     != "u"])
   using '"".join' statement
5) a = "".join([x for x in s if x not in "aeiouAEIOU"])
   using the '"".join' statement for 'x for x in s if x not in "aeiouAEIOU"'
