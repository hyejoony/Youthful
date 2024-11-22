<template>
    <h1 class="title" style="color:#658EA7;">커뮤니티</h1>
    <div>
        <RouterView />
    </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
</script>

<style scoped>
h1 {
    text-align: center;
}
div {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.title {

/* margin-left: 50px; */
margin-bottom: 40px;
margin-top: 20px;

}
</style>