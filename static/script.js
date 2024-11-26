const showCustomQuote = document.getElementById("custom-quote-show");
const showRandomQuote = document.getElementById("random-quote-show");

// Hide and show the divs when the page loads
hideCustomQuoteDiv()
showRandomQuoteDiv()

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
    customQuote.style.display = "none";
}

function hideRandomQuoteDiv() {
    // Why can't I just hide the entire div? Who knows...
    const newQuote = document.getElementById("new-quote");
    newQuote.style.display = "none";
    showCustomQuote.style.display = "none";
}

function showCustomQuoteDiv() {
    const customQuote = document.getElementById("custom-quote");
    customQuote.style.display = "block";
}

function showRandomQuoteDiv() {
    // Why can't I just show the entire div? hell if i know...
    const newQuote = document.getElementById("new-quote");
    newQuote.style.display = "block";
    showCustomQuote.style.display = "block";
}
