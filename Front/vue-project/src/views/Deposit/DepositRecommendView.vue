<template>
    <ProductShortcut />
    <ProductRecoHeader />
    <div class="container">

        <ProductListContent />
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
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