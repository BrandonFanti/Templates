
function updateThemeIcon(new_icon){
    new_icon
        .parentElement.parentElement.parentElement
        .children[0].children[0]
        .replaceWith(new_icon.cloneNode(true))
}

// Set theme to the user's preferred color scheme
function updateThemeTo(theme) {
  document.querySelector("html").setAttribute("data-bs-theme", theme);
  Array.from(document.querySelectorAll('[data-bs-theme-value]'))
    .forEach((itheme)=>{
        if(itheme.getAttribute('data-bs-theme-value') == theme){
            updateThemeIcon(itheme.children[0])
        }
    })
}

function updateTheme() {
  if(!window.localStorage.getItem('theme', 'dark')){
    var colorMode = window.matchMedia("(prefers-color-scheme: light)").matches ?
      "light":
      "dark" ;
    active = document.querySelectorAll(".bi.theme-icon-active")[0];
    console.log("Updating color mode: from ", active);
  }else{
    colorMode = window.localStorage.getItem('theme', 'dark')
  }
  updateThemeTo(colorMode);
}


function addThemeListeners(){
    theme_switcher = document.querySelector(".theme-switcher").children[1];
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateTheme)
    Array.from(theme_switcher.querySelectorAll(".bi"))
    .forEach((theme_selection_node)=>{
        console.log("Adding listener to ", theme_selection_node.parentElement)
        theme_selection_node.parentElement.addEventListener('click',(node)=>{
            new_theme = node.target.getAttribute('data-bs-theme-value')
            node.target.parentElement.parentElement.children[0].children[0]
                .replaceWith(node.target.children[0].cloneNode(true))
            updateThemeTo(new_theme);
            window.localStorage.setItem('theme', new_theme)
        })
    })
}

// Set theme on load
updateTheme()
addThemeListeners()
