//  제출 이벤트 받기 -> 이벤트 핸들링
//  제출된 입력 값들을 참조
//  입력값에 문제가 있는 경우 이를 감지
//  가입 환영 인사를 제공
const form = document.getElementById('form');
form.addEventListener('submit', function (event) {
    event.preventDefault()// 기존 기능을 차단 

    let userId = event.target.id.value
    let userPw = event.target.pw.value
    let userPw2 = event.target.pwCheck.value
    let userName = event.target.name.value
    let userEmail = event.target.email.value
    let userPhone = event.target.phone.value
    let userGender = event.target.gender.value
    let userPosition = event.target.position.value
    let userIntro = event.target.intro.value

    console.log(userId, userPw, userPw2, userName, userEmail, userPhone, userGender, userPosition, userIntro)

    if(userId.length < 6){
        alert("아이디가 너무 짧습니다 6자 이상 작성해 주세요 !")
        return
    }
    if(userPw !== userPw2){
        alert("비밀번호가 일치하지 않습니다 !")
        return    
    }
    //  가입 환영 인사
    document.body.innerHTML = ""
    document.write(`<p>${userName}님 환영합니다.!!</p>`)
    

}) 