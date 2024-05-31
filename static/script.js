function generateDFA() {
    alphabetTextbox = document.getElementById("alphabet");
    alphabetTextbox.value = alphabetTextbox.value.replaceAll(/[\s'\]\[]/gi, "");

    // regexTextbox = document.getElementById("regex");
    // regexTextbox.value = alphabetTextbox.value.replaceAll(/[\sελ'\]\[]/gi, "");
}

// cfgTextbox = document.getElementById("cfg");
// cfgTextboxValue = cfgTextbox.value;

function generatePDA() {
    // cfgTextbox.value = cfgTextboxValue;
}

function acceptStringPDA() {
    cfgTextbox = document.getElementById("cfg");
    cfgH3Code = document.getElementById("cfg-h3-code");
    cfgH3Code.innerHTML = cfgTextbox.value;
}

window.onload = function() {
    cfgH3Code = document.getElementById("cfg-h3-code");
    cfgH3Code.value = cfgH3Code.value.replaceAll("<br>", "\n");
};

// DFA
let regex1RadioDFA = document.getElementById("regex1-radio-dfa");
let regex2RadioDFA = document.getElementById("regex2-radio-dfa");
let regex1RadioDFALabel = document.getElementById("regex1-radio-label-dfa");
let regex2RadioDFALabel = document.getElementById("regex2-radio-label-dfa");
let regexTextbox = document.getElementById("regex");
let alphabetTextbox = document.getElementById("alphabet");

regex1RadioDFA.checked = true;

function changeRegexDFA() {
    if (regex1RadioDFA.checked) {
        console.log(regex1RadioDFALabel.innerHTML);
        regexTextbox.value = regex1RadioDFALabel.innerHTML;
        alphabetTextbox.value = "a, b";
    }
    if (regex2RadioDFA.checked) {
        console.log(regex2RadioDFALabel.innerHTML);
        regexTextbox.value = regex2RadioDFALabel.innerHTML;
        alphabetTextbox.value = "0, 1";
    }
}

// CFG
let regex1RadioCFG = document.getElementById("regex1-radio-cfg");
let regex2RadioCFG = document.getElementById("regex2-radio-cfg");
let cfg1Div = document.getElementById("regex1-cfg-div");
let cfg2Div = document.getElementById("regex2-cfg-div");

regex1RadioCFG.checked = true;

function changeCFG() {
    if (regex1RadioCFG.checked) {
        cfg1Div.style.display = "block";
        cfg2Div.style.display = "none";
    }
    if (regex2RadioCFG.checked) {
        cfg2Div.style.display = "block";
        cfg1Div.style.display = "none";
    }
}

// PDA
let regex1RadioPDA = document.getElementById("regex1-radio-pda");
let regex2RadioPDA = document.getElementById("regex2-radio-pda");
let pda1ImageDiv = document.getElementById("regex1-pda-img");
let pda2ImageDiv = document.getElementById("regex2-pda-img");

regex1RadioPDA.checked = true;

function changePDA() {
    if (regex1RadioPDA.checked) {
        pda1ImageDiv.style.display = "block";
        pda2ImageDiv.style.display = "none";
    }
    if (regex2RadioPDA.checked) {
        pda2ImageDiv.style.display = "block";
        pda1ImageDiv.style.display = "none";
    }
}
