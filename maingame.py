# Main Game File
# This file connects all chapter modules. This is the file i will run

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def main():

    current = "chapter1"

    while True:

        if current == "chapter1":
            current = chapter1.play()

        elif current == "chapter2":
            current = chapter2.play()

        elif current == "chapter3":
            current = chapter3.play()

        elif current == "chapter4":
            current = chapter4.play()

        elif current == "chapter5":
            current = chapter5.play()

        elif current == "win":
            print()
            print("You win. Thanks for playing.")
            break

        elif current == "lose":
            print()
            print("Game over. Thanks for playing.")
            break

        else:
            print()
            print("Error: Unknown chapter name:", current)
            break

if __name__ == "__main__":
    main()
