<template>
    <v-btn-toggle class="toggle-color" v-model="toggle_exclusive">
        <v-btn 
      :class="{ 'selected-btn': toggle_exclusive === '예금' }"
      value="예금"
    >
      예금
    </v-btn>
    <v-btn 
      :class="{ 'selected-btn': toggle_exclusive === '적금' }"
      value="적금"
    >
      적금
    </v-btn>
    </v-btn-toggle>

    <div style="margin-left: 55px; margin-top: 20px;">
        <span @click="goback" class="clickable-title">전체 |</span>
        <span class="clickable-title"> 추천</span>
    </div>

    <h3 style="margin-left: 55px; margin-top: 10px;">님을 위해 추천드리는 상품 목록이에요.</h3>
    <div style="display: flex; margin-left: 55px; margin-top:10px;">
        <h5 class="hashtag"> 20대 초반 </h5>
        <h5 class="hashtag">대학생</h5>
        <h5 class="hashtag">월 소득 50만원 이하</h5>
        <h5 class="hashtag">대전광역시</h5>
    </div>
    <v-card class="mt-4" width="900" height="600px" elevation="2">
        <card-head class="filterbtn-flex">
            <div class="mt-3 pr-2 keyword-div" style="display: flex;">
                <v-btn style="font-size: 14px;" density="compact"
                    variant="text"><v-icon>mdi-filter-variant</v-icon>최신순</v-btn>
            </div>
            <div class="mt-3 pr-2 keyword-div" style="display: flex;">
                <v-btn style="font-size: 14px;" density="compact" variant="text"><v-icon>mdi-heart</v-icon>찜 많은
                    순</v-btn>
            </div>
        </card-head>
        <hr class="mt-2">
        <card-content v-for="article in displayedArticles">
            <h5 class="hashtag"> {{ article.keyword }}</h5>

            <h4 @click="getDetail" class="clickable-title ml-3">{{ article?.title }}</h4>
            <h5 style="color: #767676;" class="ml-3"> {{ article?.content }}</h5>
            <!-- <h5> {{  article.id }}님</h5> -->
            <!-- <h5> 댓글 {{ article.commentCount }}개</h5> -->
            <hr class="mt-5 mb-5">
        </card-content>
    </v-card>

</template>

<script setup>

import { useRouter } from 'vue-router';
const router = useRouter()
const goback = () => {
    router.push({ name: 'deposit' })

}
</script>

<style scoped>
.filterbtn-flex {
    display: flex;
    justify-content: end;
}

.toggle-color {
    color: #767676;
    border: 0.5px solid #767676;
    /* 더 얇은 테두리 */
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    /* 부드러운 그림자 효과 */
    border-radius: 4px;
    /* 모서리를 더 부드럽게 */
    margin-left: 50px;
}

.clickable-title {
    cursor: pointer;
    transition: color 0.3s ease;
}

.hashtag {
    /* margin-top: 10px; */
    /* margin-left: 10px; */
    margin-right: 10px;
    border: 2px solid #658EA7;
    background-color: #658EA7;
    border-radius: 5px;
    padding: 5px;
    color: white;
}

.selected-btn {
  background-color: #658EA7 !important;
  color: white !important;
}
</style>