v=[1300,1100,2000,1700,1900,1500,1800]
ziua=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
print("Venit saptamanal= ",sum(v))
print("Media venitului zilnic= ",round(sum(v)/7,2))
print("Ziua cu cel mai mare profit= ",ziua[v.index(max(v))])
print("Ziua cu cel mai mic profit= ",ziua[v.index(min(v))])