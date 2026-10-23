
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.stopped = False
        self.direction = "North"
        self.turns = 0

    def move_forward(self):
        if not self.stopped:
            self.position += 1
            print(
                f"{self.name} moved to position "
                f"{self.position}, facing {self.direction}"
            )
        else:
            print(f"{self.name} cannot move: obstacle ahead")

    def turn_right(self):
        directions = ["North", "East", "South", "West"]
        index = directions.index(self.direction)
        self.direction = directions[(index + 1) % 4]
        self.turns += 1

        print(f"{self.name} turned right: {self.direction}")

    def avoid_obstacle(self, front_obstacle, right_obstacle):
        if not front_obstacle:
            self.stopped = False
            print("Path is clear.")
            return

        print("Obstacle detected ahead!")

        if not right_obstacle:
            self.turn_right()
            self.stopped = False
            print("Obstacle avoided.")
        else:
            self.stopped = True
            print("Front and right are blocked. Robot stopped.")


if __name__ == "__main__":
    robot = Robot("Smart-Robot")

    robot.move_forward()

    robot.avoid_obstacle(
        front_obstacle=True,
        right_obstacle=False
    )

    robot.move_forward()

    robot.avoid_obstacle(
        front_obstacle=True,
        right_obstacle=True
    )

    robot.move_forward()