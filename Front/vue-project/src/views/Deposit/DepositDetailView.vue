<template>
    <RouterView />
    <div class="container">
        <DepositDetailHeader :deposit="deposit" />
        <DepositDetailContent :deposit="deposit" />

        <a href="/deposit" style="color: #767676; font-size: 13px" class="mt-2 mb-2">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import DepositDetailHeader from '@/components/Common/DepositDetailHeader.vue';
import DepositDetailContent from '@/components/Common/DepositDetailContent.vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { onMounted } from 'vue';
import { UseDepositStore } from '@/stores/deposit';
import { useAccountStore } from '@/stores/account';

import { RouterLink, RouterView } from 'vue-router';
import { onBeforeMount } from 'vue';

const router = useRouter()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});
const storeAccount = useAccountStore()
const storeDepoist = UseDepositStore()

const route = useRoute();

const deposit = ref('')
const id = ref('')


onMounted(() => {
    axios({
        method: 'get',
        url: `${storeDepoist.API_URL}/api/v1/deposits/${route.params.id}/`,
        headers: {
            Authorization: `Token ${storeAccount.token}`
        }
    })
        .then((res => {
            console.log('특정 data',res.data) // 객체반환
            deposit.value = res.data
            id.value = route.params.id
            console.log('id',id.value)
        }))
})


</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}

.clickable-title {
    cursor: pointer;
    transition: color 0.3s ease;
}

</style>