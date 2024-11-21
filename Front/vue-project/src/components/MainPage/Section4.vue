<template>
    <br>
    <div class="mt-6">
        <h2 style="display: inline;" class="mt-6 mb-2">내 집 주변 은행도 클릭만으로 찾을 수 있어요.</h2>
    </div><br>

    <v-card width="800" elevation="2">
        <KakaoMap />

        <v-card-text>
            <h3>전국 어디든 원하는 지역의 주변 은행 정보를 알 수 있어요.</h3>
        </v-card-text>

        <v-card-actions>
            <v-btn @click="gotoMap" class="txt-custom" rounded="xl" text="찾아보기"></v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import KakaoMap from '../Bank/KakaoMap.vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const gotoMap = () => {
    router.push({ name: 'searchbank'})
}
</script>


<style scoped>
.txt-custom {
    color: #658EA7;

}

h3 {
    font-weight: 400;
}
</style>