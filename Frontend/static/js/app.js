
document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/summary")
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent =
             `Total customers: ${data.total_customers}`;
    });

});


// alert("THIS IS THE SERVED JS FILE");
// console.log("JS FILE LOADED");
