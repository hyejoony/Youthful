<template>
    <ProductShortcut />
    <div class="container">
        <ProductRecoHeader />
        <DepositListContent />
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import DepositListContent from '@/components/Common/DepositListContent.vue';
import { ref } from 'vue'

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>