<template>
    <br>
    <v-card class="mt-4" width="900" height="800" elevation="2">
        <card-head>
            <p class="mt-2 pl-4"> {{ article?.title }}</p>
        </card-head>
        <hr style="color: #767676;" class="mt-3">
        <div class="card-user-info mt-2 pl-4" style="color: #767676;">
            <span> id님</span>
            <span> 수정날짜</span>
            <div>
                <v-btn @click="openDialog">수정하기<v-icon>mdi-pencil</v-icon></v-btn>
                <!-- 모달창 -->
                <v-dialog v-model="dialog" max-width="500">
                    <v-card>
                        <v-card-title class="ml-2" style="color: #658EA7;">게시글 수정</v-card-title>
                        <v-card-text>
                            <v-text-field v-model="editTitle" label="제목"></v-text-field>
                            <v-textarea v-model="editContent" label="내용"></v-textarea>
                            <div>
                                <p class="mb-1">키워드를 선택해주세요.</p>
                                <v-btn v-for="(btn, index) in store.buttons" :key="index"
                                    :class="{ 'active-button': editedButton === btn.caption }"
                                    @click="editButton(btn.caption)" density="compact">
                                    {{ btn.caption }}
                                </v-btn>
                            </div>

                        </v-card-text>
                        <template v-slot:actions>
                            <!-- 이 슬롯은 카드 하단에 버튼과 같은 액션 요소를 추가하는 데 사용 -->
                            <v-btn variant="text" class="ms-auto" text="취소" @click="dialog = false"></v-btn>
                            <v-btn variant="text" style="color: #658EA7;" text='저장' @click="saveChangesFunc"></v-btn>
                        </template>
                    </v-card>
                </v-dialog>
            </div>
            <v-btn @click="deleteArticleFunc">삭제하기<v-icon>mdi-trash-can-outline</v-icon></v-btn>
        </div>
        <card-content>
            <p class="mt-4 pl-4">{{ article?.content }}</p>
        </card-content>
        <hr style="color: #767676;" class="mt-3">

        <v-form @submit.prevent="saveComment">
            <div class='comment-input' style="display: flex; align-content: center;">
                <v-text-field v-model="inputComment" class="mt-1 pl-3" style="width: 70%;" density="compact"
                    placeholder="댓글 달기" prepend-inner-icon="mdi-comment-text-outline"></v-text-field>
                <v-btn type="submit" class="mb-8 ml-2 mt-1 mr-2" color="#658EA7" size="large" variant="tonal">
                    작성
                </v-btn>

            </div>
        </v-form>

        <div v-if="commentList.length > 0" v-for="comment in commentList" :key="comment.createdAt">
            <p>{{ comment.content }}
                <span>
                    <v-btn @click="UpdateComment(comment.commentId)" density="compact" icon="mdi-pencil"></v-btn>
                    <v-btn density="compact" icon="mdi-trash-can-outline"></v-btn>
                </span>
            </p>
        </div>
        <div v-else  class="ml-4" style="color: #767676;">아직 달린 댓글이 없어요.</div>
    </v-card>
    <a href="/community" style="color: #767676;">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>
</template>

<script setup>
import { UseCommunityStore } from '@/stores/community';
import { onMounted } from 'vue';
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';

const store = UseCommunityStore()
const route = useRoute()
const router = useRouter()

const id = route.params.id // 특정 id, route 파라미터 불러오기


//  - 상세페이지 불러오기

// 반응형으로 해야 안정적 (데이터 로드)
const article = ref(null)
onMounted(() => {
    // console.log('id',id)
    article.value = store.getDetail(id); // onmount
    // console.log('articlevalue',article.value)
    commentList.value = store.getComments(id) // 댓글
    // console.log(commentList.value)
})

const dialog = ref(false) // 모달창 기본설정

// 임시 수정 데이터
const editTitle = ref('')
const editContent = ref('')
// 임시 수정 변수 
const editedButton = ref(null)

// 모달 열 때 기존 내용을 수정용 변수에 복사 
const openDialog = () => {
    editTitle.value = article.value.title
    editContent.value = article.value.content
    dialog.value = true
    editedButton.value = article.value.keyword
}

const editButton = (caption) => {
    editedButton.value = caption
}

// 데이터 저장
// - 파라미터로 불러왔으니 매개변수 필요없음x
const saveChangesFunc = () => {
    const result = store.saveUpdateChanges(id, editTitle, editContent, editedButton)
    if (result) {
        dialog.value = false
    }
}

// 삭제
const deleteArticleFunc = () => {
    store.deleteArticle(id)
    router.push({ name: 'community' })

}

// 댓글 
const inputComment = ref('') // 사용자 입력 댓글
const commentList = ref([])
// 댓글 저장
const saveComment = () => {
    store.saveComment(id, inputComment)
    inputComment.value = '' // 입력 필드 초기화


}

const UpdateComment = (commentId) => {
    store.UpdateComment(id,commentId)
}

// 테스트용 // 데이터 초기화
// store.resetArticle()

</script>

<style scoped>
.card-user-info {
    font-size: 15px,

}

.active-button {
    background-color: #658EA7;
    color: white;
}
</style>