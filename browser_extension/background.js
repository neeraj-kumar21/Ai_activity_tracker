console.log("AI Activity Tracker Background Started");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.type === "BROWSER_ACTIVITY") {

        console.log("Browser Activity Received:");
        console.log("Title:", message.title);
        console.log("URL:", message.url);

        fetch("http://127.0.0.1:5000/browser-activity", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title: message.title,
                url: message.url
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Python Response:", data);
        })
        .catch(error => {
            console.error("Python Connection Error:", error);
        });
    }

    return true;
});