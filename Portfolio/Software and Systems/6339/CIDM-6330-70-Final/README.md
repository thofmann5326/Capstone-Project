# Finale Project Overview

## Introduction
Welcome to my application! The problem this app is having a system to track assessments I perform
for customers at my job. This app uses Django and the Rest-API to resolve this problem.

## Features
### Customer Management
- The application maintains a comprehensive database of customers, including their primary locations, assigned Alignment Engineers, and vCIOs.
- Each customer can have multiple projects, proposed projects, assessments, and recommendations associated with them.

### User Roles
- Three distinct user roles are defined: Alignment Engineer, vCIO, and Project Manager.
- Users are equipped with essential information such as their names, email addresses, and security groups.

### Project Management
- Projects are tracked through their lifecycle, from proposal to completion.
- Proposed projects can be freely created but are typically converted into projects.
- Project details, including status, project manager, cost, and completion date, are efficiently managed within the system.

### Assessment and Recommendation System
- Assessments are performed using predefined templates and are linked to specific customers and site locations.
- Recommendations generated from assessments are categorized based on their priority and status, aiding in effective decision-making.
- Recommendations can be associated with assessments and proposed projects for seamless workflow management.

### Technology Inventory
- Customers' technology inventories are tracked, including details such as device names, types, make, model, and warranty information.
- This data can be imported from external systems or added manually, ensuring accurate and up-to-date records.

## Usage
### Installation
To install and run the application locally, follow these steps:
1. Clone or download the repository from GitHub.
2. Install the necessary dependencies using pip.

        pip install -r requirements.txt

3. Set up the database by running migrations.

        python manage.py makemigrations

        python manage.py migrate

4. Start the Django development server.

        pip install -r requirements.txt