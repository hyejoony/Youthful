<template>
    <h2 class="mt-6 mb-2">‘우대 금리, 기준 중위소득..’ 금융용어가 어렵게 느껴졌다면?</h2>
    <div style="width: 800px;" class="elevation-3">
        <v-carousel height="400" progress="grey" hide-delimiters>
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
                <v-sheet height="100%">
                    <div class="d-flex fill-height justify-center align-center">
                        <div class="text-h2">
                            {{ slide }} Slide
                            <img style="width: 150px;" src="@/assets/images/chatbot.png" alt="chatbot_png">
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

<style scoped></style>