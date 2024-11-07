document.addEventListener("DOMContentLoaded", function() {
    const myList = document.querySelector(".my_list");

    //add
    document.getElementById("add_item").addEventListener("click", function() {
        const newLi = document.createElement("li");
        newLi.textContent = "Item";
        myList.appendChild(newLi);
    });

    //remove
    document.getElementById("remove_item").addEventListener("click", function() {
        const lastItem = myList.lastElementChild;
        if (lastItem) {
            myList.removeChild(lastItem);
        }
    });

    //clear
    document.getElementById("clear_list").addEventListener("click", function() {
        myList.innerHTML = '';
    });
});
