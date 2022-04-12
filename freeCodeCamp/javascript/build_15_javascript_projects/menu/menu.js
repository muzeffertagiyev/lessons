const menu = [
  {
    id: 1,
    title: "buttermilk pancakes",
    category: "breakfast",
    price: 15.99,
    img: "./images/item-1.jpeg",
    desc: `I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed `,
  },
  {
    id: 2,
    title: "diner double",
    category: "lunch",
    price: 13.99,
    img: "./images/item-2.jpeg",
    desc: `vaporware iPhone mumblecore selvage raw denim slow-carb leggings gochujang helvetica man braid jianbing. Marfa thundercats `,
  },
  {
    id: 3,
    title: "godzilla milkshake",
    category: "shakes",
    price: 6.99,
    img: "./images/item-3.jpeg",
    desc: `ombucha chillwave fanny pack 3 wolf moon street art photo booth before they sold out organic viral.`,
  },
  {
    id: 4,
    title: "country delight",
    category: "breakfast",
    price: 20.99,
    img: "./images/item-4.jpeg",
    desc: `Shabby chic keffiyeh neutra snackwave pork belly shoreditch. Prism austin mlkshk truffaut, `,
  },
  {
    id: 5,
    title: "egg attack",
    category: "lunch",
    price: 22.99,
    img: "./images/item-5.jpeg",
    desc: `franzen vegan pabst bicycle rights kickstarter pinterest meditation farm-to-table 90's pop-up `,
  },
  {
    id: 6,
    title: "oreo dream",
    category: "shakes",
    price: 18.99,
    img: "./images/item-6.jpeg",
    desc: `Portland chicharrones ethical edison bulb, palo santo craft beer chia heirloom iPhone everyday`,
  },
  {
    id: 7,
    title: "bacon overflow",
    category: "breakfast",
    price: 8.99,
    img: "./images/item-7.jpeg",
    desc: `carry jianbing normcore freegan. Viral single-origin coffee live-edge, pork belly cloud bread iceland put a bird `,
  },
  {
    id: 8,
    title: "american classic",
    category: "lunch",
    price: 12.99,
    img: "./images/item-8.jpeg",
    desc: `on it tumblr kickstarter thundercats migas everyday carry squid palo santo leggings. Food truck truffaut  `,
  },
  {
    id: 9,
    title: "quarantine buddy",
    category: "shakes",
    price: 16.99,
    img: "./images/item-9.jpeg",
    desc: `skateboard fam synth authentic semiotics. Live-edge lyft af, edison bulb yuccie crucifix microdosing.`,
  },
  {
    id: 10,
    title: "quarantine dinner",
    category: "dinner",
    price: 39.99,
    img: "./images/item-10.jpeg",
    desc: `skateboard fam synth authentic semiotics. Live-edge lyft af, edison bulb yuccie crucifix microdosing.`,
  },
];


const sectionCenter=document.querySelector('.section-center');
const btnContainer=document.querySelector('.btn-container')


document.addEventListener('DOMContentLoaded',function(){
  displayMenuItems(menu);
  displayMenuBtns()
});


function displayMenuItems(menuItems){
  let displayMenu=menuItems.map(function(item){  //using map method will show all items of menu.we should put something inside function() to call all items inside list
    return `<article class="menu-item">
              <img src=${item.img} class="photo" alt=${item.title}/>
              <div class="item-info">
                <header>
                  <h4>${item.title}</h4>
                  <h4 class="price">$${item.price}</h4>
                </header>
                <p class="item-text">${item.desc}</p>
              </div>
            </article>`
  });
  
  displayMenu=displayMenu.join(""); //using join method will show all articles.we should put brakets otherwise comma will be written between artiles and html will not work properly
  sectionCenter.innerHTML=displayMenu;
};

function displayMenuBtns(){
  const categories=menu.reduce(function(values,item){//with help of 'reduce' we get unique categories from menu list
    if (!values.includes(item.category)){  //'!' sybmol make 'includes' works oppositly.
      values.push(item.category)
    }
    return values
  },['all']);
  const categoryBtns=categories.map(function(category){
    return `<button class="filter-btn" type="button" data-id=${category}>${category}</button>`
  }).join("")
  btnContainer.innerHTML=categoryBtns


   // filter btn items
  const filterBtns=document.querySelectorAll('.filter-btn')
 
  filterBtns.forEach(function(btn){
    btn.onclick=function(e){
      const category=e.currentTarget.dataset.id;
      const menuCategory=menu.filter(function(menuItem){
        if(menuItem.category===category){
          return menuItem
        }
      })
      if(category==='all'){
        displayMenuItems(menu)
      }
      else{
        displayMenuItems(menuCategory)
      }

                        //working of dataset property:we create data attribute in buttons in html starting with name "data-" and continuning the text you add it like below:
                        //<button data-id="all"> All</button>   giving text will be as "all" like my text in btn tag for making it readable.After "data-" we can add name whatever we want,but this time we will put name "id".
                        //if we name it as data-id then we should use in js as "dataset.id"
                        //text after point should be as we named in html
    };
  })
};