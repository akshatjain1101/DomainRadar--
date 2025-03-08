from django.shortcuts import render
import sqlite3 
import os

def home(request):
    # Path to your database file
    db_path = os.path.join(os.path.dirname(__file__), "../database/domainRadar.db")

    # Connecting to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all domain data
    query = "SELECT domain_name, registration_date, registrar, industry_keywords, whois_data FROM domains"
    cursor.execute(query)
    result = cursor.fetchall()  # Fetch all records
    print(result)
    # Closing the connection
    conn.close()

    # Pass data to the template
    return render(request, "dashboard.html", {"domains": result})
