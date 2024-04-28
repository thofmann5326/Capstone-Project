import random
import sqlite3
import string
from datetime import datetime, timedelta

# Path to the SQLite database file
db_path = r'.\Prototype Project Demo\Assessment Project\Project Code\src\Assessment\Assessment\db.sqlite3'

try:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database")
except sqlite3.Error as e:
    print("Error connecting to SQLite database:", e)
    # Exit the script or handle the error accordingly


def random_date(start_date, end_date):
    # Generate a random date between start_date and end_date
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate projects


def generate_projects(customer_id, num_projects):
    # Generate project records for the given customer
    for _ in range(num_projects):
        name = f"Project {_+1}"
        status = random.choice(["In Progress", "Completed", "On Hold"])
        cost = random.randint(1000, 100000)
        description = f"Description for {name}"
        completion_date = random_date(
            datetime.now(), datetime.now() + timedelta(days=365))
        # Assuming there are 10 project managers
        project_manager_id = random.randint(1, 10)
        cursor.execute("INSERT INTO AssessmentAPI_project (name, status, cost, description, completion_date, project_manager) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, status, cost, description, completion_date.strftime('%Y-%m-%d'), project_manager_id))
        conn.commit()

# Function to generate proposed projects


def generate_proposed_projects(customer_id, num_proposed_projects):
    # Generate proposed project records for the given customer
    for _ in range(num_proposed_projects):
        name = f"Proposed Project {_+1}"
        completion_date = random_date(
            datetime.now(), datetime.now() + timedelta(days=365))
        description = f"Description for {name}"
        cursor.execute("INSERT INTO AssessmentAPI_proposedproject (name, completion_date, description, customer) VALUES (?, ?, ?, ?)",
                       (name, completion_date.strftime('%Y-%m-%d'), description, customer_id))
        conn.commit()

# Function to generate recommendations


def generate_recommendations(customer_id, num_recommendations):
    # Generate recommendation records for the given customer
    for _ in range(num_recommendations):
        name = f"Recommendation {_+1}"
        # Generate a random completion date between 6 months to 5 years from the current date
        completion_date = datetime.now() + timedelta(days=random.randint(180, 1825))
        # Extract only the date part and format as "YYYY-MM-DD"
        completion_date = completion_date.strftime('%Y-%m-%d')
        description = f"Description for {name}"
        status = random.choice(["Completed", "In Progress", "Approved",
                                "Declined", "On Hold", "Proposed"])
        priority = random.randint(1, 10)
        # Assuming there are 3 assessments per customer
        assessment_id = random.randint(1, 3)
        cursor.execute("INSERT INTO AssessmentAPI_recommendation (name, completion_date, description, status, priority, assessment, customer) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, completion_date, description, status, priority, assessment_id, customer_id))
        conn.commit()

# Function to generate assessments


def generate_assessments(customer_id, num_assessments):
    # Generate assessment records for the given customer
    for _ in range(num_assessments):
        date = random_date(
            datetime.now(), datetime.now() + timedelta(days=365))
        score = random.randint(0, 100)
        percent_complete = random.randint(0, 100)
        comments = f"Comments for assessment {_+1}"
        status = random.choice(
            ["Completed", "In Progress", "On Hold", "Scheduled"])
        site_location = random.choice(["Site A", "Site B", "Site C"])
        # Assuming there are 3 assessment templates
        assessment_template_id = random.randint(1, 3)
        # Assuming there are 3 alignment engineers
        alignment_engineer_id = random.randint(1, 4)
        cursor.execute("INSERT INTO AssessmentAPI_assessment (date, score, percent_complete, comments, status, site_location, assessment_template, alignment_engineer, customer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (date.strftime('%Y-%m-%d'), score, percent_complete, comments, status, site_location, assessment_template_id, alignment_engineer_id, customer_id))
        conn.commit()

# Function to generate technology inventory entries


def generate_serial_number():
    # Generate a random alphanumeric serial number
    serial_length = 10
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(serial_length))

# Function to generate technology inventory entries


def generate_technology_inventory(customer_id, num_entries):
    # Generate technology inventory entries for the given customer
    device_makes = {
        "Server": ["Dell", "HP", "Lenovo", "Cisco", "IBM"],
        "Workstation": ["Dell", "HP", "Lenovo", "Apple", "Microsoft"],
        "Firewall": ["Cisco", "Fortinet", "Juniper", "Palo Alto", "SonicWall"],
        "Switch": ["Cisco", "HP", "Juniper", "Dell", "Ubiquiti"],
        "UPS": ["APC", "Eaton", "CyberPower", "Tripp Lite", "Vertiv"],
        "Other": ["Google", "Amazon", "Microsoft", "Apple", "Samsung"],
        "Unknown": ["Unknown"]
    }
    device_models = {
        "Server": ["PowerEdge", "ProLiant", "ThinkSystem", "UCS", "System x"],
        "Workstation": ["Precision", "Z", "ThinkStation", "iMac", "Surface Studio"],
        "Firewall": ["ASA", "FortiGate", "SRX", "Palo Alto", "NSA"],
        "Switch": ["Catalyst", "ProCurve", "EX", "PowerConnect", "UniFi"],
        "UPS": ["Smart-UPS", "5P", "CyberPower", "Tripp Lite", "Liebert"],
        "Other": ["Pixel", "Echo", "Surface", "iPhone", "Galaxy"],
        "Unknown": ["Unknown"]
    }

    device_types = ["Workstation"] * int(0.8 * num_entries) + \
        ["Server", "Firewall", "Switch", "UPS", "Other", "Unknown"]
    remaining_entries = num_entries - len(device_types)
    remaining_device_types = ["Server", "Firewall",
                              "Switch", "UPS", "Other", "Unknown"]
    for i in range(remaining_entries):
        device_types.append(random.choice(remaining_device_types))

    for device_type in device_types:
        device_index = random.randint(0, len(device_makes[device_type]) - 1)
        device_make = device_makes[device_type][device_index]
        device_model = device_models[device_type][device_index]
        device_name = f"{device_make} {device_model}"
        site_location = random.choice(["Site A", "Site B", "Site C"])
        # Random alphanumeric serial number
        serial_number = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10))
        operating_system = random.choice(["Windows", "Linux", "macOS"])

        date_purchased = random_date(
            datetime.now() - timedelta(days=365*8), datetime.now())
        date_warranty_expired = (
            date_purchased + timedelta(days=365*5)).strftime('%Y-%m-%d')
        age_years = (datetime.now() - date_purchased).days // 365
        date_last_updated = random_date(
            datetime.now() - timedelta(days=365), datetime.now()).strftime('%Y-%m-%d')

        cursor.execute("INSERT INTO AssessmentAPI_technologyinventory (device_name, site_location, type, make, model, serial_number, operating_system, date_purchased, date_warranty_expired, age_years, date_last_updated, customer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (device_name, site_location, device_type, device_make, device_model, serial_number, operating_system, date_purchased.strftime('%Y-%m-%d'), date_warranty_expired, age_years, date_last_updated, customer_id))
        conn.commit()


# Retrieve customer IDs from the database
cursor.execute("SELECT id FROM AssessmentAPI_customer")
customer_ids = [row[0] for row in cursor.fetchall()]

# Generate data for each customer
for customer_id in customer_ids:
    generate_projects(customer_id, 15)
    generate_proposed_projects(customer_id, 10)
    generate_recommendations(customer_id, 6)
    generate_assessments(customer_id, 3)
    generate_technology_inventory(customer_id, 20)

# Close the database connection
conn.close()
