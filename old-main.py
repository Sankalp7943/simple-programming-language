'''
PRINT
WHILE
FOR
ADD
TO
FROM
if else, else if
WHAT IS
SAY for printing
stack(put on top), print stack
queue Put in queue
debugging

for age 6-12.
Contribute for more interactive additions
help us raise money to provide the facilities to the unfortunate kids in our country who lack basic health and education

gate xor etc

play with string

dictionaries

linked list= connect and disconnect

variable
output with tkinter with smart squirtle or a puppy

OOPS there is a mistake somewhere, can you help me find out

sound when done well,, daily small problem. tells you about datastructures and algorithm

Very good.

Tell us your name







". "
variable description
'''
#x = txt.split(", ")
#program= code file

program= 'ADD 50 TO 32. ADD 10 TO 5. SUB 4 FROM 2.'


keywords={}

#keywords['ADD']=add

program_list= program.split(". ")
program_list[-1]=program_list[-1][0:len(program_list[-1])-1]
#print(program_list)
for _ in program_list:
     tokens=str(_).split(" ")
     #print(tokens)
     if 'ADD' in tokens:
          idx=tokens.index('TO')
          ans=(float(tokens[idx-1])+float(tokens[idx+1]))
          if float(ans)==int(ans):
               print(int(ans))
          else:
               print(float(ans))
     elif 'SUB' in tokens:
          idx=tokens.index('FROM')
          ans=(float(tokens[idx+1])-float(tokens[idx-1]))
          if float(ans)==int(ans):
               print(int(ans))
          else:
               print(float(ans))
                

