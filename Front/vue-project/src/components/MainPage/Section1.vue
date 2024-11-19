<template>
    <h2 class="mt-6 mb-2">‘우대 금리, 기준 중위소득..’ 금융용어가 어렵게 느껴졌다면?</h2>
    <div style="width: 800px;" class="elevation-3">
        <v-carousel height="400" progress="grey" hide-delimiters>
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
                <v-sheet height="100%">
                    <div class="d-flex fill-height justify-center align-center">
                        <div v-if="i === 0" style="display: flex;">
                            <img style="width: 100px;" src="@/assets/images/chatbot.png" alt="chatbot_png">
                            <div class="ml-8">
                                <h2 style="color: #658EA7;">AI 챗봇 '유스'에게 무엇이든
                                    물어보세요!</h2>
                                    <hr width="380px"><br>
                                <div style="color: #767676;">
                                    <h3>어려운 내용이 많은 예적금 상품과 정부지원금,</h3>
                                    <h3 class="mt-1">'유스'와 함께라면 자산관리를 쉽게 시작하고 이어갈 수 있어요.</h3>
                                </div>
                            </div>
                        </div>

                        <div v-if="i === 1">
                            <h3>뿐만 아니라 Youthful에서 제공하는 서비스를 이용하다가,</h3>
                            <h3 class="mt-1">낯선 용어가 있다면 언제든지 물어보세요.</h3>
                        </div>
                        
                        <div v-if="i === 2">
                            대화예시창을 넣자
                        </div>
                    </div>
                </v-sheet>
            </v-carousel-item>
        </v-carousel>
    </div>
</template>

<script setup>
const slides = ["First", "Second", "Third"]; 
</script>

<style scoped>
img {
    transform: scaleX(-1);
}
</style>