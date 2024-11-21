<template>
    <br>
    <v-card v-if="article" class="mt-4" width="900" height="500" elevation="2">
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
                <v-dialog v-model="store.dialog" max-width="500">
                    <v-card>
                        <v-card-title class="ml-2" style="color: #658EA7;">게시글 수정</v-card-title>
                        <v-card-text>
                            <v-text-field v-model="store.editTitle" label="제목"></v-text-field>
                            <v-textarea v-model="store.editContent" label="내용"></v-textarea>
                            <div>
                                <p class="mb-1">키워드를 선택해주세요.</p>
                                <v-btn v-for="(btn, index) in store.buttons" :key="index"
                                    :class="{ 'active-button': store.selectedButton === index }" @click="selectButton(index)"
                                    density="compact">
                                    {{ btn.caption }}
                                </v-btn>
                            </div>

                        </v-card-text>
                        <template v-slot:actions>
                            <!-- 이 슬롯은 카드 하단에 버튼과 같은 액션 요소를 추가하는 데 사용 -->
                            <v-btn variant="text" class="ms-auto" text="취소" @click="store.dialog = false"></v-btn>
                            <v-btn variant="text" style="color: #658EA7;" text='저장' @click="saveChangesFunc"></v-btn>
                        </template>
                    </v-card>
                </v-dialog>
            </div>
            <v-btn @click="deleteArticleFunc(article.id)">삭제하기<v-icon>mdi-trash-can-outline</v-icon></v-btn>
        </div>
        <card-content>
            <p class="mt-4 pl-4">{{ article?.content }}</p>
        </card-content>
        <hr style="color: #767676;" class="mt-3">
        <div class='comment-input' style="display: flex; align-content: center;">
            <v-text-field class="mt-1 pl-3" style="width: 70%;" density="compact" placeholder="댓글 달기"
                prepend-inner-icon="mdi-comment-text-outline"></v-text-field>
            <v-btn class="mb-8 ml-2 mt-1 mr-2" color="#658EA7" size="large" variant="tonal">
                작성
            </v-btn>
        </div>
        <div class='comment-list'>
            <p>댓글 목록</p>
            <p> 님 좀 짱인듯<span>
                    <v-btn density="compact" icon="mdi-pencil"></v-btn>
                    <v-btn density="compact" icon="mdi-trash-can-outline"></v-btn>
                </span>
            </p>
        </div>
    </v-card>
    <a href="#" style="color: #767676;">이전 페이지로 돌아가기<v-icon>mdi-chevron-left</v-icon></a>
</template>

<script setup>
import { UseCommunityStore } from '@/stores/community';
import { onMounted } from 'vue';
import { ref } from 'vue'
const store = UseCommunityStore()
import { useRoute } from 'vue-router';
const route = useRoute()
const id = route.params.id // route 파라미터 불러오기

const article = ref(null)
// 반응형으로 해야 안정적 
onMounted(()=> {
    article.value = store.getDetail(id); // onmount

})

// 모달 열 때 기존 내용을 수정용 변수에 복사 
const openDialog = () => {
    store.editTitle = article.value.title
    store.editContent = article.value.content
    store.dialog = true
    store.editedButton = article.value.keyword
}

// 데이터 저장
// - 파라미터로 불러왔으니 매개변수 필요없음x
const saveChangesFunc = () => {
    store.saveUpdateChanges(id)
}

// Function to select a button
const selectButton = (index) => {
    // Update the selected button index
    store.selectButton(index)
};


const deleteArticleFunc = (id) => {
    store.deleteArticle(id)
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