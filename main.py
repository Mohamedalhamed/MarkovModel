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
        print("=====================", end='')
    print("")
def afficherTab(tab, col, ligne, curr):
    # Tabulate MM
    print("")
    print("")
    print("TRANSITION PROBABILITIES:")
    print("")
    print("FROM PAGE".ljust(15), end="")
    for i in range(col):
        if i == col - 1:
            print(f"{'Line Count'.ljust(18)}", end="")
        else:
            print(f"TO PAGE {i}".center(18), end="")
    print("")

    # Add separators
    print(" ", end="")
    afficheSeparateur(col, 1)

    # Add content
    for i in range(ligne):
        if i == curr:
            prefix = "> "
        else:
            prefix = "  "
        print(f"{prefix}Page {i}".ljust(15), end="")
        total = 0
        for j in range(col):
            if j == col-1 : # skip percentage calculation for the Line Count column
                contenu = f"{tab[i][j].nb}".center(12)
            else:
                contenu = f"{min(tab[i][j].stat * 100, 100):5.2f}%".center(12)
#({tab[i][j].nb})
            con = f"{contenu}".ljust(18)
            print(con, end="")
        print("")

    # Add separators between rows
    print(" ", end="")
    afficheSeparateur(col, 0)
    print("=" * 50)

# Variables
nbL, nbC = 5, 6
max_cellule = 0
MM = [[Cellule(0, 0) for i in range(nbC)] for j in range(nbL)]

# Initialize all cells in MM with nb=0 and stat=0
for i in range(nbL):
    for j in range(nbC):
        MM[i][j] = Cellule(0, 0)

# Prompt the user for the next page and update MM array with transition probability
prev = -1
curr = 0
nextPage = ""
while True:
    # Display the current page and prompt the user for the next page
    print("Where you from:", prev)
    print("Where you are:", curr)
    nextPage = input("Where you go: (please enter a number 0-4, q: quit, Q: Quit program)\n> ")

    # Check if the user has entered a valid page number
    if nextPage.isdigit():
        nextPage = int(nextPage)
        while nextPage < 0 or nextPage >= nbL:
            nextPage = int(input("Please enter a valid page number (0-4)\n> "))

        # Update MM array with the observed transition
        MM[prev][nextPage].nb += 1
        MM[curr][nbC - 1].nb += 1
        for k in range(nbC):
            MM[curr][k].stat = float(MM[prev][k].nb) / float(MM[curr][nbC - 1].nb)

        # Display the MM array in tabular format
        afficherTab(MM, nbC, nbL, curr)

        # Set the current page as the previous page and the next page as the current page
        prev = curr
        curr = nextPage

    # Check if the user wants to quit the program
    elif nextPage in ["q", "Q"]:
        print("Quitting program...")
        sys.exit(1)
