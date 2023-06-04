import requests
import sqlite3

# Gets IP address of the user
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

# Gets data by taking IP as an input
def get_data(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    data = {
        "ip": ip_address,
        "version": response.get('version') or "N/A",
        "city": response.get("city") or "N/A",
        "region": response.get("region") or "N/A",
        "country": response.get("country_name") or "N/A",
        "latitude": response.get("latitude") or "N/A",
        "longitude": response.get("longitude") or "N/A",
        "postal": response.get("postal") or "N/A",
        "org": response.get("org") or "N/A",
    }
    add_data(data)
    return data


schema_file_path = "data/schema.sql"
database_file_path = "data/database.db"

# Creates an empty database
def create_db():
    connection = sqlite3.connect(database_file_path)
    with open(schema_file_path) as schema_file:
        schema_commands = schema_file.read().split(';')
        for command in schema_commands:
            command = command.strip()
            if command:
                connection.execute(command)
    connection.commit()
    connection.close()

# Adds data to the database
def add_data(data):
    connection = sqlite3.connect(database_file_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO users (ip, ip_version, city, region, country, latitude, longitude, postal, org) 
        VALUES (:ip, :version, :city, :region, :country, :latitude, :longitude, :postal, :org)
    """, data)
    connection.commit()
    connection.close()

# Gets all the data from the database
def get_db_data():
    connection = sqlite3.connect(database_file_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    connection.close()

    # Convert rows to a list of dictionaries
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in rows]

    return data