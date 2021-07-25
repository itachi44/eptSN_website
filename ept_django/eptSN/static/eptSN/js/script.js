//########################################## MAP FORM #################################//



    

let signInBtn= document.getElementById("SignIn");
let logInBtn= document.getElementById("logIn");
let textOverlay=document.getElementById("textOver");
let closeModal1= document.getElementById("closeModal1");
let closeModal2= document.getElementById("closeModal2");
//ajouter le bouton de validation aussi



signInBtn.addEventListener("click",function(e){
    textOverlay.style.display="none";



});


logInBtn.addEventListener("click",function(e){
    textOverlay.style.display="none";

});



closeModal1.addEventListener("click",function(e){
    textOverlay.style.display="block";

});

closeModal2.addEventListener("click",function(e){
    textOverlay.style.display="block";

});



