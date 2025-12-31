# Sales Lead Tracker - Simple CRM Tool
# Track leads, update status, calculate pipeline value

leads = [
    ["John Smith", "Acme Corp", "john@acme.com", "New", 50000],
    ["Sarah Lee", "TechStart", "sarah@techstart.com", "Contacted", 75000],
    ["Mike Chen", "Global Inc", "mike@global.com", "Proposal", 100000],
    ["Emma Wilson", "StartupX", "emma@startupx.com", "Won", 30000],
    ["David Brown", "Enterprise Co", "david@enterprise.com", "Lost", 60000]
]

# Headers for clarity
HEADERS = ["Name", "Company", "Email", "Status", "Value ($)"]

STATUSES = ["New", "Contacted", "Proposal", "Won", "Lost"]

def print_leads():
    print("\n" + "="*80)
    print("SALES LEAD TRACKER")
    print("="*80)
    print(f"{HEADERS[0]:<15} {HEADERS[1]:<20} {HEADERS[2]:<25} {HEADERS[3]:<12} {HEADERS[4]:>10}")
    print("-"*80)
    for lead in leads:
        print(f"{lead[0]:<15} {lead[1]:<20} {lead[2]:<25} {lead[3]:<12} ${lead[4]:>9}")
    print("-"*80)

def calculate_pipeline():
    total_pipeline = sum(lead[4] for lead in leads if lead[3] in ["New", "Contacted", "Proposal"])
    won_revenue = sum(lead[4] for lead in leads if lead[3] == "Won")
    print(f"Total Pipeline Value: ${total_pipeline:,}")
    print(f"Won Revenue: ${won_revenue:,}")
    print(f"Conversion Rate: {len([l for l in leads if l[3] == 'Won']) / len(leads) * 100:.1f}%")

def add_lead():
    print("\n--- Add New Lead ---")
    name = input("Name: ")
    company = input("Company: ")
    email = input("Email: ")
    value = int(input("Deal Value ($): "))
    leads.append([name, company, email, "New", value])
    print("Lead added successfully!")

def update_status():
    print_leads()
    index = int(input("\nEnter lead number to update (0 to {}): ".format(len(leads)-1)))
    if 0 <= index < len(leads):
        print(f"\nCurrent status: {leads[index][3]}")
        print("Available: " + ", ".join(STATUSES))
        new_status = input("New status: ").title()
        if new_status in STATUSES:
            leads[index][3] = new_status
            print("Status updated!")
        else:
            print("Invalid status.")
    else:
        print("Invalid number.")

def main():
    print("🧑‍💼 SALES LEAD TRACKER - Welcome to the bag 🧑‍💼\n")
    
    while True:
        print("\nOptions:")
        print("1. View all leads")
        print("2. Add new lead")
        print("3. Update lead status")
        print("4. View pipeline summary")
        print("5. Quit")
        
        choice = input("\nChoose (1-5): ")
        
        if choice == "1":
            print_leads()
        elif choice == "2":
            add_lead()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print_leads()
            calculate_pipeline()
        elif choice == "5":
            print("\nThanks for using the tracker. Go close those deals 💰")
            break
        else:
            print("Invalid choice — try again.")

if __name__ == "__main__":
    main()