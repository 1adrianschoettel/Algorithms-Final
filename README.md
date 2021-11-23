# Project name - Global-Food-Solutions

Global food solutions is an app that allows customers to order food in segovia and deliver it
to their homes or at "food lockers" where they can pick them up.

Our app has three main functions:

1. It gives customers the choice of choosing between a daily or weekly menu.

2. It allows customers to choose between two options between every meal of the day (breakfast,
lunch and dinner), including a vegan option.

3. It finds the shortest route to deliver to all the customers in Segovia at once.


# Installation

To be able to run our program, make sure you have the following things installed:

- Python programming language - It will work in all versions between 3.6 and 3.9.
- Libraries - In order to run our program, we make use of the following library: heapq
To download the library type the following command:
pip install heapq_max

After having python installed in the correct versiona and loading the libraries, open the file
gbs.py and run the program. It is important to mention that our code is divided in three sections:

1. The first one is user interface where they can order.
2. Then we also pasted the algorithm we used to situate the food lockers in the most efficient spots.
3. Finally, the third part is the algorithm that finds the shortest path when delivering through Segovia.

# Usage

When a customer enters our app, they will be welcomed and asked the following:

1. The type of subscription they want:
  They can choose between daily or monthly.
  
2. If they are vegan or not:
  In the case of answering yes, they will be shown the vegan option for that day.
 
3. Next, what day do they want to receive the menu
  The program will display the options for the weekday the user chooses
  
4. The user will be asked to input what option they prefer for each meal
  The system will then print the menu the user has chosen and will inform that the order will be shipped 
  as soon as possible.
  
# Extra Information about other algorithms  

This GitHub repository contains 3 files apart from this one: 
1. Main interface: The code that the customer would use to order
2. 
  
One of the other two algorithms we used is the Greedy algorithm.

It’s functionality is to provide us with the minimum amount of lockers needed to cover all the neighborhoods to maximize our efficiency.
It will not be user-oriented because it is of no use to the user, however, it’s very useful for us though as it will save us a lot of money 
but it only needs to be used once. It is important to mention that it must be updated and reused if we move to new locations or we want a different level of specificity (we want to have a locker close to every street instead of to every neighborhood). 
This algorithm is configured by setting all the possible lockers and which neighborhoods they are connected to, and output is the minimum amount of lockers that covers all the neighborhoods. It doesn’t require any inputs. 

# Credits

The developers of this project are:
Borja Martos
Enrique Pérez Hernández
Antón Martín Retoritillo
Karl von Sanden
Talal Shehadeh
Adrian Schoettel
