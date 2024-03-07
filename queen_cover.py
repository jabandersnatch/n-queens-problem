"""
This script solves the minimum queen cover problem using Pyomo in a class-based structure.
Description: 
Given a chessboard of size 8 x 8, the goal is to place the minimum number of queens such that every
square is attacked by at least one queen.

Created on Mon March 25 17:07:12 2024

@author:
    Juan Andrés Méndez Galvis
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


class QueenCoverSolver:
    """
    Class to solve the minimum queen cover problem using Pyomo.

    Given a chessboard of a specified size (default 8 x 8), the goal is to place
    the minimum number of queens such that every square is attacked by at least one queen.
    """

    def __init__(self, board_size=8):
        """
        Initialize the solver with a given board size.

        Args:
            board_size (int): Size of the chessboard (default is 8).
        """
        self.board_size = board_size
        self.coverage_matrix = {}
        self.model = None

    def generate_coverage_matrix(self):
        """
        Calculates which squares each queen can attack on a chessboard.

        Returns:
            dict: A dictionary representing the coverage matrix. Keys are (square1, square2)
                  tuples, and values are 1 if a queen placed on square2 can attack square1, 0 otherwise.
        """
        coverage_matrix = {}
        # TODO: Implement the algorithm to compute the coverage matrix.
        # Hint: Queens can attack horizontally, vertically, and diagonally.
        self.coverage_matrix = coverage_matrix
        return coverage_matrix

    def create_pyomo_model(self, coverage_matrix):
        """
        Creates the Pyomo model for the queen placement problem.

        Args:
            coverage_matrix (dict): The coverage matrix computed for the chessboard.

        Returns:
            ConcreteModel: A Pyomo ConcreteModel representing the problem.
        """
        model = ConcreteModel()

        # TODO: Implement the Pyomo model for the queen placement problem.
        # Define the set of squares on the board.
        # Hint: Remeber not because the board is essentially a 2D grid means that your set size should behave like a 2D grid.

        # Define binary decision variables.

        # Define the objective function: minimize the total number of queens placed.

        # Define constraints

        self.model = model
        return model

    def solve_and_visualize(self):
        """
        Solves the Pyomo model and visualizes the queen placements.

        This method should:
         - Solve the model using a specified solver (e.g., 'glpk').
         - Print the objective function value.
         - Extract the solution and visualize the queen placements using the
           'visualize_queens' function.
        """
        if self.model is None:
            raise ValueError("The model has not been created. Run create_pyomo_model() first.")

        solver = SolverFactory("glpk")
        results = solver.solve(self.model, tee=True)

        print("Objective function value: ", self.model.obj())
        print("Results:", results)

        queens = []
        for i in self.model.squares:
            if self.model.x[i]() == 1:
                pos = (i - 1) % 8, (i - 1) // 8  # Convert to chess notation
                queens.append(chr(pos[0] + 97) + str(pos[1] + 1))

        visualize_queens(queens)


if __name__ == "__main__":
    solver = QueenCoverSolver(board_size=8)
    start_time = time.time()
    coverage_matrix = solver.generate_coverage_matrix()
    print("Coverage matrix computed in:", time.time() - start_time, "seconds")

    model = solver.create_pyomo_model(coverage_matrix)

    solver.solve_and_visualize()
