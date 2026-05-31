from game.game_manager import GameManager


def main():
    game = GameManager("Ninja Game", 1024, 640)
    game.run()


if __name__ == "__main__":
    main()
