
from math import sqrt

def info():
    print("""\nWelcome to my console! \nThe commands for the complex numbers are:
    add        - add number to the list
    show       - to see all the numbers
    print      - to see a specific number from the list
    modify     - to modify a specific number from the list
    delete     - delete a number from the list
    delete all - delete all the numbers from the list
    P2         - to display the longest sequence with the property 2
    P3         - to display the longest sequence with the property 3
    P11        - to display the longest sequence with the property 11 
    exit       - to close the application
    info       - show this information again.\n""")


def get_real(c):      #basic 'getter'
     #return c[0]
     return c[0]
        #return c["re"]

def set_real(c,val):   #basic 'setter'
        #c[0]=val
     c=(val,c[1])
        #c["re"]=val

def get_imag(c):
        #return c[1]
     return c[1]
        #return c["im"]

def set_imag(c,val):
        #c[1]=val
     c=(c[0],val)
        #c["im"]=val

        
def valid_add(s): #checks if the input is an integer
    x = input(s)
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            if x == "exit": exit()
            print("non-numerical value!")
            x = input(s)


def read_complexNr(): #read a complex number from the console
    re = valid_add("Real part: ")
    im = valid_add("Imaginary part: ")
    return (re,im)
  
    
def modify_nr(l): #setter
    print("Insert the number you want to modify:")
    x = read_complexNr()
    if x not in l: print("This number is not in the list, try again."); return
    print("Insert the new number: ")
    newValue = read_complexNr()
    l[l.index(x)] = newValue
    
   
def add_nr(l): #add number to the list from the console
    print("{}.".format(len(l)+1),end = ' ')
    l.append(read_complexNr())


def delete_nr(l): #delete a specific number from the list
    x = valid_add("Insert the index of the number you want to delete: ")
    if x in range(1,len(l)+1):
        l.pop(x-1)
    else: print("The list has no number at this index, try again.")

    
def print_nr_format(nr): #prints the tuple in a complex number format
    if nr[1]>=0:
            print("{}+{}i".format(nr[0],nr[1]))
    else: print("{}{}i".format(nr[0],nr[1]))


def print_nrs(l): #prints all the numbers
    n = len(l)
    if not n: print("There are no numbers in the list."); return
    d = len(str(n))
    print("Index    Complex Number \n-----------------------")
    for i in range(0,n):
        print("{}.".format(i+1),end = " "*(7+d-len(str(i+1))))    
        print_nr_format(l[i])


def print_specificNR(l,index): #prints a specific number from the list, works as a getter
        if index < 1 or index > len(l):
            print("The list has no number at this index, try again.")
            return
        print_nr_format(l[index-1])


def compute_modulus(x):
    return sqrt(x[0]*x[0]+x[1]*x[1])


def prop2(l): #computes the longest seqence of numbers that contains at most 3 distinct values
    n = len(l)
    if not n : print("There are no numbers in the list."); return
    values = []                                                         # the list that contains the distinct values
    pMax=0; cl=0; maxl=0;                                               # the posiiton of the longest sequnce, the current length and the max length are initialized to 0
    for i in range(0,n-1):
        ok = 0
        for j in range(i,n):                                            # we iterate over all the complex numbers
                if l[j] not in values:
                         values.append(l[j])                            # we add the distinct values
                if len(values)<=3:                                      # if there are more than 3 distinct numbers, we evaluate the sequence up till that point
                            cl+=1
                else:
                        if cl>maxl:
                            maxl = cl
                            pMax = j
                        break
                if j==n-1 and cl>maxl: ok = 1
        if ok:
            pMax = n
            maxl = cl
            break
        cl = 0
        values.clear()
    print_nrs(l[pMax-maxl:pMax])                                        # print the longest sequence
    

def prop3(l): #computes the longest sequence of numbers with the same modulus
    n = len(l)
    if not n : print("There are no numbers in the list."); return
    mod = compute_modulus(l[0])
    j = 1
    cl = 1
    maxl = 1
    for i in range(1,n):
        modc = compute_modulus(l[i])
        if modc==mod:
            cl+=1
        else:
            if cl>maxl:
                maxl = cl
                j = i
            cl = 1
            mod = modc
    if cl>maxl:
        maxl = cl
        j = n
    print_nrs(l[j-maxl:j])
              

def prop11(l):
    n = len(l)
    if not n : print("There are no numbers in the list."); return
    poz_max = 0
    cl = 1
    maxl = 0
    ok1 = 0 ; ok2 = 0
    for i in range(0,n-1):
          if l[i][0]<l[i+1][0] and ok2!=1:
               cl+=1; ok1=1
          elif ok1 and l[i][0]>l[i+1][0]:
               cl+=1; ok2=1
          else: 
            if cl>maxl and ok1==1 and ok2==1:
                maxl = cl
                poz_max = i
            cl = 1
            ok1=0; ok2=0
            
    if cl>maxl and ok1==1 and ok2==1:
                maxl = cl
                poz_max = n-1
    if maxl<3 : print("No MOUNTAIN"); return
    print_nrs(l[poz_max-maxl+1:poz_max+1])
     

#the MAIN
def my_console ():
    list_c = [(10,3),(6,3),(1,6),(1,-6),(1,3),(1,-7),(2,1),(4,-12),(1,0),(4,7),(4,7),(4,4),(4,7),(4,7),(4,4),(1,1),(1,1),(1,1)]
    commands = {
        "add": add_nr,
        "delete": delete_nr,
        "modify": modify_nr,
        "show": print_nrs,
        "P2": prop2,
        "P3": prop3,
        "P11": prop11
        }
    info()
    while True:
        cmd = input("SCM\Console>")
        if cmd == "exit":
            exit()
        elif cmd in commands:
            commands[cmd](list_c)
        elif cmd == "print": #getter
            print_specificNR(list_c,valid_add("Type the index of the number (starting from 1): "))
        elif cmd == "delete all":
            list_c.clear()
        elif cmd == "info": info()
        else: print("invalid command")
    

my_console()
        
