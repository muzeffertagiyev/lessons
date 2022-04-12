
//Btns
const toggleBtn=document.querySelector('.sidebar-toggle');
const closeBtn=document.querySelector('.close-btn');

//Sidebar 

const sidebar=document.querySelector('.sidebar')



document.addEventListener('DOMContentLoaded',function(){

    toggleBtn.onclick=function(){
        // if(sidebar.classList.contains('show-sidebar')){
        //     sidebar.classList.remove('show-sidebar')
        // }
        // else{
        //     sidebar.classList.add('show-sidebar')
        // }
        sidebar.classList.toggle('show-sidebar')
    }
    closeBtn.onclick=function(){
        sidebar.classList.remove('show-sidebar')
    }

});