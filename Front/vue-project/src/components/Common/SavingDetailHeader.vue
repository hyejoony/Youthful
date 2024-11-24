<template>
    <div class='top-div-flex'>
        <v-card class="product-card mt-3 ml-2 pb-3" width="800">
            <div class="card-flex mt-3 ml-7 pt-1">
                <h3>{{saving.fin_prdt_nm}} | {{ saving.kor_co_nm }}</h3>
                <!-- <span class="bank-name ml-10 mt-1"> {{ saving. }} </span> -->
                <span class="ml-10 mt-1" style="font-size: 14px;"> 
                    <v-icon size="small" style="color: #658EA7;">mdi-heart</v-icon> 찜 개수 {{ saving.likes_count }}개
                </span>
            </div>
        </v-card>
        <v-card class="mt-3 ml-2" width="90">
            <v-btn
                class=" heart-center"
                @click="toggleLike"
                variant="text"
                elevation="0"
            >
                <v-icon
                    size="large"
                    style="color: #658EA7;"
                >
                    {{ isLiked ? 'mdi-heart' : 'mdi-heart-outline' }}
                </v-icon>
            </v-btn>
        </v-card>
    </div>
</template>

<script setup>

const props = defineProps({
    saving: Object
})

import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAccountStore } from '@/stores/account';
import { useRoute } from 'vue-router';
const storeAccount = useAccountStore()
const route = useRoute()

// 반응형 상태 정의
const isLiked = ref(false)
const likesCount = ref(props.saving.likes_count)

// API 통신을 위한 기본 설정
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1',
    headers: {
            Authorization: `Token ${storeAccount.token}`
        }
})

// 초기 좋아요 상태 확인
const fetchLikeStatus = async () => {
    try {
        const response = await api.get(`/savings/${route.params.id}/`)
        isLiked.value = response.data.is_liked
        likesCount.value = response.data.likes_count
    } catch (error) {
        console.error('좋아요 상태 조회 중 오류 발생:', error)
    }
}

// 컴포넌트 마운트 시 초기 상태 로드
onMounted(() => {
    fetchLikeStatus()
})

// 좋아요 토글 함수
const toggleLike = async () => {
    try {
        const action = isLiked.value ? 'unlike' : 'like'
        const response = await api.put(`/savings/${route.params.id}/`, { action })
        
        isLiked.value = response.data.is_liked
        likesCount.value = response.data.likes_count
        console.log('수정 성공')
    } catch (error) {
        console.error('좋아요 처리 중 오류 발생:', error)
    }
}

</script>


<style scoped>
.top-div-flex {
    display: flex;
}

.card-flex {
    display: flex;
}

.heart-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
}
.heart-top-left {
    padding-left: 16px;
    padding-top: 16px;
}
</style>