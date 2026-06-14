const STORAGE_KEY = "contract_system_contracts";

let allContracts = [];

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function loadContractsFromStorage() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        allContracts = raw ? JSON.parse(raw) : [];
    } catch {
        allContracts = [];
    }

    renderContracts(allContracts);
}

function saveContracts() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(allContracts));
}

function showError(message) {
    document.getElementById("formError").textContent = message;
}

function renderContracts(contracts) {
    const table = document.getElementById("contractsTable");
    table.innerHTML = "";
    document.getElementById("contractsCount").textContent = contracts.length;

    contracts.forEach((contract) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${escapeHtml(contract.number)}</td>
            <td>${escapeHtml(contract.title)}</td>
            <td>${escapeHtml(contract.contractor)}</td>
            <td>${escapeHtml(contract.amount)}</td>
            <td><span class="status">${escapeHtml(contract.status)}</span></td>
            <td>
                <button class="delete-btn" data-number="${escapeHtml(contract.number)}">
                    Удалить
                </button>
            </td>
        `;
        table.appendChild(row);
    });

    table.querySelectorAll(".delete-btn").forEach((button) => {
        button.addEventListener("click", () => {
            deleteContract(button.dataset.number);
        });
    });
}

function searchContracts() {
    const text = document.getElementById("searchInput").value.toLowerCase();
    const filtered = allContracts.filter(
        (contract) =>
            contract.number.toLowerCase().includes(text) ||
            contract.title.toLowerCase().includes(text)
    );
    renderContracts(filtered);
}

function addContract() {
    showError("");

    const number = document.getElementById("number").value.trim();
    const title = document.getElementById("title").value.trim();
    const contractor = document.getElementById("contractor").value.trim();
    const amountValue = document.getElementById("amount").value.trim();

    if (!number || !title || !contractor || !amountValue) {
        showError("Заполните все поля.");
        return;
    }

    const amount = parseFloat(amountValue);
    if (Number.isNaN(amount)) {
        showError("Сумма должна быть числом.");
        return;
    }

    if (allContracts.some((contract) => contract.number === number)) {
        showError("Договор с таким номером уже существует.");
        return;
    }

    allContracts.push({
        number,
        title,
        contractor,
        amount,
        status: "Активен",
        created_at: new Date().getFullYear().toString(),
        end_date: (new Date().getFullYear() + 1).toString(),
    });

    saveContracts();
    document.getElementById("number").value = "";
    document.getElementById("title").value = "";
    document.getElementById("contractor").value = "";
    document.getElementById("amount").value = "";
    searchContracts();
}

function deleteContract(number) {
    allContracts = allContracts.filter((contract) => contract.number !== number);
    saveContracts();
    searchContracts();
}

document.getElementById("addBtn").addEventListener("click", addContract);
document.getElementById("searchInput").addEventListener("keyup", searchContracts);

loadContractsFromStorage();
