import random
import os
import pygame


TITLE = "title.txt"

def showTitle(TITLE):
    with open(TITLE) as file:
        title = file.read()
    print(title)
    return title


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return 0


def selectRandomElement(list):
    return random.choice(list)


def choosePlayMode():
    while True:
        try:
            clearScreen()
            showTitle(TITLE)
            print("1 - Play against the Computer")
            print("2 - Play against another Player")
            
            option = int(input("\n> "))
            
            # Stop asking for input only once option is 1 or 2
            if option in [1, 2]:
                return option
        except ValueError:
            continue


def pickMove():
    while True:
        try:
            clearScreen()
            showTitle(TITLE)
            print("Choose your move wisely...")
            print("1 - Rock\n2 - Paper\n3 - Scissor")
            
            move = int(input("\n> "))
            
            # Stop asking for input only once move is 1,2 or 3
            if move in [1,2,3]:
                return move
        except ValueError:
            continue


def playVsComputer(username, moves_list):
    computerPoints = 0
    userPoints = 0
    matches_played = 0
    matches_won_by_user = 0
    matches_won_by_pc = 0
    clearScreen()
    showTitle(TITLE)
    
    # Loop until the user chooses to exit
    while True:
        # Reset points for each new match
        computerPoints = 0
        userPoints = 0
        
        # Each round goes on until one of them reaches 3 points
        while computerPoints < 3 and userPoints < 3:
            # PC is the default winner
            final_winner = "PC"
            
            computerChoice = selectRandomElement(moves_list)
            userChoice = pickMove()
            
            # Only change points if it's not a draw
            if computerChoice != userChoice:
                if computerChoice == 1:  # PC chooses Rock
                    print("PC chose Rock.")
                    if userChoice == 2:
                        userPoints += 1
                        print(f"{username} chose Paper.")
                        print(f"{username} won this round!")
                    else:  # User chooses Scissors
                        computerPoints += 1
                        print(f"{username} chose Scissors.")
                        print("PC won this round!")
                elif computerChoice == 2:  # PC chooses Paper
                    print("PC chose Paper.")
                    if userChoice == 1:
                        computerPoints += 1
                        print(f"{username} chose Rock.")
                        print("PC won this round!")
                    else:
                        userPoints += 1
                        print(f"{username} chose Scissors.")
                        print(f"{username} won this round!")
                else:  # PC chooses Scissors
                    print("PC chose Scissors.")
                    if userChoice == 1:
                        userPoints += 1
                        print(f"{username} chose Rock.")
                        print(f"{username} won this round!")
                    else:
                        computerPoints += 1
                        print(f"{username} chose Paper.")
                        print("PC won this round!")
            else:
                print("Draw!")
            
            print(f"\n{username} {userPoints} - {computerPoints} PC")
            input("\nPress ENTER to continue")
        
        # Determine match winner
        if computerPoints == 3:
            print("\nPC won this game!")
            matches_won_by_pc += 1
        else:
            print(f"{username} won the game!")
            matches_won_by_user += 1
        
        matches_played += 1
        
        # Check final winner based on total matches won
        if matches_won_by_user > matches_won_by_pc:
            final_winner = username
        else:
            final_winner = "PC"
        
        # Ask the user if they want to continue or exit
        user_input = input("Press ENTER to restart or type 'exit' to leave: ").strip().lower()
        if user_input == "exit":
            break
    
    # Display the results
    print(f"\n{username} played a total of {matches_played} matches and won {matches_won_by_user} of them!")
    
    if matches_played > 0:
        win_rate = (matches_won_by_user / matches_played) * 100
    else:
        win_rate = 0  # Edge case for no matches played
    
    print(f"Win rate: {round(win_rate, 1)}%")
    
    return final_winner, matches_won_by_user, matches_played


def main():
    
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([800, 500])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0,0,255), (250,250), 75)
        my_font = pygame.font.SysFont('JetBrainsMono MNF', 50)
        text_surface = my_font.render('Rock Paper Scissor', False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
    pygame.quit()
    
    showTitle(TITLE)
    mode = choosePlayMode()
    
    # 1 -> ROCK
    # 2 -> PAPER
    # 3 -> SCISSOR
    moves = [1, 2, 3]
    
    # Play against the computer
    if (mode == 1):
        username = input("\nWhat should we call you? ")
        playVsComputer(username,moves)

    # Play against another player
    elif (mode == 2):
        # Implement game logic
        return 0

if __name__ == '__main__':
    main()