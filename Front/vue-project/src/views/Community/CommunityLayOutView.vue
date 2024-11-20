<template>
    <h1 class="mt-4" style="color:#658EA7;">커뮤니티</h1>

    <div>
        
        <RouterView />
    </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
</script>

<style scoped>
h1 {
    margin-left: 50px;
    margin-bottom: 20px
}

div {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>