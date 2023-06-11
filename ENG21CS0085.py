#HARSHYARA BUKKAPATNAM
#ENG21CS0085
#Satisfaction function 2
#proportional-greedy rule
#dataset: poland_warszawa_2021_srodmiescie.pb
import pandas as pd
import math
vf=pd.read_csv("VOTESagt.csv")
pf=pd.read_csv("PROJECTSagt.csv")
m=51 #no.of projects
n=4092 #no.of voters
mi=1  #minimum votes
ma=15 #maximum votes
l=3823123 #budget alloctaed
util=dict() #to store utilities
B=set() #Outcome set
B.add(0) 
C=set() 
y=list()
vdt=dict() #dictionary in the format {voter_id:[...voted projects...]}
pdt=dict() #dictionary in the format {project_id:[cost]}
vdictf = vf.to_dict(orient='list')
pdictf = pf.to_dict(orient='list')
for i in range(m):
    x=pdictf['project_id'][i]
    z=pdictf['cost'][i]
    pdt[x]=z
A=list(pdt.keys())#list with all project_id s
for i in range(n):
    x=vdictf['voter_id'][i]
    for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']:
        z=vdictf[j][i]
        y.append(z)
    vdt[x]=y
    y=[]
av=list(vdt.values()) #list containing list of votes of each voter as a set
vid=list(vdt.keys()) #list containing voter_id s
for x in vdt.values():
    for i in range(15):
        if math.isnan(x[i]):
            x[i] = 0 
def totalcost(B): #function to calculate total cost of the set
    b=list(B)
    cos=0
    if len(b)==1:
        return 0
    for i in b:
        cos+=pdt[i]
    return cos
def maxutil(a): #function to calculate project with maximum utilty to add it to B
    max_value= max(a.values())
    for key, value in a.items():
        if value == max_value:
            return key
def f(Av,B): #Second Satisfaction function
    cost=0
    D=set(Av)
    Bv=D.intersection(B)
    b=list(Bv)
    if len(Bv)==1:
        return 0
    for i in Bv:
        cost+=pdt[i]
    return cost
def pgrule(): #Function for proportional-greedy rule
    for i in A:
        C=B.copy()
        for j in range(n):
            k=(f(av[j],C.add(i))-f(av[j],B))/pdt[i]
            tot+=k
        C.clear()
        util[i]=tot
    B.add(maxutil(util))
while(totalcost(B)<=l):
    pgrule() #Loop to calculate outcome set till budget limit
print("Final set:\n",B)
print("Utility of each Project:\n",util)
voter_util=dict()
tota=0
for j in range(n) and i in vid: #loop to calculate total utility of each voter
    for k in av[j]:
        tota+=util['k']
    voter_util[i]=tota
print("Utility of each Voter:\n",voter_util)