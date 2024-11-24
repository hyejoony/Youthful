<template>
    <v-card class="py-1 no-cursor-change" max-width="400" height="200" hover>
        <v-card-text>
        <template v-if="user">
            <p v-for="product in user.like_savings" :key="product.id" @click="savingDetail(product.id)" class="clickable-item">
                <v-icon style="color: #658EA7;">mdi-heart</v-icon> {{ product.fin_prdt_nm }}
            </p>
            <p v-for="product in user.like_deposits" :key="product.id" @click="depositDetail(product.id)" class="clickable-item">
                <v-icon style="color: #658EA7;">mdi-heart</v-icon> {{ product.fin_prdt_nm }}
            </p>
        </template>
        </v-card-text>
    </v-card>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

defineProps({
    user: Object
})

const savingDetail = (id) => {
    router.push({name: "savingdetail", params: { id: id }})
}

const depositDetail = (id) => {
    router.push({name: "depositdetail", params: { id: id }})
}
</script>

<style scoped>
v-card {
    background-color: #767676;
}

.no-cursor-change {
  cursor: default !important;
}

.clickable-item {
  cursor: pointer;
}

.clickable-item:hover {
  text-decoration: underline;
  color: #658EA7;
}
</style>