<template>
    <div class="container">
        <SavingDetailHeader :saving="saving" />
        <SavingDetailContent :saving="saving" />
        <v-card class="product-card mt-3 ml-2 pb-3" width="900">
            <h3 class=" ml-7 mt-1 " style="padding-top: 10px; padding-bottom: 10px;"> 이용자 리뷰 </h3>
            <hr>

            <h5 style="color: #658EA7;" @click="gotoReview" class=" ml-7 mt-1 clickable-title">이용자 리뷰 보기</h5>
        </v-card>

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
import { useAccountStore } from '@/stores/account';
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


const router = useRouter()

// const id = route.params.id
const gotoReview = () => {
    console.log('id', id)
    router.push({ name: 'savingreview' , params: { id: id.value }})
}

// 예시(Ui 보여주기위함, PROPS )
// const productInfo = [
//     { label: '가입대상', value: '실명의 개인 고객 (만 19세 이상)' },
//     { label: '가입방법', value: '인터넷 신청 가능' },
//     { label: '우대조건', value: '급여 이체 고객' },
//     { label: '만기 후 이자율', value: '3.5%' },
//     { label: '가입제한', value: '급여이체 고객전용' },
//     { label: '기타 유의사항', value: '무통장식 분할 입금' },
//     { label: '최고한도', value: '15' },
//     { label: '공시 제출월', value: '2024-10-01' }
// ]

// const interestRates = [
//     { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '12' },
//     { type: '정기예금', rate: '3.05', maxRate: '3.45', period: '24' },
//     { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '36' },
//     { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '12' }
// ]
</script>

<style scoped>

</style>