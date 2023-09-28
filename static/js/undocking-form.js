function enable_fields(){
   const b_used = document.getElementById('b_used');
   const b_door_close = document.getElementById('b_door_close');
   const b_undocked = document.getElementById('b_undocked');
   const c_used = document.getElementById('c_used');
   const c_door_close = document.getElementById('c_door_close');
   const c_undocked = document.getElementById('c_undocked');
   const b_options = Array.from(b_used.options);
   const c_options = Array.from(c_used.options);

   b_used.style.color = 'white'
   c_used.style.color = 'white'
   
   // checks if b_used is initially true to enable b_undocked field
   if (b_used.value === 'true') {
      b_door_close.removeAttribute('disabled')
      b_undocked.removeAttribute('disabled')
      b_used.style.backgroundColor = 'green';
     } else {
        b_door_close.setAttribute('disabled','')
        b_undocked.setAttribute('disabled','')
        b_used.style.backgroundColor = 'red';
     }

   if (c_used.value === 'true') {
      c_door_close.removeAttribute('disabled')
      c_undocked.removeAttribute('disabled')
      c_used.style.backgroundColor = 'green';
     } else {
      c_door_close.setAttribute('disabled','')
        c_undocked.setAttribute('disabled','')
        c_used.style.backgroundColor = 'red';
    }

    b_used.parentElement.addEventListener('click', () => {
      const true_option  = b_options.find(item => item.value === 'true');
      const false_option = b_options.find(item => item.value === 'false');

      if (b_used.value === 'true') {
         false_option.setAttribute('selected','');
         true_option.removeAttribute('selected');
         b_used.style.backgroundColor = 'red';
         b_door_close.setAttribute('disabled','');
         b_undocked.setAttribute('disabled','');
        } else {
           true_option.setAttribute('selected','');
           false_option.removeAttribute('selected');
           b_used.style.backgroundColor = 'green';
           b_door_close.removeAttribute('disabled');
           b_undocked.removeAttribute('disabled');
     }
   })

   c_used.parentElement.addEventListener('click', () => {
     const true_option  = c_options.find(item => item.value === 'true');
     const false_option = c_options.find(item => item.value === 'false');

     if (c_used.value === 'true') {
        false_option.setAttribute('selected','');
        true_option.removeAttribute('selected');
         c_used.style.backgroundColor = 'red';
         c_door_close.setAttribute('disabled','')
         c_undocked.setAttribute('disabled','')
        } else {
           true_option.setAttribute('selected','');
           false_option.removeAttribute('selected');
           c_used.style.backgroundColor = 'green';
           c_door_close.removeAttribute('disabled')
           c_undocked.removeAttribute('disabled')
     }
   })
}

enable_fields();