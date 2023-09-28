function search_fids() {
    const rows = Array.from(document.querySelectorAll('#fids-table tr'));
    const search_field = document.querySelector('#fids-search');

    search_field.addEventListener('keyup', () => {
        let val = search_field.value.trim().replace(/ +/g, ' ').toLowerCase();
        let found;
        
        rows.filter(row => {
            // Search each cell against the user input
            Array.from(row.cells).forEach(cell => {
                let text = cell.textContent.replace(/\s+/g, ' ').toLowerCase();
                // Set found to true if a match was found
                if (text.indexOf(val) > -1) {
                    found = true;
                }
            });
            if (found) {
                row.style.display = "";
                found = false;
            } else {
                row.style.display = "none";
            }
        });
    });
}
search_fids();