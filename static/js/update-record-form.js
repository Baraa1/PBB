function enable_fields(){
    const b_used = document.getElementById('b_used');
    const b_docked = document.getElementById('b_docked');
    const b_undocked = document.getElementById('b_undocked');
    const c_used = document.getElementById('c_used');
    const c_docked = document.getElementById('c_docked');
    const c_undocked = document.getElementById('c_undocked');

    b_used.style.color = 'white'
    c_used.style.color = 'white'
    
    // checks if b_used is initially true to enable b_docked field
   if (b_used.value === 'true') {
       b_docked.removeAttribute('disabled')
       b_undocked.removeAttribute('disabled')
       b_used.style.backgroundColor = 'green';
      } else {
         b_docked.setAttribute('disabled','')
         b_undocked.setAttribute('disabled','')
         b_used.style.backgroundColor = 'red';
      }
   if (c_used.value === 'true') {
      c_docked.removeAttribute('disabled')
      c_undocked.removeAttribute('disabled')
      c_used.style.backgroundColor = 'green';
   } else {
      c_docked.setAttribute('disabled','')
      c_undocked.setAttribute('disabled','')
      c_used.style.backgroundColor = 'red';
     }
   
    b_used.parentElement.addEventListener('click', () => {
       if (b_used.value === 'true') {
          b_used.value = 'false';
          b_used.style.backgroundColor = 'red';
          b_docked.setAttribute('disabled','')
          b_undocked.setAttribute('disabled','')
         } else {
            b_used.value = 'true'
            b_used.style.backgroundColor = 'green';
            b_docked.removeAttribute('disabled')
            b_undocked.removeAttribute('disabled')
      }
    })
    c_used.parentElement.addEventListener('click', () => {
       if (c_used.value === 'true') {
          c_used.value = 'false';
          c_used.style.backgroundColor = 'red';
          c_docked.setAttribute('disabled','')
          c_undocked.setAttribute('disabled','')
         } else {
            c_used.value = 'true'
            c_used.style.backgroundColor = 'green';
            c_docked.removeAttribute('disabled')
            c_undocked.removeAttribute('disabled')
      }
    })
}

enable_fields();