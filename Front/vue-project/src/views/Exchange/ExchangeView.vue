<template>

                <h1 class="title" style="color:#658EA7;">환율계산기</h1>
                <h5 style="color: #767676;">출처 : 네이버 증권(수수료 제외)</h5>

                <v-card class="v-card mx-auto" max-width="820" height="300" hover>
                    <v-form @submit.prevent="calculateExchange" class="ml-10">
                        <v-select v-model="selectedCountry" width="200px" label="통화 선택" :items="SelectCurrency"
                            variant="solo"></v-select>
                        <v-select v-model="selectedStandard" width="200px" label="기준" :items="ExchangeStandard"
                            variant="solo"></v-select>
                        <div class="amount-input-container">

                            <v-text-field @input="updateKoreanAmount" v-model="krwAmount" width="200px" clearable
                                label="KRW" variant="solo"></v-text-field>
                            <span class="korean-amount" v-if="koreanAmount">
                                {{ koreanAmount }}
                            </span>
                        </div>
                        <v-btn type="submit" variant="outlined"
                            style="color: #658EA7;"><v-icon>mdi-currency-usd</v-icon>계산하기</v-btn>
                    </v-form>
                    <h1> {{ exchangeResult }} </h1>


                </v-card><br>
                <ExchangeGraph :exchanges="exchanges"/>

</template>

<script setup>
import ExchangeGraph from '@/components/Exchange/ExchangeGraph.vue';
import { UseExchangeStore } from '@/stores/exchange';
import { ref, onMounted, computed } from 'vue';

const storeExchange = UseExchangeStore()
const exchanges = ref([])

onMounted(() => {
    storeExchange.getExchanges()
    console.log('exchanges', storeExchange.exchanges)
    exchanges.value = storeExchange.exchanges


})

// 숫자를 한글로 변환하는 함수
const numberToKorean = (number) => {
    const units = ['', '만', '억', '조'];
    const koreanNumbers = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구'];
    const positions = ['', '십', '백', '천'];

    if (number === 0) return '영원';
    if (!number) return '';

    let result = '';
    let unitIndex = 0;
    let numberString = number.toString();

    while (numberString.length > 0) {
        let segment = numberString.slice(-4);
        numberString = numberString.slice(0, -4);

        let segmentResult = '';
        for (let i = 0; i < segment.length; i++) {
            let digit = parseInt(segment[i]);
            if (digit !== 0) {
                segmentResult += (digit !== 1 || positions[segment.length - 1 - i] === '')
                    ? koreanNumbers[digit] : '';
                segmentResult += positions[segment.length - 1 - i];
            }
        }

        if (segmentResult !== '') {
            result = segmentResult + units[unitIndex] + result;
        }
        unitIndex++;
    }

    return result + '원';
};
// 입력값이 변경될 때마다 한글 금액 업데이트
const updateKoreanAmount = () => {
    if (krwAmount.value) {
        const amount = parseInt(krwAmount.value);
        koreanAmount.value = numberToKorean(amount);
    } else {
        koreanAmount.value = '';
    }
};

// 환전가격 계산 처리 변수들
const selectedCountry = ref('');
const krwAmount = ref('');
const exchangeResult = ref('');
const selectedStandard = ref('');
const koreanAmount = ref('');


// 데이터
const SelectCurrency = computed(() =>
    exchanges.value.map(exchange => exchange.country_name)
);
const ExchangeStandard = ['사실 때', '파실 때'];

const calculateExchange = () => {
    if (!selectedCountry.value || !krwAmount.value) {
        alert('국가와 환전하실 금액을 모두 입력해주세요.');
        return;
    }
    const selectedExchange = exchanges.value.find(
        exchange => exchange.country_name === selectedCountry.value
    );

    // 선택된 기준에 따라 환율 결정
    let rate;
    if (selectedStandard.value === '사실 때') {
        rate = parseFloat(selectedExchange.cash_send.replace(/,/g, '')); // 현찰 살 때 환율
    } else if (selectedStandard.value === '파실 때') {
        rate = parseFloat(selectedExchange.cash_receive.replace(/,/g, '')); // 현찰 팔 때 환율
    }

    // 쉼표 제거하고 숫자로 변환
    console.log('정제된 rate:', rate);

    const amount = parseInt(krwAmount.value);
    console.log('입력된 KRW:', amount);

    const exchangedAmount = amount / rate;
    console.log('계산된 환전액:', exchangedAmount);

    // 디버깅을 위한 통화 코드 출력
    console.log('전체 환율 데이터:', selectedExchange);

        // 천 단위 쉼표 추가 및 소수점 2자리까지 표시
    const formattedAmount = new Intl.NumberFormat('en-US', {
        maximumFractionDigits: 2,
        minimumFractionDigits: 2
    }).format(exchangedAmount);

    // 소수점 2자리까지 표시
    exchangeResult.value = `${formattedAmount} ${selectedExchange.cur_unit}`;
    console.log('exchangeResult', exchangeResult.value)
};





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
    display: flex;
    margin-bottom: 10px;
    justify-content: end;
    margin-right: 175px;
}
.amount-input-container {
    position: relative;
    margin-bottom: 16px;
}

.korean-amount {
    position: absolute;
    bottom: -10px;
    left: 12px;
    font-size: 0.9em;
    color: #666;
}
</style>