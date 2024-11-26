<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeSaving.recoSavings" class="container">
        <!-- <ProductRecoHeader /> -->
        <SavingRecommendContent :reco-savings="storeSaving.recoSavings"/>
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import SavingRecommendContent from '@/components/Common/SavingRecommendContent.vue';
import { ref } from 'vue'

import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { UseSavingStore } from '@/stores/saving';
import { onBeforeMount, onMounted } from 'vue';
const storeAccount = useAccountStore()
const router = useRouter()

const storeSaving = UseSavingStore()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

onMounted(async () => {
  try {
    await storeSaving.getRecoSavings()
    console.log('storeSaving.recoSavings', storeSaving.recoSavings)
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