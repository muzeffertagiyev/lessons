let myLeads=[]


const inputEl=document.querySelector('#input-el');
const ulEl=document.querySelector('#ul-El');
const inputBtn=document.querySelector('#input-btn');
const deleteBtn=document.querySelector('#delete-btn');
const saveTabBtn=document.querySelector('#save-tab-btn')
const leadsFromLocalStorage=JSON.parse(localStorage.getItem('myLeads'))

if (leadsFromLocalStorage){
    myLeads=leadsFromLocalStorage
    render(myLeads)
}

saveTabBtn.addEventListener('click',function(){
    
    chrome.tabs.query({active:true,currentWindow:true},function(tabs){
        myLeads.push(tabs[0].url)
        localStorage.setItem('myLeads',JSON.stringify(myLeads))
        render(myLeads)
    })

});

function render(leads){
    let listItems=''

    for(let i=0;i<leads.length;i++){
        
        listItems+=`
        <li>
            <a id='leads' href='${leads[i]}' target='_blank'>${leads[i]}
            </a>
        </li>`
    }
    ulEl.innerHTML=listItems
}
inputBtn.addEventListener('click',function(){
    myLeads.push(inputEl.value)
    localStorage.setItem('myLeads',JSON.stringify(myLeads))

    render(myLeads)
    inputEl.value=''
})
deleteBtn.addEventListener('dblclick',function(){
    let proceed=confirm('Are you sure? Do you really want to delete all Leads?');
    let text='You deleted all items';
    if (proceed){
        localStorage.clear()
        myLeads=[]
        ulEl.innerHTML=text   
    }
    else{

    }
})








