from models import ContractCreate
from repository import add_contract, get_contracts, delete_contract

def create_contract(contract: ContractCreate):
    for c in get_contracts():
        if c.number == contract.number:
            return None

    return add_contract(contract)

def list_contracts():
    return get_contracts()

def remove_contract(number: str):
    result = delete_contract(number)

    return result

def update_contract(number: str, updated_data: ContractCreate):
    contracts = get_contracts()

    for contract in contracts:
        if contract.number == number:

            contract.title = updated_data.title
            contract.contractor = updated_data.contractor
            contract.amount = updated_data.amount
            contract.status = updated_data.status
            contract.created_at = updated_data.created_at
            contract.end_date = updated_data.end_date

            return contract

    return None
