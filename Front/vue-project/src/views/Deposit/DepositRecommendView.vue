<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeDeposit.recoDeposits" class="container">
        <!-- <ProductRecoHeader /> -->
        <DepositRecommendContent :reco-deposits="storeDeposit.recoDeposits"/>
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import DepositRecommendContent from '@/components/Common/DepositRecommendContent.vue';
import { ref } from 'vue'

import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { UseDepositStore } from '@/stores/deposit';
import { onBeforeMount, onMounted } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

const storeDeposit = UseDepositStore()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

onMounted(async () => {
  try {
    await storeDeposit.getRecoDeposits()
    console.log('storeDeposit.recoDeposits', storeDeposit.recoDeposits)
  } catch (err) {
    console.error(err)
  }
})

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>