const updateHeaderDiv = document.getElementById("update_header");
const headerElement = document.querySelector("header");

updateHeaderDiv.addEventListener("click", function() {
    headerElement.textContent = "New Header!!!";
});
