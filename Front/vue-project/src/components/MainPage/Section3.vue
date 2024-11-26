<template>
    <br>
    <br>
    <div class="carousel-container ">
    <div class="mt-6">
        <div class="text-center">
        <h2 style="display: inline;" class="mt-6 mb-2">5대 은행의 예적금 정보를 알 수 있어요.</h2>
        <h2 style="display: inline;"> 물론</h2>
        <h2 style="display: inline;" class="txt-custom"> 나에게 딱 맞는 추천</h2>
        <h2 style="display: inline;">까지도요.</h2>
        </div>
    </div>
    <div class="bank-section">
        <div class="cards">
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-4 ml-8" width="35px" src="@/assets/images/kb.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>국민은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/ibk_logo.png" alt="bank_logo">
                <p class="txt-custom px-5"><b>기업은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/shc_logo.png" alt="bank_logo">
                <p class="txt-custom px-5"><b>신한은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/woori.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>우리은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8 " width="32px" src="@/assets/images/hana.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>하나은행</b></p>
            </v-card>
        </div>
    </div>
        <div class="button-container" >
            <v-btn height="45" style="color: white; background-color: #658EA7;" rounded="xl" elevation="0">
                <span  @click="gotoDeposit" class="font-weight-bold" style="font-size: medium;">추천 받아보기</span>
            </v-btn>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

const gotoDeposit = () => {
  router.push({ name: 'deposit' });
};
</script>

<style scoped>
.bank-section {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cards {
    display: flex;
}

.txt-custom {
    color: #658EA7;
}

.card-border {
    border: 2px solid #9DB9BC;
    margin: 30px;
}

.button-container {
    display: flex;
    justify-content: center;
    width: 100%;
    /* margin-top: 5px; */
}

.carousel-container {
    transition: all 0.7s;
}

.carousel-container:hover {
    transform: translateY(-15px);
}
</style>