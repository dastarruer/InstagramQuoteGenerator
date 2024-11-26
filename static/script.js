const customQuoteButton = document.getElementById("custom-quote-show");

customQuoteButton.addEventListener("click", (event) => {
    hideRandomQuoteDiv();
    const customQuote = document.getElementById("custom-quote");
    customQuote.hidden = false;
});

function hideRandomQuoteDiv() {
    const newQuote = document.getElementById("new-quote");
    newQuote.hidden = true;
    customQuoteButton.hidden = true;
}
