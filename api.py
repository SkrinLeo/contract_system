from fastapi import APIRouter, HTTPException
from models import ContractCreate
from service import create_contract, list_contracts, remove_contract
from service import update_contract

router = APIRouter()

@router.post("/contracts/")
def add_contract(contract: ContractCreate):
    result = create_contract(contract)

    if result is None:
        raise HTTPException(status_code=400, detail="Договор уже существует")

    return result

@router.get("/contracts/")
def get_all_contract():
    return list_contracts()

@router.delete("/contracts/{number}")
def delete_contract(number: str):
    result = remove_contract(number)

    if result is None:
        raise HTTPException(status_code=404, detail="Договор не найден")

    return {"Сообщение": f"Удалено contract: {result}"}

@router.put("/contracts/{number}")
def update(number: str, contract: ContractCreate):
    result = update_contract(number, contract)

    if result is None:
        raise HTTPException(status_code=404, detail="Договор не найден")

    return result