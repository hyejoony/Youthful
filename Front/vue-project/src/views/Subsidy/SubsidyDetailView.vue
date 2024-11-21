<template>
    <ProductDetailHeader/>
    <ProductDetailContent 
        :productInfo="productInfo" />

</template>

<script setup>
import { ref } from 'vue'
import ProductDetailHeader from '@/components/Common/ProductDetailHeader.vue';
import ProductDetailContent from '@/components/Common/ProductDetailContent.vue';

// 예시(Ui 보여주기위함, PROPS )
const productInfo = [
    { label: '분류', value: '실명의 개인 고객 (만 19세 이상)' },
    { label: '지원대상', value: '인터넷 신청 가능' },
    { label: '문의처', value: '급여 이체 고객' },
    { label: '지원내용', value: '3.5%' },

]


</script>

<style scoped>

</style>