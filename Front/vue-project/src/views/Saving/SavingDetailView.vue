<template>
    <RouterView />
    <div class="container">
        <SavingDetailHeader :saving="saving" />
        <SavingDetailContent :saving="saving" />

        <a href="/saving" style="color: #767676; font-size: 13px" class="mt-2 mb-2">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import SavingDetailHeader from '@/components/Common/SavingDetailHeader.vue';
import SavingDetailContent from '@/components/Common/SavingDetailContent.vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { onMounted } from 'vue';
import { UseSavingStore } from '@/stores/saving';

import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { onBeforeMount } from 'vue';
const router = useRouter()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

const storeAccount = useAccountStore()
const storeSaving = UseSavingStore()

const route = useRoute();

const saving = ref('')
const id = ref('')


onMounted(() => {
    axios({
        method: 'get',
        url: `${storeSaving.API_URL}/api/v1/savings/${route.params.id}/`,
        headers: {
            Authorization: `Token ${storeAccount.token}`
        }
    })
        .then((res => {
            console.log('특정 data',res.data) // 객체반환
            saving.value = res.data
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