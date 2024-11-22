<template>
  <v-container>
    <v-row>
      <v-col sm='12' lg="12">
        <h1 style="color:#658EA7;">
          {{ headerText }}
        </h1>

        <RouterView />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();

const headerText = computed(() => {
  return route.path.includes('review') ? '정부지원금 이용자 리뷰' : '정부지원금 비교';
});
</script>

<style scoped>
h1 {
  text-align: center;
}
</style>