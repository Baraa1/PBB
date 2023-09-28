function enable_fields(){
    const b_used = document.getElementById('b_used');
    const b_docked = document.getElementById('b_docked');
    const c_used = document.getElementById('c_used');
    const c_docked = document.getElementById('c_docked');
    const b_options = Array.from(b_used.options);
    const c_options = Array.from(c_used.options);

    b_used.style.color = 'white'
    c_used.style.color = 'white'
    
    // checks if b_used is initially true to enable b_docked field
   if (b_used.value === 'true') {
       b_docked.removeAttribute('disabled')
       b_used.style.backgroundColor = 'green';
      } else {
         b_docked.setAttribute('disabled','')
         b_used.style.backgroundColor = 'red';
      }
   if (c_used.value === 'true') {
         c_used.style.backgroundColor = 'green';
         c_docked.removeAttribute('disabled')
      } else {
         c_docked.setAttribute('disabled','')
         c_used.style.backgroundColor = 'red';
     }
   
    b_used.parentElement.addEventListener('click', () => {
       const true_option  = b_options.find(item => item.value === 'true');
       const false_option = b_options.find(item => item.value === 'false');

       if (b_used.value === 'true') {
          false_option.setAttribute('selected','');
          true_option.removeAttribute('selected');
          b_used.style.backgroundColor = 'red';
          b_docked.setAttribute('disabled','');
         } else {
            true_option.setAttribute('selected','');
            false_option.removeAttribute('selected');
            b_used.style.backgroundColor = 'green';
            b_docked.removeAttribute('disabled');
      }
    })

    c_used.parentElement.addEventListener('click', () => {
      const true_option  = c_options.find(item => item.value === 'true');
      const false_option = c_options.find(item => item.value === 'false');

      if (c_used.value === 'true') {
         false_option.setAttribute('selected','');
         true_option.removeAttribute('selected');
          c_used.style.backgroundColor = 'red';
          c_docked.setAttribute('disabled','')
         } else {
            true_option.setAttribute('selected','');
            false_option.removeAttribute('selected');
            c_used.style.backgroundColor = 'green';
            c_docked.removeAttribute('disabled')
      }
    })
}

enable_fields();
/*
b_used.addEventListener('change', () => {
   if (b_used.value === 'true') {
      b_docked.removeAttribute('disabled')
   } else {
      b_docked.setAttribute('disabled','')
   }
})
c_used.addEventListener('input', () => {
   if (c_used.value === 'true') {
      c_docked.removeAttribute('disabled')
   } else {
      c_docked.setAttribute('disabled','')
   }
})*/