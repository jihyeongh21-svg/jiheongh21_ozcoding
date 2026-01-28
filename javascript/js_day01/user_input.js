const username  = prompt("이름을 입력하세요");
console.log("입력한 이름",username);
console.log(typeof username);
const greetEl = document.querySelector("#greeting");
if (username !== null){
    greetEl.textContent=`안녕하세요 ${username}님`;
}
