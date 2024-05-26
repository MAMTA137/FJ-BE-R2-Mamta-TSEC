## Personal Finance Tracker - Backend Assignment

Starting Time: 9.00 am, 23rd May.

## Assignment Details
Task is to develop a web application where users can track their income, expenses, and investments. 
Users should be able to get insights and generate reports on their financial standing. 
The development of this project will be phased to ensure structured progress.

## Functionality

User Authentication: Implement user authentication using Django's in-built authentication system. Users should be able to register, log in, and manage their profiles.

Database Structure: Design and implement a well-defined database structure using Django models. The database should support the tracking of various financial details, including:

Income sources and the amount from each source
Expense categories and the amount spent in each
Each transaction should have a date, amount, and a description.

Transaction Management: Allow users to add, edit, and delete income and expense transactions.

Dashboard: Develop a user-friendly dashboard that provides an overview of the user's financial status. The dashboard should include graphical representations of income, expenses, and savings.

Reporting: Enable users to generate reports on their financial data, such as a monthly income vs. expenses report.

Budgeting: Implement a feature that allows users to set budget goals for different expense categories and track their progress.

## Additional Features

OAuth Integration: Integrate OAuth authentication to allow users to sign up using Google through Django Allauth or Google's API client library.

Notification System: Set up a notification system to notify users about budget overruns, etc., using email notifications through Sendgrid or another service.

Database Upgrade: Transition from SQLite to MySQL to enhance the robustness of the database setup.

Expense Splitting: Introduce a feature to split expenses with others and keep track of who owes whom.

Receipt Uploading: Allow users to upload and store receipts for their transactions.

## Tech Stack

Language: Python 3.10
Framework: Django
Frontend: HTML,Tailwind CSS (for styling)
Authentication: OAuth
Database: MySQL


Certainly! Here's the "Getting Started" guide with commands for each step, assuming you're using Django:

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/MAMTA137/FJ-BE-R2-Mamta-TSEC.git
   ```

2. **Create a .env File:**
   - Navigate to the root directory of your Django project.
   - Create a file named `.env`:
     ```
     touch .env
     ```

   **Fill in Environment Variables:**
   - Open the `.env` file in a text editor and add the following environment variables:
     ```
     DATABASE_NAME=<your_database_name>
     DATABASE_USER=<your_database_user>
     DATABASE_PASSWORD=<your_database_password>
     SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<your_google_oauth2_key>
     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<your_google_oauth2_secret>
     EMAIL_HOST_PASSWORD=<your_email_host_password>
     EMAIL_HOST_USER=<your_email_host_user>
     EMAIL_HOST_EMAIL=<your_email_host_email>
     ```

4. **Running the Application**

   **Prerequisites:**
   - Python 3.10+
   - pip (package installer)

   **Virtual Environment Setup:**
   - Create a virtual environment:
     ```
     python -m venv env
     ```

   **Activate the Virtual Environment:**
   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

   **Install Dependencies within the Virtual Environment:**
   - Navigate to the root directory of your Django project.
   - Run the following command to install dependencies listed in your `requirements.txt` file:
     ```
     pip install -r requirements.txt
     ```

   **Run the Application within the Virtual Environment:**
   - Start the Django development server:
     ```
     python manage.py runserver
     ```

   Your Django application should now be running locally. You can access it by navigating to the URL provided by the Django development server.
