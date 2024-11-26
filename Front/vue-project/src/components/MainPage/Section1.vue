<template>
    <h2 class="mt-6 mb-2">‘우대 금리, 기준 중위소득..’ 금융용어가 어렵게 느껴졌다면?</h2>
    <div style="width: 800px;" class="elevation-3">
        <v-carousel height="400" progress="grey" hide-delimiters>
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
                <v-sheet height="100%">
                    <div class="d-flex fill-height justify-center align-center">
                        <div v-if="i === 0" style="display: flex;">
                            <img class="img1" style="width: 100px;" src="@/assets/images/chatbot.png" alt="chatbot_png">
                            <div class="ml-8">
                                <h3 style="color: #658EA7;">생성형 AI 챗봇 '유스'에게 무엇이든
                                    물어보세요!</h3>
                                <hr width="350px"><br>
                                <div style="color: #767676;">
                                    <h4>어려운 내용이 많은 예적금 상품과 정부지원금,</h4>
                                    <h4 class="mt-1">'유스'와 함께라면 자산관리를 쉽게 시작하고 이어갈 수 있어요.</h4>
                                </div>
                            </div>
                        </div>

                        <div v-if="i === 1">
                            <h3> 간단한 용어 문의부터,</h3>
                            <img style="width: 100%;" src="@/assets/images/chatbot_example4.png" alt="chatbot_png">
                        </div>
                        <div v-if="i === 2">
                            <h3>예적금 상품과 정부지원금에 대한 자세한 설명까지 들을 수 있죠. </h3>
                            <img style="width: 100%;" src="@/assets/images/chatbot_example3.png" alt="chatbot_png">
                        </div>
                        
                    </div>
                </v-sheet>
            </v-carousel-item>
        </v-carousel>
    </div>
</template>

<script setup>
const slides = ["First", "Second", 'Third'];

</script>

<style scoped>
.img1 {
    transform: scaleX(-1);
}
</style>