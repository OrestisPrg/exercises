let lst = [3,5,12];

function init(){
    let table = document.querySelector('#list');
    lst.forEach((el)=>{
        let cell = document.createElement('td');
        cell.innerText = el;
        cell.style.color = 'white';
        table.appendChild(cell);
    });
    colour();
}

const frm = document.querySelector('.frm');

frm.addEventListener('submit', (e)=> {
    e.preventDefault();

    let txt = document.querySelector("#in");
    let table = document.querySelector('#list');
    if(txt.value != ''){
        let cell = document.createElement('td');
        cell.innerText = txt.value;
        cell.style.color = 'white';
        table.appendChild(cell);
        lst.push(txt.value)
    }
    else{
        alert("Please enter a value");
    }
    colour();
    txt.value = '';
    
});

function colour(){
    let cells = document.querySelector('#list').childNodes;
    for(let i=1;i<=lst.length;i++){
        if (i%3 == 0){
            cells[i].style.backgroundColor= "red";
        }
        else{
            cells[i].style.backgroundColor= "black";    
        }
    }
}