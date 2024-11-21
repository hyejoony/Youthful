<template>
    <nav>
        <RouterLink :to="{ name: 'home'}">Home</RouterLink> |
        <RouterLink :to="{ name: 'signup'}">SignUp</RouterLink> | 
        <RouterLink :to="{ name: 'login'}">Login</RouterLink> |
        <!-- 아래 v-if는 임시 방편 나중에 전체적으로 로그인 되었을 경우 안되었을 경우로 나누기 -->
        <RouterLink v-if="store.isLogin" :to="{ name: 'logout' }">Logout</RouterLink> | 
        <RouterLink v-if="store.isLogin" :to="{ name: 'profile', params: { id: store.userId }}">Profile</RouterLink> | 
        <RouterLink :to="{ name: 'exchange'}">Exchange</RouterLink> |
        <RouterLink :to="{ name: 'searchbank'}">Search Bank</RouterLink> |
        <RouterLink :to="{ name: 'community'}">Community</RouterLink> |
        <RouterLink :to="{ name: 'deposit'}">Deposit</RouterLink> 
    </nav>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore()

</script>

<style scoped>
/* routerlink 클릭 후 보라색으로 변경되는거 취소하기 */
a {
    text-decoration: none; 
    color: #767676;
    }
</style>