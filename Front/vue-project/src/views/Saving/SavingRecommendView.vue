<template>
    <ProductShortcut />
    <div class="container">
        <ProductRecoHeader />
        <SavingListContent />
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import SavingListContent from '@/components/Common/SavingListContent.vue';
import { ref } from 'vue'

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>