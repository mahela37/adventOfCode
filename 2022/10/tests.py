import os, sys, unittest
import solution


class TestSolution(unittest.TestCase):
    file = open(os.path.join(sys.path[0], "test_input.txt"), "r")
    file_contents = file.readlines()
    file.close()
    file_contents_stripped = [line.strip() for line in file_contents]

    def test_part1_1(self):
        answer = 15880
        self.assertEqual(
            solution.run_solution_first(self.file_contents_stripped),
            answer,
            "Part 1 - Calculates total strength properly",
        )

    def test_part2_1(self):
        answer = (
            "###..#.....##..####.#..#..##..####..##..\n"
            "#..#.#....#..#.#....#.#..#..#....#.#..#.\n"
            "#..#.#....#....###..##...#..#...#..#....\n"
            "###..#....#.##.#....#.#..####..#...#.##.\n"
            "#....#....#..#.#....#.#..#..#.#....#..#.\n"
            "#....####..###.#....#..#.#..#.####..###.\n"
        )
        self.assertEqual(
            solution.run_solution_second(self.file_contents_stripped),
            answer,
            "Part 2 - Draws the right shape",
        )


if __name__ == "__main__":
    unittest.main()
