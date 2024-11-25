<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeSubsidy.subsidies" class="container">
        <SubsidyListContent :subsidies="storeSubsidy.subsidies"/>
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import SubsidyListContent from '@/components/Common/SubsidyListContent.vue';
import { storeToRefs } from 'pinia';
import { ref, onMounted } from 'vue'
import { UseSubsidyStore } from '@/stores/subsidy';

import { useRouter } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { onBeforeMount } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

const storeSubsidy = UseSubsidyStore()


onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

onMounted(() => {
    storeSubsidy.getSubsidies()
    console.log('storeSubsidy.subsidies',storeSubsidy.subsidies)
})



</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>