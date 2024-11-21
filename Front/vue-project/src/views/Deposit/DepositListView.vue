<template>

    <v-btn-toggle class="toggle-color" v-model="toggle_exclusive">
        <v-btn>
            예금
        </v-btn>
        <v-btn>
            적금
        </v-btn>
    </v-btn-toggle>
    <div style="margin-left: 55px; margin-top: 20px;">
        <span class="clickable-title">전체 |</span>
        <span @click="gotoReco" class="clickable-title"> 추천</span>
        <span class="speech-bubble">
            나에게 딱 맞는 상품을 추천해드려요
        </span>
    </div>

    <!-- <div class="switch-container">
        <v-switch v-model="switchState1" :label="switchState1 ? '적금' : '예금'"></v-switch>
        <v-switch v-model="switchState2" :label="switchState2 ? '추천' : '전체'"></v-switch>
    </div> -->
    <v-card class="mt-6" width="900" height="150px">
        <div  class="card-border" >

        <div class="bank-section">
            <v-card class=" card-border" width="100" height="80px">
                <img class="mt-4 ml-8" width="35px" src="@/assets/images/kb.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>국민은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/ibk_logo.png" alt="bank_logo">
                <p class="txt-custom px-5"><b>기업은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/shc_logo.png" alt="bank_logo">
                <p class="txt-custom px-5"><b>신한은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8" width="30px" src="@/assets/images/woori.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>우리은행</b></p>
            </v-card>
            <v-card class="card-border" width="100" height="80px">
                <img class="mt-3 ml-8 " width="32px" src="@/assets/images/hana.PNG" alt="bank_logo">
                <p class="txt-custom px-5"><b>하나은행</b></p>
            </v-card>
        </div>
    </div>
    </v-card>

    <v-card class="mt-4" width="900" height="1200px" elevation="2">
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
import { ref,watch } from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter()

// const switchState1 = ref(false)
// const switchState2 = ref(false)

const selectBank = ref('') // 은행 필터

const gotoReco = () => {
    router.push({ name: 'depositrecommend'})
}
</script>

<style scoped>
.txt-custom {
    /* color: #658EA7; */
    color: #AEACAC;
}

.card-border {
    gap: 20px; /* 카드 사이의 간격 */
    margin: auto;
    margin-top: 15px;

}


.bank-section {
    display: flex;
    gap: 20px
       
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

/* 
.switch-container {
    display: flex;
    gap: 20px;
    align-items: center;
} */

.filterbtn-flex {
    display: flex;
    justify-content: end;
}

.speech-bubble {
    position: relative;
    background: #658EA7;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 1px 3px #658EA7;
    /* 추가 스타일링 */
    font-size: 14px;
    color: white;
    width: 220px;
    margin: 20px;
}

.speech-bubble::after {
    content: "";
    position: absolute;
    position: absolute;
    top: 50%;
    /* 중앙에 위치하도록 변경 */
    left: -9px;
    /* 왼쪽으로 살짝 이동 */
    transform: translateY(-50%);
    /* 세로 중앙 정렬 */
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #658EA7 transparent;
}

.clickable-title {
  cursor: pointer;
  transition: color 0.3s ease;
}

</style>