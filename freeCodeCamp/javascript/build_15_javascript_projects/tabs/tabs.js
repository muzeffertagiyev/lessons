const about=document.querySelector('.about');
const btns=document.querySelectorAll('.tab-btn');
const contents=document.querySelectorAll('.content');


document.addEventListener('DOMContentLoaded',function(){
    about.onclick=function(e){
        const id=e.target.dataset.id;
        if(id){
            btns.forEach(function(btn){
                btn.classList.remove('active')
                e.target.classList.add('active')
            });
            contents.forEach(function(content){
                content.classList.remove('active')
            })
            const element=document.getElementById(id);
            console.log(element)
            element.classList.add('active');
        }
    }
})