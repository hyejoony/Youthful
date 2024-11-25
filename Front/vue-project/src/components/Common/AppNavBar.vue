<template>
    <v-card>
      <v-layout>
        <v-navigation-drawer
          expand-on-hover
          rail
          :rail-width="56"
          width="220"
          permanent
        >
          <v-list>
            <v-list-item v-if="storeAccount.isLogin" class="user-info">
              <template v-slot:prepend>
                <v-avatar>
                  <v-img :src="`${baseUrl}${storeAccount.userImage}`" alt="User Profile"></v-img>
                </v-avatar>
              </template>
              <v-list-item-title>{{ storeAccount.userName }}</v-list-item-title>
              <v-list-item-subtitle>{{ storeAccount.userEmail }}</v-list-item-subtitle>
            </v-list-item>
            
            <v-list-item v-else>
              <template v-slot:prepend>
                <v-avatar color="#658EA7">
                  <v-icon icon="mdi-account-question"></v-icon>
                </v-avatar>
              </template>
              <v-list-item-title>로그인이 필요합니다</v-list-item-title>
            </v-list-item>
          </v-list>
  
          <v-divider></v-divider>
  
          <v-list density="compact" nav>
            <v-list-item
              to="/"
              prepend-icon="mdi-home"
              title="홈"
              value="home"
              class="nav-item"
            ></v-list-item>
  
            <v-list-item
              v-if="storeAccount.isLogin"
              :to="{ name: 'profile', params: { id: storeAccount.userId }}"
              prepend-icon="mdi-account"
              title="프로필"
              value="profile"
              class="nav-item"
            ></v-list-item>

            <v-list-item
              v-else="!storeAccount.isLogin"
              :to="{ name: 'login'}"
              prepend-icon="mdi-account"
              title="프로필"
              value="profile"
              class="nav-item"
            ></v-list-item>
  
  
            <v-list-item
              to="/deposit"
              prepend-icon="mdi-currency-usd"
              title="예적금 조회"
              value="products"
              class="nav-item"
            ></v-list-item>
  
            <v-list-item
              to="/subsidy"
              prepend-icon="mdi-cash"
              title="정부지원금 조회"
              value="subsidy"
              class="nav-item"
            ></v-list-item>
  
            <v-list-item
              to="/searchbank"
              prepend-icon="mdi-map-marker"
              title="집 주변 은행 검색"
              value="searchbank"
              class="nav-item"
            ></v-list-item>
  
            <v-list-item
              to="/exchange"
              prepend-icon="mdi-cash-sync"
              title="환전 계산기"
              value="exchange"
              class="nav-item"
            ></v-list-item>
  
            <v-list-item
              to="/community"
              prepend-icon="mdi-account-multiple"
              title="커뮤니티"
              value="community"
              class="nav-item"
            ></v-list-item>
  
            <!-- 로그인 상태에 따른 조건부 렌더링 -->
            <div v-if="!storeAccount.isLogin">
              <v-list-item
                to="/signup"
                prepend-icon="mdi-account-plus"
                title="회원가입"
                value="signup"
                class="nav-item"
              ></v-list-item>
              
              <v-list-item
                to="/login"
                prepend-icon="mdi-login"
                title="로그인"
                value="login"
                class="nav-item"
              ></v-list-item>
            </div>
            
  
            <v-list-item
              v-else
              to="/logout"
              prepend-icon="mdi-logout"
              title="로그아웃"
              value="logout"
              @click="storeAccount.logout"
              class="nav-item"
            ></v-list-item>
          </v-list>
        </v-navigation-drawer>
  
        <v-main style="padding: auto;">
        </v-main>
      </v-layout>
    </v-card>
  </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { useAccountStore } from '@/stores/account'
  import { onMounted, ref } from 'vue';
  import axios from 'axios'

  const storeAccount = useAccountStore()
  const user = ref('')
  const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';



  </script>
  


  <style scoped>
  :deep(.nav-item .v-icon) {
    color: #A3A3A3 !important;
  }
  
  .user-info {
    color: #658EA7;
  }

  </style>