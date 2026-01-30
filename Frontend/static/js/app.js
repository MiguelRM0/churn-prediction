
document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/summary")
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent =
             `Total customers: ${data.total_customers}`;
    });

});

document.getElementById("submitButton").addEventListener("click", () =>{
    console.log(document.getElementById('sqlQuery').value)
    document.getElementById('sqlQuery').value = ''
} );


document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Stops page reload!
    
    // const query = document.getElementById('sqlQuery').value;
    // ... your API call here ...
});
// alert("THIS IS THE SERVED JS FILE");
// console.log("JS FILE LOADED");
