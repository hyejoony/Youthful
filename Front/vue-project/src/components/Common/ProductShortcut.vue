<template>

        <!-- 상품 페이지 예금/적금 바로가기, 전체/추천 바로가기 컴포넌트 -->
        <v-btn-toggle v-model="toggle_exclusive" class="toggle-color" mandatory @update:modelValue="handleToggleChange">
            <v-btn v-if="isSubsidyRoute" :value="'전체'" :class="{ 'selected-btn': toggle_exclusive === '전체' }">
                전체
            </v-btn>
            <v-btn v-if="isSubsidyRoute" :value="'추천'" :class="{ 'selected-btn': toggle_exclusive === '추천' }">
                추천
            </v-btn>
            <v-btn v-if="!isSubsidyRoute" :value="'예금'" :class="{ 'selected-btn': toggle_exclusive === '예금' }">
                예금
            </v-btn>
            <v-btn v-if="!isSubsidyRoute" :value="'적금'" :class="{ 'selected-btn': toggle_exclusive === '적금' }">
                적금
            </v-btn>
        </v-btn-toggle>



        <div v-if="!isSubsidyRoute" style="margin-left: 55px; margin-top: 20px;">
            <span @click="goback" class="clickable-title" :class="{ 'active-title': selectedTitle === '전체' }">전체 </span>
            <span> | </span>
            <span @click="gotoReco" class="clickable-title" :class="{ 'active-title': selectedTitle === '추천' }">
                추천</span>
            <span class="speech-bubble">
                나에게 딱 맞는 상품을 추천해드려요
            </span>
        </div>

</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router';

const router = useRouter()
const route = useRoute()

const toggle_exclusive = ref('')
const selectedTitle = ref('')

const isSubsidyRoute = computed(() => route.path.includes('/subsidy'))

onMounted(() => {
    if (isSubsidyRoute.value) {
        toggle_exclusive.value = route.path.includes('recommend') ? '추천' : '전체'
    } else {
        toggle_exclusive.value = route.path.includes('/saving') ? '적금' : '예금'
        selectedTitle.value = route.path.includes('recommend') ? '추천' : '전체'
    }
})

const gotoReco = () => {
    if (isSubsidyRoute.value) {
        router.push('/subsidy/recommend')
    } else if (toggle_exclusive.value === '예금') {
        router.push({ name: 'depositrecommend' })
    } else {
        router.push({ name: 'savingrecommend' })
    }
    selectedTitle.value = '추천'
}

const goback = () => {
    if (isSubsidyRoute.value) {
        router.push('/subsidy')
    } else if (toggle_exclusive.value === '예금') {
        router.push({ name: 'deposit' })
    } else {
        router.push({ name: 'saving' })
    }
    selectedTitle.value = '전체'
}

const handleToggleChange = (value) => {
    if (isSubsidyRoute.value) {
        router.push(value === '추천' ? '/subsidy/recommend' : '/subsidy')
    } else {
        if (value === '예금') {
            router.push('/deposit')
        } else if (value === '적금') {
            router.push('/saving')
        }
    }
    toggle_exclusive.value = value
}
</script>


<style scoped>
.txt-custom {
    color: #AEACAC;
}

.card-border {
    gap: 20px;
    margin: auto;
    margin-top: 15px;
}

.bank-section {
    display: flex;
    gap: 20px
}

.toggle-color {
    color: #767676;
    border: 0.5px solid #767676;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    margin-left: 50px;
}

.speech-bubble {
    position: relative;
    background: #658EA7;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 1px 3px #658EA7;
    /* 추가 스타일링 */
    font-size: 14px;
    color: white;
    width: 220px;
    margin: 20px;
}

.speech-bubble::after {
    content: "";
    position: absolute;
    position: absolute;
    top: 50%;
    /* 중앙에 위치하도록 변경 */
    left: -9px;
    /* 왼쪽으로 살짝 이동 */
    transform: translateY(-50%);
    /* 세로 중앙 정렬 */
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #658EA7 transparent;
}

.clickable-title {
    cursor: pointer;
    transition: color 0.3s ease;
}


.selected-btn {
    background-color: #658EA7 !important;
    color: white !important;
}

/* 기존 스타일 유지 */
.active-title {
    font-weight: bold;
    color: #658EA7;
    /* 원하는 강조 색상으로 변경 가능 */
}

</style>