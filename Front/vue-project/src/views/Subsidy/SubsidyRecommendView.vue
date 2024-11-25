<template>
    <RouterView />
    <ProductShortcut />
    <div v-if="storeSubsidy.recoSubsidies" class="container">
        <ProductRecoHeader />
        <SubsidyRecommendContent :reco-subsidies="storeSubsidy.recoSubsidies"/>
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductRecoHeader from '@/components/Common/ProductRecoHeader.vue';
import SubsidyRecommendContent from '@/components/Common/SubsidyRecommendContent.vue';
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { UseSubsidyStore } from '@/stores/subsidy';
import { onBeforeMount, onMounted } from 'vue';

const storeAccount = useAccountStore()
const router = useRouter()

const storeSubsidy = UseSubsidyStore()

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
    router.push('/login');
  }
});

onMounted(async () => {
  try {
    await storeSubsidy.getRecoSubsidies()
    console.log('storeSubsidy.recoSubsidies', storeSubsidy.recoSubsidies)
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