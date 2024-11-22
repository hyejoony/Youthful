<template>
    <div class="container">
        <ProductDetailHeader />
        <ProductDetailContent :productInfo="productInfo" />
        <v-card class="product-card mt-3 ml-2 pb-3" width="900">
            <h3 class=" ml-7 mt-1 " style="padding-top: 10px; padding-bottom: 10px;"> 이용자 리뷰 </h3>
            <hr>

            <h5 style="color: #658EA7;" @click="gotoReview" class=" ml-7 mt-1 ">이용자 리뷰 보기</h5>
        </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import ProductDetailHeader from '@/components/Common/ProductDetailHeader.vue';
import ProductDetailContent from '@/components/Common/ProductDetailContent.vue';

const router = useRouter()

// 예시(Ui 보여주기위함, PROPS )
const productInfo = [
    { label: '분류', value: '실명의 개인 고객 (만 19세 이상)' },
    { label: '지원대상', value: '인터넷 신청 가능' },
    { label: '문의처', value: '급여 이체 고객' },
    { label: '지원내용', value: '3.5%' },

]


const gotoReview = () => {
    router.push({ name: 'subsidyreview' })
}


</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>
