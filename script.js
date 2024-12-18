function getInputValues(){
    const num1=parseFloat(document.getElementById('num1').value);
    const num2=parseFloat(document.getElementById('num2').value);
    return { num1, num2};
}

function saskaitit(){
    const{ num1, num2}=getInputValues();
    if(!isNaN(num1)&&!isNaN(num2)) {
        document.getElementById('result').textContent = num1 + num2;
    }else{
        alert('Lūdzu ievadiet darīgus skaitļus');
    }
}
function atnemt(){
    const{ num1, num2}=getInputValues();
    if(!isNaN(num1)&&!isNaN(num2)) {
        document.getElementById('result').textContent = num1 - num2;
    }else{
        alert('Lūdzu ievadiet darīgus skaitļus');
    }
}

function reizinat(){
    const{ num1, num2}=getInputValues();
    if(!isNaN(num1)&&!isNaN(num2)) {
        document.getElementById('result').textContent = num1 * num2;
    }else{
        alert('Lūdzu ievadiet darīgus skaitļus');
    }
}

function dalit(){
    const{ num1, num2}=getInputValues();
    if(!isNaN(num1)&&!isNaN(num2)) {
        document.getElementById('result').textContent = num1 / num2;
    }else{
        alert('Lūdzu ievadiet darīgus skaitļus');
    }
}