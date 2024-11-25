<template>
    <div class="product-cards">
        <v-card class="product-card ml-2" width="900">
            <div class="card-header mt-3 ml-7">
                <h3>상품 안내</h3>
            </div>
            <hr>
            <div class="card-content">
                <!-- 상품 정보 반복 -->
                <div class="info-row mt-3 ml-7">
                    <span class="label">가입대상</span>
                    <span class="value">{{ saving.join_member  }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">가입방법</span>
                    <span class="value">{{ saving.join_way }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">우대조건</span>
                    <span class="value">{{ saving.spcl_cnd }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">만기 후 이자율</span>
                    <span class="value">{{ saving.mtrt_int }}</span>
                </div>
                <!-- <div class="info-row mt-3 ml-7">
                    <span class="label">가입제한</span>
                    <span class="value">{{ saving.join_deny  }}</span>
                </div> -->
                <div class="info-row mt-3 ml-7">
                    <span class="label">기타 유의사항</span>
                    <span class="value">{{ saving.etc_note  }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">최고한도</span>
                    <span class="value">{{ saving.max_limit }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">공시 제출월</span>
                    <span class="value">{{ saving.dcls_month  }}</span>
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
                        <th>적립유형명</th>
                        <th>저축 금리 유형명</th>
                        <th>저축금리</th>
                        <th>최고 우대금리</th>
                        <th>저축기간</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="option in savingOptions" :key="option.id">
                        <td>{{ option.rsrv_type_nm }}</td>
                        <td>{{ option.intr_rate_type_nm }}</td>
                        <td>{{ option.intr_rate }}%</td>
                        <td>{{ option.intr_rate2 }}%</td>
                        <td>{{ option.save_trm }}개월</td>
                    </tr>
                </tbody>
            </v-table>
        </v-card>
    </div>
</template>

<script setup>

import { useRoute } from 'vue-router'
import { computed } from 'vue'

const props = defineProps({
    saving: Object
})

const route = useRoute()

const savingOptions = computed(() => {
    return props.saving?.saving_options || [];
})


</script>

<style scoped>
.product-cards {
    display: grid;
    gap: 20px;
    margin-top: 20px;
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