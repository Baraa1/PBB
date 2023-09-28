/*function sidebar_active_link(){
    const url = window.location.href
    const sidebar_links = document.querySelectorAll(".sub-link")
    
    sidebar_links.forEach(link => {
        const parent_element = link.parentElement.parentElement.parentElement;
        const parent_btn = parent_element.previousElementSibling;
        if (url === link.href) {
            // highlights the button. cancelled for now
            // parent_btn.style.color = "var(--bs-nav-pills-link-active-color)"
            parent_btn.classList.add('text-bg-primary')
            parent_element.classList.add('text-bg-primary')
            // toggles the arrow
            parent_btn.setAttribute('aria-expanded', 'true');
            
            // toggles the list
            parent_element.classList.toggle("collapse")
            parent_element.classList.toggle("show")

            // highlights the exact link 
            link.style.borderBottom = 'solid var(--bs-primary-border-subtle)'
            //link.style.color = 'var(--bs-warning-text-emphasis)'
        } else if (link.href !== url && parent_element.className === 'collapse show') {
            parent_element.classList.toggle("show")
            parent_btn.classList.remove('text-bg-primary')
            parent_element.classList.remove('text-bg-primary')
        }

    });
}; Old-sidebar */

function sidebar_active_link(){
    const url = window.location.href
    const sidebar_links = document.querySelectorAll(".sub-link")
    
    sidebar_links.forEach(link => {
        //console.log(link.href);
        //console.log(url);
        //console.log(url == link.href);
        //let texts            = Array.from(link.children)
            //texts.forEach(item => {
            //    item.classList.add('text-success-emphasis', 'fw-bold');
            //})
            //texts.forEach(item => {
            //    item.classList.remove('text-success', 'fw-bold');
            //})
            //if (url === link.href)
            //else if (link.href !== url)
        if (url === link.href) {
            // highlights the button
            link.classList.add('bg-success', 'border', 'border-success', 'border-opacity-25', 'text-success-emphasis', 'fw-bold')
            link.style = "--bs-bg-opacity: .1;";
        } else if (link.href !== url) {
            link.classList.remove('bg-success', 'border', 'border-success', 'border-opacity-25', 'text-success-emphasis', 'fw-bold');
        }

    });
};

/*
You can use the **split()** method in JavaScript to split a URL into an array of its parts. Then you can compare the parts of the two URLs to find the common path. Here is an example of how to use it:

```javascript
const url1 = "https://sgs-ssoc-pbb.com/dockingRecords/";
const url2 = "https://sgs-ssoc-pbb.com/dockingRecords/create_docking";

const url1Parts = url1.split("/");
const url2Parts = url2.split("/");

let commonPath = "";

for (let i = 0; i < url1Parts.length; i++) {
  if (url1Parts[i] === url2Parts[i]) {
    commonPath += "/" + url1Parts[i];
  } else {
    break;
  }
}

console.log("The common path is: " + commonPath);
```

This code will split both URLs into arrays of their parts using the **split()** method. Then it will loop through the arrays and compare each part of the two URLs. If a part is the same in both URLs, it will add it to the **commonPath** variable. If a part is different, it will break out of the loop.

I hope this helps! Let me know if you have any other questions.

Source: Conversation with Bing, 6/27/2023
(1) How to split url to get url path in JavaScript - Stack Overflow. https://stackoverflow.com/questions/39334400/how-to-split-url-to-get-url-path-in-javascript.
(2) How do I parse a URL into hostname and path in javascript?. https://stackoverflow.com/questions/736513/how-do-i-parse-a-url-into-hostname-and-path-in-javascript.
(3) How to compare two urls in javascript or jquery - Stack Overflow. https://stackoverflow.com/questions/12220345/how-to-compare-two-urls-in-javascript-or-jquery.
*/

// For parent links *explanation from chat gpt above 
function sidebar_active_sublink(){
    const url = window.location.href
    const sidebar_links = document.querySelectorAll(".link")
    const url1Parts = url.split("/");
    
    sidebar_links.forEach(link => {
        let n = 0
        const url2Parts = link.href.split("/");
        let commonPath = "";

        for (let i = 0; i < url1Parts.length; i++) {
        if (url1Parts[i] === url2Parts[i]) {
            commonPath += "/" + url1Parts[i];
            n++;
        } else {
            break;
        }
        }

        if (n>3) {
            // highlights the button
            link.classList.add('bg-primary', 'border', 'border-primary', 'border-opacity-25', 'text-primary-emphasis', 'fw-bold');
            link.style = "--bs-bg-opacity: .1;";
        } else {
            link.classList.remove('bg-primary', 'border', 'border-primary', 'border-opacity-25', 'text-primary-emphasis', 'fw-bold');
        }

    });
};

sidebar_active_link();
sidebar_active_sublink();