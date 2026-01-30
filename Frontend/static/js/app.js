
document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/summary") // When sending you get a response object
    .then(response => response.json()) // get the json off that response object , a promise 
    .then(data => { // actually use that data to do a task
        document.getElementById("result").textContent =
             `Total customers: ${data.total_customers}`;
    });

});

// On button click
document.getElementById("submitButton").addEventListener("click", () =>{
    console.log(document.getElementById('sqlQuery').value)
    document.getElementById('sqlQuery').value = ''

    // Get all the ables in my DataBase 
    fetch("/api/tables")
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent =
            data.map(t => t.table_name).join(", ");
    });
} );



document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Stops page reload!
    
});
// alert("THIS IS THE SERVED JS FILE");
// console.log("JS FILE LOADED");
