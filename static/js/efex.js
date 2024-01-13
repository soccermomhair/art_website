// // addEventListener("mouseover", (event) =>{});
// // onmouseover = (event) => {}

// var test = document.getElementsByClassName(".macrame");
// test.addEventListener('mouseover', changeDefOver);
// test.addEventListener('mouseout', changeDefOut);

// function changeDefOver(e) {
//     e.target.classList.toggle('opacity-toggle');
// }
// function changeDefOut(e) {
//     e.target.classList.toggle('opacity-toggle');
// }
// // => {
// //     event.target.style.color = "yellow";
// //     setTimeout(() => { event.target.style.color = ""; }, 500);

// // },
// // false,
// // );
// Object.onmouseover= function(){test}

document.getElementsByClassName("macrame").addEventListener("mouseover", mouseOver);
document.getElementsByClassName("macrame").addEventListener("mouseout", mouseOut);

function mouseOver() {
    document.getElementsByClassName("macrame").style.color = "yellow"
}
function mouseOut() {
    document.getElementsByClassName("macrame").style.color = "black"
}