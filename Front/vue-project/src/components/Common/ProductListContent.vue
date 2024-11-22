<template>
    <!-- 상품(예적금, 정부지원금) 전체 목록 페이지 본문 -->
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