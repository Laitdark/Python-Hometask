var cartContent = [];
function getButtons() {
    var buttons = document.getElementsByTagName("button");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].onclick = act;
    }
}


function getCart() {
    var cart = document.getElementById("cart");
    var list = document.createElement("div");
    var smallImage = document.createElement("img");
    var nameOfChosen = document.createElement("p");
    var ammount = document.createElement("p");
    var minus = document.createElement("button");
    var count = document.createElement("p");
    var plus = document.createElement("button");
    var sum = document.createElement("p");
    var totalItem = document.createElement("p");
    var totalCart = 0;
    var outputResult = document.createElement("p");


    cart.innerHTML = "";

    for (var i = 0; i < cartContent.length; i += 4) {
        if (cartContent[i + 2] == 0) {
            cartContent.splice(i, 4)
            i -= 4;
            continue;
        }
        else {
            list.innerHTML = "";
            smallImage.src = cartContent[i];
            nameOfChosen.innerHTML = cartContent[i + 1];
            ammount.innerHTML = "Ammount: ";
            minus.innerHTML = "-";
            minus.className = "minus";
            count.innerHTML = cartContent[i + 2];
            plus.innerHTML = "+";
            plus.className = "plus";
            sum.innerHTML = "Price per Item: " + cartContent[i + 3] + " UAH";
            totalItem.innerHTML = "Full Price: " + (cartContent[i + 2] * cartContent[i + 3]) + " UAH";
            totalCart += (cartContent[i + 2] * cartContent[i + 3]);

            list.appendChild(smallImage);
            list.appendChild(nameOfChosen);
            list.appendChild(ammount);
            list.appendChild(minus);
            list.appendChild(count);
            list.appendChild(plus);
            list.appendChild(sum);
            list.appendChild(totalItem);

            cart.innerHTML += list.outerHTML;
        }
    }
    if (cart.innerHTML == "") {
        outputResult.innerHTML = "Your cart is currently empty"
    }
    else {
        outputResult.innerHTML = "Value of the cart: " + totalCart + " UAH"
    }
    cart.appendChild(outputResult);
    getButtons();
}

function act(event) {
    switch (event.target.className) {
        case "minus":
            cartContent[cartContent.indexOf(event.target.parentElement.children[1].innerHTML) + 1] -= 1;
            break;
        case "plus":
            cartContent[cartContent.indexOf(event.target.parentElement.children[1].innerHTML) + 1] += 1;
            break;
        case "compCart":
            caseAccordion("compCart");
            break;
        case "comments":
            caseAccordion("comments");
            break;
        case "address":
            caseAccordion("address");
            break;
        default:
            if (cartContent.indexOf(event.target.parentElement.children[1].innerHTML) == -1) {
                cartContent.push(event.target.parentElement.children[0].src);
                cartContent.push(event.target.parentElement.children[1].innerHTML);
                cartContent.push(1);
                cartContent.push(+(event.target.parentElement.children[3].innerHTML.substr(0, (event.target.parentElement.children[3].innerHTML.length - 4))));
            }
            else {
                cartContent[cartContent.indexOf(event.target.parentElement.children[1].innerHTML) + 1] += 1;
            }
    }
    getCart();

}
function caseAccordion(acc) {
    switch (acc) {
        case 'compCart':
            var elemone = document.getElementById("compCart");
            elemone.style.display = "block";
            var elemtwo = document.getElementById("address");
            elemtwo.style.display = "none";
            var elem = document.getElementById("comments");
            elemthree.style.display = "none";
            break;
        case 'address':
            var elemone = document.getElementById("address");
            elemone.style.display = "block";
            var elemtwo = document.getElementById("compCart");
            elemtwo.style.display = "none";
            var elemthree = document.getElementById("comments");
            elemthree.style.display = "none";
            break;
        case 'comments':
            var elemone = document.getElementById("comments");
            elemone.style.display = "block";
            var elemtwo = document.getElementById("address");
            elemtwo.style.display = "none";
            var elemthree = document.getElementById("compCart");
            elemthree.style.display = "none";
            break;
    }
    acc = ''
}

window.onload = getCart;