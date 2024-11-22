<template>
    <div class="total-div">
        <v-card v-if="storeAccount.isLogin" width="900" height="80" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">내가 알고있는 정보를 공유하거나, 모르는 점을 질문해보세요.</h3>
            <v-btn @click="writeArticle" width="100" height="30" class="mt-2 ml-4"
                rounded="xl">글쓰기<v-icon>mdi-pencil</v-icon>
                <RouterLink />
            </v-btn>
        </v-card>
        <v-card v-else width="900" height="80" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">로그인 후 이용 가능해요.</h3>
            <v-btn @click="login" width="100" height="30" class="mt-2 ml-4"
                rounded="xl">로그인<v-icon>mdi-pencil</v-icon>
                <RouterLink />
            </v-btn>
        </v-card>

        <v-card class="mt-4 " width="900" height="110" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">인기 게시글</h3>
            <div class="ml-4">
                <h5 style="display: inline;">{{ storeCoummunity.keyword }} |</h5>
                <h5 style="font-weight: 400; display: inline;"> {{ storeCoummunity.title }}</h5>
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
            <card-content class="card" v-for="article in displayedArticles">
                <div class="card2">
                    <div class="left-content">
                        <h5 class="hashtag">{{ article.keyword }}</h5>
                        <h4 @click="getDetail(article.id)" class="clickable-title ml-3">{{ article.title }}</h4>
                    </div>
                    <div class="right-content">
                        <h5 style="color: #767676;" class="ml-3">{{ article.user_display_name }}님</h5> |
                        <p>댓글 {{ article.comments.length }}개</p> |
                        <p>{{ article.updated_at.slice(0, 10) }}</p>
                    </div>
                </div>
                <div>
                    <hr class="mt-5 mb-5">
                </div>
            </card-content>
        </v-card>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useRouter } from 'vue-router';
import { computed, onMounted } from 'vue';
import { UseCommunityStore } from '@/stores/community';
import { useAccountStore } from '@/stores/account';
import { ref } from 'vue'
import axios from 'axios';

const storeCoummunity = UseCommunityStore()
const storeAccount = useAccountStore()
const router = useRouter()

const API_URL = storeAccount.API_URL
const token = storeAccount.token

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/communities/`,
        headers: {
            Authorization: `Token ${token}`
        },
    })
    .then(res => {
        console.log(res.data)
        storeCoummunity.ArticleList = res.data
    })
    .catch(err => {
        console.log(err.response.data)
    })
})

const writeArticle = () => {
    router.push({ name: 'communitywrite' })
}

const getDetail = (id) => {
    console.log('id', id)
    router.push({ name: 'communitydetail', params: { id: id } })
}

// 목록 필터링
const keywords = ['예금', '적금', '지원금', '기타']
const selectedKeyword = ref('')

// 키워드 선택 함수
const selectKeyword = (keyword) => {
    selectedKeyword.value = selectedKeyword.value === keyword ? null : keyword;
};

// 필터링된 게시글 목록
const displayedArticles = computed(() => {
    if (selectedKeyword.value) {
        return storeCoummunity.ArticleList.filter(article => article.keyword === selectedKeyword.value);
    } else {
        return storeCoummunity.ArticleList;
    }
});

const login = () => {
    router.push({ name: 'login' })
}
</script>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
}

.card2 {
  display: flex;
  justify-content: space-between;
  /* align-items: flex-start; */
}

.left-content, .right-content {
  display: flex;
}

.left-content {
  align-items: flex-start;
}

.right-content {
  align-items: flex-end;
}

.ml-3 {
    margin-top: 5%;
}



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