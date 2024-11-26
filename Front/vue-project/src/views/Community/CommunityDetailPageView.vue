<template>
    <Routerview />
    <br>
    <v-card v-if="article" class="mt-4" width="800" max-height="800" elevation="2">
        <card-head>
            <p class="mt-2 pl-4"> {{ article.title }}</p>
        </card-head>
        <hr style="color: #767676;" class="mt-3">
        <div class="card-user-info mt-2 pl-4" style="color: #767676;">
            <h4 class="hashtag mb-3">{{ article.keyword }}</h4>
            <span style="font-size: 13px !important;">{{ article.user_display_name }}님 | 작성일 : {{
                article.created_at.slice(0,10) }}</span>

            <card-content>
                <h4 style="color: #658EA7;" class="mt-4 pl-1">{{ article.content }}</h4>
            </card-content>
            <div class="change">
                <v-btn variant="text" v-if="storeAccount.userId !== article.user" @click="goProfile(article.user)"
                    class="clickable-item">
                    프로필
                    <v-avatar size="24">
                        <v-img :src="`${baseUrl}${article.profile_image}`" alt="User Profile"></v-img>
                    </v-avatar>
                </v-btn>
                <div v-if="storeAccount.userId == article.user">
                    <v-btn variant="text" class="mt-3" @click="openDialog">수정<v-icon>mdi-pencil</v-icon></v-btn>
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
                                <v-btn variant="text" style="color: #658EA7;" text='저장'
                                    @click="saveChangesFunc()"></v-btn>
                            </template>
                        </v-card>
                    </v-dialog>
                </div>
                <v-btn variant="text" class="mt-3" v-if="storeAccount.userId == article.user"
                    @click="deleteArticleFunc">삭제하기<v-icon>mdi-trash-can-outline</v-icon></v-btn>
            </div>
        </div>
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
            <p style="margin-bottom: 3px; margin-left: 15px;">{{ comment.content }}
                <span>
                    <span>
                        <v-avatar v-if="storeAccount.userId !== comment.user" @click="goProfile(comment.user)"
                            class="clickable-item" size="small">
                            <v-img :src="`${baseUrl}${comment.profile_image}`" alt="Comment Profile"></v-img>
                        </v-avatar>
                        <v-btn v-if="storeAccount.userId == comment.user" @click="openDialogComment(comment)"
                            density="compact" icon="mdi-pencil">
                            <v-icon size="16px">mdi-pencil</v-icon>
                        </v-btn>
                        <v-dialog v-model="dialogComment" max-width="500">
                            <v-card>
                                <v-card-title class="ml-2" style="color: #658EA7;">댓글 수정</v-card-title>
                                <v-card-text>
                                    <v-textarea v-model="editContentComment" label="내용"></v-textarea>
                                </v-card-text>
                                <template v-slot:actions>
                                    <!-- 이 슬롯은 카드 하단에 버튼과 같은 액션 요소를 추가하는 데 사용 -->
                                    <v-btn variant="text" class="ms-auto" text="취소"
                                        @click="dialogComment = false"></v-btn>
                                    <v-btn variant="text" style="color: #658EA7;" text='저장'
                                        @click="saveChangesComment(comment.id)"></v-btn>
                                </template>
                            </v-card>
                        </v-dialog>
                    </span>
                    <v-btn v-if="storeAccount.userId == comment.user" @click="deleteComment(comment.id)"
                        density="compact" icon="mdi-trash-can-outline"></v-btn>
                </span>
            </p>
            <span class="ml-4" style="font-size: 13px !important; color: #767676;">작성자 : {{ comment.user_display_name
                }}님 | 작성일
                : {{ comment?.updated_at.slice(0, 10) }}</span>
            <hr class="mb-5">
        </div>
        <div v-else class="ml-5 mb-5" style="color: #767676;">아직 달린 댓글이 없어요.</div>
    </v-card>
    <a href="/community" style="color: #767676; font-size: 13px" class="mt-2 mb-2">이전 페이지로
        돌아가기<v-icon>mdi-chevron-left</v-icon></a>
</template>

<script setup>
import { UseCommunityStore } from '@/stores/community';
import { onMounted } from 'vue';
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { onBeforeMount } from 'vue';

const storeAccount = useAccountStore()
const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

onBeforeMount(() => {
    if (!storeAccount.isLogin) {
        router.push('/login');
    }
});

const store = UseCommunityStore()
const route = useRoute()
const router = useRouter()
const id = route.params.id // 특정 id, route 파라미터 불러오기


//  - 상세페이지 불러오기

// 반응형으로 해야 안정적 (데이터 로드)
const article = ref(null)
onMounted(() => {
    console.log('idDetail', id)
    article.value = store.getDetail(id); // onmount
    console.log('articlevalue는', article.value)
    commentList.value = store.getComments(id) // 댓글
    console.log('comment는', commentList.value)
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

// 게시글 수정
const saveChangesFunc = async () => {
    const payload = {
        id: id,
        editTitle: editTitle.value,
        editContent: editContent.value,
        editedButton: editedButton.value
    }
    const result = await store.saveUpdateChanges(payload)
    article.value.title = editTitle
    article.value.keyword = editedButton
    article.value.content = editContent
    dialog.value = false
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
const saveComment = async () => {
    const payload = {
        id: id, inputComment: inputComment.value
    }
    const result = await store.saveComment(payload)
    commentList.value.push(result)
    inputComment.value = '' // 입력 필드 초기화
}

const deleteComment = async (commentId) => {
    const result = await store.deleteComment(id, commentId)
    const index = commentList.value.findIndex(comment => comment.id === result.id)
    commentList.value.splice(index, 1)
}



const editContentComment = ref('')
const dialogComment = ref(false) // 모달창 기본설정
const currentEditingCommentId = ref(null)

const openDialogComment = (comment) => {
    currentEditingCommentId.value = comment.id
    editContentComment.value = comment.content
    dialogComment.value = true
}


// 댓글 수정
const saveChangesComment = async () => {
    const payload = {
        articleId: id,
        commentId: currentEditingCommentId.value,
        editContentComment: editContentComment.value,
    }
    const result = await store.saveUpdateChangesComment(payload)
    const comment = commentList.value.find(comment => comment.id === currentEditingCommentId.value)
    comment.content = editContentComment.value
    dialogComment.value = false
    currentEditingCommentId.value = null
}


const goProfile = (id) => {
    router.push({ name: 'profile', params: { id: id } })
}


</script>

<style scoped>
.card-user-info {
    font-size: 15px;
}

.active-button {
    background-color: #658EA7;
    color: white;
}

.change {
    display: flex;
    align-items: center;
    gap: 10px;
    /* 버튼 사이의 간격 */
}

.change>* {
    flex-shrink: 0;
    /* 자식 요소들이 줄어들지 않도록 설정 */
}

.clickable-item {
    cursor: pointer;
}

/* 버튼인데 underline 되길래 지워뒀어  */
.clickable-item:hover {
    /* text-decoration: underline; */
    color: #658EA7;
}

.hashtag {
    margin-top: 5px;
    border: 2px solid #658EA7;
    background-color: #658EA7;
    border-radius: 20px;
    padding: 5px;
    color: white;
    width: 80px;
    height: 35px;
    text-align: center;
}
</style>