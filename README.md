# Project name - Global-Food-Solutions

Global food solutions is an app that allows customers to order food in segovia and deliver it
to their homes or at "food lockers" where they can pick them up.

Our app has three main functions:

1. It gives customers the choice of choosing between a daily or weekly menu.

2. It allows customers to choose between two options between every meal of the day (breakfast,
lunch and dinner), including a vegan option.

3. It finds the shortest route to deliver to a certain customer in Segovia from his actual location.


# Installation

To be able to run our program, make sure you have the following things installed:

- Python programming language - It will work in all versions between 3.6 and 3.9.
- Libraries - In order to run our program, we make use of the following library: heapq
To download the library type the following command:
pip install heapq_max

After having python installed in the correct version and loading the libraries, open the file
main_interface.py and run the program. It is important to mention that our code is divided in three sections:

1. The first one is user interface where they can order.
2. Then we also added the algorithm we used to situate the food lockers in the most efficient spots (food_lockers.py).
3. Finally, the third part is the algorithm that finds the shortest path when delivering through Segovia (delivery.py).

# Usage

By running the main interface section, the user will experience our app.
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
2. Lockers: The algorithm used to position our lockers through Segovia
3. Delivery: The algorithm to find the shortest path for delivering the orders.
  
The algorithm used for positioning the lockers is the Greedy algorithm.

It’s functionality is to provide us with the minimum amount of lockers needed to cover all the neighborhoods to maximize our efficiency.
It will not be user-oriented because it is of no use to the user, however, it’s very useful for us though as it will save us a lot of money 
but it only needs to be used once. It is important to mention that it must be updated and reused if we move to new locations or we want a different level of specificity (we want to have a locker close to every street instead of to every neighborhood). 
This algorithm is configured by setting all the possible lockers and which neighborhoods they are connected to, and output is the minimum amount of lockers that covers all the neighborhoods. It doesn’t require any inputs. 

The algorithm used to find delivery routes is weighted graphs.

The point of the weighted graphs is to provide us with the shortest path to deliver the packages to the subscribers. The nodes represent the homes to deliver the packages to and the arrows are the distances between the houses. Then you are able to calculate the shortest path from node A which represents the head kitchen to any of the other houses that ask for orders, that way our orders are delivered efficiently and no one has to receive cold food or their food late. Obviously
this is for deliveries at home, if not, the same applies to deliver to the food lockers.

# Credits

The developers of this project are:

- Martín Retortillo, Antón
- Martos, Borja
- Pérez Hernández, Enrique
- Schoettel, Adrian
- Shehadeh, Talal
- von Sanden, Karl
