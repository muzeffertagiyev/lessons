const score = document.getElementById('score')
const timeLeft = document.getElementById('time-left')
const squares = document.querySelectorAll('.square')
const mole = document.querySelector('.mole')


let result = 0 ;
let hitPosition;
let currentTime = 60;
let timerId = null;



function randomSquare(){
    squares.forEach(function(square){
        square.classList.remove('mole')
    })
    let randomPosition = squares[Math.floor(Math.random()*9)]
    randomPosition.classList.add('mole')

    hitPosition = randomPosition.id     //we created hit position variable in above and we make 
                                    //equal it to randomPosition.id and then we can use this variable in other places as id
}
squares.forEach(function(square){
    square.addEventListener('mousedown',function(){
        if(square.id == hitPosition){
            result++
            score.textContent = result
            hitPosition = null  //if we click more than once ,it will not get score.only one score
        }
    })
})

function  moveMole(){
    timerId = setInterval(randomSquare,500) //it works as hit position.therefore we can use this variable in other places
}

moveMole()

function countDown(){
    currentTime--
    timeLeft.textContent = currentTime
    if (currentTime == 0){
        clearInterval(countDownTimerId)     //clear interval method only works for variables not for functions 
        clearInterval(timerId)
        alert(`Game is Over.Your final score is ${result}`)
    }
}

let countDownTimerId = setInterval(countDown, 1000)