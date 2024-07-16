#CS Data Handling App

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
    else:
        print(f"Ticket ID {ticket_id} not found.")
def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details}")

open_ticket("Ticket003", "Charlie", "Order not received")
open_ticket("Ticket004", "Dana", "Account locked")
update_ticket_status("Ticket001", "closed")

print("All tickets:")
display_tickets()

print("\nOpen tickets:")
display_tickets(status="open")
