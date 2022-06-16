const cardsArray = [
    {
        name:'fries',
        img:'images/fries.png'
    },
    {
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'hotdog',
        img:'images/hotdog.png'
    },
    {
        name:'ice-cream',
        img:'images/ice-cream.png'
    },
    {
        name:'milkshake',
        img:'images/milkshake.png'
    },
    {
        name:'pizza',
        img:'images/pizza.png'
    },
    {
        name:'fries',
        img:'images/fries.png'
    },
    {
        name:'cheeseburger',
        img:'images/cheeseburger.png'
    },
    {
        name:'hotdog',
        img:'images/hotdog.png'
    },
    {
        name:'ice-cream',
        img:'images/ice-cream.png'
    },
    {
        name:'milkshake',
        img:'images/milkshake.png'
    },
    {
        name:'pizza',
        img:'images/pizza.png'
    }
]
cardsArray.sort(()=>0.5-Math.random());

const gridDisplay = document.querySelector('#grid');
const result = document.querySelector('#result');
let cardChosen = []
let cardChosenIds = []
let cardsWon = []

function cardsBoard(){
    for(let i=0; i < cardsArray.length; i++){
        const card = document.createElement('img');
        card.setAttribute('src','images/blank.png')
        card.setAttribute('data-id', i)
        card.addEventListener('click',flipCard)
        gridDisplay.append(card)
    }
}

cardsBoard()

function checkMatch(){
    const cards = document.querySelectorAll('#grid img')
    const fstChosenCard = cards[cardChosenIds[0]]
    const sndChosenCard = cards[cardChosenIds[1]]

    if (fstChosenCard == sndChosenCard){
        alert("You have chose same card twice")
        fstChosenCard.setAttribute('src', 'images/blank.png')
        sndChosenCard.setAttribute('src', 'images/blank.png')
    }

    else if (cardChosen[0] == cardChosen[1]){
        alert('Your found a match')
        fstChosenCard.setAttribute('src', 'images/white.png')
        sndChosenCard.setAttribute('src', 'images/white.png')
        fstChosenCard.removeEventListener('click', flipCard)
        sndChosenCard.removeEventListener('click', flipCard)
        cardsWon.push(cardChosen)
        result.textContent = cardsWon.length
    }
    else{
        fstChosenCard.setAttribute('src', 'images/blank.png')
        sndChosenCard.setAttribute('src', 'images/blank.png')
    }
    cardChosen = []
    cardChosenIds = []
    if(cardsWon.length == cardsArray.length/2){
        result.textContent = 'You have matched all images'
    }
}

function flipCard(){
    const cardId = this.getAttribute('data-id')
    cardChosen.push(cardsArray[cardId].name)
    cardChosenIds.push(cardId)
    this.setAttribute('src',cardsArray[cardId].img)
    
    if (cardChosen.length == 2){
        setTimeout(checkMatch,500)

    }
    
}

