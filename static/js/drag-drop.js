function table_drag(){
    // Vertical constraint
    //const draggableElements = document.querySelectorAll('.draggable-element');
    const dropTargets = document.querySelectorAll(".drop-target");
    //const tableRows          = document.querySelectorAll("tbody tr");
    const shifts          = document.querySelector("#shifts-container");
    // Shifts bar drag and copy
    let drake = dragula([],{
        copy:true,
        // Allow dropping only if the target container is a target container
        accepts: function (el, target, source, sibling) {
            // console.log('el:',el, 'target:',target, 'source:',source, 'sibling:',sibling);
            //when dropTargets are dragged and dropped on another table cell
            /*  el      = The div inside the table cell
                sibling = The div inside the table cell that's dropped on
                target  = td.drop-target (the table cell dropped on)
                source  = td.drop-target (the table cell being dragged) */

            // when shifts are dragged and dropped on  a table cell
            /*  el      = The div of the shift
                sibling = The div inside the table cell that's dropped on
                target  = td.drop-target (the table cell dropped on)
                source  = section#shifts-container (the container of the draggged shift) */
            //console.log(el.classList.contains('draggable-cell'), target.classList.contains('drop-target'));
            /*if (el.classList.contains('draggable-cell')){
                // Handles table cells drag and drop
                return target.classList.contains('drop-target');
            } else if ((el.classList.contains('draggable-element'))){
                // Handles shifts drag and drop
                return target.classList.contains('drop-target');
            }*/
            return target.classList.contains('drop-target');
        },
        moves: function (el, container, handle) {
            // Check if the element is draggable
            return el.classList.contains('draggable');
        },
        revertOnSpill:true,
    });
    // Add the table cells
    dropTargets.forEach(cell => {
        drake.containers.push(cell);
    });
    // Add the shifts bar
    drake.containers.push(shifts);

    drake.on('drop', function (el, target, source, sibling) {
        //console.log('el:',el, 'target:',target, 'source:',source, 'sibling:',sibling);
        const elementData = el.children[1].textContent;
        const new_shift = target.querySelector('#id_shift');
        const sub_btn = target.querySelector('.filter');
        new_shift.value = elementData.replace(/\D/g,'');
        sub_btn.click();
    })
    /* Would've been useful but no "dragover"
    drake.on('shadow', function (el, target, source, sibling) {
        target.classList.add('light-red');
    })
    drake.on('out', function (el, target, source, sibling) {
        target.classList.remove('light-red');
    });*/
}
table_drag();

// Inside table drag and drop
let isMouseDown = false,
activeCell = null,
nextCell = null,
parentRow = null,
initPos,
dataValue;

function dragdrop(){
    const cells = Array.from(document.querySelectorAll('.draggable-cell'));
    const tableBody = document.querySelector('tbody');

    cells.forEach(function (cell) {
        // On cell click
        cell.addEventListener('drag', (e) => {
            isMouseDown = true;
            activeCell = cell;
            parentRow = activeCell.parentElement.parentElement;
            //activeCell.style.cursor = 'grabbing';
            dataValue = cell.querySelector('#id_shift').value;
            initPos = activeCell.parentElement.getBoundingClientRect().right;
            nextCell = activeCell.parentElement.nextElementSibling;
            //tableBody.classList.add('unfocused');
            parentRow.classList.add('table-danger', 'focused');
        });
    });
    // Check for mouse up within the tbody and disable the drag effect
    tableBody.addEventListener('mouseup', () => {
        isMouseDown = false;
        if (activeCell) {
            parentRow.classList.remove('table-danger', 'focused');
            activeCell = null;
        }
    });
    // Disable the drag effect if the user leaves the table body area
    tableBody.addEventListener('mouseleave', () => {
    isMouseDown = false;
    if (activeCell) {
        parentRow.classList.remove('table-danger', 'focused');
        activeCell = null;
    }
    });

    // The drag effect
    tableBody.addEventListener('mousemove', (e) => {
        if (isMouseDown && activeCell) {
            // Calculate the boundaries based on the row's dimensions
            /*const row = parentRow;
            let rowRect = row.getBoundingClientRect(),
            rowStyle = getComputedStyle(row),
            rowPaddingTop = parseFloat(rowStyle.paddingTop),
            rowPaddingBottom = parseFloat(rowStyle.paddingBottom),
            minHeight = rowRect.top + rowPaddingTop,
            maxHeight = rowRect.bottom - activeCell.offsetHeight - rowPaddingBottom;
             
            // Update the position of the active cell to follow the mouse within the row
            // Slider left
            let minWidth = rowRect.left;
            let maxWidth = rowRect.right - activeCell.offsetWidth;
            let newLeft = Math.max(minWidth, Math.min(e.clientX, maxWidth));
            let newLeft = activeCell.parentElement.getBoundingClientRect().right;
            let newTop = Math.max(minHeight, Math.min(e.clientY, maxHeight));*/
            
            // Introduce a delay of 10 milliseconds
            setTimeout(function () {
                
                // Move only when the mouse is clicked on an object and moved past the right end of the clicked on cell
                if (e.clientX >= initPos + (activeCell.parentElement.offsetWidth/5)){
                    // set initPos to the new position
                    initPos += activeCell.parentElement.offsetWidth
                    // If mouse moved beyond the next cell x-axis change the shift of the next cell
                    // Get the cell to be changed
                    const new_shift = nextCell.querySelector('#id_shift');
                    // get the submit btn
                    const sub_btn = nextCell.querySelector('.filter');
                    // Assign the new shift value
                    new_shift.value = dataValue;
                    sub_btn.click();
                    // self explanatory really
                    nextCell = nextCell.nextElementSibling;
                    //if (e.clientX >= nextCell.getBoundingClientRect().right) {
                    //}
                    // move the cell to the right "cancelled but might return to it"
                    //activeCell.style.position = 'fixed';
                    //activeCell.style.left = `${initPos}px`;
                    //activeCell.style.top = `${newTop}px`;
                }
            }, 10);
        }
    });

}
dragdrop();