<template>
    <div class='top-div-flex'>
        <v-card class="product-card mt-3 ml-2 pb-3" width="800">
            <div class="card-flex mt-3 ml-7 pt-1">
                <h3>{{saving.fin_prdt_nm}} | {{ saving.kor_co_nm }}</h3>
                <!-- <span class="bank-name ml-10 mt-1"> {{ saving. }} </span> -->
                <span class="ml-10 mt-1" style="font-size: 14px;"> 
                    <v-icon size="small" style="color: #658EA7;">mdi-heart</v-icon> 찜 개수 {{ saving.likes_count }}개
                </span>
            </div>
        </v-card>
        <v-card class="mt-3 ml-2" width="90">
            <div v-if="!$route.path.includes('/saving')" class="heart-top-left">
                <v-icon size="large" style="color: #658EA7;">mdi-heart</v-icon>
            </div>
            <div v-else class="heart-center">
                <v-icon size="large" style="color: #658EA7;">mdi-heart</v-icon>
            </div>
        </v-card>
    </div>
</template>

<script setup>

defineProps({
    saving: Object
})
</script>


<style scoped>
.top-div-flex {
    display: flex;
}

.card-flex {
    display: flex;
}

.heart-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
}
.heart-top-left {
    padding-left: 16px;
    padding-top: 16px;
}
</style>