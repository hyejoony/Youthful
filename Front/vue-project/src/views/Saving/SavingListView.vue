<template>

    <ProductShortcut />
    <div class="container">
        <ProductListHeader />
        <ProductListContent />
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductListHeader from '@/components/Common/ProductListHeader.vue';
import ProductListContent from '@/components/Common/ProductListContent.vue';
import { ref } from 'vue'



</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>