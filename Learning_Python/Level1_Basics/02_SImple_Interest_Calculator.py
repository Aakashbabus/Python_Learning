## simple intereste is calculated as P*T*R/100

P=input("enter the Principal P: ")
P= int(P)
T=input("enter the Time period in years T: ")
T= int(T)
R=input("enter the Rate of interest per annum R: ")
R= int(R)

SI = P*T*R /100

print('Maturity Amount is : ',SI+P)
print('Simple Interest is : ',SI)