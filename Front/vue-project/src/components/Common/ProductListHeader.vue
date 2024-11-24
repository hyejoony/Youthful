<template>

        <!-- 상품 전체 목록 페이지 헤더 -->
        <v-card class="mt-6 " width="815" height="150px">
            <div class="card-border">
                <div class="bank-section">
                    <v-card class=" card-border" width="100" height="80px">
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
        </v-card>

</template>

<script setup>

</script>

<style scoped>
.txt-custom {
    /* color: #658EA7; */
    color: #AEACAC;
}

.card-border {
    gap: 20px;
    /* 카드 사이의 간격 */
    margin: auto;
    margin-top: 15px;

}


.bank-section {
    display: flex;
    gap: 20px
}
</style>