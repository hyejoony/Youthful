<template>
    <div class='top-div-flex'>
        <v-card class="product-card mt-3 ml-2 pb-3" width="800">
            <div class="card-flex mt-3 ml-7 pt-1">
                <h3> props </h3>
                <span class="bank-name ml-10 mt-1"> props </span>
                <span class="ml-10 mt-1" style="font-size: 14px;">
                    <v-icon size="small" style="color: #658EA7;">mdi-heart</v-icon> 찜 props 개
                </span>
            </div>
        </v-card>
        <v-card class="mt-3 ml-2" width="90">
            <div class="pl-4 pt-4">
                <v-icon size="large" style="color: #658EA7;">mdi-heart</v-icon>
            </div>
        </v-card>
    </div>
</template>

<script setup>

</script>

<style scoped>
.top-div-flex {
    display: flex;
}

.card-flex {
    display: flex;
}


</style>