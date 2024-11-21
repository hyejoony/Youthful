<template>
    <h5 style="color: #767676;">지난 1개월 추이</h5>
    <div class="card-container">
        <v-card class="mx-auto" width="820">
            <v-virtual-scroll :items="cards" height="600">

                    <div class="div-card">
                        <v-card class="v-card" width="350" height="300" hover>
                        </v-card>
                        <v-card class="v-card" width="350" height="300" hover>
                        </v-card>
                    </div>
            </v-virtual-scroll>
        </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const cards = ref([1, 2])  // 3개의 스크롤 아이템 생성
</script>

<style scoped>
.v-card {
    margin-top: 10px;

}

.div-card {
    display: flex;
    justify-content: center;
    gap: 20px;


}

.card-container {
    display: flex;
    justify-content: center;
}

h5 {
    margin-left: 64.5%;
    font-weight: 400;
}
</style>