<template>
    <!-- 상품 개인 추천 페이지 컴포넌트 헤더 -->
    <div style="align-content: center;">
        <h3 v-if="route.path.includes('subsidy')" style=" margin-top: 10px;">{{ store.userName
        }} 님을 위해 추천드리는 정부지원금 목록이에요.
        </h3>
        <h3 v-else style=" margin-top: 50px;">{{ store.userName }}님을 위해 추천드리는 상품 목록이에요.</h3>
        <div style="display: flex;  margin-top:10px;">
            <h5 class="hashtag"> {{ store.userBirthyear }}년생 </h5>
            <h5 class="hashtag">{{ store.userCareer }}</h5>
            <h5 class="hashtag">기준중위소득{{ store.userIncome }}</h5>
            <h5 class="hashtag">{{ store.userRegion }}</h5>
        </div>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue';
import { useAccountStore } from '@/stores/account';
const store = useAccountStore()
const route = useRoute()


</script>

<style scoped>
.hashtag {
    /* margin-top: 10px; */
    /* margin-left: 10px; */
    margin-right: 10px;
    border: 2px solid #658EA7;
    background-color: #658EA7;
    border-radius: 5px;
    padding: 5px;
    color: white;
}
</style>