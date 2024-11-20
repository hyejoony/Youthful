<template>
    <nav>
        <RouterLink :to="{ name: 'home'}">Home</RouterLink> |
        <RouterLink :to="{ name: 'signup'}">SignUp</RouterLink> | 
        <RouterLink :to="{ name: 'login'}">Login</RouterLink> |
        <RouterLink :to="{ name: 'profile'}">Profile</RouterLink> |
        <RouterLink :to="{ name: 'exchange'}">Exchange</RouterLink> |
        <RouterLink :to="{ name: 'searchbank'}">Search Bank</RouterLink> |
        <RouterLink :to="{ name: 'community'}">Community</RouterLink> |
    </nav>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>
/* routerlink 클릭 후 보라색으로 변경되는거 취소하기 */
a {
    text-decoration: none; 
    color: #767676;
    }
</style>