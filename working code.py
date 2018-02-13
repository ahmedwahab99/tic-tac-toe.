grid=["a","b","c","d","e","f","g","h","i"]
print(grid[0],"|",grid[1],"|",grid[2])
print("----------")
print(grid[3],"|",grid[4],"|",grid[5])
print("----------")
print(grid[6],"|",grid[7],"|",grid[8])

counter=0
while True:   
    if counter%2==0: #player 1
        p1=int(input("Enter odd number:"))

        while (p1%2==0): 
            p1=int(input("That wasnt an odd number, try again:"))

        while (p1 in grid):
            p1=int(input("Number is taken, choose another number"))

        s1=input("Enter spot")
        while True:
            
            if s1 in grid:
                if(s1 == "a"):
                    x=0
                elif (s1 == "b"):
                    x=1 
                elif (s1 == "c"):
                    x=2
                elif (s1 == "d"):
                    x=3    
                elif (s1 == "e"):
                    x=4
                elif (s1 == "f"):
                    x=5
                elif (s1 == "g"):
                    x=6
                elif (s1 == "h"):
                    x=7
                elif (s1 == "i"):
                    x=8
                break    
            else:
        
                print ("Spot doesnt exist or taken")
                s1=input("Try another spot:")

        while grid[x]!=s1:
            
            s1=input("Enter spot:")
            if(s1 == "a"):
                x=0
            elif (s1 == "b"):
                x=1
            elif (s1 == "c"):
                x=2
            elif (s1 == "d"):
                x=3    
            elif (s1 == "e"):
                x=4
            elif (s1 == "f"):
                x=5
            elif (s1 == "g"):
                x=6
            elif (s1 == "h"):
                x=7
            elif (s1 == "i"):
                x=8

        grid[grid.index(s1)]=p1  # grid[x]= p1 or replace
        print(grid[0],"|",grid[1],"|",grid[2])
        print("----------")
        print(grid[3],"|",grid[4],"|",grid[5])
        print("----------")
        print(grid[6],"|",grid[7],"|",grid[8])
        
        if (grid[0]!="a" and grid[1]!="b" and grid[2]!="c"):
           if(grid[0]+grid[1]+grid[2]==15):
              break
        elif(grid[3]!="d" and grid[4]!="e" and grid[5]!="f"):
           if(grid[3]+grid[4]+grid[5]==15):
              break
        elif(grid[6]!="g" and grid[7]!="h" and grid[8]!="i"):
           if(grid[6]+grid[7]+grid[8]==15):
              break
        elif(grid[0]!="a" and grid[3]!="d" and grid[6]!="g"):
           if(grid[0]+grid[3]+grid[6]==15):
              break
        elif(grid[1]!="b" and grid[4]!="e" and grid[7]!="h"):
           if(grid[1]+grid[4]+grid[7]==15):
              break
        elif(grid[2]!="c" and grid[5]!="f" and grid[8]!="i"):
           if(grid[2]+grid[5]+grid[8]==15):
              break
        elif(grid[0]!="a" and grid[4]!="e" and grid[8]!="i"):
           if(grid[0]+grid[4]+grid[8]==15):
              break
        elif(grid[2]!="c" and grid[4]!="e" and grid[6]!="g"):
           if(grid[2]+grid[4]+grid[6]==15):
              break 


    if counter%2!=0: #player 2
        p2=int(input("Enter even number"))

        while (p2%2!=0): 
            p2=int(input("That was not an even number, try again:"))

        while (p2 in grid):
            p2=int(input("Number is taken, choose another number"))

        s2=input("Enter spot")
        while True:
            
            if s2 in grid:
                
                if(s2 == "a"):
                    x=0
                elif (s2 == "b"):
                    x=1 
                elif (s2 == "c"):
                    x=2
                elif (s2 == "d"):
                    x=3    
                elif (s2 == "e"):
                    x=4
                elif (s2 == "f"):
                    x=5
                elif (s2 == "g"):
                    x=6
                elif (s2 == "h"):
                    x=7
                elif (s2 == "i"):
                    x=8
                break    
            else:
        
                print ("Spot doesnt exist or taken")
                s2=input("Try another spot")
       
        while grid[x]!=s2:
            
            s2=input("Enter spot")
            if(s2 == "a"):
                x=0
            elif (s2 == "b"):
                x=1
            elif (s2 == "c"):
                x=2
            elif (s2 == "d"):
                x=3    
            elif (s2 == "e"):
                x=4
            elif (s2 == "f"):
                x=5
            elif (s2 == "g"):
                x=6
            elif (s2 == "h"):
                x=7
            elif (s2 == "i"):
                x=8
        grid[grid.index(s2)]=p2
        print(grid[0],"|",grid[1],"|",grid[2])
        print("----------")
        print(grid[3],"|",grid[4],"|",grid[5])
        print("----------")
        print(grid[6],"|",grid[7],"|",grid[8])

        if (grid[0]!="a" and grid[1]!="b" and grid[2]!="c"):
           if(grid[0]+grid[1]+grid[2]==15):
              break
        elif(grid[3]!="d" and grid[4]!="e" and grid[5]!="f"):
           if(grid[3]+grid[4]+grid[5]==15):
              break
        elif(grid[6]!="g" and grid[7]!="h" and grid[8]!="i"):
           if(grid[6]+grid[7]+grid[8]==15):
              break
        elif(grid[0]!="a" and grid[3]!="d" and grid[6]!="g"):
           if(grid[0]+grid[3]+grid[6]==15):
              break
        elif(grid[1]!="b" and grid[4]!="e" and grid[7]!="h"):
           if(grid[1]+grid[4]+grid[7]==15):
              break
        elif(grid[2]!="c" and grid[5]!="f" and grid[8]!="i"):
           if(grid[2]+grid[5]+grid[8]==15):
              break
        elif(grid[0]!="a" and grid[4]!="e" and grid[8]!="i"):
           if(grid[0]+grid[4]+grid[8]==15):
              break
        elif(grid[2]!="c" and grid[4]!="e" and grid[6]!="g"):
           if(grid[2]+grid[4]+grid[6]==15):
              break 
    counter=counter+1      

if counter%2==0:
    print ("congrats player 1, you won")
       
elif counter%2!=0:
    print ("congrats player 2, you won")
        













