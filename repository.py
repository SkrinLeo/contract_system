from models import ContractCreate

contracts = []

def add_contract(contract: ContractCreate):
    contracts.append(contract)
    return contract

def get_contracts():
    return contracts

def delete_contract(number: str):
    for i in range(len(contracts)):
        if contracts[i].number == number:
            return contracts.pop(i)

    return None