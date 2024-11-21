<template>
    <div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore()

onMounted(() => {
    store.logout()
})

</script>

<style scoped>

</style>