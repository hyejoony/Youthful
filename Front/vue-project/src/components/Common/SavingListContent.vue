<template>
    <div class="table-container mt-7">
        <v-data-table v-if="props.savings && props.savings.length" :headers="headers" :items="props.savings" class="elevation-1">
            <template v-slot:header="{ props }">
                <thead>
                    <tr>
                        <th v-for="header in props.headers" :key="header.key" :class="['column sortable', header.key]"
                            @click="props.sort(header.key)">
                            {{ header.title }}
                            <v-icon small>{{ props.sortBy.includes(header.key) ? 'mdi-arrow-up' : '' }}</v-icon>
                        </th>
                    </tr>
                </thead>
            </template>
            <template v-slot:item="{ item }">
                <tr>
                    <td class="td-1">{{ item.kor_co_nm }}</td>
                    <td class="clickable-title" @click="gotoDetail(item.id)">{{ item.fin_prdt_nm }}</td>
                    <td>{{ getInterestRate(item.saving_options, 6) }}</td>
                    <td>{{ getInterestRate(item.saving_options, 12) }}</td>
                    <td>{{ getInterestRate(item.saving_options, 24) }}</td>
                    <td>{{ getInterestRate(item.saving_options, 36) }}</td>
                    <td><v-icon style="color: #658EA7;" >mdi-heart</v-icon> {{ item.likes_count }}개</td>

                </tr>
            </template>
        </v-data-table>
    </div>
</template>

<script setup>
import { ref ,onMounted} from 'vue'
import { useRouter, useRoute } from 'vue-router';
const route = useRoute()

const router = useRouter()
// defineProps를 최상위 레벨에서 사용
const props = defineProps({
    savings: Array
})


const gotoDetail = (id) => {
    router.push({ name: 'savingdetail', params: { id }})
    console.log('id',id)


}


onMounted(() => {
  console.log('Mounted:', props.savings)
})


const headers = [
    { title: '은행명', key: 'fin_prdt_nm', align: 'start', sortable: true },
    { title: '상품명', key: 'kor_co_nm', align: 'start', sortable: true },
    { title: '6개월', key: 'intr_rate_6', align: 'start', sortable: true },
    { title: '12개월', key: 'intr_rate_12', align: 'start', sortable: true },
    { title: '24개월', key: 'intr_rate_24', align: 'start', sortable: true },
    { title: '36개월', key: 'intr_rate_36', align: 'start', sortable: true },
    { title: '찜 개수', key: 'likes_count', align: 'start', sortable: true },

]

const getInterestRate = (options, term) => {
    const option = options.find(opt => opt.save_trm === term);
    return option ? option.intr_rate2 : '-'
    }

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

.clickable-title {
    cursor: pointer;
    transition: color 0.3s ease;
}


</style>