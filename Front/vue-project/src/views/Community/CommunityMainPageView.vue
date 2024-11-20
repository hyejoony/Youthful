<template>
    <div class="total-div">
        <v-card width="900" height="80" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">로그인 후 이용 가능해요.</h3>
            <v-btn @click="writeArticle" width="100" height="30" class="mt-2 ml-4" rounded="xl">글쓰기<v-icon>mdi-pencil</v-icon>
                <RouterLink />
            </v-btn>
        </v-card>

        <v-card class="mt-4 " width="900" height="110" elevation="2">
            <h3 class="mt-2 pl-4" style="color: #658EA7;">인기 게시글</h3>
            <div class="ml-4">
                <h5 style="display: inline;">키워드 |</h5>
                <h5 style="font-weight: 400; display: inline;"> 제목</h5>
            </div>
        </v-card>
        <v-card class="mt-4" width="900" height="700" elevation="2">
            <card-head>
                <div class="mt-3 pr-2 keyword-div" style="display: flex;">
                    <v-btn style="font-size: 14px;" density="compact"
                        variant="text"><v-icon>mdi-filter-variant</v-icon>내 글
                        보기</v-btn>

                    <span style="font-weight: 400; font-size: 14px;">키워드 검색<v-icon>mdi-magnify</v-icon></span>
                    <v-btn class="ml-1" density="compact">적금</v-btn>
                    <v-btn class="ml-2" density="compact">예금</v-btn>
                    <v-btn class="ml-2" density="compact">지원금</v-btn>
                </div>
            </card-head>
            <hr style="color: #767676;" class="mt-3">
            <card-content>

            </card-content>
        </v-card>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useRouter } from 'vue-router';
const router = useRouter()

const writeArticle = () => {
    router.push({name: 'communitywrite'})
}
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
</style>