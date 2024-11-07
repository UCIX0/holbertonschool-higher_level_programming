const addItemDiv = document.getElementById("add_item");
const myList = document.querySelector(".my_list");

addItemDiv.addEventListener("click", function() {
    const newLi = document.createElement("li");
    newLi.textContent = "Item";
    myList.appendChild(newLi);
});
