const customQuoteButton = document.getElementById("custom-quote-show");

customQuoteButton.addEventListener("click", (event) => {
    const randomQuote = document.getElementById("random-quote");
    randomQuote.hidden = true;
});
