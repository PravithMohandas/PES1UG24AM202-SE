import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from ai import AI
from board import Board
from game import Battleship


class BoardFleetTests(unittest.TestCase):
    def test_hitting_ship_records_damage(self):
        board = Board()
        board.place_ship({(0, 0), (0, 1)}, "Destroyer")
        self.assertIs(board.fire((0, 0)), True)
        self.assertIn((0, 0), board.hits)
        self.assertNotIn("Destroyer", board.sunk_ships)
        self.assertFalse(board.all_sunk())

    def test_sinking_one_ship_does_not_sink_other_ship(self):
        board = Board()
        board.place_ship({(0, 0), (0, 1)}, "Destroyer")
        board.place_ship({(2, 2)}, "Patrol Boat")
        board.fire((0, 0))
        board.fire((0, 1))
        self.assertEqual(board.ship_sunk_at((0, 1)), "Destroyer")
        self.assertIn("Destroyer", board.sunk_ships)
        self.assertNotIn("Patrol Boat", board.sunk_ships)
        self.assertFalse(board.all_sunk())

    def test_repeated_shot_does_not_apply_damage_again(self):
        board = Board()
        board.place_ship({(1, 1), (1, 2)}, "Submarine")
        self.assertIs(board.fire((1, 1)), True)
        hits_after_first_shot = set(board.hits)
        self.assertIsNone(board.fire((1, 1)))
        self.assertEqual(board.hits, hits_after_first_shot)
        self.assertFalse(board.all_sunk())

    def test_entire_fleet_must_be_sunk(self):
        board = Board()
        board.place_ship({(0, 0), (0, 1)}, "Destroyer")
        board.place_ship({(2, 2)}, "Patrol Boat")
        for pos in ((0, 0), (0, 1)):
            board.fire(pos)
        self.assertFalse(board.all_sunk())
        board.fire((2, 2))
        self.assertTrue(board.all_sunk())
        self.assertEqual(board.sunk_ships, {"Destroyer", "Patrol Boat"})

    def test_repeated_miss_is_also_rejected(self):
        board = Board()
        board.place_ship({(0, 0)}, "Patrol Boat")
        self.assertIs(board.fire((5, 5)), False)
        self.assertIsNone(board.fire((5, 5)))

    def test_board_rejects_invalid_shot_without_recording_it(self):
        board = Board()
        board.place_ship({(0, 0)}, "Patrol Boat")

        for pos in ((-1, 0), (0, 6), (6, 0), (1, 1, 1), [0, 0]):
            with self.subTest(pos=pos):
                with self.assertRaises(ValueError):
                    board.fire(pos)
        self.assertEqual(board.shots, set())
        self.assertEqual(board.hits, set())

    def test_board_accepts_corner_coordinates(self):
        board = Board()
        board.place_ship({(0, 0), (5, 5)}, "Corner Ship")

        self.assertIs(board.fire((0, 0)), True)
        self.assertIs(board.fire((5, 5)), True)
        self.assertEqual(board.hits, {(0, 0), (5, 5)})

    def test_task1_ai_coordinates_remain_zero_based_tuples(self):
        ai = AI(size=6)
        ai.tried.add((1, 2))
        pos = ai.choose()
        self.assertIsInstance(pos, tuple)
        self.assertEqual(len(pos), 2)
        self.assertTrue(0 <= pos[0] < 6 and 0 <= pos[1] < 6)
        self.assertIn(pos, ai.tried)
        self.assertNotEqual(pos, (1, 2))

    def test_game_has_multiple_distinct_ships(self):
        game = Battleship()
        self.assertEqual(game.player.ship_count, 2)
        self.assertEqual(game.enemy.ship_count, 2)
        self.assertEqual(len(game.enemy.ships), 5)


class AITargetingTests(unittest.TestCase):
    def test_prefers_adjacent_untried_cell_after_hit(self):
        ai = AI(size=6)
        hit = (2, 2)
        ai.tried.add(hit)
        ai.record_result(hit, True)
        with patch("ai.random.choice", side_effect=lambda choices: choices[0]):
            pos = ai.choose()
        self.assertIn(pos, {(1, 2), (3, 2), (2, 1), (2, 3)})
        self.assertIn(pos, ai.tried)

    def test_never_chooses_a_coordinate_twice(self):
        ai = AI(size=2)
        shots = [ai.choose() for _ in range(4)]
        self.assertEqual(len(set(shots)), 4)
        self.assertEqual(ai.tried, set(shots))
        self.assertIsNone(ai.choose())

    def test_uses_normal_targeting_when_there_has_been_no_hit(self):
        ai = AI(size=3)
        with patch("ai.random.choice", side_effect=lambda choices: choices[0]) as chooser:
            pos = ai.choose()
        self.assertEqual(pos, (0, 0))
        self.assertEqual(len(chooser.call_args.args[0]), 9)
        self.assertEqual(ai.hits, set())

    def test_returns_none_when_no_untried_cells_remain(self):
        ai = AI(size=1)
        self.assertEqual(ai.choose(), (0, 0))
        self.assertIsNone(ai.choose())


class ShotFeedbackTests(unittest.TestCase):
    def run_game(self, inputs):
        output = io.StringIO()
        # Use known empty player-board cells so feedback counts are deterministic.
        ai_choices = [(0, c) for c in range(6)]
        with patch("builtins.input", side_effect=inputs), \
             patch("game.AI.choose", side_effect=ai_choices), \
             redirect_stdout(output):
            Battleship().run()
        return output.getvalue()

    def test_player_hit_printed_once(self):
        # (2,2) in zero-based coordinates is entered as 3,3.
        output = self.run_game(["3,3", "q"])
        self.assertEqual(output.count("HIT!"), 1)
        self.assertEqual(output.count("MISS!"), 1)  # one AI shot is also resolved

    def test_player_miss_printed_once(self):
        output = self.run_game(["1,1", "q"])
        self.assertEqual(output.count("MISS!"), 2)  # player miss plus AI miss
        self.assertEqual(output.count("HIT!"), 0)

    def test_sinking_ship_prints_sunk_once(self):
        output = self.run_game(["3,3", "3,4", "3,5", "q"])
        self.assertEqual(output.count("SUNK!"), 1)
        self.assertIn("SUNK! You sank the Destroyer!", output)

    def test_repeated_shot_does_not_print_second_result_or_fire_ai(self):
        output = self.run_game(["3,3", "3,3", "q"])
        self.assertEqual(output.count("HIT!"), 1)
        self.assertEqual(output.count("AI fired at"), 1)
        self.assertIn("Already fired there.", output)

    def test_ai_hit_and_miss_each_get_one_result(self):
        game = Battleship()
        output = io.StringIO()
        # First AI shot hits the Patrol Ship; second AI shot misses.
        with patch("builtins.input", side_effect=["1,1", "1,2", "q"]), \
             patch("game.AI.choose", side_effect=[(1, 1), (5, 5)]), \
             redirect_stdout(output):
            game.run()
        text = output.getvalue()
        # The single HIT/MISS labels cover both player and AI shots; no duplicate
        # AI-specific result messages should be emitted.
        self.assertEqual(text.count("HIT!"), 1)
        self.assertEqual(text.count("MISS!"), 3)  # two player misses plus AI miss
        self.assertNotIn("AI scored a hit.", text)
        self.assertNotIn("AI missed.", text)

    def test_invalid_coordinates_do_not_produce_shot_feedback(self):
        output = self.run_game(["7,1", "abc", "q"])
        self.assertIn("Outside board.", output)
        self.assertIn("Use row,col.", output)
        self.assertEqual(output.count("HIT!"), 0)
        self.assertEqual(output.count("MISS!"), 0)
        self.assertEqual(output.count("SUNK!"), 0)
        self.assertEqual(output.count("AI fired at"), 0)

    def test_player_can_fire_at_valid_board_boundaries(self):
        output = self.run_game(["1,1", "6,1", "q"])
        self.assertNotIn("Outside board.", output)
        self.assertEqual(output.count("HIT!"), 1)  # bottom-left ship cell
        self.assertEqual(output.count("MISS!"), 3)  # two AI misses and one player miss

    def test_player_can_sink_entire_fleet_and_win(self):
        output = self.run_game(["3,3", "3,4", "3,5", "5,1", "6,1"])
        self.assertIn("You sank the entire enemy fleet. You win!", output)
        self.assertEqual(output.count("SUNK!"), 2)
        # The final player shot wins immediately; no extra AI shot follows it.
        self.assertEqual(output.count("AI fired at"), 4)

    def test_quitting_produces_no_shot_feedback(self):
        output = self.run_game(["q"])
        self.assertNotIn("HIT!", output)
        self.assertNotIn("MISS!", output)
        self.assertNotIn("SUNK!", output)
        self.assertNotIn("AI fired at", output)


if __name__ == "__main__":
    unittest.main()
