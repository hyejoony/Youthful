<template>
  <v-data-table :headers="headers" :items="datas" class="elevation-3" :items-per-page="-1" hide-default-footer>
    <template v-slot:item="{ item }">
      <tr style="color: #767676;">
        <td class="td-1">{{ item.category }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.manage }}</td>
        <td>{{ item.target }}</td>
      </tr>
    </template>
  </v-data-table>
</template>

<script setup>
import { ref } from 'vue'

const headers = [
  { title: '카테고리', key: 'category', align: 'start' },
  { title: '지원금명', key: 'name', align: 'start' },
  { title: '주최기관', key: 'manage', align: 'start' },
  { title: '대상', key: 'target', align: 'start' },
]

const datas = ref([
  { category: '주거', name: '대전시 청년 월세지원금', manage: '국토교통부', target: '2~4년제 대학생' },
  { category: '의료', name: '코로나 특별 한시 지원금', manage: '국토교통부', target: '기준중위 소득 120%' },
  { category: '생활', name: '청년 생활안정 지원금', manage: '보건복지부', target: '기준중위 소득 100% 이하' },
  { category: '학업', name: '2024 대전인재육성장학생', manage: '대전광역시청', target: '차상위계층' },
  { category: '창업', name: '대전시 청년 창업 지원금', manage: '중소벤처기업부', target: '만 29세 이하 예비창업자' },
  { category: '교육', name: '청년 역량강화 지원사업', manage: '여성가족부', target: '만 19-34세 여성' },
  { category: '주거', name: '무주택 청년 가구 월세 지원사업', manage: '대전광역시청', target: '대전시 거주 19세~39세 청년' }
])
</script>

<style scoped>
.td-1 {
  color: #658EA7 !important;
  font-weight: 600;
}
</style>