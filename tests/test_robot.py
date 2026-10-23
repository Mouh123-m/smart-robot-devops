
import sys
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from robot import Robot


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("Test-Robot")

    def test_robot_moves_forward(self):
        self.robot.move_forward()

        self.assertEqual(self.robot.position, 1)

    def test_robot_turns_right_when_path_is_blocked(self):
        self.robot.avoid_obstacle(
            front_obstacle=True,
            right_obstacle=False
        )

        self.assertEqual(self.robot.direction, "East")
        self.assertFalse(self.robot.stopped)
        self.assertEqual(self.robot.turns, 1)

    def test_robot_stops_when_both_paths_are_blocked(self):
        self.robot.avoid_obstacle(
            front_obstacle=True,
            right_obstacle=True
        )

        self.assertTrue(self.robot.stopped)
        self.assertEqual(self.robot.direction, "North")


if __name__ == "__main__":
    unittest.main()
