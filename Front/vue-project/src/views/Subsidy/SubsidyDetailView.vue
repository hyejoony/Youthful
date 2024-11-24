<template>
    <RouterView />
    <div class="container">
        <SubsidyDetailHeader :subsidy="subsidy" />
        <SubsidyDetailContent :subsidy="subsidy" />
        <v-card class="product-card mt-3 ml-2 pb-3" width="900">
            <h3 class=" ml-7 mt-1 " style="padding-top: 10px; padding-bottom: 10px;"> 이용자 리뷰 </h3>
            <hr>

            <h5 style="color: #658EA7;" @click="gotoReview" class=" ml-7 mt-1 clickable-title">이용자 리뷰 보기</h5>
        </v-card>

        <a href="/subsidy" style="color: #767676; font-size: 13px" class="mt-2 mb-2">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import SubsidyDetailHeader from '@/components/Common/SubsidyDetailHeader.vue';
import SubsidyDetailContent from '@/components/Common/SubsidyDetailContent.vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { onMounted } from 'vue';
import { UseSubsidyStore } from '@/stores/subsidy';
import { useAccountStore } from '@/stores/account';
const storeAccount = useAccountStore()
const storeSubsidy = UseSubsidyStore()

import { RouterLink, RouterView } from 'vue-router';
import { onBeforeMount } from 'vue';

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

const route = useRoute();

const subsidy = ref('')
const id = ref('')


onMounted(() => {
    axios({
        method: 'get',
        url: `${storeSubsidy.API_URL}/api/v1/subsidies/${route.params.id}/`,
        headers: {
            Authorization: `Token ${storeAccount.token}`
        }
    })
        .then((res => {
            console.log('특정 data',res.data) // 객체반환
            subsidy.value = res.data
            id.value = route.params.id
            console.log('id',id.value)
        }))
})


const router = useRouter()

// const id = route.params.id
const gotoReview = () => {
    console.log('id', id)
    router.push({ name: 'subsidyreview' , params: { id: id.value }})
}


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
