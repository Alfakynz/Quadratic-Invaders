import signal
import sys
from game import Game

def main():
    Game()

# Made by ChatGPT to handle Ctrl+C gracefully (try & except doesn't work well with Pyxel)
def handle_interrupt(sig, frame):
    print("\nGame interrupted by user. Exiting gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_interrupt)
    main()