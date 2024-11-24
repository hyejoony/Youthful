<template>
    <v-card class="py-1 no-cursor-change" max-width="400" height="200" hover>
        <v-card-text>
            <template v-if="user">
                <p v-for="product in user.like_subsidies" :key="product.id" @click="subsidyDetail(product.id)" class="clickable-item">
                    <v-icon style="color: #658EA7;">mdi-heart</v-icon> {{ product.name }}</p>
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

const subsidyDetail = (id) => {
    router.push({name: "subsidydetail", params: { id: id }})
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