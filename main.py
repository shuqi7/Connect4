from gameInterface import *

def main():
    while True:
        mode = input("Please enter 'text' or 'graphics' mode you want to play: ")
        if mode == "text":
            textMode()
            break
        elif mode == "graphics":
            window.mainloop()
            break
        else:
            print("Invalid! Please enter again!")



main()