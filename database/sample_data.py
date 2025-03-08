import sqlite3
import random

# Connect to SQLite database
conn = sqlite3.connect('domainRadar.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM domains')
cursor.execute('DELETE FROM user_keywords')

# Insert sample domain data
domains = [
    ('techinnovators.com', '2025-03-03', 'Google Domains', 'tech, innovation', '{"domain_name": "techinnovators.com", "registrar": "Google Domains", "creation_date": "2025-03-03", "expiry_date": "2026-03-03", "owner": "Tech Innovations LLC", "email": "contact@techinnovators.com", "country": "US"}'),
    ('healthsolutions.com', '2025-03-04', 'Tucows Domains Inc.', 'health, solutions', '{"domain_name": "healthsolutions.com", "registrar": "Tucows Domains Inc.", "creation_date": "2025-03-04", "expiry_date": "2026-03-04", "owner": "Health Solutions Ltd.", "email": "info@healthsolutions.com", "country": "GB"}'),
    ('fintechstartups.com', '2025-03-05', 'Dynadot, LLC', 'finance, tech', '{"domain_name": "fintechstartups.com", "registrar": "Dynadot, LLC", "creation_date": "2025-03-05", "expiry_date": "2026-03-05", "owner": "FinTech Ventures", "email": "support@fintechstartups.com", "country": "AU"}'),
    ('greenenergy.com', '2025-03-06', 'NameSilo, LLC', 'energy, green', '{"domain_name": "greenenergy.com", "registrar": "NameSilo, LLC", "creation_date": "2025-03-06", "expiry_date": "2026-03-06", "owner": "Green Energy Corp.", "email": "contact@greenenergy.com", "country": "US"}'),
    ('smartgadgets.com', '2025-03-07', 'IONOS SE', 'tech, gadgets', '{"domain_name": "smartgadgets.com", "registrar": "IONOS SE", "creation_date": "2025-03-07", "expiry_date": "2026-03-07", "owner": "Smart Gadgets Inc.", "email": "support@smartgadgets.com", "country": "DE"}'),
    ('medtechinnovations.com', '2025-03-08', 'Porkbun LLC', 'medical, tech', '{"domain_name": "medtechinnovations.com", "registrar": "Porkbun LLC", "creation_date": "2025-03-08", "expiry_date": "2026-03-08", "owner": "MedTech Innovations", "email": "info@medtechinnovations.com", "country": "US"}'),
    ('wellnesshub.com', '2025-03-09', 'Hostinger, UAB', 'health, wellness', '{"domain_name": "wellnesshub.com", "registrar": "Hostinger, UAB", "creation_date": "2025-03-09", "expiry_date": "2026-03-09", "owner": "Wellness Hub LLC", "email": "contact@wellnesshub.com", "country": "UK"}'),
    ('cybersecuritysolutions.com', '2025-03-10', 'Cloudflare, Inc.', 'security, tech', '{"domain_name": "cybersecuritysolutions.com", "registrar": "Cloudflare, Inc.", "creation_date": "2025-03-10", "expiry_date": "2026-03-10", "owner": "Cyber Security Solutions", "email": "admin@cybersecuritysolutions.com", "country": "US"}'),
]

# Generating 90 more entries
domains_list = [
    'autonomousfuture.ai', 'blockchainpayments.io', 'sustainableliving.org', 'cloudsecurityhub.com', 
    'airoboticslabs.com', 'fitnessgenius.com', 'nextgenbiotech.com', 'quantumcomputinglabs.com', 
    'digitalmarketingedge.com', 'futureofcommerce.com', 'cleantechstartups.net', 'ethicalfashionhub.org', 
    'gamingrevolution.xyz', 'spaceexplorationtech.com', 'supplychainai.io', 'onlineshoppinghub.co', 
    'virtualrealityworlds.com', 'cyberlawconsultants.com', 'deeptechventures.ai', 'renewableresources.net'
]

registrars = ['GoDaddy, LLC', 'Namecheap, Inc.', 'Google Domains', 'Tucows Domains Inc.', 'Dynadot, LLC',
              'NameSilo, LLC', 'IONOS SE', 'Porkbun LLC', 'Hostinger, UAB', 'Cloudflare, Inc.']

industries = ['tech, startup', 'health, wellness', 'finance, tech', 'energy, green', 'security, AI',
              'robotics, automation', 'biotech, pharma', 'cloud, security', 'marketing, digital', 
              'gaming, esports']

countries = ['US', 'CA', 'GB', 'AU', 'DE', 'IN', 'SG', 'JP', 'FR', 'NL']

for i in range(90):
    domain_name = f"{random.choice(domains_list).replace(' ', '').lower()}"
    reg_date = f"2025-03-{random.randint(11, 31):02d}"  # Random date in March 2025
    registrar = random.choice(registrars)
    industry = random.choice(industries)
    country = random.choice(countries)
    
    whois_data = f'''{{
        "domain_name": "{domain_name}",
        "registrar": "{registrar}",
        "creation_date": "{reg_date}",
        "expiry_date": "2026-03-{random.randint(1, 31):02d}",
        "owner": "Company {i+1}",
        "email": "info@{domain_name}",
        "country": "{country}"
    }}'''
    
    domains.append((domain_name, reg_date, registrar, industry, whois_data))

# The list now contains 100 entries

cursor.executemany('''
INSERT INTO domains (domain_name, registration_date, registrar, industry_keywords, whois_data) VALUES (?, ?, ?, ?, ?)
''', domains)

# Define broad categories
broad_categories = [
    'Archiving Service', 'Call Center', 'Collection Agency', 'College Recruiting', 'Courier Service',
    'Debt Collections', 'Delivery', 'Document Preparation', 'Employee Benefits', 'Extermination Service',
    'Facilities Support Services', 'Housekeeping Service', 'Human Resources', 'Knowledge Management',
    'Office Administration', 'Packaging Services', 'Physical Security', 'Project Management', 'Staffing Agency',
    'Trade Shows', 'Virtual Workforce', 'Advertising', 'Agriculture', 'Applications', 'Artificial Intelligence',
    'Bioinformatics', 'Blockchain', 'Apparel', 'E-Commerce', 'Social', 'Consumer Electronics', 'Consumer Goods',
    'Content', 'Data', 'Design', 'Education', 'Energy', 'Events', 'Finance', 'Food and Beverage', 'Gaming',
    'Government', 'Hardware', 'Health Care', 'Information Technology', 'Internet', 'Investment', 'Software',
    'Real Estate', 'Telecommunications', 'Transportation', 'Travel', 'Virtual Reality', 'Web Development'
]

# Insert broad categories into user_keywords
user_keywords = [(1, category) for category in broad_categories] + [(2, category) for category in broad_categories]

cursor.executemany('''
INSERT INTO user_keywords (user_id, keyword) VALUES (?, ?)
''', user_keywords)

# Add broad categories to industries list
industries.extend(broad_categories)

# Commit the changes and close the connection
conn.commit()
conn.close()