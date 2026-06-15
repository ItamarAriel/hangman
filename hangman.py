import os
import subprocess

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    
    # shell=True forces Windows to run 'cls' inside the command prompt environment
    subprocess.run([command], shell=True)

def clean_input(msg):
    while True:
        clear_screen()
        clean = input(msg).strip()

        if not clean:
            print("Invalid input: The secret phrase cannot be empty or only spaces.")
            continue

        if clean.replace(" ", "").isalpha():
            return " ".join(clean.split()).lower()
        
        print("Invalid input: Only letters (a-z) and spaces are allowed. Numbers are not permitted.")

def clean_input_char(msg):
    while True:
        clean = input(msg)

        if len(clean) == 1 and clean.isalpha():
            return clean.lower()

        else:
            print("Invalid input: valid a..z, only 1 letter.")

def main():
    running = ""
    while running != "exit":
        clear_screen()
        word = clean_input("Enter a word to guess: ")

        lives = 10
        guesses = []
        found = ["?"] * len(word)

        for k in range(len(word)):
            if word[k] == " ":
                found[k] = " "

        again = False
        while lives:
            clear_screen()
            print(f"Guessed: {guesses} lives: {lives}")
            print(f"word: {"".join(found)}")
            if again:
                print(f"You already guessed that letter try another one")
                again = False

            l = clean_input_char("Guess a letter: ")

            if l in found or l in guesses:
                again = True

            elif l in word:
                for j in range(len(word)):
                    if l == word[j]:
                        found[j] = l
                        guesses.append(l)

            else:
                lives -= 1
                guesses.append(l)


            if "".join(found) == word:
                break

        if lives:
            print(f"You guessed right the word was: {word}")
        else:
            print(f"You lost no more guesses")

        print(f"type exit to exit or press enter for another round")
        running = input().lower()

if __name__ == "__main__":
    main()