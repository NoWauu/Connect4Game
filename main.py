def Affichage_Menu():
    """
    Cette fontion affiche le menu principal.
    """
    menu = (
        " ─────────────═ Menu ═─────────────",
        "  1 -> Jouer",
        "  2 -> Voir les règles",
        "  3 -> Changer le nom des joueurs",
        "  0 -> Quitter le programme",
    )
    print()
    # Boucle pour afficher le menu.
    for i in menu:
        print(i)
    print()


def Menu():
    """
    Cette fonction vérifie que le choix de l'utilisateur ou des utilisateurs
    est un entier et que ce choix fait partie du menu.

    Elle renvoie le choix.
    """
    test = True
    # Boucle permettant de boucler sur le choix tant qu'il est faux
    while test:
        Affichage_Menu()
        try:
            # Teste si l'entrée est un entier et récupère la saisie
            choix = int(input(" Faites votre choix : "))
            # Permet de quitter la boucle
            test = False
            # vérifie si l'utilisateur a fait l'un des choix demandé
            choix_valide = 0 <= choix < 4
            if not choix_valide:
                raise ValueError
        except ValueError:
            # Message d'erreur si l'entrée n'est pas valide.
            print("Veuillez entrer une action parmi celles disponibles. ")
    return choix


def Choix_Joueur(tour, jetons_tuple, joueur1, joueur2):
    """
    Cette fonction permet l'alternance entre les différents joueur et
    d'indiquer quel jeton placer au jeu.

    Elle prend en paramètres le nombre de tours écoulés, les jetons utilisés
    et le nom des deux joueurs.

    Elle retourne le jeton à utiliser et le nom du joueur qui y est associé.
    """
    # Choix du jeton selon le tour
    if tour % 2 == 1:
        jeton = jetons_tuple[0]
        joueur = joueur1
    else:
        jeton = jetons_tuple[1]
        joueur = joueur2
    return jeton, joueur


def Choix_ligne(grille, colonne):
    ligne = -1
    # On détermine la ligne où le jeton va tomber
    while grille[ligne][colonne] != " ":
        ligne -= 1
    return ligne


def Poser_Jeton(grille: list, jeton="?", joueur="J"):
    """
    Cette fonction ajoute le jeton du joueur à la bonne place dans la grille.

    Elle prend en argument la grille : 'grille' ainsi que sa largeur : 'L',
    elle prend aussi comme argument le jeton à poser : 'Jeton'.

    Elle retourne la nouvelle grille.
    """
    test = True
    # Boucle permettant de boucler sur le choix tant qu'il est faux
    while test:
        Afficher_Grille(grille)
        print(f" À {joueur} de jouer !")
        try:
            colonne = int(input(" Veuillez entrer le numéro de la colonne : "))
            colonne -= 1
            # vérifie si l'utilisateur a choisi une colonne existante
            valide = 0 <= colonne < 7
            if not valide:
                raise ValueError
            # Vérifie si la colonne est pleine
            Choix_ligne(grille, colonne)
            test = False
        except ValueError:
            print(" Veuillez entrer un numéro de colonne valide. ")
        except IndexError:
            print(" La colonne choisie est déjà pleine.")
    ligne = Choix_ligne(grille, colonne)
    # On ajoute le jeton à la grille
    grille[ligne][colonne] = jeton
    return grille, ligne, colonne


def VerifPuissance4(tab: list, i: int, j: int) -> bool:
    """
    Cette fonction vérifie si le joueur a gagné.

    Elle prend en argument la grille : 'tab' ainsi que les coordonnées du jeton
    à vérifier : 'i' et 'j'.

    Elle retourne True si le joueur a gagné, False sinon.
    """

    # On vérifie si le joueur a gagné en vérifiant les lignes
    for k in range(4):
        # Si les points testés ne correspondent pas
        if tab[i][j] != tab[i][j + k]:
            # Quitter la boucle
            break
        # Si la boucle n'a pas été quittée
        # Alors les points sont les mêmes
        if k == 3:
            return True

    # On vérifie si le joueur a gagné en vérifiant les colonnes
    for k in range(4):
        if tab[i][j] != tab[i + k][j]:
            break
        if k == 3:
            return True

    # On vérifie si le joueur a gagné en vérifiant les diagonales
    # Diagonale ascendante
    for k in range(4):
        if tab[i][j] != tab[i + k][j + k]:
            break
        if k == 3:
            return True

    # Diagonale descendante
    for k in range(4):
        if tab[i][j] != tab[i + k][j - k]:
            break
        if k == 3:
            return True
    return False


def Afficher_Grille(grille: list):
    """
    Cette fonction affiche la grille de jeu.

    Elle prend en paramètres la complétion de cette grille : 'grille'.
    """
    # Affiche la bandeau du jeu
    print("""  ─────────────────────────────
           PUISSANCE 4
  ─────────────────────────────""")
    print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    for colonne in range(5):
        print("  ║ ", end="")
        for ligne in range(7):
            print(grille[colonne][ligne], end=" ║ ")
        print()
        print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══", end="╣\n")
    print("  ║ ", end="")
    for ligne in range(7):
        print(grille[5][ligne], end=" ║ ")
    print()
    print("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╝")
    print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print()


def Affichage_Fin(grille, joueur, Win):
    """
    Cette fonction se lance à la fin de chaque partie et affiche un message de
    victoire si quelqu'un a gagné ou un message de match nul si aucun des
    joueurs n'a réussi à se départager durant la partie.

    Elle prend en paramètres la grille de jeu, le joueur qui a gagné et le
    booléen disant si quelqu'un a gagné la partie.
    """
    # Affichage en fin de partie
    if Win:
        Afficher_Grille(grille)
        print(f" Bravo {joueur} ! Vous avez gagné !")
    else:
        Afficher_Grille(grille)
        print(" Dommage pour vous... Vous avez fait un match nul.")


def Jeu(joueur1, joueur2):
    """
    Cette fonction crée la grille de jeu, compte le nombre de tours et appelle
    les différentes fonctions pour jouer au puissance 4.

    Elle prend en paramètres le nom des deux joueurs.
    """
    # nombre de colonnes et de lignes
    nbColonnes, nbLignes, tour, Win = 7, 6, 0, False
    grille = []
    jetons_tuple = ("X", "O")
    # L et C sont inversé car le tableau est construit à l'envers
    for i in range(nbLignes):
        grille.append([" "] * nbColonnes)
    # Boucle du jeu
    while tour < 42 and not Win:
        tour += 1
        jeton, joueur = Choix_Joueur(tour, jetons_tuple, joueur1, joueur2)
        jeton = Poser_Jeton(grille, jeton, joueur)
        # On ajoute le jeton à la place choisie
        # jeton[0] correspond à la nouvelle grille
        grille = jeton[0]
        # On vérifie si l'un des joueurs à gagné
        Win = VerifPuissance4(grille, jeton[1], jeton[2])
    Affichage_Fin(grille, joueur, Win)


def Regles():
    '''
    Cette fonction affiche les règles du jeu.
    '''
    print('''
    ╔══════════════════════════════════════════════════════╗
    ║                       Règles                         ║
    ╠══════════════════════════════════════════════════════╣
    ║ Le puissance 4 est un jeu qui se joue à deux joueurs ║
    ║ représentés chacun par un jeton différent, X et O.   ║
    ║ Il se joue en alternance, le joueur X commençant.    ║
    ║                                                      ║
    ║ À chaque fois, le joueur qui joue doit poser un      ║
    ║ jeton dans une grille de 6x7 cases. Pour poser un    ║
    ║ jeton, le joueur doit indiquer le numéro de la       ║
    ║ colonne où il veut le poser. En conséquence, au fur  ║
    ║ à mesure que le jeu avance, la grille se remplit.    ║
    ║                                                      ║
    ║ Pour que la partie se termine, un des deux joueurs   ║
    ║ doit aligner 4 jetons, que ce soit à la verticale,   ║
    ║ à l'horizontal ou même en diagonal.                  ║
    ╚══════════════════════════════════════════════════════╝''')


def Noms_Joueurs(joueur1, joueur2):
    '''
    Cette fonction demande à l'utilisateur le nom des deux joueurs des
    prochaines parties.

    Elle prend en paramètres le nom des deux joueurs déjà existants.

    Elle retourne les nouveaux noms de ces deux joueurs sous la même variable.
    '''
    joueurs = [joueur1, joueur2]
    tour = ["premier", "deuxième"]

    for i, joueur in enumerate(joueurs):
        # Demande le nom du joueur tant que le nom entré est composé d'espace
        # ou de vide
        test = False
        while not test:
            joueur = input(f" Veuillez entrer le nom du {tour[i]} joueur : ")
            # retire les espaces aux extrémités du nom
            joueur = joueur.strip().capitalize()
            # vérifie si le nom entré n'est pas vide
            if joueur != "":
                test = True
            joueurs[i] = joueur
    return joueurs[0], joueurs[1]


def main():
    '''
    Cette fonction est la fonction principale, elle se lance au début et permet
    d'appeler le menu.
    '''
    # Initialisation des variables
    choix = -1
    # Boucle pour le choix
    joueur1, joueur2 = 'X', 'O'
    while choix != 0:
        choix = Menu()
        if choix == 0:
            print("Fermeture du programme...")
        elif choix == 1:
            # Lancement du jeu
            Jeu(joueur1, joueur2)
        elif choix == 2:
            Regles()
        elif choix == 3:
            # Récupère le nom des de joueurs
            joueur1, joueur2 = Noms_Joueurs(joueur1, joueur2)


main()
