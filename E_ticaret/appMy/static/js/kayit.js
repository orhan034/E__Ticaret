const containers = document.querySelector(".containers"),
    goziconn = document.querySelectorAll(".gozicon"),
    pass = document.querySelectorAll(".password"),
    signUp = document.querySelector(".signup-link"),
    login = document.querySelector(".login-link");
    
goziconn.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click",()=>{
        pass.forEach(pass => {
            if(pass.type==="password"){
                pass.type = "text"
            }
            else{
                pass.type = "password"
            }
        })
    })
});

signUp.addEventListener("click", ()=>{
    containers.classList.add("active");
});

login.addEventListener("click", ()=>{
    containers.classList.remove("active");
});