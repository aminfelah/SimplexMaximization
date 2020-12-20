print("******Application Simplex maximization******")
print("Ecrire start pour commencer a entrer les coefficients des variables ")
print("Ecrire next pour se deplacer vers une nouvelle contrainte")
print("appuiyer sur Enter pour donner un nouveau coefficient")
print("Ecrire end pour soumettre les equation")
TableauSimplex = []
VariableEntree = []
PositionPivot = []

def EntrerDonnee(TableauSimplex):
    x = input()
    if x == 'start':
        row = []
        print("Veuillez Saisir La Fonction objectif")
        x = input()
        while x != "next":
            row.append(x)
            x = input()

        print("la fonction objectiv est :", row)
    print("La Fonction objectif est Terminee")
    print("Veuillez Envoyer Les Fonctions contraintes")
    while x != "end":

        while x != "next":
            row.append(x)
            x = input()
        TableauSimplex.append(row)
        row = []
        print("Ajouter une Autre contrainte ?")
        x = input()


def creationMatrice(TableauSimplex):
    for i in range(len(TableauSimplex) - 1):
        TableauSimplex[0].append(0)
        for j in range(len(TableauSimplex) - 1):
            if (i + 1 == j + 1):
                TableauSimplex[i + 1].append(1)
            else:
                TableauSimplex[i + 1].append(0)
    LastRow = []
    for i in range(len(TableauSimplex[0])+1):
        LastRow.append(0)
    TableauSimplex.append(LastRow)
    TableauSimplex.append(TableauSimplex[0])
    TableauSimplex[-1].append(0)

    for j in range(len(TableauSimplex)):
        TableauSimplex[j] = [float(i) for i in TableauSimplex[j]]
    for i in range(len(TableauSimplex) - 3):
        VariableEntree.append(0)
        PositionPivot.append(0)


def CalculSimplex(TableauSimplex):
    for i in range(len(TableauSimplex) - 3):
        TableauSimplex[i + 1].append(-1)
    row = []
    pos_x=TableauSimplex[len(TableauSimplex)-1].index(max(TableauSimplex[len(TableauSimplex) - 1]))

    for i in range(len(TableauSimplex) - 3):
        if TableauSimplex[i + 1][TableauSimplex[len(TableauSimplex) - 1].index(max(TableauSimplex[len(TableauSimplex) - 1]))] > 0:
            TableauSimplex[i + 1][len(TableauSimplex[i + 1]) - 1] = TableauSimplex[i + 1][-len(TableauSimplex) + 1] / TableauSimplex[i + 1][
                TableauSimplex[len(TableauSimplex) - 1].index(max(TableauSimplex[len(TableauSimplex) - 1]))]
        else:
            TableauSimplex[i + 1][len(TableauSimplex[i + 1]) - 1] = 999999999
        row.append(TableauSimplex[i+1][len(TableauSimplex[i+1])-1])
    pos_y=row.index(min(row))

    for i in range(len(TableauSimplex) - 3):
        TableauSimplex[i + 1].pop()
    TableauSimplex[pos_y+1] = [x / TableauSimplex[pos_y+1][pos_x]  for x in TableauSimplex[pos_y+1]]
    for i in range(len(TableauSimplex) - 3):
        if i+1 != pos_y+1 and TableauSimplex[i+1][pos_x]!=0:
            TableauSimplex[i+1] = [x / TableauSimplex[i+1][pos_x] for x in TableauSimplex[i+1]]
            TableauSimplex[i+1] = [x1 - x2 for (x1, x2) in zip(TableauSimplex[i+1], TableauSimplex[pos_y+1])]
    VariableEntree[pos_y] = TableauSimplex[0][pos_x]
    PositionPivot[pos_y] = pos_x
    for i in range(len(VariableEntree)):
        if VariableEntree[i]!=0:
            TableauSimplex[i+1] = [x / TableauSimplex[i+1][PositionPivot[i]] for x in TableauSimplex[i+1]]

    for i in range(len(TableauSimplex[-2])):
        sum = 0
        for j in range(len(VariableEntree)):
           sum += VariableEntree[j]* TableauSimplex[j+1][i]
        TableauSimplex[-2][i]=sum
    TableauSimplex[-1] = [x1 - x2 for (x1, x2) in zip(TableauSimplex[0], TableauSimplex[-2])]

    return TableauSimplex

def BoucleSimplex(TableauSimplex):
    for i in range(len(TableauSimplex[-1])):
        if TableauSimplex[-1][i]> 0:
            return True
    return False

def AfficheResults(TableauSimplex):
    i=1
    for j in range (len(VariableEntree)):
        if VariableEntree[j]!= 0:
            print("La valeur de X",i, " est ",TableauSimplex[j+1][-(len(TableauSimplex)-2)])
            i=i+1
    print("La valeur maximale est ",TableauSimplex[-2][-(len(TableauSimplex)-2)])






EntrerDonnee(TableauSimplex)
creationMatrice(TableauSimplex)
print(TableauSimplex)
while BoucleSimplex(TableauSimplex):
    TableauSimplex = CalculSimplex(TableauSimplex)
    print(TableauSimplex)

AfficheResults(TableauSimplex)
