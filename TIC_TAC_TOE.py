import tkinter as tk

def print_winner():
    """Affiche un message de victoire pour le joueur actuel, puis réinitialise le jeu après 3 secondes."""
    global win
    win = True  # Indique qu'un joueur a gagné
    message_label.config(text=f"Le joueur {current_player} a gagné le jeu!")  # Affiche le gagnant
    root.after(3000, reset_game)  # Attendre 3 secondes avant de réinitialiser la grille

def print_draw():
    """Affiche un message de match nul, puis réinitialise le jeu après 3 secondes."""
    message_label.config(text="Match nul!")  # Affiche le message de match nul
    root.after(3000, reset_game)  # Attendre 3 secondes avant de réinitialiser la grille

def switch_player():
    """Change le joueur actuel de 'X' à '0' et vice versa."""
    global current_player
    current_player = '0' if current_player == 'X' else 'X'  # Alterne entre 'X' et '0'

def check_win():
    """Vérifie si le joueur actuel a gagné ou s'il y a un match nul."""
    # Vérification des lignes et des colonnes pour une victoire
    for i in range(3):
        # Vérifie chaque ligne pour une victoire
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            print_winner()
            return True
        # Vérifie chaque colonne pour une victoire
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            print_winner()
            return True
    # Vérification des deux diagonales pour une victoire
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        print_winner()
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        print_winner()
        return True

    # Vérification de match nul : si toutes les cases sont remplies sans victoire
    if all(buttons[row][col]['text'] != "" for row in range(3) for col in range(3)):
        print_draw()  # Affiche le message de match nul si toutes les cases sont remplies
        return True

    return False  # Retourne False si pas de victoire ou de match nul

def place_symbol(row, column):
    """Place le symbole du joueur actuel dans la case sélectionnée si elle est vide."""
    global win
    if not win and buttons[row][column]['text'] == "":
        # Place le symbole du joueur actuel dans la case sélectionnée
        buttons[row][column].config(text=current_player)
        
        # Vérifie si ce coup a donné lieu à une victoire ou un match nul
        if not check_win():  # Si personne n'a gagné ou s'il n'y a pas de match nul
            switch_player()  # Change de joueur uniquement si le jeu continue
            message_label.config(text=f"Joueur {current_player}, à vous de jouer")  # Indique le prochain joueur

def reset_game():
    """Réinitialise la grille pour démarrer une nouvelle partie."""
    global win, current_player
    win = False  # Réinitialise l'état de victoire
    current_player = 'X'  # Le joueur 'X' commence toujours
    message_label.config(text="Joueur X, à vous de jouer")  # Réinitialise le message d'état
    # Vide chaque bouton de la grille et le réactive
    for row in buttons:
        for button in row:
            button.config(text="", state="normal")

def draw_grid():
    """Crée une grille 3x3 de boutons pour le jeu de Tic Tac Toe."""
    for row in range(3):
        button_row = []
        for col in range(3):
            # Crée un bouton avec une commande qui place le symbole du joueur actuel
            button = tk.Button(root, font=("Arial", 20), width=5, height=2,
            command=lambda r=row, c=col: place_symbol(r, c))
            button.grid(row=row, column=col)  # Positionne le bouton dans la grille
            button_row.append(button)  # Ajoute le bouton à la ligne actuelle
        buttons.append(button_row)  # Ajoute la ligne de boutons à la grille

# Initialisation des variables globales
buttons = []  # Liste pour stocker les boutons du jeu
current_player = 'X'  # Le joueur 'X' commence toujours
win = False  # État de victoire, initialisé à False

# Création de la fenêtre du jeu
root = tk.Tk()
root.title("Tic Tac Toe")
root.minsize(300, 350)

# Label pour afficher les messages de jeu (par exemple, joueur gagnant ou match nul)
message_label = tk.Label(root, text="Joueur X, à vous de jouer", font=("Arial", 15))
message_label.grid(row=3, column=0, columnspan=3)

# Dessiner la grille
draw_grid()

# Boucle principale de tkinter
root.mainloop()
