console.log("AI Activity Tracker Started");

const title = document.title;
const url = window.location.href;

console.log("Page Title:", title);
console.log("Page URL:", url);

chrome.runtime.sendMessage({
    type: "BROWSER_ACTIVITY",
    title: title,
    url: url
});