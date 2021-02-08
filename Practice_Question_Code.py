# Priyadarshan Ghosh
import os
import random

files = os.listdir('Input_Files/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-3]

def solve(m,t2,t3,t4,ing,shuff):
    i,score = 0, 0

    random.shuffle(shuff)
    
    tt,ttt,tttt = [],[],[]

    while i < m:

        if i+2 <= m and t2 > 0:
            t2 -= 2 
            tt.append([shuff[i],shuff[i+1]]) 
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]])) 
            i += 2
        
        elif i+3 <= m and t3 > 0:
            t3 -= 3
            ttt.append([shuff[i],shuff[i+1],shuff[i+2]])
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]]+ing[shuff[i+2]]))
            i += 3
        
        elif i+4 <= m and t4 > 0:
            t4 -= 4
            tttt.append([shuff[i],shuff[i+1],shuff[i+2],shuff[i+3]])
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]]+ing[shuff[i+2]]+ing[shuff[i+3]]))
            i += 4
 
        else:
            break

        score += ss**2

    return len(tt),len(ttt),len(tttt),tt,ttt,tttt,score 

for i in range(l):

    with open('Input_Files/'+files[i]+'.in', 'r') as f:

        content = f.readlines()
        ingredients = []
        m, t2, t3, t4 = [int(x) for x in content[0].split()]
        for j in range(1,m+1):

            ingredient = content[j].split()[1:]
            ingredients.append((ingredient))
    
    bestscore = 0
    besttwo,bestthree,bestfour = [],[],[]
    vals = list(range(m))

    for _ in range(10000):
        l2,l3,l4,two,three,four,score = solve(m,2*t2,3*t3,4*t4,ingredients,vals)
 
        if score > bestscore:
            bestscore,besttwo,bestthree,bestfour = score,two,three,four

    with open('Output_Files/'+files[i]+'.out', 'w') as f:
        f.write(str(l2+l3+l4)+'\n')
        
        for ii in range(l2):
            f.write('2 ')
            for j in range(2):
                f.write(str(besttwo[ii][j])+' ')
            f.write('\n')
        for ii in range(l3):
            f.write('3 ')
            for j in range(3):
                f.write(str(bestthree[ii][j])+' ')
            f.write('\n')
        for ii in range(l4):
            f.write('4 ')
            for j in range(4):
                f.write(str(bestfour[ii][j])+' ')
            f.write('\n')
    
    
    print("Done ",files[i],"\nScore :",bestscore)
 
print("All Output Done")


