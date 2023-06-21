const bar = document.getElementById("bar");
const kapat = document.getElementById("kapat");
const nav = document.getElementById("navbar");

if(bar){
    bar.addEventListener("click", function(){
        nav.classList.add("active");
    })
}
if(kapat){
    kapat.addEventListener("click", function(){
        nav.classList.remove("active");
    })
}

