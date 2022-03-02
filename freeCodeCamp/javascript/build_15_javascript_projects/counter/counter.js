// set initial value 
let count=0

//value variable
const value=document.querySelector('#value');

//btn variable
const btns=document.querySelectorAll('.btn');

btns.forEach(function(btn){
    btn.addEventListener('click',function(e){
        let style=e.currentTarget.classList;

        if(style.contains('decrease')){
            count--
        }
        else if(style.contains('increase')){
            count++
        }
        else{
            count=0
        }


        if(count<0){
            value.style.color='red'
        }
        if(count>0){
            value.style.color='green'
        }
        if(count===0){
            value.style.color='#222'
        }

        value.textContent=count
    })
})