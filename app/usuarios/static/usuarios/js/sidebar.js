document.addEventListener('DOMContentLoaded', function(){
    const body = document.querySelector("body")
    const sidebar = body.querySelector(".sidebar")
    const toggle = body.querySelector('.toggle')
    if (sidebar && toggle){
        toggle.addEventListener("click", () => {
            sidebar.classList.toggle('close');
        })
    } else {
        console.error("elementos nao encontrados")
    }
})