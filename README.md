# Package Delivery System

## Project Overview
This project implements a package delivery routing system for a local delivery company. It demonstrates skills in data structures, algorithms, and object-oriented programming in Python.

## Features
- Efficient package delivery routing using a nearest neighbor algorithm
- Custom hash table implementation for quick package lookup
- Simulation of multiple delivery trucks with different constraints
- Real-time package status updates based on user-specified times
- CSV data parsing for addresses, distances, and package information

## Key Components
1. `main.py`: Contains the core logic for package delivery simulation and user interface
2. `MyHashMap.py`: Implements a custom hash map for efficient package storage and retrieval

## Technologies Used
- Python 3
- CSV file handling
- Object-Oriented Programming
- Data Structures (Hash Maps, Lists)
- Algorithms (Nearest Neighbor)

## How It Works
1. Package data is loaded from CSV files into a custom hash map
2. Three delivery trucks are initialized with specific package loads and constraints
3. A nearest neighbor algorithm determines the most efficient delivery route for each truck
4. Users can check the status of all packages or a specific package at any given time

## Running the Program
1. Ensure you have Python 3 installed on your system
2. Clone this repository to your local machine
3. Navigate to the project directory
4. Run `python main.py` in your terminal
5. Follow the on-screen prompts to interact with the system

## Skills Demonstrated
- Algorithm design and implementation
- Data structure creation and manipulation
- File I/O operations
- Time complexity optimization
- User interface design

## Future Improvements
- Implement a more sophisticated routing algorithm (e.g., genetic algorithm)
- Add a graphical user interface for easier interaction
- Incorporate real-time traffic data for more accurate delivery time estimates
