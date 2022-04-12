const modelOverlay=document.querySelector('.modal-overlay');

const modalBtn=document.querySelector('.modal-btn');
const closeBtn=document.querySelector('.close-btn');




document.addEventListener('DOMContentLoaded',function(){
    

    modalBtn.onclick=function(){
        
        modelOverlay.classList.add('open-modal')
        
    }

    closeBtn.onclick=function(){
        modelOverlay.classList.remove('open-modal')
    }


})