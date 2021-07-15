window.addEventListener("scroll", (event) => {
    let scroll = this.scrollY;

    if(scroll >= 300){
        document.getElementById("Navigasi").classList.add("bg-dark");
    } else {
        document.getElementById("Navigasi").classList.remove("bg-dark");
    }
});