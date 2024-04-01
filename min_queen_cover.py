"""
This script solves the minimum queen cover problem using Pyomo.
Description: 
Given a chessboard of size 8 x 8, the goal is to place the minimum
number of queens such that every square is attacked by at least 
one queen.

Created on Mon March 25 17:07:12 2024

@author: Juan Andrés Méndez Galvis
"""

import time

from pyomo.environ import (
    Binary,
    ConcreteModel,
    ConstraintList,
    Objective,
    RangeSet,
    Var,
)
from pyomo.opt import SolverFactory

from queen_mapper import visualize_queens

BOARD_SIZE = 8


def generate_coverage_matrix():
    """Calculates which squares each queen can attack on a chessboard.
    Returns:
        A dictionary representing the coverage matrix. Keys are (square1, square2)
        tuples, and values are 1 if square1 is attacked by a queen on square2, 0 otherwise.
    """
    coverage_matrix = {}
    for i in range(1, (BOARD_SIZE + 1)):
        for j in range(1, (BOARD_SIZE + 1)):
            for k in range(1, (BOARD_SIZE + 1)):
                for l in range(1, (BOARD_SIZE + 1)):
                    if i == k or j == l or abs(i - k) == abs(j - l):
                        coverage_matrix[
                            (BOARD_SIZE * (i - 1) + j, BOARD_SIZE * (k - 1) + l)
                        ] = 1
                    else:
                        coverage_matrix[
                            (BOARD_SIZE * (i - 1) + j, BOARD_SIZE * (k - 1) + l)
                        ] = 0

    return coverage_matrix


def create_pyomo_model(coverage_matrix):
    """Creates the Pyomo model for the queen placement problem."""
    model = ConcreteModel()

    # Sets
    model.squares = RangeSet(1, BOARD_SIZE**2)

    # Variables
    model.x = Var(model.squares, domain=Binary)

    # Objective
    model.obj = Objective(expr=sum(model.x[i] for i in model.squares))

    # Constraints
    model.full_coverage = ConstraintList()
    for i in model.squares:
        model.full_coverage.add(
            sum(model.x[j] for j in model.squares if coverage_matrix[(i, j)] == 1) >= 1
        )

    return model


def solve_and_visualize(model):
    """Solves the Pyomo model and visualizes the results."""
    solver = SolverFactory("glpk")
    results = solver.solve(model)

    print("Objective function value: ", model.obj())
    print("Results:", results)

    queens = []
    for i in model.squares:
        if model.x[i]() == 1:
            pos = (i - 1) % 8, (i - 1) // 8  # Convert to chess notation
            queens.append(chr(pos[0] + 97) + str(pos[1] + 1))

    visualize_queens(queens)


if __name__ == "__main__":
    start_time = time.time()
    queen_coverage_matrix = generate_coverage_matrix()
    end_time_coverage_matrix = time.time()
    model = create_pyomo_model(queen_coverage_matrix)
    end_time_model = time.time()
    solve_and_visualize(model)

    print("Coverage matrix execution time:", end_time_coverage_matrix - start_time)
    print("Total execution time:", end_time_model - start_time)
