const daysTag   = document.querySelectorAll(".days"),
currentDate     = document.querySelector(".current-date"),
selectedMonth   = document.querySelector(".month"),
selectedYear    = document.querySelector(".year");

// getting new date, current year and month
let currYear  = selectedYear.textContent,
currMonth = selectedMonth.textContent - 1;

// storing full name of all months in array
const months = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"];
currentDate.innerText = `${months[currMonth]} ${currYear}`; // passing current mon and yr as currentDate te

const renderCalendar = () => {
    daysTag.forEach(daytag => {
        // adding active class to li if the current day, month, and year matched
        let isToday = daytag.textContent == date.getDate() && currMonth === new Date().getMonth() && currYear === new Date().getFullYear() ? "active" : "";
        if (isToday) {daytag.classList.add(isToday);}
        console.log(daytag.textContent.replace(/\D/g,''), date.getDate())
    });
}
renderCalendar();