<template>
        <ProductShortcut />
        <div class=container>
        <ProductListHeader />
        <ProductListContent />
    </div>
</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductListHeader from '@/components/Common/ProductListHeader.vue';
import ProductListContent from '@/components/Common/ProductListContent.vue';
import { ref } from 'vue'

// const switchState1 = ref(false)
// const switchState2 = ref(false)



</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}


</style>