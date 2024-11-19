<template>
  <br>
  <div class='flex'>
    <div class="ml-10 mr-10 mt-1">
      <Logo />
    </div>
    <div class="title">
      <h1 style="color: #658EA7; display: inline; ">Youthful, </h1>
      <h1 class="mt-2" style="display: inline;">1인 청년 가구 자산관리 서비스</h1>
      <h3>경제 개념은 어렵고, 돈을 어떻게 모아야할지 막막한 청년들을 위한 금융 나침반</h3>
      <!-- <h3 style='display: inline;'>나침반</h3> -->
    </div>
  </div>
  <Section1 />
  <Section2 />
  <Section3 />
  <Section4 />
  <Section5 />



</template>

<script setup>
import Logo from '@/components/Common/Logo.vue';
import Section1 from '@/components/MainPage/Section1.vue';
import Section2 from '@/components/MainPage/Section2.vue';
import Section3 from '@/components/MainPage/Section3.vue';
import Section4 from '@/components/MainPage/Section4.vue';
import Section5 from '@/components/MainPage/Section5.vue';
</script>

<style scoped>
.title {

  /* margin-left: 50px; */
  margin-bottom: 20px
}

.flex {
  display: flex;
}
</style>