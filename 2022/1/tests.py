import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = ["10", "20", "30", "\n", "2", "4", "6", "\n", "30", "40", "50", None]
        answer = 120
        self.assertEqual(
            solution.run_solution(input), answer, "Works with multiple elves"
        )

    def test_2(self):
        input = ["10", "20", "30", None]
        answer = 60
        self.assertEqual(solution.run_solution(input), answer, "Works with one elf")

    def test_3(self):
        input = []
        answer = 0
        self.assertEqual(solution.run_solution(input), answer, "Works with no elves")


if __name__ == "__main__":
    unittest.main()
