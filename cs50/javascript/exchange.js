document.addEventListener('DOMContentLoaded',()=>{

    document.querySelector('form').onsubmit=function(){

        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        .then(response=>response.json())
        .then(data=>{
            const currency=document.querySelector('#currency').value;
            const rate=data.error[currency];

            if(rate !== undefined){
                document.querySelector('#result').innerHTML=rate;
            }
            else{
                document.querySelector('#result').innerHTML="Invalid currency name"
            }

            

        });
        return false; 
  
    }
    
});