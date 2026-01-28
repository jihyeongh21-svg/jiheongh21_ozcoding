console.log('hello world sjdkaskd');
// const username = "후츠릿";
const buttonEl = document.querySelector(".button")
console.log("buttonEl",buttonEl);

const nameEl = document.querySelector(".name")
console.dir(nameEl);
const handleClick = () => {
    console.log('click');
    const username = window.prompt("니미 시발년아 !!!");
    console.log("🚀 ~ handleClick ~ username:", username)
    nameEl.innerText = username
};// 화삻표 험수




buttonEl.addEventListener("click",handleClick);



