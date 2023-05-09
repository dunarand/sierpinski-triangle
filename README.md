# sierpinski-triangle

![Sierpinski Triangle](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Sierpinski_triangle.svg/1024px-Sierpinski_triangle.svg.png)

A Python script to create and plot a Sierpinski triangle consisting of as much points as you wish, or your memory can handle.

## What is a Sierpinski triangle?

A [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) is a [fractal](https://en.wikipedia.org/wiki/Fractal_curve) consisting of equilateral triangles.

## How to create a Sierpinski triangle?

There are several ways to create a Sierpinski triangle, as can be found in the link above. *Chaos game* is one such way of creating a Sierpinski triangle. It is a simple algorithm given by the following steps:

1. Pick three points $c_1, c_2, c_3\in\mathbb{R}^2$ that are not colinear; that is, $c_1, c_2, c_3$ defines a triangle
2. Select a point $p_0\in\mathbb{R}^2$
3. Pick a random corner point $c_n$ and set $p_{i+1}$ as the midpoint between $c_n$ and $p$; that is, $$p_{i+1}= \frac{1}{2}\times (c_n + p_i)$$
4. Repeat step 3

The resulting sequence of points $\{p_i\}_{i \in I}$ is an approximation of a Sierpinski triangle. Computing more points results in a more detailed representation.

Note that it is not necessary to pick the initial point on or within the triangle. Any sequence whose initial point is outside of the triangle will eventually converge to inside of the triangle.

## How this code works?

I have decided to create a simple class `Sierpinski` that generates the triangle by using the above algorithm. In order to calculate the points faster, I decided to use Python's `multiprocessing` library. Since each new point on a given sequence is dependent on the previous points, parallel computation is not possible. However, by considering multiple sequences, we can calculate the points on each sequence individually. Since randomness is part of the algorithm and any sequence defined as in the algorithm converges to the same region, we can approximate the Sierpinski triangle by using multiple sequences of points where each sequence individually follows the same algorithm. Therefore, by changing the parameters `initial_points_count` and `iteration_count`, one can create a Sierpinski triangle consisting of n-many points where n is the the product of those variables.

For the simplicity, `initial_points`, $p_0$'s in our algorithm, are chosen as the tip of the equilateral triangle. Then, we create `initial_points_count`-many sequences of points where each sequence consists of `iteration_count`-many points. At the end, we plot these points using `matplotlib.pyplot`.

Note that you can change the coordinates of the equilateral triangle to literally any other triangle. Also, choosing `initial_points` differently will again result in a Sierpinski triangle. However, changing the initial points $p_0$'s may result in dots scattered within regions that are supposed to be empty.
