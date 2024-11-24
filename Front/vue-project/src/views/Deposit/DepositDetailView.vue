<template>
    <ProductDetailHeader/>
    <ProductDetailContent 
        :productInfo="productInfo" 
        :interestRates="interestRates"/>

</template>

<script setup>
import { ref } from 'vue'
import ProductDetailHeader from '@/components/Common/SubsidyDetailHeader.vue';
import ProductDetailContent from '@/components/Common/SubsidyDetailContent.vue';

// 예시(Ui 보여주기위함, PROPS )
const productInfo = [
    { label: '가입대상', value: '실명의 개인 고객 (만 19세 이상)' },
    { label: '가입방법', value: '인터넷 신청 가능' },
    { label: '우대조건', value: '급여 이체 고객' },
    { label: '만기 후 이자율', value: '3.5%' },
    { label: '가입제한', value: '급여이체 고객전용' },
    { label: '기타 유의사항', value: '무통장식 분할 입금' },
    { label: '최고한도', value: '15' },
    { label: '공시 제출월', value: '2024-10-01' }
]

const interestRates = [
    { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '12' },
    { type: '정기예금', rate: '3.05', maxRate: '3.45', period: '24' },
    { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '36' },
    { type: '정기예금', rate: '2.04', maxRate: '3.45', period: '12' }
]
</script>

<style scoped>

</style>