<template>


        <h1 style="color:#658EA7;">
          {{ headerText }}
        </h1>

        <RouterView />

</template>

<script setup>
import { RouterView, useRoute } from 'vue-router';
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { onBeforeMount } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

const route = useRoute();

const headerText = computed(() => {
  return route.path.includes('review') ? '정부지원금 이용자 리뷰' : '정부지원금 비교';
});
</script>

<style scoped>
h1 {
  text-align: center;
}
</style>