let saveEl=document.getElementById('save-el');
let countEl=document.getElementById('count-el');
let count=0


function increment(){
    count++
    countEl.textContent=count;


}

function save(){
    let saved=count+" - ";
    saveEl.textContent+=saved;
    countEl.textContent=0;
    count=0;
}



let num1=8;
let num2=2

document.getElementById('num1-el').textContent=num1;
document.getElementById('num2-el').textContent=num2;

let sumEl=document.getElementById('sum-el');

function add(){
    
    sumEl.textContent='Sum:'+(num1+num2);
    
}


function subtract(){
    
    sumEl.textContent='Sum:'+(num1-num2);
}
function divide(){
    sumEl.textContent='Sum:'+(num1/num2);

}
function multiply(){
    sumEl.textContent='Sum:'+(num1*num2);

}