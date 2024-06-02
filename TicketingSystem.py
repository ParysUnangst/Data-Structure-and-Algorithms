import queue
import time
import threading
from datetime import datetime
import random

# Ticket class to represent each ticket with a number and timestamp
class Ticket:
    def __init__(self, number):
        self.number = number
        self.timestamp = datetime.now()

    def __str__(self):
        return f'Ticket #{self.number} at {self.timestamp}'

# TicketingSystem class to manage the queue of tickets
class TicketingSystem:
    def __init__(self):
        # Initialize a queue to hold the tickets
        self.ticket_queue = queue.Queue()
        self.ticket_number = 0

    def generate_ticket(self):
        # Increment the ticket number for each new ticket
        self.ticket_number += 1
        # Create a new Ticket object
        ticket = Ticket(self.ticket_number)
        # Add the ticket to the queue
        self.ticket_queue.put(ticket)
        # Print the generated ticket details
        print(f'Generated: {ticket}')

    def serve_ticket(self):
        while True:
            # Check if the queue is not empty
            if not self.ticket_queue.empty():
                # Get the next ticket from the queue
                ticket = self.ticket_queue.get()
                # Print the details of the ticket being served
                print(f'Serving: {ticket}')
                # Simulate the time taken to serve the ticket
                time.sleep(random.uniform(0.5, 2.0))
            else:
                # If the queue is empty, wait for a second before checking again
                time.sleep(1)

# Function to simulate generating tickets at random intervals
def generate_tickets(ticketing_system, num_tickets):
    for _ in range(num_tickets):
        # Generate a new ticket
        ticketing_system.generate_ticket()
        # Simulate random arrival intervals between ticket generations
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    # Create an instance of the TicketingSystem
    ticketing_system = TicketingSystem()

    # Number of tickets to generate
    num_tickets = 10

    # Start a separate thread to serve tickets from the queue
    serving_thread = threading.Thread(target=ticketing_system.serve_ticket, daemon=True)
    serving_thread.start()

    # Generate the specified number of tickets
    generate_tickets(ticketing_system, num_tickets)

    # Allow some time for all tickets to be served before ending the program
    time.sleep(20)
