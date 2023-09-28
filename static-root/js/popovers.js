function remove_tags() {
  const toolTips = document.querySelectorAll('[data-bs-toggle="popover"]')
  toolTips.forEach(element => {
    const strippedString = element.getAttribute('data-bs-content').replace(/(<([^>]+)>)/gi, "");
    element.setAttribute('data-bs-content', strippedString)
  });
}
remove_tags();

/*  const originalString = `
  <div>
    <p>Hey that's <span>somthing</span></p>
  </div>
`;

const strippedString = originalString.replace(/(<([^>]+)>)/gi, "");

console.log(strippedString);*/


/* global bootstrap: false */

(() => {
    'use strict'
  
    // Tooltip and popover demos
    document.querySelectorAll('.tooltip-demo')
      .forEach(tooltip => {
        new bootstrap.Tooltip(tooltip, {
          selector: '[data-bs-toggle="tooltip"]'
        })
      })
  
    document.querySelectorAll('[data-bs-toggle="popover"]')
      .forEach(popover => {
        new bootstrap.Popover(popover)
      })
  
    document.querySelectorAll('.toast')
      .forEach(toastNode => {
        const toast = new bootstrap.Toast(toastNode, {
          autohide: false
        })
  
        toast.show()
      })
  
    // Disable empty links and submit buttons
    /*document.querySelectorAll('[href="#"], [type="submit"]')
      .forEach(link => {
        link.addEventListener('click', event => {
          event.preventDefault()
        })
      }) */
  
    function setActiveItem() {
      const { hash } = window.location
  
      if (hash === '') {
        return
      }
  
      const link = document.querySelector(`.bd-aside a[href="${hash}"]`)
  
      if (!link) {
        return
      }
  
      const active = document.querySelector('.bd-aside .active')
      const parent = link.parentNode.parentNode.previousElementSibling
  
      link.classList.add('active')
  
      if (parent.classList.contains('collapsed')) {
        parent.click()
      }
  
      if (!active) {
        return
      }
  
      const expanded = active.parentNode.parentNode.previousElementSibling
  
      active.classList.remove('active')
  
      if (expanded && parent !== expanded) {
        expanded.click()
      }
    }
  
    setActiveItem()
    window.addEventListener('hashchange', setActiveItem)
})()

// makees popoveres dismissable
const popover = new bootstrap.Popover('.popover-dismiss', {
    trigger: 'focus'
  })