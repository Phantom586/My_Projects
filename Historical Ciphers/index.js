// Retrieving the Plain Text and Key
let inp_1  = document.getElementById("inp_1");
let inp_2 = document.getElementById("inp_2");


// Retrieving the Fields to Display the Outputs
let out = document.getElementById("out");
let t_area = document.getElementById("t_area");
let text = document.getElementById("txt");
let ret = document.getElementById("txt1");
let store = [];


// Regular Expresssion To check for all Alphabets
let letters = /^[A-Za-z]+$/;
// Regular Expression to check for UpperCase Alphabets
let upper = /^[A-Z]+$/;

// Array containing all UpperCase Alphabets
let lst = []
for (let i = 65; i < 91; i++) {
    lst.push(String.fromCharCode(i));
}  



// ------------ Caesar's Cipher Function --------------
function Caesar(c) {
    if (c.match(letters)) {
        c = c.toUpperCase();
        c = (((c.charCodeAt() - 65) + 13) % 26) + 65;
        console.log(c);
    }
    return String.fromCharCode(c);
}
// ------------ Caesar's Cipher Function End ----------



// ------------- Mono Cipher Function ------------------
function genKey(key) {
    let encoded = "";
    let arr = [];
    // initializing the array of length - 26  with 0's
    for (let i = 0; i < 26; i++) { arr[i] = 0; }

    for (let i = 0; i < key.length; i++) {
        if (key[i] >= 'A' && key[i] <= 'Z') {
            if (arr[key[i].charCodeAt() - 65] == 0) {
                encoded += key[i];
                arr[key[i].charCodeAt() - 65] = 1;
            }
        }
        else if (key[i] >= 'a' && key[i] <= 'z') {
            if(arr[key[i].charCodeAt() - 97] == 0) {
                encoded += key[i];
                arr[key[i].charCodeAt() - 97] = 1;
            }
        }
    }

    for (let i = 0; i < 26; i++) {
        if (arr[i] == 0){
            arr[i] = 1;
            encoded += String.fromCharCode(i + 65);
        }
    }
    return encoded;
}

// Function that generates encodes(cipher) the message
function monoAlph(msg, encoded) {
    let cipher = "";

    for (let i = 0; i < msg.length; i++) {
        if (msg[i] >= 'a' && msg[i] <= 'z') {
            let pos = msg[i].charCodeAt() - 97;
            cipher += encoded[pos];
        }
        else if (msg[i] >= 'A' && msg[i] <= 'Z') {
            let pos = msg[i].charCodeAt() - 65;
            cipher += encoded[pos];
        }
        else {
            cipher += msg[i];
        }
    }
    return cipher;
}

// ------------- Mono Cipher Function End ----------------


// ------------- Shift Cipher Function  -------------------
function Shifting_Encrypt(msg, key) {
    let cipher = "";
    for (let i = 0; i < msg.length; i++) {
        if (msg[i].match(upper)) {
            cipher += String.fromCharCode((msg[i].charCodeAt() + key - 65) % 26 + 65);
        }
        else {
            cipher += String.fromCharCode((msg[i].charCodeAt() + key - 97) % 26 + 97);
        }
    }
    return cipher;
}


function Shifting_Decrypt(msg, key) {
    let cipher = "";
    for (let i = 0; i < msg.length; i++) {
        if (msg[i].match(upper)) {
            cipher += String.fromCharCode((msg[i].charCodeAt() + key - 65) % 26 + 65);
        }
        else {
            cipher += String.fromCharCode((msg[i].charCodeAt() + key - 97) % 26 + 97);
        }
    }
    return cipher;
}
// ------------- Shift Cipher Function End ----------------

function Vigenere(str, key) {

    let l = key.length;
    let Cipher = [];
    for (let i = 0; i < str.length; i++) {
        if (str[i] != ' ') {
            k = lst.indexOf(key[i % l]);
            m = lst.indexOf(str[i]);
            Cipher.push(lst[(m + k) % 26]);
        }
        else {
            Cipher.push(' ');
        }
    }
    // Joining the array into String and returning
    return Cipher.join('');
}
// ------------ Vigenere's Cipher Function End------------




// ------------ Function that Chooses Which Encryption Algo is to be Used ----------

 
function choose_algo() {
    var option=document.getElementById('option').value;
    // Caesar's Cipher
    if (option == "cs") {

        let plain_text = inp_1.value;
        if (plain_text.length != 0) {
            let cipher = "";
            for (let i = 0; i < plain_text.length ; i++) {
                cipher += Caesar(plain_text[i]);
            }
            out.value = cipher;
            store.push(cipher);
        }
    }
    // Mono Cipher
    else if (option == "mn") {

        let message = inp_1.value;
        let key = inp_2.value;
        let encoded  = genKey(key);
        let c_text = monoAlph(message, encoded);
        out.value = c_text;
        store.push(c_text);
    }
    // Shift Cipher
    else if (option == "sf") {

        let message = inp_1.value;
        let shift = inp_2.value;
        let cipher = Shifting_Encrypt(message, shift);
        out.value = cipher;
        store.push(cipher);
    }
    // Vigenere's Cipher
    else if (option == "vg") {

        let str = inp_1.value.toUpperCase();
        let keyword = inp_2.value.toUpperCase();
        let Cipher_Text = ' ';
        Cipher_Text = Vigenere(str, keyword);
        out.value = Cipher_Text;
        store.push(Cipher_Text);
    }
}



// -------------- BruteForce Function ------------------

function BruteForce() {

    let msg = out.value;
    let Decoded_Text = "";
    let i = 1;
    do {
        let temp = msg;
        let Decoded_Text = Shifting_Decrypt(temp, i);
        t_area.style.display = "block";
        text.style.display = "block";
        // Decoded_Text.push(Text);
        t_area.value += " Tried : " + i + "\n" + Decoded_Text + "\n";
        i++;
    } while (i < 32);
    store.push(Decoded_Text);
}

// -------------- BruteForce Function End -------------- 


function choose_dec() {
    let l = store.length;
    console.log(store);
    out.value = store[l];
}


function retrieve() {
    text.innerHTML = "Ciphers Retrieved :";
    text.style.display = "block";
    ret.style.display = "block";
}