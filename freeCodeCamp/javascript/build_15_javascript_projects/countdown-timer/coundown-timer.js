const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const weekdays = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];

const deadline=document.querySelector('.deadline')
const giveawayDate=document.querySelector('.giveaway')
const items=document.querySelectorAll('.deadline-format h4')

let tempDate=new Date()
let tempDay=tempDate.getDate()
let tempYear=tempDate.getFullYear()
let tempMonth=tempDate.getMonth()
// for giveawayDate
// let futureDate=new Date(2022,2,27,12,50,0)

let futureDate=new Date(tempYear,tempMonth,tempDay+10,11,30) //it adds 10 days to current date.

const date=futureDate.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })

const year=futureDate.getFullYear()
const hours=futureDate.getHours()
const minutes=futureDate.getMinutes()
const day=futureDate.getDate()
const month=months[futureDate.getMonth()]
const weekday=weekdays[futureDate.getDay()]

giveawayDate.textContent=`giveaway ends on ${weekday}, ${day} ${month} ${year} ${date}`

//future time in milliseconds 
const futureMilliSecs=futureDate.getTime()

//for remained time function
function getRemainingTime(){
const today=new Date().getTime();
const t=futureMilliSecs-today

// values in milliseconds 
const oneDay=24*60*60*1000;
const oneHour=60*60*1000;
const oneMinute=60*1000;
const oneSecond=1000;

//calculate all values
let days=Math.floor(t/oneDay);
let hours=Math.floor((t%oneDay)/oneHour);
let minutes=Math.floor((t%oneHour)/oneMinute);
let seconds=Math.floor((t%oneMinute)/oneSecond)

function format(i){
  if(i<10){
    return i=`0${i}`
  }
  return i
}
//set values array
const values=[days,hours,minutes,seconds];
items.forEach(function(item,index){
  item.innerHTML=format(values[index])
  
})
if(t<0){
  clearInterval(countdown)
  deadline.innerHTML=`<h4 class="expired">Sorry ,this GiveAway has expired</h4>`;
}
}
//countdown
let countdown=setInterval(getRemainingTime,1000)//it means that remaining time will change every 1000 milliseconds(1sec ) it is what we wanted

getRemainingTime();