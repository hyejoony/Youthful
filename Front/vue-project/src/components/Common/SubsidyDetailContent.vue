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
                    <span class="label">분류</span>
                    <span class="value">{{ subsidy.name_category }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">지원대상</span>
                    <span class="value">{{ subsidy.target }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">내용</span>
                    <span class="value">{{ subsidy.content }}</span>
                </div>
                <div class="info-row mt-3 ml-7">
                    <span class="label">문의처</span>
                    <span class="value">{{ subsidy.contact }}</span>
                </div>
            </div>
        </v-card>

    </div>
</template>

<script setup>

defineProps({
    subsidy: Object
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