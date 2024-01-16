import random

def roll_dice():
    """Simuler le lancer de deux dés."""
    return random.randint(1, 6) + random.randint(1, 6)

def get_valid_number(prompt):
    """Demander à l'utilisateur de saisir un nombre valide."""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Veuillez saisir un nombre valide.")

def play_game():
    """Fonction principale pour jouer au jeu de dés."""
    print("Bienvenue dans le jeu de dés!")

    players = get_valid_number("Entrez le nombre de joueurs : ")
    player_names = []

    for player in range(players):
        name = input(f"Entrez le nom du Joueur {player + 1}: ")
        player_names.append(name)

    scores = [0] * players

    while True:
        for player in range(players):
            input(f"{player_names[player]}, appuyez sur Entrée pour lancer les dés...")

            total = roll_dice()
            scores[player] += total

            print(f"{player_names[player]}, vous avez obtenu un total de {total}.")
            print(f"Score actuel de {player_names[player]} : {scores[player]}")

            if scores[player] >= 31:
                print(f"Félicitations, {player_names[player]} a gagné!")
                return

if __name__ == "__main__":
    play_game()
