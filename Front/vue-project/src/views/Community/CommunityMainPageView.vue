<template>
    <div class="total-div">
        <v-card width="900" height="80" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">로그인 후 이용 가능해요.</h3>
            <v-btn @click="writeArticle" width="100" height="30" class="mt-2 ml-4"
                rounded="xl">글쓰기<v-icon>mdi-pencil</v-icon>
                <RouterLink />
            </v-btn>
        </v-card>

        <v-card class="mt-4 " width="900" height="110" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">인기 게시글</h3>
            <div class="ml-4">
                <h5 style="display: inline;">{{ store.keyword }} |</h5>
                <h5 style="font-weight: 400; display: inline;"> {{ store.title }}</h5>
            </div>
        </v-card>
        <v-card class="mt-4" width="900" height="1200px" elevation="2">
            <card-head>
                <div class="mt-3 pr-2 keyword-div" style="display: flex;">
                    <v-btn style="font-size: 14px;" density="compact"
                        variant="text"><v-icon>mdi-filter-variant</v-icon>내 글
                        보기</v-btn>

                    <span style="font-weight: 400; font-size: 14px;">키워드 검색<v-icon>mdi-magnify</v-icon></span>
                    <v-btn v-for="keyword in keywords" :key="keyword" class="ml-2" density="compact"
                        :class="{ 'active-button': selectedKeyword === keyword }"
                        :color="selectedKeyword === keyword ? ' #658EA7' : ''" @click="selectKeyword(keyword)">
                        {{ keyword }}
                    </v-btn>
                </div>
            </card-head>
            <hr style="color: #767676;" class="mt-3">
            <card-content v-for="article in displayedArticles">
                <h5 class="hashtag"> {{ article.keyword }}</h5>

                <h4 @click="getDetail(article.id)" class="clickable-title ml-3">{{ article?.title }}</h4>
                <h5 style="color: #767676;" class="ml-3"> {{ article?.content }}</h5>
                <!-- <h5> {{  article.id }}님</h5> -->
                <!-- <h5> 댓글 {{ article.commentCount }}개</h5> -->
                 <hr class="mt-5 mb-5">
            </card-content>
        </v-card>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useRouter } from 'vue-router';
import { computed } from 'vue';
import { UseCommunityStore } from '@/stores/community';
import { ref } from 'vue'

const store = UseCommunityStore()
const router = useRouter()

const writeArticle = () => {
    // 초기화
    store.inputTitle = ''
    store.inputContent = ''
    store.selectedButton = ''
    router.push({ name: 'communitywrite' })

}

const getDetail = (id) => {
    console.log(id)
    router.push({ name: 'communitydetail', params: { id: id } })

}

// 목록 필터링
const keywords = ['예금', '적금', '지원금']
const selectedKeyword = ref('')

// 키워드 선택 함수
const selectKeyword = (keyword) => {
    selectedKeyword.value = selectedKeyword.value === keyword ? null : keyword;
};

// 필터링된 게시글 목록
const displayedArticles = computed(() => {
    if (selectedKeyword.value) {
        return store.ArticleList.filter(article => article.keyword === selectedKeyword.value);
    } else {
        return store.ArticleList;
    }
});
</script>

<style scoped>
.keyword-div {
    justify-content: end;
}

.total-div {
    display: flex;
    align-items: center;
    flex-direction: column;

}

h1 {
    margin-left: 50px;
    margin-bottom: 20px
}

.hashtag {
    margin-top: 5px;
    margin-left: 5px;
    margin-right: 10px;
    border: 2px solid #658EA7;
    background-color: #658EA7;
    border-radius: 20px;
    padding: 5px;
    color: white;
    width: 70px;
    height: 32px;
    text-align: center;
}

.active-button {
    background-color: #658EA7;
    color: white;
}

.clickable-title {
  cursor: pointer;
  transition: color 0.3s ease;
}

</style>