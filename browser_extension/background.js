chrome.tabs.onActivated.addListener(async (activeInfo) => {

    let tab = await chrome.tabs.get(activeInfo.tabId);

    console.log("Tab Changed");

    console.log("Tiltle : " + tab.title);

    console.log("URL : " + tab.url);

});
