const form = document.getElementById('form');

form.addEventListener('submit', function (event) {
    // 1. 새로고침 막기
    event.preventDefault(); 

    // 2. 입력값 가져오기
    let userId = event.target.id.value;
    let userPw = event.target.pw.value;
    let userPw2 = event.target.pwCheck.value;
    let userName = event.target.name.value;
    let userEmail = event.target.email.value;
    let userPhone = event.target.phone.value;
    
    // 라디오 버튼(성별) 값 가져오기
    let userGender = event.target.gender.value;

    // 3. 유효성 검사 (아이디 길이)
    if(userId.length < 6){
        alert("아이디가 너무 짧습니다. 6자 이상 작성해 주세요!");
        return;
    }
    
    // 4. 유효성 검사 (비밀번호 일치)
    if(userPw !== userPw2){
        alert("비밀번호가 일치하지 않습니다!");
        return;    
    }

    // 5. 알림창에 보여줄 메시지 만들기
    // \n 은 '줄바꿈' 기호입니다.
    let message = `🎉 회원가입 성공! \n\n`;
    message += `아이디: ${userId} \n`;
    message += `이름: ${userName} \n`;
    message += `이메일: ${userEmail} \n`;
    message += `전화번호: ${userPhone} \n`;
    message += `성별: ${userGender === 'male' ? '남자' : '여자'}`;

    // 6. 알림창 띄우기 (여기서 사용자가 확인을 누를 때까지 멈춤)
    alert(message);

    // 7. 페이지 이동하기
    window.location.href = "./admin.html"; 
});