<template>
    <div class="table-container mt-7">
            <v-data-table
                :headers="headers"
                :items="datas"
                class="elevation-1"
            >
                <template v-slot:header="{ props }">
                    <thead>
                        <tr>
                            <th
                                v-for="header in props.headers"
                                :key="header.key"
                                :class="['column sortable', header.key]"
                                @click="props.sort(header.key)"
                            >
                                {{ header.title }}
                                <v-icon small>{{ props.sortBy.includes(header.key) ? 'mdi-arrow-up' : '' }}</v-icon>
                            </th>
                        </tr>
                    </thead>
                </template>
                <template v-slot:item="{ item }">
                    <tr>
                        <td class="td-1">{{ item.category }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.manage }}</td>
                        <td>{{ item.target }}</td>
                        <td>{{ item.likes }}개</td>
                    </tr>
                </template>
            </v-data-table>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const headers = [
    { title: '카테고리', key: 'category', align: 'start', sortable: true },
    { title: '지원금명', key: 'name', align: 'start', sortable: true },
    { title: '주최기관', key: 'manage', align: 'start', sortable: true },
    { title: '대상', key: 'target', align: 'start', sortable: true },
    { title: '찜 갯수', key: 'likes', align: 'start', sortable: true },
]

const datas = ref([
    { category: '주거', name: '대전시 청년 월세지원금', manage: '국토교통부', target: '2~4년제 대학생', likes: 15 },
    { category: '의료', name: '코로나 특별 한시 지원금', manage: '국토교통부', target: '기준중위 소득 120%', likes: 8 },
    { category: '생활', name: '청년 생활안정 지원금', manage: '보건복지부', target: '기준중위 소득 100% 이하', likes: 22 },
    { category: '학업', name: '2024 대전인재육성장학생', manage: '대전광역시청', target: '차상위계층', likes: 18 },
    { category: '창업', name: '대전시 청년 창업 지원금', manage: '중소벤처기업부', target: '만 29세 이하 예비창업자', likes: 30 },
    { category: '농업', name: '대전 청년 농업인 육성 지원사업', manage: '농림축산식품부', target: '만 40세 미만 농업인', likes: 12 },
    { category: '학업', name: '청년 역량강화 지원사업', manage: '여성가족부', target: '만 19-34세 여성', likes: 25 },
    { category: '주거', name: '무주택 청년 가구 월세 지원사업', manage: '대전광역시청', target: '대전시 거주 19세~39세 청년', likes: 20 }
])
</script>

<style scoped>
.table-container {
    max-width: 1000px;
}

.option-card {
    padding: 20px;
}

:deep(.v-data-table) {
    background-color: white;
    border-radius: 4px;
    overflow: hidden;
}

:deep(.v-data-table th) {
    background-color: #f5f5f5;
    color: #333;
    font-weight: 700;
    border-bottom: 1px solid #e0e0e0;
    text-transform: uppercase;
    cursor: pointer;
}

:deep(.v-data-table td) {
    padding: 12px;
    border-bottom: 1px solid #e0e0e0;
    color: #666;
}

:deep(.v-data-table tr:hover) {
    background-color: #f8f9fa;
}

.td-1 {
    color: #658EA7 !important;
    font-weight: 600;
}

:deep(.sortable:hover) {
    background-color: #e9ecef;
}

:deep(.v-icon) {
    margin-left: 4px;
    font-size: 14px;
}
</style>