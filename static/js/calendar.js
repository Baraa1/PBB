function createCalendar(){
    const currentDate     = document.querySelector(".current-date"),
    selectedMonth   = document.querySelector(".month"),
    selectedYear    = document.querySelector(".year");

    // getting new date, current year and month
    let currYear  = selectedYear.textContent,
    currMonth = selectedMonth.textContent - 1;

    // storing full name of all months in array
    const months = ["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"];
    currentDate.innerText = `${months[currMonth]} ${currYear}`; // passing current mon and yr as currentDate te
};
createCalendar();

function dragdrop(){
    const draggableElements = document.querySelectorAll('.draggable-element');
    const dropTargets = document.querySelectorAll('.drop-target');

    draggableElements.forEach(element => {
        element.addEventListener('dragstart', (event) => {
            event.dataTransfer.setData('elementData', element.textContent);
        })
    });

    dropTargets.forEach(element => {
        element.addEventListener('dragover', (event) => {
            event.preventDefault();
            element.classList.add('light-red')
        });
    });
    dropTargets.forEach(element => {
        element.addEventListener('dragleave', (event) => {
            event.preventDefault();
            element.classList.remove('light-red')
        });
    });
    dropTargets.forEach(element => {
        element.addEventListener('drop', (event) => {
            const elementData = event.dataTransfer.getData('elementData');
            const new_shift = element.querySelector('#id_shift');
            const sub_btn = element.querySelector('.filter');
            element.classList.remove('bg-dark');
            new_shift.value = elementData.replace(/\D/g,'');
            sub_btn.click();
        });
    });
}
dragdrop();

function read_cells(values){
    const table_rows = document.querySelectorAll(`tbody .days1`);
    const col_np     = parseInt(values['shift_date']) + 2;
    const counter      = document.querySelector(`#s${values['shift_id']}-${values['shift_date']} h6`);
    const prev_total   = parseInt(counter.textContent);
    console.log(prev_total)
    let new_total        = 0;
    table_rows.forEach(row => {
        const colElement = row.querySelector(`td:nth-child(${col_np}) h6`);
        const shift_tag  = colElement.querySelector(`.targ`);
        const p_tag = colElement.querySelector(".cell-counter");
        if (String(shift_tag.textContent.trim('')) === String(values['shift_name'])){
            //counter.textContent = prev_total + 1
            new_total += 1;
            p_tag.textContent = prev_total;
        };
    });
    if (new_total !== prev_total){
        counter.textContent = new_total;
    } else {
        counter.textContent = prev_total
    }
};
function recalc(){
    for (let element in calls_dict) {
        read_cells(calls_dict[element]);
    }
}
recalc()
setInterval(recalc, 10000); // 60000 milliseconds is equal to 1 minute