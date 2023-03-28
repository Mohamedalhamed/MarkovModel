import sys
class Cellule:
    def __init__(self, nb, stat):
        self.nb = nb
        self.stat = stat

def afficheSeparateur(n, deb_ligne):
    # Tabulation before each line for column titles
    for i in range(deb_ligne):
        print(" ", end='')
    for i in range(n):
        print("+-------------------", end='')
    print("+")


def afficheTab(tab, col, ligne):
    print("\n" + "=" * 50)
    print("TRANSITION PROBABILITIES:\n\n")

    # Display column headers
    print("FROM PAGE".ljust(15), end="")
    for i in range(col - 1):
        print(f"TO PAGE {i}".ljust(18), end="")
    print(f"TO PAGE TOT".ljust(17))

    # Display row headers and cells
    for i in range(ligne):
        print(f"Page {i}".ljust(15), end="")
        for j in range(col):
            contenu = f"{tab[i][j].stat * 100:.2f}% ({tab[i][j].nb})".center(18)
            print(contenu, end="")
        print()

    print("=" * 50)
# Variables
nbL, nbC = 5, 6
max_cellule = 0
MM = [[Cellule(0, 0) for j in range(nbC)] for i in range(nbL)]

# Initialize all cells in MM with nb=0 and stat=0
for i in range(nbL):
    for j in range(nbC):
        MM[i][j] = Cellule(0, 0)

# Prompt the user for the next page and update MM array with transition probability
prev, curr = -1, 0
nextPage = -1
while True:
    # Display the current page and prompt the user for the next page
    print("Vous venez de " + str(prev) + ".\nVous êtes en " + str(curr))
    nextPage = int(input("Prochaine page (sortie du programme " + str(nbL) + ") : "))

    # Check if the user has entered a valid page number
    while nextPage < 0 or nextPage >= nbL:
        if nextPage == nbL:
            print("Sortie du programme")
            sys.exit(1)
        nextPage = int(input("Prochaine page (sortie du programme " + str(nbL) + ") : "))

    # Update MM array with the observed transition
    MM[prev][curr].nb += 1
    MM[prev][nbC - 1].nb += 1
    for k in range(nbC):
        MM[prev][k].stat = float(MM[prev][k].nb) / float(MM[prev][nbC - 1].nb)

    # Display the MM array in tabular format
    afficheTab(MM, nbC, nbL)

    # Set the current page as the previous page and the next page as the current page
    prev = curr
    curr = nextPage