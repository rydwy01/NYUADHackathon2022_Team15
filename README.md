
![Logo](https://i.ibb.co/tbPGLJy/Group-2-1.png)


# Salem Teslam سلم تسلم

Salem Teslam (سلم تسلم) is a mobile application that uses Quantum Computing and google maps API to calculate and output the shortest overall route for multiple deliveries, optimizing delivery time and order. 

## Link to Presentation

- https://docs.google.com/presentation/d/1IvcqOcLi9b86j30i0UjKGVizsd7-bF7zIc280YRzTnQ/edit#slide=id.g121001384d4_2_10


## Problem Statement


Delivery driving accidents are the number one cause of death and disability in the UAE. 
Often times delivery drivers within the UAE are in a rush to deliver food to demanding customers and cram as many orders as possible within the day since they are getting paid by commission. This leads to countless accidents and increase in drivers' unemployment rates.

## Solution

Mobile application for delivery drivers with the following features:
- Driver inputs locations he would like to travel to
- User interface shows a routed map with all the locations in optimal order and distance with estimated duration
- Each time the driver reaches one of the locations, it verifies that he has reached and removes that point from the route.

- The impact of this application is to reduce time taken for drivers to deliver orders and in turn reducing on road stress and hopefully reducing number of motorcycle accidents.

## Software Ingredients

Frontend: Flutter

-Used for the user interface which displays a map, takes in multiple locations as inputs and outputs the optimal route of onto the maps.

Backend: Node.js and Google Maps API

-Used to take in the google maps API and calculates the distance/duration between each pair of locations (nodes) and outputs this data in the form of an adjacency matrix

Quantum Computing Algorithms

-Takes in the number of locations inputted by user and uses them as nodes. The edges between the nodes have weights on them which are the durations between pairs of nodes from the backend.

-Solves Traveling Salesman Problem by transforming the problem into QUBO -> Ising Hamiltonian -> Variational Quantum Eigensolver or Quantum Annealing.

-Outputs optimal order of locations which takes the least time/distance in the form of an ordered array of the numbered nodes.


## Team Members 

- Abdallah Saleh
- Bhavica Mohta
- Nour Abdelmoneim 
- Omar El Herraoui
- Omar Aburish
- Yousra Farhani


## Mentors

- Shoaib Mohammed
- Mousa Farajallah
- David Morcuende
- Sama Kanbour

## Group

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

