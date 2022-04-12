const questions=document.querySelectorAll('.question');




document.addEventListener('DOMContentLoaded',function(){
    questions.forEach(function(question){
        const btn=question.querySelector('.question-btn');
        
        btn.onclick=function(){
            questions.forEach(function(item){
                if(item!==question){
                    item.classList.remove('show-text')
                }
            })
            question.classList.toggle('show-text');
        }

    });

});


//TOGGLE METHOD

// const btns=document.querySelectorAll('.question-btn');

// document.addEventListener('DOMContentLoaded',function(){
//     btns.forEach(function(btn){
//         btn.onclick=function(forbtns){
//             const question=forbtns.currentTarget.parentElement.parentElement
//             question.classList.toggle('show-text')
//         }
//     })
// })

