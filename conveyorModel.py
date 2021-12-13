import math
import random
import matplotlib.pyplot as plt

cl=[]
v = float(input("qual a velocidade da esteria? (1, 2 ou 3) "))
temp = float(input("qual a temperatura? "))
c = float(input("Qual a concentração do lubrificante (entre 0.1 e 1) "))

c = c*0.9
Aini = z = 0.28
Amin = 0.15
i = v*temp/110
consumo = 0


for n in range(0,3):
  ton= int(input("qual o tempo on em segundos? "))
  toff= int(input("qual o tempo off em segundos? "))
  ttotal = 200
  n = round(ttotal/(ton + toff))
  consumo = consumo + ton*n*c*10/0.9

  for n in range(0,n):
    for t in range(0,ton):
      x=round(random.uniform(0.95,1.05), 3)
      if c == i:
        i = i*x
      t=t/10
      z = Aini - (c-i)*t
      if z >= Amin:
        z=z*x
        cl.append(z)
      else:
        z = Amin*x
        cl.append(z)

    afin = z

    for t in range(0,toff):
      x=round(random.uniform(0.95,1.05), 3)
      if c == i:
        i = i*x
      t=t/60
      z = afin 
      if z <= Aini:
        z=z + i*t
        z=z*x
        cl.append(z)
      else:
        z = Aini*x
        cl.append(z)
    Aini = z

  plt.figure(figsize=(6, 3))
  plt.plot(cl)
  plt.show()

  print("\n seu modelo consumiu " + str(consumo) + " mls do produto até agora. \n")
