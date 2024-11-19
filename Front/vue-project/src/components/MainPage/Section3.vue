<template>
    <div class="mt-6">
        <h2 style="display: inline;" class="mt-6 mb-2">5대 은행의 예적금 정보를 알 수 있어요.</h2>
        <h2 style="display: inline;"> 물론</h2>
        <h2 style="display: inline;" class="txt-custom"> 나에게 딱 맞는 추천</h2>
        <h2 style="display: inline;">까지도요.</h2>
    </div>
    <div>
        <div class="cards">
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/kb_logo.PNG" alt="KB_bank_logo">
                <p class="txt-custom px-5"><b>국민은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/kb_logo.PNG" alt="KB_bank_logo">
                <p class="txt-custom px-5"><b>기업은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/kb_logo.PNG" alt="KB_bank_logo">
                <p class="txt-custom px-5"><b>신한은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/kb_logo.PNG" alt="KB_bank_logo">
                <p class="txt-custom px-5"><b>우리은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/kb_logo.PNG" alt="KB_bank_logo">
                <p class="txt-custom px-5"><b>하나은행</b></p>
            </v-card>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

.cards {
    display: flex;
}
.txt-custom {
    color: #658EA7;

}

.card-border {
    border: 2px solid #9DB9BC;
    /* 테두리 색상 및 두께 설정 */
}
</style>