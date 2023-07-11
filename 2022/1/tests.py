import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_part1_1(self):
        input = ["10", "20", "30", "\n", "2", "4", "6", "\n", "30", "40", "50", None]
        answer = 120
        self.assertEqual(
            solution.run_solution_first(input),
            answer,
            "Part 1 - Works with multiple elves",
        )

    def test_part1_2(self):
        input = ["10", "20", "30", None]
        answer = 60
        self.assertEqual(
            solution.run_solution_first(input), answer, "Part 1 - Works with one elf"
        )

    def test_part1_3(self):
        input = []
        answer = 0
        self.assertEqual(
            solution.run_solution_first(input), answer, "Part 1 - Works with no elves"
        )

    def test_part2_1(self):
        input = [
            "10",
            "20",
            "30",
            "\n",
            "2",
            "4",
            "6",
            "\n",
            "30",
            "40",
            "50",
            "\n",
            "30",
            "40",
            "80",
            None,
        ]
        answer = 330
        self.assertEqual(
            solution.run_solution_second(input),
            answer,
            "Part 2 - Works with multiple elves",
        )

    def test_part2_2(self):
        input = ["10", "20", "30", None]
        answer = 60
        self.assertEqual(
            solution.run_solution_second(input), answer, "Part 2 - Works with one elf"
        )

    def test_part2_3(self):
        input = []
        answer = 0
        self.assertEqual(
            solution.run_solution_second(input), answer, "Part 2 - Works with no elves"
        )


if __name__ == "__main__":
    unittest.main()
