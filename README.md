# README: Queen Mapper and Minimum Queen Cover Solver

## Introduction

This documentation covers the usage of two scripts: `queen_mapper.py` and a Pyomo script for solving the minimum queen cover problem. Both scripts were created by Juan Andrés Méndez and are designed to interact with each other to visualize and solve problems related to the placement of queens on a chessboard.

## Installation of Pygame in Anaconda

Before running `queen_mapper.py`, you need to have Pygame installed. Here is how to install Pygame in an Anaconda environment:

1. Open your Anaconda terminal.
2. Type the following command and press Enter:
   ```
   conda install cogsci::pygame
   ```
3. Wait for the installation to complete.

## Using `queen_mapper.py`

### Description

`queen_mapper.py` visualizes the attack paths of queens on a chessboard. Users can specify the positions of the queens, and the program will highlight the squares under attack. It also checks if all squares are covered by the queens' attack paths.

### How to Run

1. Ensure you have Pygame installed in your environment.
2. Place `queen_mapper.py` in your working directory.
3. Run the script from your terminal or command prompt:
   ```
   python queen_mapper.py
   ```
4. The script will display a window with a chessboard and queens placed on the positions defined in the `queen_positions` list within the script.

### Demo

To run a demo, modify the `queen_positions` list in the `if __name__ == "__main__":` section at the bottom of the script. For example, to place queens at positions a1, g5, f7, and b2, ensure the list is set as follows:

```python
queen_positions = ["a1", "g5", "f7", "b2"]
```

Run the script again to see the updated board.

## Using the Pyomo Script for Minimum Queen Cover

### Description

This script solves the minimum queen cover problem using Pyomo, aiming to place the minimum number of queens on an 8x8 chessboard so that every square is under attack by at least one queen.

### Setup

1. Ensure Pyomo and a suitable solver (like GLPK or CBC) are installed in your environment.
2. Have `queen_mapper.py` in the same directory for visualization purposes.

### How to Run

1. Complete the implementation of `generate_coverage_matrix()` in the Pyomo script to compute which squares can be attacked by each queen.
2. Fill out the `create_pyomo_model()` function with the necessary sets, variables, objective function, and constraints based on the coverage matrix.
3. Run the script from your terminal or command prompt:
   ```
   python queen_cover.py
   ```
4. The script will solve the minimum queen cover problem and then visualize the solution using `queen_mapper.py`.

### Understanding the Flow

1. `generate_coverage_matrix()` computes the attack paths for potential queen placements.
2. `create_pyomo_model(coverage_matrix)` creates the optimization model.
3. `solve_and_visualize(model)` solves the model and displays the resulting queen positions on the chessboard.

### Execution Time Reporting

The script will print the time taken to compute the coverage matrix and the total execution time, providing insights into the computational efficiency of the solution process.

## Conclusion

These scripts offer a comprehensive approach to understanding and solving the minimum queen cover problem on a chessboard, with `queen_mapper.py` providing a visual representation of queen attacks and the Pyomo script offering a mathematical optimization solution.
