import random
import os

def main():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Welcome to Dysthymia.
In this game, you will fight Dysthymia.
Dysthymia is a mental illness that affects your mood, thoughts, and behavior.
It can be difficult to fight. there are 2 endings to this game.
you have to fight Dysthymia for 10 turns.
          press any key to continue...
""")
    input()
    turn = 0
    health = 100
    while True:
        if turn > 10 and health < 50:
            print("You have lost the fight against Dysthymia.")
            input()
            print("you think about ending it all.")
            input()
            print("you have commited suicide.")
            input()
            print("Now you feel better.")
            input()
            break
        elif turn > 10 and health > 50:
            print("You have won the fight against Dysthymia. You are now free...")
            input()
            print("you take a walk outside and breath the air...")
            input()
            print("You get hit by a car and get paralyzed...")
            input()
            print("you wish you were dead.")
            input()
            break

        turn += 1
        input(f"Turn {turn}. Press any key to continue... ")
        while True:
            action = input("what will you do? (fight, rest, or run) ")
            action = action.lower()
            if action in ["fight", "rest", "run", "help", "quit", "d+", "d-"]:
                if action == "fight":
                    c = random.random()
                    if c < 0.5 and c > 0.3:
                        print("You took anti depressants...")
                        input()
                        print("you feel better.")
                        clear()
                        health += 10
                        input()
                        break
                    elif c < 0.3:
                        print("you took anti depressants...")
                        input()
                        print("you are getting more suicidal.")
                        health -= 10
                        input()
                        clear()
                        break
                    elif c > 0.5 and c < 0.6:
                        print("you took anti depressants...")
                        input()
                        print("you dont feel like yourself.")
                        health -= 5
                        input()
                        clear()
                        break
                    elif c > 0.6 and c < 0.7:
                        print("you took anti depressants...")
                        input()
                        print("you feel numb.")
                        health -= 10
                        input()
                        clear()
                        break
                    elif c > 0.7 and c < 0.8:
                        print("you went to therapy...")
                        input()
                        print("he doesnt understand you.")
                        health -= 20
                        input()
                        clear()
                        break
                    elif c > 0.8 and c < 0.9:
                        print("you went to therapy...")
                        input()
                        print("you feel better after talking it out.")
                        health += 15
                        input()
                        clear()
                        break
                    elif c > 0.9:
                        print("you took anti depressants...")
                        input()
                        print("it made you feel worse, you feel like you are losing control.")
                        health -= 30
                        input()
                        clear()
                        break

                elif action == "rest":
                    c = random.random()
                    if c < 0.5 and c > 0.3:
                        print("you slept well...")
                        input()
                        print("you feel better.")
                        health += 10
                        input()
                        clear()
                        break
                    elif c < 0.3:
                        print("you can't sleep...")
                        input()
                        print("you are getting more suicidal.")
                        health -= 10
                        input()
                        clear()
                        break
                    elif c > 0.5 and c < 0.6:
                        print("you rest well...")
                        input()
                        print("you feel better.")
                        health += 5
                        input()
                        clear()
                        break
                    elif c > 0.6:
                        print("you slept well...")
                        input()
                        print("you dont feel like waking up...")
                        health -= 10
                        input()
                        clear()
                        break

                elif action == "run":
                    c = random.random()
                    if c < 0.5 and c > 0.3:
                        print("you went for a walk...")
                        input()
                        print("you feel better.")
                        health += 10
                        input()
                        clear()
                        break
                    elif c < 0.3 and c > 0.2:
                        print("you went for a walk...")
                        input()
                        print("you feel tired, but better.")
                        health += 5
                        input()
                        clear()
                        break
                    elif c > 0.5 and c < 0.6:
                        print("you started cutting yourself as a way to run from your problems...")
                        input()
                        print("you felt better intially, but now you feel worse.")
                        health -= 10
                        input()
                        clear()
                        break
                    elif c > 0.6 and c < 0.7:
                        print("you started running...")
                        input()
                        print("you feel danger, but you want to embrace it.")
                        input()
                        print("you get hit by a car.")
                        health -= 30
                        input()
                        clear()
                        break
                    elif c > 0.7:
                        print("you started running...")
                        input()
                        print("you feel better.")
                        health += 10
                        input()
                        clear()
                        break

                elif action == "quit":
                    print("you can't quit now.")
                    break

                elif action == "help":
                    print("You can fight, rest, or run. You can also quit the game.")
                    break
                    
                elif action == "d+":
                    health += 200
                    break

                elif action == "d-":
                    health -= 200
                    break
            else:
                print("Invalid action. Please try again.")



if __name__ == "__main__":
    main()
