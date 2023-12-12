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

function read_cells(values){
    const table_rows = document.querySelectorAll(`tbody .days1`);
    //const col_np     = parseInt(values['shift_date']) + 2;
    const counter      = document.querySelector(`#s${values['shift_id']}-${values['shift_date']} h6`);
    const prev_total   = parseInt(counter.textContent);
    let new_total        = 0;

    table_rows.forEach(row => {
        //const colElement = row.querySelector(`td:nth-child(${col_np}) h6`);
        const colElement = row.querySelector(`.d${values['shift_date']} h6`);
        const shift_tag  = colElement.querySelector(`.targ`);
        const p_tag = colElement.querySelector(".cell-counter");
        if (String(shift_tag.textContent.trim('')) === String(values['shift_name'])){
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

function calculate_employees(){
    for (let element in calls_dict) {
        read_cells(calls_dict[element]);
    }
}

calculate_employees()
// setInterval(recalc, 120000); // 60000 milliseconds is equal to 1 minute

function calculate_week_hours() {
    const weekCounters = document.querySelectorAll('.week-counter')
    let monthly_hours,
    monthly_ot;
    weekCounters.forEach(week => {
        let totalHours  = 0,
        otHours         = 0;
        monthly_hours   = week.parentElement.querySelector('.month-counter').querySelector('h4');
        monthly_ot      = week.parentElement.querySelector('.month-ot-counter').querySelector('h4');
        let week_cell = week.querySelector('h4');
        let ot_cell = week.nextElementSibling.querySelector('h4');
        
        let currentCell = week.previousElementSibling;
        for (let i = 0; i <= 6; i++) {
            totalHours += parseInt(currentCell.querySelector('.total-hours').textContent);
            console.log(currentCell.querySelector('.allowance').textContent)
            otHours += parseInt(currentCell.querySelector('.allowance').textContent);
            console.log(otHours)
            currentCell = currentCell.previousElementSibling;
        }
        if (totalHours > 48) {
            otHours += totalHours - 48;
        }
        // Each week
        week_cell.textContent = totalHours;
        // Full month
        monthly_hours.textContent = parseInt(monthly_hours.textContent) + totalHours;
        // Each week ot
        ot_cell.textContent = otHours;
        // Full month ot
        monthly_ot.textContent = parseInt(monthly_ot.textContent) + otHours;
    })
}
// Listens for htmx responses and applies changes accordingly
function recalc(){
    const dropTargets1 = document.querySelectorAll(".drop-target");
    dropTargets1.forEach(cell => {
        cell.addEventListener('htmx:afterSwap', function(event) {
            calculate_employees();
            calculate_employees();
            calculate_week_hours()
            // Works but doesnt account for other shifts
            // let swappedElement = event.detail.elt;
            // let shiftName = swappedElement.querySelector(`.targ`).textContent;
            // let shiftDay = swappedElement.querySelector(`.hx-date`).textContent;
            // console.log(swappedElement);
            // console.log(`${shiftName}`,shiftDay);
            // // Once to change the value of the hidden cell in the tfoot
            // read_cells(calls_dict[`${shiftName}-${shiftDay}`])
            // // Twice to apply the values changes to the column cells
            // read_cells(calls_dict[`${shiftName}-${shiftDay}`])
        });
    })
};
recalc();