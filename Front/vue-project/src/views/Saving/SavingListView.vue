<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeSaving.savings" class="container">
        <ProductListHeader />
        <SavingListContent :savings="storeSaving.savings"/>
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductListHeader from '@/components/Common/ProductListHeader.vue';
import SavingListContent from '@/components/Common/SavingListContent.vue';
import { ref, onMounted } from 'vue'
import { UseSavingStore } from '@/stores/saving'

import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';
import { onBeforeMount } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});


const storeSaving = UseSavingStore()
onMounted(() => {
    storeSaving.getSavings()
    console.log('storeSaving.savings',storeSaving.savings)
})


</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>