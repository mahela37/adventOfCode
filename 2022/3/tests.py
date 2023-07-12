import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_part1_1(self):
        input = ["test", "aBBa"]
        answer = 49
        self.assertEqual(
            solution.run_solution_first(input),
            answer,
            "Part 1 - Calculates priority properly and sums total",
        )

    def test_part1_2(self):
        input = ["temp", "cats"]
        answer = 0
        self.assertEqual(
            solution.run_solution_first(input),
            answer,
            "Part 1 - Returns 0 when there are no common items",
        )

    def test_part2_1(self):
        input = ["abcd", "afgh", "iajk"]
        answer = 1
        self.assertEqual(
            solution.run_solution_second(input),
            answer,
            "Part 2 - Calculates priority for one group",
        )

    def test_part2_2(self):
        input = ["abcd", "aefg", "fghi"]
        answer = 0
        self.assertEqual(
            solution.run_solution_second(input),
            answer,
            "Part 2 - Does not add to count if partial intersection",
        )

    def test_part2_3(self):
        input = ["abcd", "afgh", "iajk", "bnc", "abh", "irb"]
        answer = 3
        self.assertEqual(
            solution.run_solution_second(input),
            answer,
            "Part 2 - Calculates priority for multiple groups",
        )


if __name__ == "__main__":
    unittest.main()
