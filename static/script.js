const showCustomQuote = document.getElementById("custom-quote-show");
const showRandomQuote = document.getElementById("random-quote-show");

// Toggle to the custom quote form
showCustomQuote.addEventListener("click", (event) => {
    hideRandomQuoteDiv();
    showCustomQuoteDiv();
});

// Toggle to the random quote form
showRandomQuote.addEventListener("click", (event) => {
    showRandomQuoteDiv();
    hideCustomQuoteDiv();
});

function hideCustomQuoteDiv() {
    const customQuote = document.getElementById("custom-quote");
    customQuote.hidden = true;
}

function hideRandomQuoteDiv() {
    // Why can't I just hide the entire div? Who knows...
    const newQuote = document.getElementById("new-quote");
    newQuote.hidden = true;
    showCustomQuote.hidden = true;
}

function showCustomQuoteDiv() {
    const customQuote = document.getElementById("custom-quote");
    customQuote.hidden = false;
}

function showRandomQuoteDiv() {
    // Why can't I just show the entire div? hell if i know...
    const newQuote = document.getElementById("new-quote");
    newQuote.hidden = false;
    showCustomQuote.hidden = false;
}
