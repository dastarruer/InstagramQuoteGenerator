const showCustomQuote = document.getElementById("custom-quote-show");
const showRandomQuote = document.getElementById("random-quote-show");

// When the 'custom-quote-show' button is pressed, hide the random quote and show the custom quote section
showCustomQuote.addEventListener("click", (event) => {
    hideRandomQuoteDiv();
    showCustomQuoteDiv();
});

showRandomQuote.addEventListener("click", (event) => {
    showRandomQuoteDiv();
    hideCustomQuoteDiv();
});

function hideCustomQuoteDiv() {
    const customQuote = document.getElementById("custom-quote");
    customQuote.hidden = true;
}

function hideRandomQuoteDiv() {
    const newQuote = document.getElementById("new-quote");
    newQuote.hidden = true;
    showCustomQuote.hidden = true;
}

function showCustomQuoteDiv() {
    const customQuote = document.getElementById("custom-quote");
    customQuote.hidden = false;
}

function showRandomQuoteDiv() {
    const newQuote = document.getElementById("new-quote");
    newQuote.hidden = false;
    showCustomQuote.hidden = false;
}
