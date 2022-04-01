# NYUADHackathon2022_Team15

## SALEM TESSLAM

Salem Tesslam solves issues of congestion, environmental solution, and , importantly, relieves the pressure of time constraint for delivery drivers looking to make multiple stops that can lead to severe vehicle accidents.  We implement Quantum Computing as a means of getting the fastest, most efficient routes in ways that classical computers couldn't complete within a reasonable amount of time to come up with a solution to the famous, NP-hard, travelling salesman problem.  The user can enter multiple points where they must reach for a dropoff of goods, and our algorithm takes into account all the factors necessary to make their ride quicker, thus discouraging them from weaving in and out of traffic just to get a job done quicker and make more money.  This app will prove to be a fantastic use of a new, innovative technology for social good.

We implemented two quantum algorithms which work on two separate industry quantum computers and use slightly different algorithms to give the user the option to decide between them and compare efficiency of the calculated route: The first uses Amazon Web Server's BraKet framework and solves the TSP using Quantum Annealing and Dwaves, while the second uses IBM's Qiskit framework and incorporates the VQE algorithm.

## AWS BraKet method

We used AWS BraKet to try to solve the TSP.  We first have a long list of import statements in our code which calls in all the necessary libraries to run a quantum computing algorithm in python.  We then have a function in the file **BraKet_tsp.py** that is called with a parameter **map_file**, which will be provided by another file which downloads the google maps API to be displayed on our frontend.  

From there, we load the map data into a pandas array and find the distances between selected dropoff points, and then multiple steps are taken to finalize setting up a graph which contains nodes representing the stopping points along the route and edges connecting all the stopping points for which direct travel between them is possible (i.e. if there are no obstacles that can't be surpassed without going through another designated stopping point) and assigning them weights.

From the completed graph data we are then able to formulate it into a QUBO (Quantum Unconstrained Binary Optimization) formula so that it can be in a format which is applicable to a Quantum Algorithm.

Once we have an actual optimization problem defined in the QUBO form we can convert it to an Ising Hamiltonian in order to make it applied to Quantum waves.

Lastly, we solve our optimization problem using Quantum Annealing and D-wave claculations to select the optimal route for the delvery person to travel.  A list of the optimal order of travel along with it's total distance required to complete the route is returned as the solution and written to a text file **braket_solution.txt**


