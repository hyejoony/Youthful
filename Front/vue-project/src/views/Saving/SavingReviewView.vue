<template>
    <h4 class="pa-4 mb-2">보조금 이름</h4>
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
            <p v-if="subsidy?.comments?.length === 0">아직 작성된 리뷰가 없어요. 리뷰를 남겨보세요.</p>
            <v-list v-else>
                <!-- 각 리뷰 항목을 순회하며 표시 -->
                <v-list-item v-for="(review, index) in subsidy?.comments" :key="index">
                    <v-list-item-content>
                        <!-- 리뷰 텍스트 및 버튼들 -->
                        <div class="d-flex align-center justify-space-between">
                            <v-list-item-title style="font-size: 15px;"> {{ review.content }}</v-list-item-title>
                            <div class="button-group">
                                <!-- 수정 버튼 (모달 열기) -->
                                <v-btn icon small @click="openEditDialog(review, index)" class="icon-button">
                                    <v-icon size="19">mdi-pencil</v-icon>
                                </v-btn>
                                <!-- 삭제 버튼 -->
                                <v-btn icon small @click="deleteReview(review.id, index)" class="icon-button">
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
                        <span class="text-caption mr-2">작성자 {{ review.user }}</span>
                        <span class="text-caption ">작성일자 {{ review.updated_at.match(/^(\d{4}-\d{2}-\d{2})/)[1] }}</span>

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
                    <v-row class="mt-2">
                        <v-col cols="12">
                            <!-- 별점 선택 컴포넌트 -->
                            <v-rating v-model="editedRating" hover clearable :length="5" :size="32" color="#658EA7" />
                            <!-- 선택된 별점 표시 -->
                            <span class="ml-2">{{ editedRating || '0' }}점</span>
                        </v-col>
                    </v-row>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="#658EA7" @click="updateReview">수정 완료</v-btn>
                    <v-btn text @click="closeEditDialog">취소</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>
    <div style="text-align: center;">
        <a href="/subsidy/detail/${subsidyId}" style="color: #767676; font-size: 13px;" class="mt-2 mb-2">이전 페이지로
            돌아가기<v-icon>mdi-chevron-left</v-icon></a>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { UseSavingStore } from '@/stores/saving';
import { useAccountStore } from '@/stores/account';
import { useRoute } from 'vue-router';
const storeAccount = useAccountStore()
const storeSaving = UseSavingStore()
const route = useRoute()

const saving = ref('') // 여기에서 내가 사용할 변수 

const savingId = route.params.id
onMounted(() => {
    axios({
        method: 'get',
        url: `${storeSaving.API_URL}/api/v1/savings/${route.params.id}/`,
        headers: {
            Authorization: `Token ${storeAccount.token}`
        }
    })
        .then((res => {
            console.log('상세 적금 데이터 반환', res.data) // 객체반환
            saving.value = res.data
            console.log('saving', saving)
        }))
})

// 리뷰 생성 -------------------------------------------------------------------
const reviewText = ref('');
const rating = ref(0);

// - 비동기처리 !! 
const submitReview = async () => {
    if (!reviewText.value.trim()) {
        alert('리뷰 내용을 입력해주세요.');
        return;
    }
    if (!rating.value) {
        alert('별점을 선택해주세요.');
        return;
    }

    const newComment = {
        content: reviewText.value,
        rating: rating.value,
        id: savingId
    };

    try {
        const response = await axios({
            method: 'post',
            url: `${storeSaving.API_URL}/api/v1/savings/${route.params.id}/comments/`,
            headers: {
                Authorization: `Token ${storeAccount.token}`
            },
            data: newComment
        });

        // API 응답에서 새로 생성된 댓글 정보를 받아옵니다.
        const createdComment = response.data;

        saving.value.comments.push(createdComment);

        // 입력 필드 초기화
        reviewText.value = '';
        rating.value = 0;

        console.log('댓글이 성공적으로 추가되었습니다.', saving.value.comments);

    } catch (error) {
        console.error('댓글 추가 중 오류 발생:', error);
    }
};


// 리뷰 수정 ----------------------------------------------------------------------------------
const editDialog = ref(false); // 모달 상태
const editedReviewText = ref(''); // 수정할 리뷰 내용
const editedRating = ref('')
const currentReviewId = ref(null);
const currentReviewIndex = ref(null)

// 모달 열기 함수 
const openEditDialog = (review, index) => {
    console.log('opendialog_idx', index)
    editedReviewText.value = review.content; // 기존 리뷰 내용으로 초기화
    currentReviewId.value = review.id
    currentReviewIndex.value = index
    console.log('review.rating', review.rating)
    editedRating.value = review.rating

    console.log('currentReviewId)', currentReviewId.value)
    editDialog.value = true; // 모달 열기
};

// 모달 닫기 함수
const closeEditDialog = () => {
    editDialog.value = false; // 모달 닫기
};


const updateReview = async () => {

    const newComment = {
        content: editedReviewText.value,
        rating: editedRating.value,
    };

    try {
        const response = await axios({
            method: 'put',
            url: `${storeSaving.API_URL}/api/v1/savings/${savingId}/comments/${currentReviewId.value}/`,
            headers: {
                Authorization: `Token ${storeAccount.token}`
            },
            data: newComment
        });


        saving.value.comments[currentReviewIndex.value] = response.data;

        // 입력 필드 초기화
        reviewText.value = '';
        rating.value = 0;

        console.log('댓글이 성공적으로 수정되었습니다.', saving.value.comments);
        editDialog.value = false; // 모달닫기

    } catch (error) {
        console.error('댓글 수정 중 오류 발생:', error);
    }
};


// 리뷰 삭제 ---------------------------------------------------------------------------

const deleteReview = async (reviewId, index) => {

    try {
        const response = await axios({
            method: 'delete',
            url: `${storeSaving.API_URL}/api/v1/savings/${savingId}/comments/${reviewId}/`,
            headers: {
                Authorization: `Token ${storeAccount.token}`
            },

        });

        saving.value.comments.splice(index, 1)

        editDialog.value = false; // 모달닫기

    } catch (error) {
        console.error('댓글 삭제 중 오류 발생:', error);
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