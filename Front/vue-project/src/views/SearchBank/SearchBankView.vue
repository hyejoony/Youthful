<template>
    <h1 class="mt-4" style="color:#658EA7;">내 집 주변 은행 찾기</h1>
    <div class="flex">
        <v-form>
            <div class="select-container" style="width: 1000px;">
                <v-select label="광역시/도" :items="location1" variant="solo"></v-select>
                <v-select label="시/군/구" :items="location2" variant="solo"></v-select>
                <v-select label="은행명" :items="bankname" variant="solo"></v-select>
                <v-btn style="height: 56px; color: #658EA7;  font-size: 18px;"
                    rounded="small"><v-icon>mdi-map</v-icon>찾기</v-btn>
            </div>
        </v-form>

        <v-card height="600px" width="1000px" hover>
            <KakaoMap />
        </v-card>
    </div>
</template>

<script setup>
const location1 = ['서울특별시', '부산광역시', '대구광역시']; // 예시 데이터
const location2 = ['강남구', '해운대구', '중구']; // 예시 데이터
const bankname = ['국민은행', '신한은행', '우리은행']; // 예시 데이터
import KakaoMap from '@/components/Bank/KakaoMap.vue';
</script>

<style scoped>
.select-container {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-top: 30px;

}

h1 {
    margin-left: 50px;
    margin-bottom: 20px
}

.flex {
    display: flex;
    flex-direction: column;
    margin: auto;
    align-items: center;

}
</style>