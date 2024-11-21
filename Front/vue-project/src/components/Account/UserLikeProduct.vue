<template>
    <v-card class="py-1" max-width="400" height="200" hover>
        <v-card-text>
            <template v-if="user">
                <p v-for="product in user.like_savings" :key="product.id"><v-icon style="color: #658EA7;">mdi-heart</v-icon> {{ product.fin_prdt_nm }}</p>
                <p v-for="product in user.like_deposits" :key="product.id"><v-icon style="color: #658EA7;">mdi-heart</v-icon> {{ product.fin_prdt_nm }}</p>
            </template>
        </v-card-text>
    </v-card>
</template>

<script setup>
defineProps({
    user: Object
})

</script>

<style scoped>
v-card {
    background-color: #767676;
}
</style>