<template>
  <RouterView />
  <ProductShortcut />
  <div v-if="storeDeposit.deposits" class="container">
      <ProductListHeader @bank-selected="filterByBank" />
      <DepositListContent :deposits="filteredDeposits" />
  </div>
</template>

<script setup>
import ProductShortcut from '@/components/Common/ProductShortcut.vue';
import ProductListHeader from '@/components/Common/SavingListHeader.vue';
import DepositListContent from '@/components/Common/DepositListContent.vue';
import { ref, onMounted } from 'vue';
import { UseDepositStore } from '@/stores/deposit';
import { useAccountStore } from '@/stores/account';
import { useRouter } from 'vue-router';
import { onBeforeMount } from 'vue';

const storeAccount = useAccountStore();
const router = useRouter();

onBeforeMount(() => {
if (!storeAccount.isLogin) {
  router.push('/login');
}
});

const storeDeposit = UseDepositStore();
const selectedBank = ref(null); // 선택된 은행
const filteredDeposits = ref([]); // 필터링된 상품 목록

onMounted(() => {
storeDeposit.getDeposits();
filteredDeposits.value = storeDeposit.deposits; // 초기값으로 모든 deposits 설정
});

// 은행 선택 시 호출되는 함수
const filterByBank = (bankName) => {
if (selectedBank.value === bankName) {
  // 이미 선택된 은행이면 초기화
  selectedBank.value = null;
  filteredDeposits.value = storeDeposit.deposits; // 모든 상품 표시
} else {
  // 새로운 은행 선택
  selectedBank.value = bankName;
  filteredDeposits.value = storeDeposit.deposits.filter(deposit => deposit.kor_co_nm === bankName);
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