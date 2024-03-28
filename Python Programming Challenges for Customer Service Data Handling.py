#Question 3

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def new_ticket(service_tickets, ticket_num, name, issue, status):
    if ticket_num not in service_tickets:
        service_tickets[ticket_num]= {"Customer": name, "Issue": issue, "Status": status}
        print(f"{ticket_num} has been added to the list.")
    else:
        print(f"{ticket_num} already exists")
    

def update_ticket_status(service_tickets, num):
    if service_tickets[num]["Status"] == "open":
        update = {"Status": "closed"}
        service_tickets[num].update(update)
        
    else:
        update = {"Status": "open"}
        service_tickets[num].update(update)

    print(f"{num} has been updated.")

def display_tickets(service_tickets):
    for tickets, information in service_tickets.items():
        print(f"{tickets}:")
        for x, y in information.items():
            print(f"-   {x}: {y}")

new_ticket(service_tickets, "Ticket003", "David", "Invalid User name", "closed")
update_ticket_status(service_tickets, "Ticket001")
display_tickets(service_tickets)