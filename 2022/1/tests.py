import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_says_hi(self):
        self.assertEqual(
            solution.run_solution("hi"), "hello world hi", "Should return right value"
        )

    def test_says_bye(self):
        self.assertEqual(
            solution.run_solution("bye"),
            "hello world bye",
            "Should return right value",
        )


if __name__ == "__main__":
    unittest.main()
