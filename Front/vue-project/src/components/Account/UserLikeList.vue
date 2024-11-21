<template>
    <v-container>
        <v-row>
            <v-col cols="12" style='margin-top: 8%;'>
                <h4 class="mb-2">찜 목록</h4>
                <h4 style="color: #767676;" class="mb-2">예적금</h4>
                <UserLikeProduct :user="user"/>
            </v-col>
            <v-col cols="12 mt-5">
                <h4 style="color: #767676;" class="mb-2">정부지원금</h4>
                <UserLikeSubsidy :user="user"/>
            </v-col>

        </v-row>
    </v-container>
</template>

<script setup>
import UserLikeProduct from '@/components/Account/UserLikeProduct.vue';
import UserLikeSubsidy from '@/components/Account/UserLikeSubsidy.vue';
defineProps({
    user: Object
})
</script>

<style scoped></style>