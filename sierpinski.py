"""
A basic Python class for creating a Sierpinski triangle with the ability to
also plot it using `matplotlib.pyplot`.
"""

import multiprocessing
from random import choice
import functools
import operator
import matplotlib.pyplot as plt

class Sierpinski:
    """
    NAME
        sierpinski
    
    DESCRIPTION
        Sierpinski triangle generator
        =============================
        Generates a list of points that define a Sierpinski triangle.
    
    PARAMETERS
        `initial_points_count (int)`: the number of initial points to
            individually iterate over
        `iteration_count (int)`: the number of iterations per initial point
        `corner_points (list[tuple])`: corners of the main triangle
    
    METHODS
        midpoint
        midpoint_iter
        generate_points
        plot
    """

    def __init__(self, initial_points_count:int,
                 iteration_count: int,
                 corner_points: list[tuple]) -> None:
        self.initial_points_count = initial_points_count
        self.iteration_count = iteration_count
        self.corner_points = corner_points
        initial_point = choice(self.corner_points)
        self.initial_points = [
            initial_point for i in range(initial_points_count)
        ]
        self.points_list = []
        self.color_list = []

    def midpoint(self,
                 point_1: tuple[float, float],
                 point_2: tuple[float, float]) -> tuple[float, float]:
        """Given two points `point_1` and `point_2`, returns the midpoint of
        `point_1` and `point_2`."""
        return (0.5*(point_1[0]+point_2[0]), 0.5*(point_1[1]+point_2[1]))

    def midpoint_iter(self, point: tuple[float, float]) -> list[float]:
        """Given a point `point`, returns a list of points where each point
        is generated by the following algorithm:

        1. Select the last item in the points list
        2. Choose a corner point randomly
        3. Select the midpoint of the point in step 1 and step 2
        4. Add the midpoint in step 4 to the points list"""
        points = [point]
        i = 0
        while i < self.iteration_count:
            points.append(
                self.midpoint(choice(self.corner_points), points[-1])
            )
            i += 1
        return points[1:] # excluding the initial point to prevent overlapping points

    def generate_points(self) -> None:
        """Generates a list of points that define the Sierpinski triangle."""
        with multiprocessing.Pool() as pool:
            self.points_list = pool.map(
                self.midpoint_iter,
                self.initial_points
            )
        self.points_list = functools.reduce(
            operator.iconcat, self.points_list, []
        ) # flattens the list self.points_list

    def plot(self) -> None:
        """Plots the Sierpisnki triangle."""
        if self.points_list == []:
            self.generate_points()
        plt.axis('off')
        plt.scatter(
            [point[0] for point in self.points_list],
            [point[1] for point in self.points_list],
            marker = ".",
            c = 'black',
            s = 1
        )
        plt.show()
