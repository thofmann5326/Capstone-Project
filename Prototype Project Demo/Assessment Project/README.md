# Finale Project Overview

## Introduction
Welcome to my application! The problem this app is having a system to track assessments I perform
for customers at my job. This app uses Django and the Rest-API to resolve this problem.

## Features
### Customer Summary

**Purpose**: The Customer Summary view provides a comprehensive overview of a specific customer, including their basic information, assessment summaries, recommendations, and machine inventory.

**Key Features**:
1. **Customer Information**: Displays essential details such as company name, primary location, and assigned alignment engineer and VCIO.
2. **Assessment Summary**: Lists the assessments conducted for the customer, including dates, scores, completion status, and site locations.
3. **Recommendations**: Provides information on recommendations generated from assessments, including names, descriptions, and statuses.
4. **Machine Inventory**: Presents a table of the customer's technology inventory, including device names, types, makes, models, and warranty information.

### Technology Inventory

**Purpose**: The Technology Inventory view offers a detailed list of all technology assets associated with a customer, including devices, their specifications, and warranty information.

**Key Features**:
1. **Device List**: Displays a table of devices in the inventory, including device names, types, makes, models, and warranty information.
2. **Search and Filter**: Allows users to search and filter devices based on various criteria such as device name, type, make, and model.
3. **Detailed Information**: Provides comprehensive details for each device, ensuring users have access to all relevant information.

### Assessment

**Purpose**: The Assessment view allows users to create, edit, and review assessments conducted for a specific customer.

**Key Features**:
1. **Assessment Form**: Provides a form to create or edit assessments, including fields for assessment details such as date, score, completion status, and site location.
2. **Recommendations Integration**: Integrates with the recommendation system to associate recommendations with assessments for better workflow management.
3. **Site Location Selection**: Allows users to select the site location for which the assessment is being conducted.
4. **Data Validation**: Ensures data entered in the assessment form is valid and meets predefined criteria.

These views collectively provide a comprehensive interface for managing customer-related information, technology inventory, and assessment processes within the application.


## Usage
### Installation
To install and run the application locally, follow these steps:
1. Clone or download the repository from GitHub.

2. You will need to naviagte to the same directory as the Manage.py

       cd ".\Prototype Project Demo\Assessment Project\Project Code\src\Assessment\Assessment"

3. Install the necessary dependencies using pip.

        pip install -r requirements.txt

4. Set up the database by running migrations.

        python manage.py makemigrations

        python manage.py migrate

5. Start the Django development server.

        python manage.py runserver

6. Here are links to take you to the views

[Customer Summary](http://127.0.0.1:8000/customer-summary/) | [Technology Inventory](http://127.0.0.1:8000/technology-inventory/) | [Assessment](http://127.0.0.1:8000/assessment/1/edit/)
