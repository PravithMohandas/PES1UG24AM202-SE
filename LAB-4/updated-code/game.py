from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        self.player.place_ship({(1, 1), (1, 2), (1, 3)}, "Patrol Ship")
        self.player.place_ship({(4, 3), (4, 4)}, "Submarine")

        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)}, "Destroyer")
        self.enemy.place_ship({(4, 0), (5, 0)}, "Patrol Boat")

    def show(self):
        print("\nYour shots are coordinates like 2,3.")
        print("Enemy ship cells remaining:", len(self.enemy.ships - self.enemy.hits))
        print("Enemy ships sunk:", len(self.enemy.sunk_ships), "/", self.enemy.ship_count)

    @staticmethod
    def _report_shot(board, pos, shooter):
        """Resolve and report one actual shot. Rejected shots produce no feedback."""
        result = board.fire(pos)
        if result is None:
            return None

        if result:
            print("HIT!")
            sunk_name = board.ship_sunk_at(pos)
            if sunk_name:
                print(f"SUNK! {shooter} sank the {sunk_name}!")
        else:
            print("MISS!")

        return result

    def run(self):
        print("Battleship")
        while True:
            self.show()
            raw = input("> ").strip().lower()
            if raw == "q":
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col.")
                continue

            if not (0 <= pos[0] < Board.SIZE and 0 <= pos[1] < Board.SIZE):
                print("Outside board.")
                continue

            if pos in self.enemy.shots:
                print("Already fired there.")
                continue

            # Board.fire determines the result; this method prints feedback once.
            self._report_shot(self.enemy, pos, "You")

            if self.enemy.all_sunk():
                print("You sank the entire enemy fleet. You win!")
                return

            # AI selection is not a shot result and must not print HIT/MISS.
            ai_pos = self.ai.choose()
            if ai_pos is None:
                print("AI has no untried coordinates remaining.")
                continue

            ar, ac = ai_pos
            print(f"AI fired at {ar + 1},{ac + 1}")
            ai_result = self._report_shot(self.player, ai_pos, "AI")
            self.ai.record_result(ai_pos, ai_result is True)

            if self.player.all_sunk():
                print("The AI sank your entire fleet. You lose!")
                return
