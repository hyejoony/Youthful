<template>
    <div class='top-div-flex'>
        <v-card class="product-card mt-3 ml-2 pb-3" width="800">
            <div class="card-flex mt-3 ml-7 pt-1">
                <h3>신한 5 연금 예금</h3>
                <span class="bank-name ml-10 mt-1">신한은행</span>
                <span class="ml-10 mt-1" style="font-size: 14px;">
                    <v-icon size="small" style="color: #658EA7;">mdi-heart</v-icon> 찜 12개
                </span>
            </div>
        </v-card>
        <v-card class="mt-3 ml-2" width="90">
            <div class="pl-4 pt-4">
                <v-icon size="large" style="color: #658EA7;">mdi-heart</v-icon>
            </div>
        </v-card>
    </div>
    <div class="product-cards">
        <v-card class="product-card ml-2" width="900">
            <div class="card-header mt-3 ml-7">
                <h3>상품 안내</h3>
            </div>
            <hr>
            <div class="card-content">
                <!-- 상품 정보 반복 -->
                <div class="info-row mt-3 ml-7" v-for="(item, index) in productInfo" :key="index">
                    <span class="label">{{ item.label }}</span>
                    <span class="value">{{ item.value }}</span>
                </div>
            </div>
        </v-card>
        <v-card class="option-card mt-3 ml-2" width="900">
            <div class="card-header">
                <h3>옵션</h3>
            </div>
            <hr>
            <v-table>
                <thead>
                    <tr>
                        <th>저축 금리 유형명</th>
                        <th>저축금리</th>
                        <th>최고 우대금리</th>
                        <th>저축기간</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in interestRates" :key="index">
                        <td>{{ item.type }}</td>
                        <td>{{ item.rate }}%</td>
                        <td>{{ item.maxRate }}%</td>
                        <td>{{ item.period }}개월</td>
                    </tr>
                </tbody>
            </v-table>
        </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'

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
.top-div-flex {
    display: flex;
}

.product-cards {
    display: grid;
    gap: 20px;
    margin-top: 20px;
}

.card-flex {
    display: flex;
}

.card-header {
    margin-bottom: 15px;
}

.bank-name {
    color: #666;
    font-size: 14px;
}

.info-row {
    display: flex;
    margin-bottom: 12px;
}

.label {
    width: 120px;
    color: #666;
    font-size: 14px;
}

.value {
    flex: 1;
    font-size: 14px;
}

.option-card {
    padding: 20px;
}

:deep(.v-table th) {
    background-color: #f5f5f5;
    color: #333;
    font-weight: 700;
    border-bottom: 1px solid #e0e0e0;
}

:deep(.v-table td) {
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
    color: #666;
}

:deep(.v-table tr:hover) {
    background-color: #f8f9fa;
}
</style>