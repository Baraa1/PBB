function sidebar_active_link(){
    const url = window.location.href
    const sidebar_links = document.querySelectorAll(".sub-link")
    
    sidebar_links.forEach(link => {
        const parent_element = link.parentElement.parentElement.parentElement;
        const parent_btn = parent_element.previousElementSibling;
        if (url === link.href) {
            // highlights the button. cancelled for now
            parent_btn.style.color = "var(--bs-nav-pills-link-active-color)"
            
            // toggles the arrow
            parent_btn.setAttribute('aria-expanded', 'true');
            
            // toggles the list
            parent_element.classList.toggle("collapse")
            parent_element.classList.toggle("show")

            // highlights the exact link 
            link.style.borderBottom = 'solid var(--bs-primary)'
            link.style.color = 'var(--bs-light)'
        } else if (link.href !== url && parent_element.className === 'collapse show') {
            parent_element.classList.toggle("show")
        }

    });
};

sidebar_active_link();