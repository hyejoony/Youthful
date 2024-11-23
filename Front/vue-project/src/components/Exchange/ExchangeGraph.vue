<template>
    <h3 class="mt-3" style="color: #658EA7; text-align: center">가장 방문이 많은 6개국의 지난 3개월 추이</h3>
    <h5 style="color: #767676;">매일 오후 11시 업데이트</h5>
    <div class="card-container">
        <v-card class="mt-0" width="820">
            <v-virtual-scroll :items="cards" height="600">
                <div class="div-card mb-2" v-for="(row, rowIndex) in rows" :key="rowIndex">
                    <v-card v-for="(exchange, index) in row" :key="index" class="v-card" width="800" height="300" hover>
                        <img :src="exchange.image_src" alt="Currency Image" style="width: 100%; height: 250px;" />
                        <div class="ml-3">{{ exchange.country_name }} ({{ exchange.cur_unit }})</div>
                    </v-card>
                </div>
            </v-virtual-scroll>
        </v-card>
    </div>
</template>


<script setup>
import { ref, computed } from 'vue'
const cards = ref([1])  // 3개의 스크롤 아이템 생성
// props 정의
const props = defineProps({
    exchanges: Array
});

// rows를 계산하여 각 행에 2개의 카드를 배치
const rows = computed(() => {
    const itemsPerRow = 2; // 한 행에 보여줄 아이템 수
    const result = [];

    // props.exchanges에 접근하여 데이터 처리
    for (let i = 0; i < Math.min(props.exchanges.length, 6); i += itemsPerRow) {
        result.push(props.exchanges.slice(i, i + itemsPerRow));
    }

    return result;
});
</script>

<style scoped>
.v-card {
    margin-top: 10px;

}

.div-card {
    display: flex;
    justify-content: center;
    gap: 20px;


}

.card-container {
    display: flex;
    justify-content: center;
}

h5 {
    font-weight: 400;
    display: flex;
    margin-bottom: 10px;
    justify-content: end;
    margin-right: 175px;
}
</style>