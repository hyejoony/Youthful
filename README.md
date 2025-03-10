### 1인 청년 자산 관리 도움 서비스
# <img src='./README_IMG/logo.png' alt='logo' width=30> Youthful

### 목차

1️⃣ [기획 배경](#기획-배경)  
2️⃣ [업무 분담 내역](#업무-분담-내역)  
3️⃣ [설계 및 목업](#설계-및-목업)  
4️⃣ [데이터베이스 모델링 및 명세서](#데이터베이스-모델링-및-명세서)  
5️⃣ [금융 상품 추천 알고리즘](#금융-상품-추천-알고리즘)  
6️⃣ [서비스 대표 기능](#서비스-대표-기능)  
7️⃣ [후기](#후기)  


## 기획 배경

> 1. 경제 개념은 어렵고, 돈은 어떻게 모아야 할지 막막한 청년
- 자산관리에 도움이 되는 예금, 적금, 보조금 정보를 제공
- 챗봇을 통한 경제 용어 질문

> 2. 특정 금융상품에 대해 나와 비슷한 사람의 생각
- 예적금 및 보조금 찜 기능
- 프로필 페이지에서의 정보 조회
- 커뮤니티 및 보조금 리뷰


## 업무 분담 내역

- 프로젝트 기간 : 2023/11/15 ~ 2023/11/26 (약 12일)

| 팀원   | 역할 |
|--------|------|
|김경환| Back End - ERD, 아키텍처, 기능 명세서, 동작 시나리오, project의 settig, 모든 app의 model/serializer/view함수, 추천 알고리즘, 회원 커스터마이징, axios로 회원/커뮤니티/예적금/보조금 데이터 연결 및 비동기 처리 |
|전혜준| Front End - API 명세서, 디자인 구상 및 vuetify로 전체 페이지 구현, axios로 보조금 데이터 연결 및 비동기 처리, 환율 계산기 기능 구현(네이버 증권 페이지 크롤링 데이터 수집), 내 집 주변 은행 찾기(카카오맵 API 활용), 웹페이지 메인 아이디어 기획, PPT, 생성형 AI 챗봇 구현 |


## 설계 및 목업
### 💻 기술 스택
**Back-end**
- Language
    - python
- framework
    - django
    - django-rest-framework
    - dj-rest-auth
    - pillow

**Front-end**

- Language
    - javascript
- framework
    - Vue3
    - vuetify
    - bootstrap
    - pinia
    - axios

### 👷🏻‍♂️ 아키텍처
<img src="./README_IMG/architecture.png" alt='architecture'/>

### ✍🏻 목업
[🔗 Figma Link](https://www.figma.com/design/xeOfzhOs75pUmivYMvly4k/Untitled?node-id=0-1&node-type=canvas&t=3YP7YGG4k6fZLgH5-0)
<img src="./README_IMG/figma.png" alt='Figma'/>


## 데이터베이스 모델링 및 명세서

### 🗂️ ERD
<img src="./README_IMG/erd.png" alt='erd'/>

### 🎬 기능 명세서
<img src="./README_IMG/functional_specification.png" alt='functional_specification'/>

### 📬 API 명세서
<img src='./README_IMG/api_specification.png' alt='API 명세서' />


## 금융 상품 추천 알고리즘

### 1️⃣ 더미 데이터 생성
- 1000명의 유저 데이터 생성
- 청년 관련 지원금 데이터 추가

### 2️⃣ 추천 알고리즘
- 유저의 나이, 소득, 지역, 직업 정보 기반
    - 나이 ± 5살 이내 = 2점
    - 기준 중위소득 동일 = 2점
    - 지역 동일 = 1점
    - 직업 동일 = 1점
- 특정 상품의 찜한 유저 정보 기반
    - 특정 상품을 찜한 유저의 정보가 본인과 동일할 시 
    - 위 기준에 따라 상품의 점수 측정
    - 상품의 점수가 높은 순으로 내림차순 정렬



## 서비스 대표 기능

### 1️⃣ 회원가입, 로그인 페이지
https://github.com/user-attachments/assets/ede26178-f0b1-4cdf-9b9a-3731b608e008
- 회원가입
    - 소득, 지역, 직업은 리스트 박스 형태로 처리
    - 이메일은 유니크 해야 하며, 형식을 맞춰야 함
    - 비밀번호는 8~16 자의 영어 대소문자, 숫자, 특수문자 2가지로 이루어져야 함
    - 별칭 제외 모두 필수 필드

https://github.com/user-attachments/assets/3db7262b-9e00-4a01-ae85-155cfab871e5
- 로그인
    - 실패 시 에러메세지를 띄워 사용자로 하여금 아이디와 비밀번호를 다시 확인할 수 있도록 함

### 2️⃣ 메인 페이지
https://github.com/user-attachments/assets/2bd9ef47-a28e-4677-ae58-a8b53645d1d7

- 금융 나침반을 나타내는 로고
- 챗봇 `유스`에 대한 설명을 나타내는 carousel
- 금융 상품 추천 대표 UI
- 동적 지도 이미지
- 챗봇 `유스` 아이콘
- 왼쪽에 각 페이지로 넘어갈 수 있는 동적 Navbar
    - 본인 프로필 사진 및 nickname과 email

### 3️⃣ 프로필 페이지
https://github.com/user-attachments/assets/424e2375-0482-4d1a-9254-aed09ce53ffa


- 별칭이 있을 경우 별칭, 없을 경우 이메일의 @이전까지 표시
- 해당 유저의 나이, 지역, 소득, 직업 정보
- 해당 유저가 찜한 예적금 및 지원금 정보
    - 클릭시 해당 상품 상세페이지로 이동
- 본인 프로필일 경우 회원정보 수정 버튼
    - 프로필 이미지, 소득, 지역, 직업 수정 가능

### 4️⃣ 예적금 조회 페이지
https://github.com/user-attachments/assets/f44e53e7-d90c-4b54-823f-bdafe21074c9


https://github.com/user-attachments/assets/f2f1978d-e8e0-4fd5-92e4-8ba68b0f6337

- 예금 및 적금으로 넘어갈 수 있는 버튼
- 전체 및 추천 페이지로 넘어갈 수 있는 버튼
- 해당 은행 상품만 필터링 해주는 버튼
- 상품 리스트를 나타내는 테이블
    - 찜 개수 표시
    - 각 필드명 클릭 시 오름차순 정렬
    - 페이지네이션 기능 구현
- 상품 명 클릭 시 상세 페이지로 이동
    - 찜 기능 구현

### 5️⃣ 정부지원금 조회 페이지
https://github.com/user-attachments/assets/0e5690f2-ee39-4056-be47-c77194c06991
- 전체 및 추천 페이지로 넘어갈 수 있는 버튼
- 지원금명을 기준으로 카테고리 명 생성
- 상품 리스트를 나타내는 테이블
    - 찜 개수 표시
    - 각 필드명 클릭 시 오름차순 정렬
    - 페이지네이션 기능 구현

https://github.com/user-attachments/assets/bff2abf9-216d-4423-b69a-8b50339dc0f0
- 상품 명 클릭 시 상세 페이지로 이동
    - 찜 기능 구현
    - 이용자 리뷰 생성 및 조회 기능
        - 리뷰 와 별점 미입력 시 경고창
        - 본인 리뷰인 경우 수정 및 삭제 가능
        - 본인 리뷰가 아닌 경우 프로필 사진 클릭 시 해당 유저의 프로필 페이지로 이동

### 6️⃣ 주변 은행 검색 페이지
https://github.com/user-attachments/assets/ad7bd276-f8de-4607-a227-28a5d4ae0606

- 광역시/도, 시/군/구, 은행명 선택 후 찾기 클릭 시 주변에 있는 은행 위치 표시
- 위치 아이콘 클릭 시 정확한 은행명 표시
- 지도 확대 및 축소 기능

### 6️⃣ 환율 계산기 페이지
https://github.com/user-attachments/assets/b071da16-3272-4031-aa39-cc15f7b9bb5c

- 통화, 기준, 한화 선택 후 계산하기 버튼 클릭 시 선택한 통화로 얼마인지 계산 후 반환
- 가장 방문이 많은 6개국의 지난 3개월 환율 추이 그래프 표시
- 매일 오후 11시 자동 크롤링 후 데이터 업데이트

### 7️⃣ 커뮤니티 페이지
https://github.com/user-attachments/assets/e7f18a34-2d62-430d-84f9-cbb6bf95cfd4
- 로그인 여부
    - 비로그인 시 로그인 하러 가기 버튼
    - 로그인 시 글쓰기 버튼
- 게시글 목록을 나타내는 테이블
    - 자신이 작성한 게시글만 보기
    - 해당 키워드에 해당하는 게시글만 보기
    - 프로필 사진 클릭 시 해당 유저의 프로필 페이지 이동
    - 댓글 개수 표시
    - 제목 선택 시 상세 페이지로 이동

https://github.com/user-attachments/assets/9c16db75-b84b-40c3-ac31-dc11f9bdc074

https://github.com/user-attachments/assets/b4b1e74a-bca9-437b-9fcf-ab12bef75b9d
- 인기 게시글
    - 댓글 개수가 많은 순으로 게시글 3개 표시
    - 제목 선택 시 상세 페이지로 이동
- 게시글 상세 페이지
    - 본인 게시글일 경우 수정 및 삭제 기능
    - 아닐 경우 해당 유저의 프로필 페이지로 이동 가능한 프로필 사진 표시
    - 댓글 기능
        - 본인 댓글일 경우 수정 및 삭제 기능
        - 아닐 경우 해당 유저의 프로필 페이지로 이동 가능한 프로필 사진 표시

### 8️⃣ 챗봇 기능
https://github.com/user-attachments/assets/5adb0320-3113-40d2-a518-317b395b77c6

- 금융 용어 문의
- 예적금 상품과 정부 지원금에 대한 자세한 설명


## 후기

### 🙇🏻‍♂️ 김경환
아이디어 구상과 설계 단계에서는 무엇을 어떻게 구현해야 할지 막막했습니다. 구현을 시작한 후에는 다음 단계가 막연하게 느껴지기도 했습니다. 
하지만 수업시간에 정리했던 내용을 참고하며 차근차근 진행한 결과, 모든 구현을 마칠 수 있었습니다.

프로젝트를 마무리하면서 크게 느낀 점은 두 가지입니다.
첫째, 초기 설계의 중요성입니다. 프로젝트를 초반 설계대로 완벽히 개발하는 것은 쉽지 않았지만, 
설계가 명확할수록 해당 부분의 개발은 훨씬 수월했습니다.
둘째, 팀원에 대한 신뢰의 필요성입니다. 이전에는 특정 기능을 제가 직접 개발해야만 다음 단계로 넘어갈 수 있다고 생각했지만, 
이번 프로젝트를 통해 팀원을 믿고 맡겼을 때 기능이 더 쉽고 빠르게 구현된다는 점을 깨달았습니다.

이 경험을 통해 짧게나마 협업의 중요성을 배울 수 있었고, 다음 프로젝트에서는 코드와 파일 구조를 더욱 최적화하여 개발하고 싶습니다.


### 🙇🏻‍♀️ 전혜준 
프론트엔드라는 직무에 대한 흥미가 생겨 진로로 고민하는 계기가 되었습니다. 앞으로 FE로 성장하는 제가 기대가 됩니다.
REST API 설계 구조를 이해하고 일부 직접 구현해봄으로써, 막연히 두려웠던 BackEnd 분야가 생각보다 재밌게 느껴졌습니다. 또한  1학기 초반에 비해 코드 읽는 실력이 확실히 늘었음을 느껴 뿌듯합니다. 

작은 부분부터 팀원과 같이 논의하며 하나씩 작업해가는 과정을 통해 서로 많이 배울 수 있었습니다. 





