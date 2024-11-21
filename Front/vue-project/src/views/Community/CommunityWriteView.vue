<template>
    <v-card width="900" height="400" elevation="4">
        <card-title>
            <v-text-field v-model="inputTitle" placeholder="제목을 작성해주세요." variant="solo"></v-text-field>
        </card-title>
        <hr style="color: #767676;">
        <card-content>
            <v-text-field v-model="inputContent" class="v-text-field2" placeholder="본문을 작성해주세요." ></v-text-field>
        </card-content>
        <div>
            <p>키워드를 선택해주세요.</p>
            <!-- <v-btn v-for="(btn, index) in store.buttons" :key="index" :class="{ 'active-button': store.selectedButton === index }"
                @click="store.selectButton(index)" density="compact">
                {{ btn.caption }}
            </v-btn> -->
        </div>
    </v-card>
    <v-btn @click="SaveArticleFunc" class="mt-2" density="compact">글 올리기</v-btn>
</template>

<script setup>
import { UseCommunityStore } from '@/stores/community';
import { useRouter } from 'vue-router';
import { ref } from 'vue'
const router = useRouter()
const store = UseCommunityStore()

// 이 컴포넌트에서 입력한 데이터 
const inputTitle = ref('')
const inputContent = ref('')

// 인자로 전달
const SaveArticleFunc = () => { 
    store.SaveArticle(inputTitle, inputContent)
    // console.log('articlelist', store.ArticleList)
    router.push({name: 'community'})
}




</script>


<style scoped>
.v-text-field2 {
    height: 200px;
}

.active-button {
    background-color: #658EA7; 
    color: white;
}

</style>