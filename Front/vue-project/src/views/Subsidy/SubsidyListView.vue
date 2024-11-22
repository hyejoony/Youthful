<template>
    <ProductShortcut />
    <div class="container">
        <SubsidyListContent />
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import SubsidyListContent from '@/components/Common/SubsidyListContent.vue';
import { UseSubsidyStore } from '@/stores/subsidy';
import { ref, onMounted } from 'vue'

const storeSubsidy = UseSubsidyStore()
onMounted(() => {
    storeSubsidy.getSubsidies()
    
})


</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>