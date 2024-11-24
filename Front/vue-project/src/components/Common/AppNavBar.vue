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
            <!-- // nickname 없음 email 로 처리 추가 필요 -->
            <v-list-item class="user-info"
            v-if="store.isLogin == true"
              prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
              title="store.nickname || store.email.split "
              subtitle="store.email"
            ></v-list-item>
            <v-list-item v-else-if="!store.isLogin">
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
              v-if="store.isLogin"
              :to="{ name: 'profile', params: { id: store.userId }}"
              prepend-icon="mdi-account"
              title="프로필"
              value="profile"
              class="nav-item"
            ></v-list-item>

            <v-list-item
              v-else="!store.isLogin"
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
            <div v-if="!store.isLogin">
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
              @click="store.logout"
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
  
  const store = useAccountStore()
  </script>
  
  <style scoped>
  :deep(.nav-item .v-icon) {
    color: #A3A3A3 !important;
  }
  
  .user-info {
    color: #658EA7;
  }

  </style>