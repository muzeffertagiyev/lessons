document.addEventListener('DOMContentLoaded',()=>{

    document.querySelector('select').onchange=function(){
        document.querySelector('h1').style.fontSize=this.value;
    };




    document.querySelectorAll('button').forEach(function(button){
        button.onclick=function(){
            document.querySelector('h1').style.color=button.dataset.color;
        };
    });

});



// document.addEventListener('DOMContentLoaded',()=>{
//     document.querySelector('#red').onclick=function(){
//         document.querySelector('h1').style.color='red';

//     };
//     document.querySelector('#blue').onclick=function(){
//         document.querySelector('h1').style.color='blue';
//     };
//     document.querySelector('#green').onclick=function(){
//         document.querySelector('h1').style.color='green';
//         document.querySelector('h1').style.fontSize='35px';
//         document.querySelector('h1').style.backgroundColor='yellow';
//     };



// });