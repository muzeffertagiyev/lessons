
let cards=[]

let sum=0

let player={
    name:'Muzeffer',
    chips:140
}

let playerEl=document.getElementById('player-el');

playerEl.innerHTML=player.name+": $"+player.chips

let isAlive=false;
let hasBlackJack=false;
let message=""

let messageEl=document.getElementById('message-el');
let cardsEl=document.querySelector("#cards-el");
let sumEl=document.getElementById('sum-el');

function getRandomCard(){

    let random= Math.floor(Math.random()*13)+1;
    if (random===1){
        return 11
    }
    else if(random>10){
        return 10
    }
    else{
        return random
    }
}

function renderGame(){
    if (sum<=20){
        message="do you want to draw new card?";
    }
    else if (sum===21){
        message="Wohoo! You have got BlackJack";
        
        hasBlackJack=true;
    }
    else{
        message= "You are out of the game"
        isAlive=false;
    }

    cardsEl.textContent="Cards: "
    for(let i=0;i<cards.length;i++){
        cardsEl.textContent+=cards[i]+" "
    }

    sumEl.textContent='Sum:'+sum
    messageEl.textContent=message
}
function newCard(){
    
    if (isAlive === true && hasBlackJack===false){
        let card=getRandomCard();
        sum=sum+card
        cards.push(card)
        renderGame()
    }
}
function startGame(){
    isAlive=true;
    let nmb1=getRandomCard()
    let nmb2=getRandomCard()
    cards=[nmb1,nmb2]
    sum=nmb1+nmb2
    renderGame()
}




