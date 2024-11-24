<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeDeposit.deposits" class="container">
        <ProductListHeader />
        <DepositListContent :deposits="storeDeposit.deposits"/>
    </div>

</template>

<script setup>

import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductListHeader from '@/components/Common/ProductListHeader.vue';
import DepositListContent from '@/components/Common/DepositListContent.vue';
import { ref, onMounted } from 'vue'
import { UseDepositStore } from '@/stores/deposit'
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


const storeDeposit = UseDepositStore()
onMounted(() => {
    storeDeposit.getDeposits()
    console.log('storeDeposit.deposits',storeDeposit.deposits)
})


</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;

}
</style>