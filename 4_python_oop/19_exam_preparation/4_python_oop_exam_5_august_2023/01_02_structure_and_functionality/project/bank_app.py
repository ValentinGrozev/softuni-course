from typing import List
from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPES_OF_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_TYPES_OF_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        self.granted_loans = 0

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPES_OF_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_TYPES_OF_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPES_OF_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_TYPES_OF_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda lo: lo.__class__.__name__ == loan_type, self.loans))

        if client.__class__.__name__ == "Student" and loan_type != "StudentLoan":
            raise Exception("Inappropriate loan type!")

        if client.__class__.__name__ == "Adult" and loan_type != "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        self.get_granted_loans()
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_sum = sum(sum(loan.amount for loan in c.loans) for c in self.clients)
        average_interest = sum(c.interest for c in self.clients)
        if average_interest == 0:
            average = 0
        else:
            average = average_interest / len(self.clients)

        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {sum(c.income for c in self.clients):.2f}\n"
        result += f"Granted Loans: {self.granted_loans}, Total Sum: {total_sum:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n"
        result += f"Average Client Interest Rate: {average:.2f}"

        return result

    def get_granted_loans(self):
        self.granted_loans += 1
