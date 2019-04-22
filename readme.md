## selenium 설치

* 구글 크롬에서 selenium extension을 설치한다. https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=en

## 조사 대상 리스트

* https://search.naver.com/search.naver?&query=%EC%A0%84%EA%B5%AD+%EB%8C%80%ED%95%99%EA%B5%90 사이트에 있는 63개 대학교에 대해 selenium side 파일을 만든다.

## side 파일 만드는 방법

* chrome에서 selenium extension 버튼을 클릭한다.
* Record a new test in new project를 선택한다.
* PROJECT NAME에는 대학교명을 입력한다(예 : KC대학교)
* BASE URL에는 사이트 주소를 입력한다(예 : http://www.kcu.ac.kr)
  * URL에 "https://" 를 붙이지 않고 "http://" 를 붙인다.
  * 도메인 마지막에는 슬래시를 붙이지 않는다.
* Start Recording을 누른다.
* 사이트 메인 페이지에서 "로그인", "포털", "웹메일", "인트라넷" 등을 찾아 클릭한다.
* ID에는 "testtest"를 입력한다. 간혹 메일 형식으로 입력을 해야 하는 경우에는 "test@test.net"을 입력한다.
* PW에는 "11111111"을 입력한다.
* 로그인 버튼을 누른다(당연히 로그인은 안됨).
* 화면을 닫는다.
* selenium에서 Stop Recording을 누른다.
* 파일을 저장한다(예 : www.kcu.ac.kr.side)
* github에 올린다.

