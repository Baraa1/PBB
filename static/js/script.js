// Disables search field enter kry default action
document.querySelectorAll('.stop-enter').forEach(element => {
    element.addEventListener('keydown', (e) => {
        if (e.code === "Enter") {
            e.preventDefault();
        }
    });
});

function toggle_sidebar() {
    const dashboard = document.querySelector('.dashboard-wrapper');
    const sidebar = document.querySelector('.sidebar');
    const sidebar_title = document.querySelector('.title-link');
    const toolbar = document.querySelector('.toolbar');
    const hamburger = document.querySelector('.hamburger');
    const line1 = document.querySelector('.line1');
    const line2 = document.querySelector('.line2');
    const line3 = document.querySelector('.line3');
    const search_form = document.querySelector('.search-form');
    const toolbar_btns = document.querySelector('.toolbar-btns');
    
    // to hide the title
    //sidebar_title.style.fontSize = '0'

    hamburger.addEventListener('click', () => {
        if (dashboard.classList.contains('show-sidebar')) {
            dashboard.classList.remove('show-sidebar');
            dashboard.classList.toggle('hide-sidebar');
            sidebar.style.padding = '0';
            line1.style.backgroundColor = 'var(--bs-light)';
            line2.style.backgroundColor = 'var(--bs-light)';
            line3.style.backgroundColor = 'var(--bs-light)';
            // to remove search bar and btns for phones
            if (screen.width <= 500) {
                if (search_form != null) {
                    search_form.style.display = 'flex';
                }
                toolbar_btns.style.display = 'flex';
            }
            sidebar_title.style.fontSize = '0'
            //const remove_sidebar = setTimeout(() => {sidebar.style.display = 'none'}, 380)
        } else {
            //sidebar.style.padding = '0.35em 1em 0 1em'
            dashboard.classList.remove('hide-sidebar');
            dashboard.classList.toggle('show-sidebar');
            line1.style.backgroundColor = 'var(--bs-dark)';
            line2.style.backgroundColor = 'var(--bs-dark)';
            line3.style.backgroundColor = 'var(--bs-dark)';
            if (screen.width <= 500) {
                if (search_form != null) {
                    search_form.style.display = 'none';
                }
                toolbar_btns.style.display = 'none';
            }
            sidebar_title.style.fontSize = '1.25rem'
        }
        //getComputedStyle(sidebar).getPropertyValue('--sidebar-column')
        //toolbar.style.setProperty('--toolbar-column', '2 / 15')
        //content.style.setProperty('--display-content-column', '2 / 15')
    })
};
toggle_sidebar();

/*const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '85c15c1c5fmshcb571d1bd467699p18d536jsnb45c9303946e',
		'X-RapidAPI-Host': 'aerodatabox.p.rapidapi.com'
	}
};

fetch('https://aerodatabox.p.rapidapi.com/flights/airports/icao/OEDF/2023-02-03T08:00/2023-02-03T14:00?withLeg=true&withCancelled=true&withCodeshared=true&withCargo=true&withPrivate=true&withLocation=false', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));*/