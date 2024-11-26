<template>
    <!-- 상품 전체 목록 페이지 헤더 -->
    <v-card class="mt-6" >
        <div class="card-border">
            <div class="bank-section">
                <v-card 
                    v-for="bank in banks" 
                    :key="bank.name" 
                    class="card-border" 
                    @click="selectBank(bank.name)"
                >
                    <img class="mt-3 ml-8" :src="bank.logo" width="30px" alt="bank_logo">
                    <p class="txt-custom px-5"><b>{{ bank.name }}</b></p>
                </v-card>
            </div>
        </div>
    </v-card>
</template>

<script setup>
import { defineEmits } from 'vue';

// 이미지 임포트
import kbLogo from '@/assets/images/kb.png';
import ibkLogo from '@/assets/images/ibk_logo.png';
import shcLogo from '@/assets/images/shc_logo.png';
import wooriLogo from '@/assets/images/woori.png';
import hanaLogo from '@/assets/images/hana.png';

const emit = defineEmits();
const banks = [
    { name: '국민은행', logo: kbLogo },
    { name: '기업은행', logo: ibkLogo },
    { name: '신한은행', logo: shcLogo },
    { name: '우리은행', logo: wooriLogo },
    { name: '하나은행', logo: hanaLogo }
];

// 은행 선택 시 부모에게 이벤트를 발생시킴
const selectBank = (bankName) => {
    emit('bank-selected', bankName);
};
</script>

<style scoped>
.txt-custom {
    color: #AEACAC;
}

.card-border {
    gap: 20px;
    margin: auto;
    /* margin-top: 15px; */
}

.bank-section {
    display: flex;
    gap: 20px;
}
</style>