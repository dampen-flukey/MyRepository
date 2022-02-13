function deleteItem(index) {
    console.log("calling delete...", index)
    itemArrayStr = localStorage.getItem("itemsJSON");
    itemArray = JSON.parse(itemArrayStr);
    itemArray.splice(index, 1);
    localStorage.setItem('itemsJSON', JSON.stringify(itemArray));
    display();
}
function clearListFunc() {
    itemArrayStr = localStorage.getItem("itemsJSON");
    itemArray = JSON.parse(itemArrayStr);
    if (localStorage.getItem('itemsJSON') != null && itemArray.length > 0) {
        let result = confirm("Are you sure you want to delete?");
        if (result) {
            //Logic to delete the item
            localStorage.clear();
            display();
        }
    } else {
        confirm("Your List seems empty. click ok to continue..")
    }

}

function display() {
    console.log('calling display..');
    if (localStorage.getItem('itemsJSON') != null && itemArray.length > 0) {
        `<tr>
            <th scope="col">Sl. No.</th>
            <th scope="col">Title</th>
            <th scope="col">Description</th>
            <th scope="col">Action</th>
        </tr>`
    }
    itemArrayStr = localStorage.getItem("itemsJSON");
    itemArray = JSON.parse(itemArrayStr);
    let tableBody = document.getElementById("tableBody");
    let str = "";
    if (itemArray != null && itemArray.length > 0)
        itemArray.forEach((element, index) => {
            str += `<tr>
        <th scope="row">${index + 1}</th>
        <td>${element[0]}</td>
        <td>${element[1]}</td>
        <th><button class="btn btn-sm btn-danger" onclick = "deleteItem(${index})">Delete</button></th>
    </tr>`
        });
    tableBody.innerHTML = str;
}

function additem() {
    console.log("click hua")
}
function update() {

    console.log("updating list....")
    title = document.getElementById("title").value;
    desc = document.getElementById("description").value;
    if (localStorage.getItem("itemsJSON") == null) {
        itemArray = [];
        itemArray.unshift([title, desc]);
        localStorage.setItem("itemsJSON", JSON.stringify(itemArray));
        console.log(`added item with title "${title}" to list.`)
    } else {
        itemArrayStr = localStorage.getItem("itemsJSON");
        itemArray = JSON.parse(itemArrayStr);
        itemArray.unshift([title, desc]);
        localStorage.setItem("itemsJSON", JSON.stringify(itemArray));
        console.log(`added item with title "${title}" to list.`);
    }
    display();
}
itemArrayStr = localStorage.getItem("itemsJSON");
itemArray = JSON.parse(itemArrayStr);
add = document.getElementById("addItem")
add.addEventListener('click', update);
display();
clearList = document.getElementById("clearList");
clearList.addEventListener("click", clearListFunc);
// deleteItem = document.getElementById("deleteItem");
// deleteItem.addEventListener('click', deleteItemFunc);

