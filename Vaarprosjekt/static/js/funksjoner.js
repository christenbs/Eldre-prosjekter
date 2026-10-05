
function openNav() {
    document.getElementById("mySidenav").style.width = "545px";
    document.querySelector("#navAktivator").classList.add("displayNone")
    document.querySelector("#navAktivator2").classList.remove("displayNone")
    document.querySelector("#navAktivator2").classList.add("displayBlock")
} 
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.querySelector("#navAktivator").classList.remove("displayNone")
    document.querySelector("#navAktivator2").classList.remove("displayBlock")
    document.querySelector("#navAktivator2").classList.add("displayNone")
}           
function unFavoritiser(id) {
    document.querySelector("#indexFavoritiser"+id).classList.remove("displayNone")
    document.querySelector("#indexUnFavoritiser"+id).classList.remove("displayBlock")
    document.querySelector("#indexUnFavoritiser"+id).classList.add("displayNone")
} 
function favoritiser(id) {
    document.querySelector("#indexFavoritiser"+id).classList.add("displayNone")
    document.querySelector("#indexUnFavoritiser"+id).classList.remove("displayNone")
    document.querySelector("#indexUnFavoritiser"+id).classList.add("displayBlock")
}           
