x=[1,4,-2,7,3]
y=x
produs=1
for i in range(0,len(x)):
    produs*=x[i]
print("Suma primelor 3 componente ale lui x= ",x[0]+x[1]+x[2])
print("Suma componentelor variabilei y= ",sum(y))
print("Produsul componentelor variabilei x= ",produs)
print("Valoarea absoluta a componentei a 3-a a variabilei y= ",abs(y[2]))
print("Suma primelor componente ale variabilelor x si y",x[0]+y[0])
