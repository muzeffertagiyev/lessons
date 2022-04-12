// ****** SELECT ITEMS **********
const alert = document.querySelector('.alert');
const form = document.querySelector('.grocery-form');
const grocery = document.getElementById('grocery');
const submitBtn = document.querySelector('.submit-btn');
const container = document.querySelector('.grocery-container');
const list = document.querySelector('.grocery-list');
const clearBtn = document.querySelector('.clear-btn');

// edit option
let editElement;
let editFlag = false;
let editID = "";

// ****** EVENT LISTENERS **********
document.addEventListener('DOMContentLoaded',function(){
    form.onsubmit = addItem
    clearBtn.onclick = clearItems
})
// ****** FUNCTIONS **********
function addItem(e){
    e.preventDefault();
    const value = grocery.value
    const id = new Date().getTime().toString();
    if(value !== '' && editFlag === false){
        //'add item to the list'
        const element = document.createElement('article')//it creates a tag

        //add class
        element.classList.add('grocery-item')//it adds a class into new created above tag

        // add id 
        const attr = document.createAttribute('data-id');//it creates attribute 
        // Ex. <div class='some'></div> class in here is attribute
        attr.value = id;    //it makes our attribute's value equal to id virable have been writen in above if condition
        element.setAttributeNode(attr);//data-id  attribute with its value will be created inside our element tag(article tag)
        element.innerHTML = `
        <p class="title">${value}</p>
        <div class="btn-container">
            <button type="button" class="edit-btn">
                <i class="fas fa-edit"></i>
            </button>
            <button type="button" class="delete-btn">
                <i class="fas fa-trash"></i>
            </button>
        </div>`
        // append child 
        list.appendChild(element); //it is appending list virable with element's value

        //edit function
        const editBtn = element.querySelector('.edit-btn');
        editBtn.addEventListener('click',editItem)
        // delete function
        const deleteBtn = element.querySelector('.delete-btn');
        deleteBtn.addEventListener('click',deleteItem)
       
        //display alert
        displayAlert('item was aded to the list','success');
        //show container
        container.classList.add('show-container');
        //add to local storage
        addToLocalStorage(id,value);
    
        //set back to default
        setBackToDefault();
    }
    else if(value !== '' && editFlag === true){  //when edititem function was clicked the editflag is equal to true in our funcion 117th line of our code 
        editElement.innerHTML = value
        displayAlert('item was edited','success')
        //edit local storage
        editLocalStorage(editID, value)

        setBackToDefault()
        
    }
    else{
        // console.log('empty_value')
        displayAlert('please enter value', 'danger')
    }
}

//display alert function
function displayAlert(text,action){
    alert.textContent = text
    alert.classList.add(`alert-${action}`)
    //remove alert after some seconds
    setTimeout(function(){
        alert.textContent = ''
        alert.classList.remove(`alert-${action}`)
    },1000)
}

// clear items
function clearItems(){
    const items = document.querySelectorAll('.grocery-item');
    if(items.length > 0){
        items.forEach(function(item){
            list.removeChild(item)
        })
    }
    container.classList.remove('show-container')
    displayAlert('All items were deleted','danger')
    setBackToDefault();
    localStorage.removeItem('list')
}

// delete function
function deleteItem(e){
   const element = e.currentTarget.parentElement.parentElement;
   const id = element.dataset.id
   list.removeChild(element);
   if(list.children.length === 0){//it means that if there is not anytthing inside list then remove show-container
       container.classList.remove('show-container')
   }
   displayAlert('Item were deleted','danger')
   setBackToDefault();

   //remove from local storage
   removeFromLocalStorage(id);
}
//edit function
function editItem(e){
    const element = e.currentTarget.parentElement.parentElement;
    //set edit item
    editElement = e.currentTarget.parentElement.previousElementSibling;
    grocery.value = editElement.innerHTML;
    editFlag = true
    editID = element.dataset.id
    submitBtn.textContent = 'edit'
}

//set back to default
function setBackToDefault(){
    grocery.value = "";
    editFlag = false;
    editID = "";
    submitBtn.textContent = 'submit'; 
};
// ****** LOCAL STORAGE **********
function addToLocalStorage(id, value){
    const grocery = {id:id,value:value};
    let items = getLocalStorage();
    items.push(grocery);
    localStorage.setItem('list',JSON.stringify(items));
}
function removeFromLocalStorage(id){
    let items = getLocalStorage();
    items = items.filter(function(item){
        if(item.id !== id){
            return item
        }
    });
    localStorage.setItem('list',JSON.stringify(items));
}
function editLocalStorage(id,value){

}
function getLocalStorage(){
   return  localStorage.getItem('list')?JSON.parse(localStorage.getItem('list')):[];
}
// ****** SETUP ITEMS **********
