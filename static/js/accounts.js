function deactivate_acc() {
    toggleSwitchs = document.querySelectorAll('.deactivate');
    toggleSwitchs.forEach(element => {
        element.addEventListener('click', (e) => {
            e.preventDefault();
        }) 
    });
}

function swap_text() {
    const modalsbtns = document.querySelectorAll('.activation-btn')
    console.log(modalsbtns)
    modalsbtns.forEach(btn => {
        console.log('ac1')
        btn.addEventListener('click', () => {
            console.log('ac2')
            const mbody = btn.parentElement.previousElementSibling;
            if(btn.textContent.includes('Activate')) {
                btn.textContent = 'Deactivate';
                mbody.textContent = mbody.textContent.replace('Activate', 'Deactivate')
            } else {
                btn.textContent = 'Activate';
                mbody.textContent = mbody.textContent.replace('Deactivate', 'Activate')
            }
        })
    })
}

swap_text();
// prevent switch from automatically toggling
deactivate_acc();