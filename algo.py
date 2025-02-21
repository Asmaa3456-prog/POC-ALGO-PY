##
#  Créez un programme qui crée et initialise un tableau, puis inversez ce tableau sans utiliser un tableau supplémentaire.#

tables = int(input("Saisir le nombre d elements : "))
table=[0]*(tables)

for i in range (tables):
        table[i]=int(input("donner lesnombres  : "))
        index1=0
        index2=tables-1
while (index1<index2 ):
        ex = table[index1]
        table[index1] = table[index2]
        table[index2] = ex
        index1+=1
        index2-=1
for i in range(tables):
      print("le table inverse",table[i])

