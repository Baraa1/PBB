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
    const col_np     = parseInt(values['shift_date']) + 2;
    const counter      = document.querySelector(`#s${values['shift_id']}-${values['shift_date']} h6`);
    const prev_total   = parseInt(counter.textContent);
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