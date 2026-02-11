# 🌐 추가 학습: 다중 클라이언트 구독 (Broadcasting)

## 1. 개념
- 지금까지는 혼자서만 실습하여 자신이 보낸 메시지가 다시 자신에게만 돌아옵니다. 하지만 실무에서는 "다중 클라이언트"라고, 여러 명이 한 번에 대화할 수 있는 경우가 많습니다.
- 다중 클라이언트 구독은 **모든 클라이언트가 같은 채널을 공유**합니다.
- 이 때 한 명이 보낸 메시지가 전체에게 전송됩니다.

---

## 2. 핵심 아이디어
- 서버는 연결된 소켓(ws)을 **리스트/집합(set)에 저장**합니다.
- 메시지가 오면 -> 리스트에 있는 모든 클라이언트에게 전송(broadcast)합니다.

---

## 3. 예제 코드

```python
# main.py

from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

clients = set()  # 연결된 클라이언트 보관

@app.route("/")
def index():
    return render_template("chat.html")

@sock.route('/ws')
def websocket(ws):
    clients.add(ws)
    try:
        while True:
            data = ws.receive()
            if data is None:
                break
            # 모든 클라이언트에게 메시지 전송
            for client in clients:
                client.send(data)
    finally:
        clients.remove(ws)
```

```html
<!-- templates/chat.html -->

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>다중 클라이언트 채팅</title>
</head>
<body>
  <h1>채팅방</h1>
  <input id="msg" placeholder="메시지 입력" />
  <button onclick="sendMsg()">Send</button>
  <ul id="chat"></ul>

  <script>
    let ws = new WebSocket("ws://127.0.0.1:5000/ws");

    ws.onmessage = (event) => {
      let li = document.createElement("li");
      li.textContent = event.data;
      document.getElementById("chat").appendChild(li);
    };

    function sendMsg() {
      let msg = document.getElementById("msg").value;
      ws.send(msg);
      document.getElementById("msg").value = ""; // 입력창 비우기
    }
  </script>
</body>
</html>
```

---

## 4. 실습 방법
1. 서버를 실행한 뒤 브라우저 탭을 **2개 이상 열어봅니다.**
2. 한쪽에서 메시지를 입력하면 -> 다른 탭에도 동시에 출력됩니다.
3. 실제 서비스에서는 이 방식을 활용하여 **실시간 채팅**, **협업 도구**, **알림 시스템** 등을 구현합니다.
