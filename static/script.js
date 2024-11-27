const customQuoteDiv = document.getElementById("custom-quote");
const randomQuoteDiv = document.getElementById("random-quote");
const customQuoteShowBtn = document.getElementById("custom-quote-show");
const randomQuoteShowBtn = document.getElementById("random-quote-show");

// Hide the custom quote div when the page loads
customQuoteDiv.style.display = "none";

// Toggle the custom quote div 
customQuoteShowBtn.addEventListener("click", () => {
    customQuoteDiv.style.display = "block"; // Show custom-quote
    randomQuoteDiv.style.display = "none"; // Hide random-quote
});

// Toggle the random quote div
randomQuoteShowBtn.addEventListener("click", () => {
    customQuoteDiv.style.display = "none"; // Hide custom-quote
    randomQuoteDiv.style.display = "flex"; // Show random-quote
});
