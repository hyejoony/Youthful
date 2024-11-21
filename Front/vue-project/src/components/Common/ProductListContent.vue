<template>
    <!-- 상품 전체 목록 페이지 본문 -->
    <v-card class="mt-4" width="900" height="1200px" elevation="2">
        <card-head class="filterbtn-flex">
            <div class="mt-3 pr-2 " style="display: flex;">
                <v-btn style="font-size: 14px;" density="compact"
                    variant="text"><v-icon>mdi-filter-variant</v-icon>최신순</v-btn>
            </div>
            <div class="mt-3 pr-2" style="display: flex;">
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

</script>

<style scoped>
.filterbtn-flex {
    display: flex;
    justify-content: end;
}
</style>