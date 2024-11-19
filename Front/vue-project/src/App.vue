<template>
  <div>
    <AppNavBar />
  </div>
  <RouterView />
</template>

<script setup>
import AppNavBar from './components/Common/AppNavBar.vue';
</script>
<style>
/* 브라우저에 폰트 로드, 정의한 거 알리기 */
/* 브라우저  태그 기본 글씨크기 */
/* p,span : weight 400(regular) */
/* h1,h2,h3 : 700(bold) */
/* 태그마다 extrabold나 light 적용하고 싶으면 <style> h1 {font-weight: 700;}  지정 */
@font-face {
  font-family: 'Pretendard';
  src: url('@/assets/fonts/Pretendard-Light.ttf') format('truetype');
  font-weight: 300;
  font-style: normal; 
} 

@font-face {
  font-family: 'Pretendard';
  src: url('@/assets/fonts/Pretendard-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Pretendard';
  src: url('@/assets/fonts/Pretendard-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

@font-face {
  font-family: 'Pretendard';
  src: url('@/assets/fonts/Pretendard-ExtraBold.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
}


/* 전역설정 */
body, #app  {
  font-family: 'Pretendard', sans-serif !important;
}

</style>