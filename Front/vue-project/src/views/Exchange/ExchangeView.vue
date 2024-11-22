<template>
    <v-container>
        <v-row>
            <v-col sm='12' lg="12">
                <h1 class="title" style="color:#658EA7;">환율계산기</h1>
                <h5 style="color: #767676;">출처 : 네이버 증권</h5>

                <v-card class="v-card mx-auto" max-width="820" height="300" hover>
                    <v-form class="ml-10">
                        <v-select width="200px" label="통화 선택" :items="SelectCurrency" variant="solo"></v-select>
                        <v-text-field width="200px" clearable label="KRW" variant="solo"></v-text-field>
                        <v-select width="200px" label="기준" :items="ExchangeStandard" variant="solo"></v-select>
                    </v-form>
                    <h1>890</h1>
                </v-card><br>
                <ExchangeGraph />
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import ExchangeGraph from '@/components/Exchange/ExchangeGraph.vue';

// 데이터
const SelectCurrency = ['USD', 'EUR', 'JPY']; // 예시 데이터
const ExchangeStandard = ['매매기준율', '송금 보내실 때', '송금 받으실 때']; // 예시 데이터
</script>

<style scoped>
.v-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    /* 공간분배 */
}

h1 {
    text-align: center;
}

.title {

    /* margin-left: 50px; */
    margin-bottom: 40px;
    margin-top: 20px;

}

h5 {
    font-weight: 400;
    margin-left: 64%;
}
</style>