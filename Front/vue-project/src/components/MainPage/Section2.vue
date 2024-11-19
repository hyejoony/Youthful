<template>
    <br>
    <div>
        <h2 class="mt-6 mb-2">Youthful 서비스는,</h2>
        <h3 class="txt-custom" style="display: inline;">나의</h3>
        <h3 style="display: inline;"> 나이, 직업, 사는 지역에 따라</h3>
        <h3 class="txt-custom" style="display: inline;"> 정부지원금 목록을 추천</h3>
        <h3 style="display: inline;">해줘요.</h3>
    </div><br>
    <div style="width: 800px;">
        <v-card elevation="2">
            <v-card-item>
                <div>
                    <div class="text-overline mb-1">
                    </div>
                    <div class="mb-1">
                        <div style="display: flex;">
                            <h5 class="hashtag"> 20대 초반 </h5>
                            <h5 class="hashtag">대학생</h5>
                            <h5 class="hashtag">월 소득 50만원 이하</h5>
                            <h5 class="hashtag">대전광역시</h5>
                        </div>
                    </div>
                    <div class="text-caption"></div>
                </div>
            </v-card-item>
            <Section2Table />

        </v-card>
    </div>
    <v-btn height="45" class="mt-3" style="color: white; background-color: #658EA7;" rounded="xl" elevation="0">
        <span class="font-weight-bold" style="font-size: medium;">추천 받아보기</span></v-btn>

</template>

<script setup>
import Section2Table from './Section2Table.vue';
</script>

<style scoped>
.txt-custom {
    color: #658EA7;
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
</style>