############################################
#TESTE COM VALORES REAIS E FIXOS FUNCIONANDO 
############################################

# %% teste LLS 6 anos
import matplotlib.pyplot as plt
import numpy as np
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

acrit = 4 
leaf_age = [acrit / 2, acrit / 2 * 2, acrit / 2 * 3]  #years
print(leaf_age)
print("\n")

print("folhas jovens")
u = -0.4              #umol CO2 m2 S-1  
acrit = 4            #year
a = 0.5             #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1            #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 4         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1.9            #year
print (fa(u,acrit,a))
print("\n")

print("folhas maduras")
u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 3            #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 4            #year
print (fa(u,acrit,a))
print("\n")

print("folhas velhas")
u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 4.5            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 6            #year
print (fa(u,acrit,a))
print("\n")

print ("folhas morreram")


# %% teste LLS 3 anos

import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

acrit = 2
leaf_age = [acrit / 2, acrit / 2 * 2, acrit / 2 * 3]  #years
print(leaf_age)

print("\n")

print("folhas jovens")
u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.3           #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.5           #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.7           #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 2         #year
a = 0.9            #year
print (fa(u,acrit,a))
print("\n")

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 2            #year
print (fa(u,acrit,a))
print("\n")

print("folhas velhas")
u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.3          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.7          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 3            #year
print (fa(u,acrit,a))

print ("folhas morreram")


# %% LLS 6 acrit 4 com médias de 'a'

import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))
    
u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1            #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 3            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5            #year
print (fa(u,acrit,a))

# %% LLS 3 acrit 2 com médias de 'a'

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.5           #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.5          #year
print (fa(u,acrit,a))





####################################################
#TESTE CASO VALORES FOSSSEM DE 0 A 1 POR COEFICIENTE
####################################################
# %% teste coef
import math
import numpy as np 

def fa(u, acrit, a):
    return min(1,math.exp(u*(acrit-a)))

def value_recalc(rest_time):
    return 0.03 * rest_time

u = 30   
a = 3     
acrit = 4

value_recalc(u) 
print(value_recalc(u))

value_recalc(acrit)
print(value_recalc(acrit))

value_recalc(a)
print(value_recalc(a))

print(fa(value_recalc(u), value_recalc(acrit), value_recalc(a)))





############################################
#TESTE CASO VALORES FOSSEM DE 0 A 1 "NA MÃO"
############################################
# %% teste velho com valores de u e 'a' definidos para testar o acrit
#confirmado q tem que ser inversamente proporcional

import math
def fa(u, acrit, a):
    return min(1,math.exp(u*(acrit-a)))

u = 0.4
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 1

print (fa(u, acrit, a))

u = 0.4
acrit = 0.2 #idade 2 anos (LLS=3) num range de 0 a 10
a = 1

print (fa(u, acrit, a))

# %% teste com valores de u e acrit definidos para testar o 'a'
import math
def fa(u, acrit, a):
    return min(1,math.exp(u*(acrit-a)))

#teste jovem
u = 0.6
acrit = 0.4
a = 2

print (fa(u, acrit, a))

#teste maduro
u = 0
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 0

print (fa(u, acrit, a))

#teste velho
u = 0.4
acrit = 0.4
a = 1

print (fa(u, acrit, a))

# %% teste com valores de acrit e 'a' definidos para testar a ordem do u
#tem que ser inversamente proporcional também pelo visto 
#então o 0.6 vai pra jovem e o 0.4 para velho e maduro vai para 0... ??

import math
def fa(u, acrit, a):
    return min(1,math.exp(u*(acrit-a)))

# u jovem sendo 0.6
u = 0.6
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 2

print (fa(u, acrit, a))

# u jovem sendo 0.4
u = 0.4
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 2

print (fa(u, acrit, a))
print("\n")
# u maduro sendo 0 
u = 0
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 2 #alterando para 2 só para ver o resultado

print (fa(u, acrit, a))

#u maduro sendo 1 
u = 1
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 2 

print (fa(u, acrit, a))

# u velho sendo 0.4 
u = 0.4
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 1 #alterando para 2 só para ver o resultado

print (fa(u, acrit, a))

#u maduro sendo 0.6 
u = 0.6
acrit = 0.4 #idade 4 anos (LLS=6) num range de 0 a 10
a = 1 

print (fa(u, acrit, a))

# %% teste com vcmax em photons
import math
def fa(u, acrit, a):
    return min(1,math.exp(u*(acrit-a)))
    
#não vale a pena 
# u jovem sendo 0.6
u = 0.0100
acrit = 0.7 #idade de 3 anos num range de 0 a 10
a = 2

print (fa(u, acrit, a))

# u jovem sendo 0.4
u = 0.0256
acrit = 0.7 #idade de 3 anos num range de 0 a 10
a = 2

print (fa(u, acrit, a))


#a_crit = np.linspace(start = 0.1, stop = 8.3, num = 100)