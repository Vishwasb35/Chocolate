
---

Chocolate House Application

This Python application simulates a fictional chocolate house that manages:

Seasonal flavor offerings: Tracks seasonal chocolate flavors available at different times of the year.

Ingredient inventory: Manages inventory of ingredients like cocoa, milk, etc.

Customer flavor suggestions and allergy concerns: Collects customer feedback on flavor ideas and tracks any allergy concerns.


The application uses SQLite as the database backend for storing the data.

Features

Add, view, and manage seasonal flavor offerings.

Track ingredient inventory, including quantity.

Collect customer suggestions for new chocolate flavors, along with any allergy concerns.



---

Table of Contents

Requirements

Setup Instructions

Running the Application

Running with Docker

Testing

SQL Queries

Notes



---

Requirements

Python 3.x or higher

SQLite (comes pre-installed with Python)

Docker (optional for containerization)



---

Setup Instructions

1. Clone the repository:

git clone https://github.com/yourusername/chocolate-house.git
cd chocolate-house


2. Install dependencies:

The project uses Python dependencies listed in requirements.txt. Install them using pip:

pip install -r requirements.txt




---

Running the Application

1. Run the application directly:

After installing the dependencies, you can run the application as follows:

python app.py

This will:

Initialize the SQLite database with the required tables.

Add some sample data for seasonal flavors, ingredients, and customer suggestions.

Display the data in the terminal.





---

Running with Docker

If you prefer to run the application in a containerized environment, follow these steps.

1. Build the Docker image:

First, build the Docker image using the Dockerfile:

docker build -t chocolate-house .


2. Run the Docker container:

Once the image is built, run the container:

docker run -p 5000:5000 chocolate-house

This will run the application inside a Docker container.




---

Testing

The project includes basic unit tests to validate the functionality of the application.

1. Run the tests:

The tests are located in the test/ directory. To run the tests, use the following command:

python -m unittest test/test_app.py

This will run the test suite and output the results in the terminal.




---

SQL Queries

Here are some SQL queries you can run to manually interact with the database.

Fetch all seasonal flavors:

SELECT * FROM seasonal_flavors;

Fetch all ingredients:

SELECT * FROM ingredients;

Fetch all customer suggestions:

SELECT * FROM customer_suggestions;



---

Notes

1. Database Initialization: When the application starts, the database (chocolate_house.db) is created if it doesn't already exist. It contains three tables:

seasonal_flavors: Stores details about seasonal chocolate flavors.

ingredients: Tracks ingredient inventory and quantities.

customer_suggestions: Stores feedback from customers, including flavor suggestions and allergy concerns.



2. Customization: You can easily modify the app.py and database.py files to add new features or adjust the application's behavior, such as adding new tables or modifying the existing ones.


3. Development: If you want to develop further, you can add more features, such as integrating a web framework like Flask or FastAPI, or creating a front-end to allow customers to submit flavor suggestions through a web interface.


4. SQLite: SQLite is used for simplicity in this project. In a production environment, you may want to replace it with a more scalable database system like PostgreSQL or MySQL.




---

Example Data

Here are some example outputs you might see when running the application:

Seasonal Flavors:

Pumpkin Spice - A warm seasonal flavor with cinnamon and pumpkin (Available from 2024-10-01 to 2024-12-31)
Mint Chocolate - A refreshing mint paired with rich chocolate (Available from 2024-11-01 to 2024-12-31)

Ingredients:

Cocoa - Quantity: 100
Milk - Quantity: 50

Customer Suggestions:

John Doe suggests Caramel Sea Salt (Allergies: Peanuts)


---

Folder Structure

Here is a breakdown of the project folder structure:

chocolate_house/
│
├── app.py                # Main Python application logic
├── database.py           # SQLite database connection and queries
├── models.py             # ORM-style models for database (optional but good for clarity)
├── requirements.txt      # Required Python libraries
├── Dockerfile            # Dockerfile for containerizing the app
├── README.md             # Documentation and instructions for running the app
└── test/
    └── test_app.py       # Unit test file for validation


---

License

This project is open-source and available under the MIT License. See the LICENSE file for more details.


---

This README.md provides all the necessary details for anyone to set up, run, and understand the Chocolate House application. You can modify the project further and add additional features as needed.


