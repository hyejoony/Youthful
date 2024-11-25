<template>
  <RouterView />
  <ProductShortcut />
  <div v-if="storeSaving.savings" class="container">
      <SavingListHeader @bank-selected="filterByBank" />
      <SavingListContent :savings="filteredSavings" />
  </div>
</template>

<script setup>
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import SavingListHeader from '@/components/Common/SavingListHeader.vue';
import SavingListContent from '@/components/Common/SavingListContent.vue';
import { ref, onMounted } from 'vue';
import { UseSavingStore } from '@/stores/saving';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';
import { onBeforeMount } from 'vue';

const storeAccount = useAccountStore();
const router = useRouter();
const storeSaving = UseSavingStore();

const selectedBank = ref(null); // 선택된 은행
const filteredSavings = ref([]); // 필터링된 상품 목록

onBeforeMount(() => {
  if (!storeAccount.isLogin) {
      router.push('/login');
  }
});

onMounted(() => {
  storeSaving.getSavings();
  filteredSavings.value = storeSaving.savings; // 초기값으로 모든 savings 설정
});

// 은행 선택 시 호출되는 함수
const filterByBank = (bankName) => {
  if (selectedBank.value === bankName) {
      // 이미 선택된 은행이면 초기화
      selectedBank.value = null;
      filteredSavings.value = storeSaving.savings; // 모든 상품 표시
  } else {
      // 새로운 은행 선택
      selectedBank.value = bankName;
      filteredSavings.value = storeSaving.savings.filter(saving => saving.kor_co_nm === bankName);
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>