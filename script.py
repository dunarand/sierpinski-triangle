from sierpinski import Sierpinski

if __name__ == "__main__":
    INITIAL_POINTS_COUNT = 1000
    ITERATION_COUNT = 1000
    CORNER_POINTS = [
        (0, 0),
        (6, 0),
        (3, 3*(3**0.5))
    ]
    Sierpinski(INITIAL_POINTS_COUNT, ITERATION_COUNT, CORNER_POINTS).plot()
