
// On page load fetch summary data 
document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/summary") // When sending you get a response object
    .then(response => response.json()) // get the json off that response object , a promise 
    .then(data => { // actually use that data to do a task
        document.getElementById("result").textContent =
             `Total customers: ${data.total_customers}`;
    });

});
// 
// On button click fetch table names
document.getElementById("submitButton").addEventListener("click", () =>{
    // Get the SQL query from the input field
    const query = document.getElementById('sqlQuery').value.trim();
    // Basic validation if query is empty
    if (!query) {
        document.getElementById("result").textContent = "Please enter a query.";
        return;
    }

    // Send the SQL query to the backend
    fetch("/api/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: query })
    })
    .then(res => res.json())
    .then(data => {
        console.log("SQL Results:", data.results);

        
        const container = document.getElementById("result");
        container.innerHTML = ""; // Clear previous results

        if(!data.results || data.results.length === 0) {
            container.textContent = "No results found.";
            return
        }

        const table = document.createElement("table");
        table.className = "sql-table";

        const thead = document.createElement("thead");
        const headerRow = document.createElement("tr");

        Object.keys(data.results[0]).forEach(col => {
            const th = document.createElement("th");
            th.textContent = col;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement("tbody");
        data.results.forEach(row => {
            const tr = document.createElement("tr");
            Object.values(row).forEach(val => {
                const td = document.createElement("td");
                td.textContent = val;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        container.appendChild(table);
    })
    .catch(error => {
        document.getElementById("result").textContent = `Error: ${error.message}`;
    });


} );


// On form submit prevent page reload
document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Stops page reload!
    
});
// alert("THIS IS THE SERVED JS FILE");
// console.log("JS FILE LOADED");
