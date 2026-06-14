from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from database import engine, Base
from api import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>

    <html lang="ru">

    <head>

        <meta charset="UTF-8">

        <title>Система договоров</title>

        <style>

            body{
                font-family: Arial;
                background:#eef2f7;
                margin:0;
                padding:0;
            }

            header{
                background:#2c3e50;
                color:white;
                padding:20px;
                text-align:center;
                font-size:28px;
                font-weight:bold;
            }

            .container{
                width:90%;
                margin:auto;
                margin-top:30px;
            }

            .stats{
                display:flex;
                gap:20px;
                margin-bottom:20px;
            }

            .stat-card{
                flex:1;
                background:white;
                padding:20px;
                border-radius:12px;
                box-shadow:0 2px 10px rgba(0,0,0,0.1);
                text-align:center;
            }

            .stat-number{
                font-size:32px;
                font-weight:bold;
                color:#27ae60;
            }

            .card{
                background:white;
                padding:20px;
                border-radius:12px;
                box-shadow:0 2px 10px rgba(0,0,0,0.1);
                margin-bottom:20px;
            }

            h2{
                margin-top:0;
                color:#333;
            }

            .form{
                display:grid;
                grid-template-columns: repeat(4, 1fr);
                gap:10px;
            }

            input{
                padding:12px;
                border:1px solid #ccc;
                border-radius:8px;
                font-size:14px;
            }

            .search{
                width:100%;
                margin-bottom:20px;
                padding:14px;
                border-radius:10px;
                border:1px solid #ccc;
                font-size:16px;
            }

            button{
                padding:12px;
                border:none;
                border-radius:8px;
                cursor:pointer;
                font-size:14px;
                color:white;
            }

            .add-btn{
                grid-column: span 4;
                background:#27ae60;
            }

            .add-btn:hover{
                background:#219150;
            }

            .delete-btn{
                background:#e74c3c;
            }

            .delete-btn:hover{
                background:#c0392b;
            }

            table{
                width:100%;
                border-collapse:collapse;
                margin-top:20px;
            }

            table th,
            table td{
                padding:14px;
                border-bottom:1px solid #ddd;
                text-align:left;
            }

            table th{
                background:#34495e;
                color:white;
            }

            tr:hover{
                background:#f5f5f5;
            }

            .status{
                padding:6px 10px;
                border-radius:6px;
                color:white;
                background:#27ae60;
                display:inline-block;
            }

        </style>

    </head>

    <body>

        <header>
            Система учета договоров
        </header>

        <div class="container">

            <div class="stats">

                <div class="stat-card">
                    <div class="stat-number" id="contractsCount">0</div>
                    <div>Всего договоров</div>
                </div>

            </div>

            <div class="card">

                <h2>Добавить договор</h2>

                <div class="form">

                    <input id="number" placeholder="Номер договора">

                    <input id="title" placeholder="Название">

                    <input id="contractor" placeholder="Контрагент">

                    <input id="amount" placeholder="Сумма">

                    <button class="add-btn" onclick="addContract()">
                        Добавить договор
                    </button>

                </div>

            </div>

            <div class="card">

                <h2>Поиск договоров</h2>

                <input
                    class="search"
                    id="searchInput"
                    onkeyup="searchContracts()"
                    placeholder="Введите номер или название договора..."
                >

            </div>

            <div class="card">

                <h2>Список договоров</h2>

                <table>

                    <thead>

                        <tr>
                            <th>Номер</th>
                            <th>Название</th>
                            <th>Контрагент</th>
                            <th>Сумма</th>
                            <th>Статус</th>
                            <th>Действия</th>
                        </tr>

                    </thead>

                    <tbody id="contractsTable">

                    </tbody>

                </table>

            </div>

        </div>

        <script>

        let allContracts = []


        async function loadContracts() {

            const response = await fetch('/contracts/')

            const contracts = await response.json()

            allContracts = contracts

            renderContracts(contracts)
        }


        function renderContracts(contracts){

            const table = document.getElementById('contractsTable')

            table.innerHTML = ''

            document.getElementById('contractsCount').innerText =
                contracts.length

            contracts.forEach(contract => {

                table.innerHTML += `
                    <tr>
                        <td>${contract.number}</td>
                        <td>${contract.title}</td>
                        <td>${contract.contractor}</td>
                        <td>${contract.amount}</td>

                        <td>
                            <span class="status">
                                ${contract.status}
                            </span>
                        </td>

                        <td>
                            <button
                                class="delete-btn"
                                onclick="deleteContract('${contract.number}')"
                            >
                                Удалить
                            </button>
                        </td>

                    </tr>
                `
            })
        }


        function searchContracts(){

            const text = document
                .getElementById('searchInput')
                .value
                .toLowerCase()

            const filtered = allContracts.filter(contract =>

                contract.number.toLowerCase().includes(text)
                ||
                contract.title.toLowerCase().includes(text)

            )

            renderContracts(filtered)
        }


        async function addContract() {

            const contract = {

                number: document.getElementById('number').value,

                title: document.getElementById('title').value,

                contractor: document.getElementById('contractor').value,

                amount: parseFloat(
                    document.getElementById('amount').value
                ),

                status: "Активен",

                created_at: "2025",

                end_date: "2026"
            }

            await fetch('/contracts/', {

                method:'POST',

                headers:{
                    'Content-Type':'application/json'
                },

                body: JSON.stringify(contract)
            })

            loadContracts()
        }


        async function deleteContract(number) {

            await fetch(`/contracts/${number}`, {

                method:'DELETE'

            })

            loadContracts()
        }

        loadContracts()

        </script>

    </body>

    </html>
    """
