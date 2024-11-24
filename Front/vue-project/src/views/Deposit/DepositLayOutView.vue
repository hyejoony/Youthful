<template>
    <h1 style="color:#658EA7;">예금 비교</h1>
<RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';
import { onBeforeMount } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

</script>

<style scoped>
h1 {
text-align: center;
}
</style>