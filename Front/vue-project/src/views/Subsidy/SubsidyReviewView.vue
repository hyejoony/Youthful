<template>
    <h4 class="pa-4 mb-">보조금 이름</h4>
    <v-card width="800" class="pa-4">
        <!-- 리뷰 작성 폼 -->
        <v-form @submit.prevent="submitReview">
            <v-row align="center">
                <v-col cols="10">
                    <!-- 리뷰 텍스트 입력 필드 -->
                    <v-text-field v-model="reviewText" placeholder="리뷰를 남겨보세요." hide-details></v-text-field>
                </v-col>
                <v-col cols="2">
                    <!-- 리뷰 제출 버튼 -->
                    <v-btn type="submit" color="#658EA7" class="ml-2" rounded='xl'>리뷰 남기기</v-btn>
                </v-col>
            </v-row>
            <v-row class="mt-2">
                <v-col cols="12">
                    <!-- 별점 선택 컴포넌트 -->
                    <v-rating v-model="rating" hover clearable :length="5" :size="32" color="#658EA7" />
                    <!-- 선택된 별점 표시 -->
                    <span class="ml-2">{{ rating || '0' }}점</span>
                </v-col>
            </v-row>
        </v-form>

        <v-divider class="my-4"></v-divider>

        <!-- 리뷰 목록 표시 영역 -->
        <div class="review-list">
            <v-list>
                <!-- 각 리뷰 항목을 순회하며 표시 -->
                <v-list-item v-for="(review, index) in subsidy.comments" :key="index">
                    <v-list-item-content>
                        <!-- 리뷰 텍스트 및 버튼들 -->
                        <div class="d-flex align-center justify-space-between">
                            <v-list-item-title>{{ review.text }}</v-list-item-title>
                            <div class="button-group">
                                <!-- 좋아요 버튼 -->
                                <v-btn icon small @click="toggleLike(index)" class="icon-button">
                                    <v-icon size="19" :color="review.liked ? '#658EA7' : ''">
                                        {{ review.liked ? 'mdi-heart' : 'mdi-heart-outline' }}
                                    </v-icon>
                                </v-btn>
                                <!-- 수정 버튼 (모달 열기) -->
                                <v-btn icon small @click="openEditDialog(review, index)" class="icon-button">
                                    <v-icon size="19">mdi-pencil</v-icon>
                                </v-btn>
                                <!-- 삭제 버튼 -->
                                <v-btn icon small @click="deleteReview(index)" class="icon-button">
                                    <v-icon size="19">mdi-delete</v-icon>
                                </v-btn>
                            </div>
                        </div>
                        <v-list-item-subtitle>
                            <!-- 리뷰의 별점을 읽기 전용으로 표시 -->
                            <v-rating :model-value="review.rating" style="margin-bottom: 4px;" readonly :length="5"
                                :size="16" color="#658EA7" />
                        </v-list-item-subtitle>
                        <!-- 작성자 및 작성일자 정보 -->
                        <span class="text-caption mr-2">작성자 {{ review.author }}</span>
                        <span class="text-caption">작성일자 {{ review.date }}</span>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </div>

        <!-- 수정 모달창 -->
        <v-dialog v-model="editDialog" max-width="600px">
            <v-card>
                <v-card-title>리뷰 수정</v-card-title>
                <v-card-text>
                    <!-- 수정할 리뷰 내용 입력 필드 -->
                    <v-text-field v-model="editedReviewText" placeholder="리뷰 내용을 수정하세요." hide-details></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="#658EA7" @click="updateReview">수정 완료</v-btn>
                    <v-btn text @click="closeEditDialog">취소</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </v-card>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { UseSubsidyStore } from '@/stores/subsidy';
import { useAccountStore } from '@/stores/account';
import { useRoute } from 'vue-router';
const storeAccount = useAccountStore()
const storeSubsidy = UseSubsidyStore()
const route = useRoute()

const subsidy = ref('')

onMounted(() => {
    axios({
        method: 'get',
        url: `${storeSubsidy.API_URL}/api/v1/subsidies/${route.params.id}/`,
        headers: {
            Authorization: `Token ${storeAccount.token}`
        }
    })
        .then((res => {
            console.log('상세 보조금 데이터 반환',res.data) // 객체반환
            subsidy.value = res.data
        }))
})

const reviewText = ref('');
const rating = ref(0);
const reviews = ref([]);
const editDialog = ref(false); // 모달 상태
const editedReviewText = ref(''); // 수정할 리뷰 내용
let currentEditIndex = ref(null); // 현재 수정 중인 리뷰 인덱스

const submitReview = () => {
    if (!reviewText.value.trim()) {
        alert('리뷰 내용을 입력해주세요.');
        return;
    }
    if (!rating.value) {
        alert('별점을 선택해주세요.');
        return;
    }

    // 현재 날짜 생성
    const currentDate = new Date().toLocaleDateString();

    reviews.value.push({
        text: reviewText.value,
        rating: rating.value,
        author: '익명', // 실제 사용시 로그인된 사용자 이름으로 대체
        date: currentDate,
        liked: false
    });

    console.log('리뷰 내용:', reviewText.value);
    console.log('별점:', rating.value);

    reviewText.value = '';
    rating.value = 0;
};

// 좋아요 토글 함수
const toggleLike = (index) => {
    reviews.value[index].liked = !reviews.value[index].liked;
};

// 모달 열기 함수
const openEditDialog = (review, index) => {
    editedReviewText.value = review.text; // 기존 리뷰 내용으로 초기화
    currentEditIndex.value = index; // 현재 수정 중인 인덱스 저장
    editDialog.value = true; // 모달 열기
};

// 모달 닫기 함수
const closeEditDialog = () => {
    editDialog.value = false; // 모달 닫기
};

// 리뷰 수정 함수
const updateReview = () => {
    if (currentEditIndex.value !== null) {
        reviews.value[currentEditIndex.value].text = editedReviewText.value; // 수정된 내용으로 업데이트
    }
    closeEditDialog(); // 모달 닫기
};

// 리뷰 삭제 함수
const deleteReview = (index) => {
    if (confirm('정말로 이 리뷰를 삭제하시겠습니까?')) {
        reviews.value.splice(index, 1);
    }
};
</script>

<style scoped>
.v-rating {
    display: inline-flex;
    align-items: center;
}

.button-group {
    display: flex;
    align-items: center;
}

/* 버튼의 배경과 테두리 없애기 */
.icon-button {
    box-shadow: none;
}

/* 버튼 크기 조정 */
.icon-button .v-btn {
    width: 20px;
    height: 20px;
}
.clickable-title {
    cursor: pointer;
    transition: color 0.3s ease;
}

</style>