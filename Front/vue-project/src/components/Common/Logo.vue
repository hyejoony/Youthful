<template>
    <div class='container'>
        <div style='--d:1'></div>
        <div style='--d:2'></div>
        <div style='--d:3'></div>
        <div style='--d:4'></div>
        <div style='--d:5'></div>
        <div style='--d:6'></div>
    </div>
</template>

<script setup>

</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    overflow: hidden;
    width: 100%;
    height: 100%;
    background: #CACACA;
    display: flex;
    align-items: center;
    justify-content: center;
}

.container {
    /* 내부 자식 요소들이 컨테이너 요소 중앙에 정렬되도록 해줍니다. */
    display: flex;
    align-items: center;
    justify-content: center;
    width: 95px;
    /* 330px의 절반 */
    height: 95px;
    /* 330px의 절반 */

    /* border-raius 는 차례대로 Top, Right, Bottom, Left 순으로 값이 적용됩니다.*/
    border-radius: 20% 50% 20% 50%;

    /* 약간 희미하게 빛을 받는 듯한 느낌을 주기 위해 border 를 추가하고,
    부드러운 색감 변화를 주기 위해 linear-gradient 를 설정해줍니다.
 */
    border: 1px solid rgba(101, 142, 167, 0.6); 
    background: linear-gradient(180deg, #658EA7, #B0D2E6);
    /* 트랜잭션과 애니메이션 적용을 위한 옵션입니다.  */
    transition: border-radius 0.5s;
    animation: rotation 10s infinite linear;

}


.container::before {
    transition: 0.5s;
    /* position을 absolute로 지정하고, left,top, translate 를 조정하여 container 중앙에 
    정렬시킵니다. */
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 75px;
    /* 330px의 절반 */
    height: 75px;
    /* 330px의 절반 */

    background: white;

    /* radius 를 조절하여 모서리를 둥글게 만들어주고, 2px 정도의 외곽선을 만들어줍니다. */
    border-radius: 15% 15% 15% 15%;
    /* 혹은 border-radius: 15% */
    /* border: 2px solid rgba(101, 142, 167, 0.6); */
    /* 가시성 우선순위를 after에 생성된 요소보다 크게 하여 위로 올라가게 해줍니다.*/
    z-index: 1;

}

/* after 도 동일하게 작업하는데, before에 지정된 요소 보다 크기를 크게하고, 가시성을 보다 낮게
   지정하여 겹치게 해줍니다.
*/
.container::after {
    transition: 0.5s;
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 80px;
    /* 290px의 절반 */
    height: 80px;
    /* 290px의 절반 */
    z-index: 0;
    background: #F3F4F5;
    border-radius: 15% 15% 15% 15%;
    border: 2px solid rgba(101, 142, 167, 0.6);
}


.container {
    /* ---생략 ---*/
    animation: rotation 10s infinite linear;
}

@keyframes rotation {
    0% {
        transform: rotate(0);
    }

    100% {
        transform: rotate(360deg);
    }
}

/* .container 요소 내에 중첩하여 div 요소를 입력해줍니다. */
.container {
    div {
        /* --rotate 는 사용자 정의 변수입니다. --d 와 동일합니다.*/
        --rotate: calc(60deg*var(--d));

        /* 가시성을 앞서 container 요소의 bofore, after 보다 높게 해줍니다.*/
        z-index: 2;

        /* 세로로 길고 가로로 좁은 둥근 형태의 스타일을 만들어줍니다.*/
        width: 10px;
        /* 20px의 절반 */
        height: 37px;
        /* 150px의 절반 */
        border: 2px solid rgba(101, 142, 167, 0.6);
        border-radius: 20px;
        background-image: linear-gradient(180deg, #658EA7, #B0D2E6);
        /* 각 요소가 모두 독립된 레이어에서 동작하도록 absolute 로 지정합니다. */
        position: absolute;

        /* 앞서 할당한 --rotate을 var 함수를 이용해 rotate 함수의 인자로 전달합니다. 
     그리고 각 요소가 서로의 꼭짓점에 맞물리도록 설정하기 위해 translate를 사용하여 위치를 조정합니다.
   */
        transform: rotate(var(--rotate)) translate(19px);

        /* hover 를 통해 transition 을 적용 시 각 요소마다 트랜잭션의 시작 지점을 달리하기 위해 
      0.05s와 각 요소의 --d 에 할당된 값을 곱해주어 시간차를 만들어줍니다.*/
        transition-delay: calc(var(--d)*0.05s);

        /* 성능최적화를 위해 트랜잭션을 적용할 속성을 선택하여 각 속성 마다 실행할 트랜잭션 시간을
      지정해줍니다.
   */
        transition: transform 0.5s, border-radius 0.5s, width 1s, height 1s;
    }
}

.container:hover {
    border-radius: 50%;

    /* 별 모양 로고를 구성하는 각 요소가 교차하듯이 펼쳐지면서 컨테이너 주위를 감싸게 해줍니다.
    여기서 교차가 가능하게 하는 것은 translate 를 -200px 로 설정하여 서로 마주보고 있는 각 요소가
    마주보는 방향으로 200px 이동하영 교차되기 때문입니다.
  */
    div {
        width: 25px;
        /* 100px의 절반 */
        height: 10px;
        /* 20px의 절반 */
        transform: rotate(var(--rotate)) translate(-50px);
    }
}

/* 둥근 사각형이 원 모양이 됩니다.*/
.container:hover::before,
.container:hover::after {
    border-radius: 50%;
}
</style>