<template>
    <div class="total-div">
        <v-card v-if="storeAccount.isLogin" width="900" height="90" elevation="2">
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

        <v-card class="mt-4 " width="900" height="120" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">인기 게시글</h3>
            <div class="ml-4" v-for="popArticle in storeCoummunity.popArticleList" :key="popArticle.id">
                <h5 style="display: inline;">{{ popArticle.keyword }} |</h5>
                <h5 @click="getDetail(popArticle.id)" class="clickable-title" style="font-weight: 400; display: inline;"> {{ popArticle.title }}</h5>
            </div>
        </v-card>
        <v-card class="mt-4 mb-5" width="900" max-height="900px" elevation="2">
            <card-head>
                <div class="mt-3 pr-2 keyword-div" style="display: flex;">
                    <v-btn style="font-size: 14px;" density="compact"
                        variant="text" @click="toggle"><v-icon>mdi-filter-variant</v-icon>내 글
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
            <template v-if="myLook">
                <card-content class="card" v-for="article in myPaginatedArticles">
                    <div class="card2" v-if="article">
                        <div class="left-content">
                            <h5 class="hashtag">{{ article.keyword }}</h5>
                            <h4 @click="getDetail(article.id)" class="clickable-title ml-3">{{ article.title }}</h4>
                        </div>
                        <div class="right-content">
                            <h5 @click="goProfile(article.user)" style="color: #767676;" class="ml-3 clickable-item">{{ article.user_display_name }}님</h5> |
                            <p>댓글 {{ article.comments.length }}개</p> |
                            <p>{{ article.updated_at?.slice(0, 10) }}</p>
                        </div>
                    </div>
                    <div>
                        <hr class="mt-5 mb-5">
                    </div>
                </card-content>
                <v-pagination
                    v-model="currentPage"
                    :length="Math.ceil(myDisplayedArticles.length / itemsPerPage)"
                    @input="myHandlePageChange"
                ></v-pagination>
            </template>
            <template v-else>
                <!-- <card-content class="card" v-for="article in displayedArticles"> -->
                <card-content class="card" v-for="article in paginatedArticles">
                    <div class="card2" v-if="article">
                        <div class="left-content">
                            <h5 class="hashtag">{{ article.keyword }}</h5>
                            <h4 @click="getDetail(article.id)" class="clickable-title ml-3">{{ article.title }}</h4>
                        </div>
                        <div class="right-content">
                            <v-avatar @click="goProfile(article.user)" class="clickable-item" size="small">
                                <v-img :src="`${baseUrl}${article.profile_image}`" alt="Article Profile"></v-img>
                            </v-avatar>                            
                            <h5 style="color: #767676;" class="ml-3">{{ article.user_display_name }}님 | </h5>
                            <p>댓글 {{ article.comments.length }}개 | </p>
                            <p>{{ article.updated_at?.slice(0, 10) }}</p>
                        </div>
                    </div>
                    <div>
                        <hr class="mt-5 mb-5">
                    </div>
                </card-content>
                <v-pagination
                    v-model="currentPage"
                    :length="Math.ceil(displayedArticles.length / itemsPerPage)"
                    @input="handlePageChange"
                ></v-pagination>
            </template>
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
const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

onMounted(() => {
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/communities/`,
        headers: {
            Authorization: `Token ${token}`
        },
    })
    .then(res => {
        return storeCoummunity.ArticleList = res.data
    })
    .then(articles => {
        console.log(articles)
        // 댓글 수를 기준으로 내림차순 정렬
        const sortedArticles = articles.sort((a, b) => b.comments.length - a.comments.length);
        // 상위 3개 항목 선택
        const topThreeArticles = sortedArticles.slice(0, 3);
        // storeCoummunity.popArticleList에 저장
        storeCoummunity.popArticleList = topThreeArticles;

        console.log(articles[0].user)
        console.log(storeAccount.userId)

        // user 값이 storeCoummunity.userId와 일치하는 항목만 필터링
        const myArticles = articles.filter(article => article.user == storeAccount.userId);
        // 필터링된 결과를 storeCoummunity.myArticleList에 저장
        console.log(myArticles)
        storeCoummunity.myArticleList = myArticles;
    })
    .catch(err => {
        console.log(err)
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

const myLook = ref(false)
const toggle = () => {
    myLook.value = !myLook.value
}
const myDisplayedArticles = computed(() => {
    if (myLook) {
        return storeCoummunity.myArticleList
    } else {
        return storeCoummunity.ArticleList
    }
})

const login = () => {
    router.push({ name: 'login' })
}

const currentPage = ref(1)
const itemsPerPage = ref(10)

const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return displayedArticles.value.slice(start, end)
})

const handlePageChange = (page) => {
  currentPage.value = page
}

const myCurrentPage = ref(1)
const myItemsPerPage = ref(10)

const myPaginatedArticles = computed(() => {
  const start = (myCurrentPage.value - 1) * myItemsPerPage.value
  const end = start + myItemsPerPage.value
  return myDisplayedArticles.value.slice(start, end)
})

const myHandlePageChange = (page) => {
  myCurrentPage.value = page
}

const goProfile = (id) => {
    router.push({name: 'profile', params: { id: id }})
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

.clickable-item {
  cursor: pointer;
}

.clickable-item:hover {
  text-decoration: underline;
  color: #658EA7;
}

</style>