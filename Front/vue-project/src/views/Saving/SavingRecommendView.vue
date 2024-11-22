<template>
    <ProductShortcut />
    <div class="container">
        <ProductRecoHeader />
        <SubsidyListContent />
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import SubsidyListContent from '@/components/Common/SubsidyListContent.vue';
import { ref } from 'vue'

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>