<template>
    <v-container>
        <v-row>
            <v-col sm='12' lg="12">
                <RouterView />
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped></style>