function toggle_table() {
    const table = document.getElementById("bookHistoryTable");
    const link = document.getElementById("toggleLink");
    if (table.style.display === "none") {
        table.style.display = "table";
        link.textContent = "Скрыть";
    } else {
        table.style.display = "none";
        link.textContent = "Показать";
    }
}
