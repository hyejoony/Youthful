<template>
    <ProductShortcut />
    <div class="container">
        <SubsidyListContent />
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import SubsidyListContent from '@/components/Common/SubsidyListContent.vue';
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