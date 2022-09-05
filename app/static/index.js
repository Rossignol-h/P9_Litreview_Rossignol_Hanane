const more_less = document.querySelector('.show-hide-btn')
const half = document.querySelector('.half-content')
const full = document.querySelector('.full-content')


function showHide() {
    more_less.classList.toggle("active");
    full.classList.toggle("active");
    half.classList.toggle("active");
}
