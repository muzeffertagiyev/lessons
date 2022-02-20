const img=[
    'icon.png',
    'icon.png',
    'icon.png'
]

let getImage=document.querySelector('div');


function images(){
    let template=''
    for(let i=0;i<img.length;i++){
        template+=`<img src='${img[i]}'>`
        
    }
    getImage.innerHTML=template
}
images()