"""
Точка входа в игру
"""
from game_state import GameState

def main():
    """запуск игры"""

    gast = GameState()
    gas = gast.quest
    print(f"{gas.questn}{gas.questdesc}")

if __name__ == "__main__":
    main()
