<template>
    <h5 style="color: #767676;">지난 1개월 추이</h5>
    <div class="div-card">
        <v-card class="v-card" width="400" height="300" hover>

        </v-card>
        <v-card class="v-card" width="400" height="300" hover>
        </v-card>
    </div>
</template>

<script setup>

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

h5 {
    margin-left: 64.5%;
    font-weight: 400;
}
</style>