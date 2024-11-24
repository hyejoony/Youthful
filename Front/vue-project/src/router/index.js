import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/Account/SignUpView.vue'
import AccountLayOutView from '@/views/Account/AccountLayOutView.vue'
import LoginView from '@/views/Account/LoginView.vue'
import LogoutView from '@/views/Account/LogoutView.vue'
import ProfileView from '@/views/Account/ProfileView.vue'
import ExchangeView from '@/views/Exchange/ExchangeView.vue'
import SearchBankView from '@/views/SearchBank/SearchBankView.vue'
import CommunityLayOutView from '@/views/Community/CommunityLayOutView.vue'
import CommunityMainPageView from '@/views/Community/CommunityMainPageView.vue'
import CommunityDetailPageView from '@/views/Community/CommunityDetailPageView.vue'
import CommunityWriteView from '@/views/Community/CommunityWriteView.vue'
import DepositLayOutView from '@/views/Deposit/DepositLayOutView.vue'
import DepositDetailView from '@/views/Deposit/DepositDetailView.vue'
import DepositListView from '@/views/Deposit/DepositListView.vue'
import DepositRecommendView from '@/views/Deposit/DepositRecommendView.vue'
import SavingDetailView from '@/views/Saving/SavingDetailView.vue'
import SavingLayOutView from '@/views/Saving/SavingLayOutView.vue'
import SavingListView from '@/views/Saving/SavingListView.vue'
import SavingRecommendView from '@/views/Saving/SavingRecommendView.vue'
import SubsidyLayOutView from '@/views/Subsidy/SubsidyLayOutView.vue'
import SubsidyDetailView from '@/views/Subsidy/SubsidyDetailView.vue'
import SubsidyListView from '@/views/Subsidy/SubsidyListView.vue'
import SubsidyRecommendView from '@/views/Subsidy/SubsidyRecommendView.vue'
import SubsidyReviewView from '@/views/Subsidy/SubsidyReviewView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/account/',
      component: AccountLayOutView,
      children: [
        {
          path: '/signup',
          name: 'signup',
          component: SignUpView
        },
        {
          path: '/login',
          name: 'login',
          component: LoginView
        },
        {
          path: '/profile/:id',
          // path: '/profile',
          name: 'profile',
          component: ProfileView
        },
        {
          path: '/logout',
          name: 'logout',
          component: LogoutView
        },
      ]
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView,
    },
    {
      path: '/searchbank',
      name: 'searchbank',
      component: SearchBankView,
    },
    {
      path: '/',
      component: CommunityLayOutView,
      children: [
        {
          path: '/community',
          name: 'community',
          component: CommunityMainPageView
        },
        {
          path: '/community/detail/:id',
          name: 'communitydetail',
          component: CommunityDetailPageView
        },
        {

          path: '/community/write',
          name: 'communitywrite',
          component: CommunityWriteView
        },
      ]
      
    },
    {
      path: '/',
      component: DepositLayOutView,
      children: [
        {
          path: '/deposit',
          name: 'deposit',
          component: DepositListView
        },
        {
          path: '/deposit/detail/:id',
          name: 'depositdetail',
          component: DepositDetailView 
        },
        {

          path: '/deposit/recommend',
          name: 'depositrecommend',
          component: DepositRecommendView
        },
      ]
      
    },
    {
      path: '/',
      component: SavingLayOutView,
      children: [
        {
          path: '/saving',
          name: 'saving',
          component: SavingListView
        },
        {
          path: '/saving/detail/:id',
          name: 'savingdetail',
          component: SavingDetailView 
        },
        {
          path: '/saving/recommend',
          name: 'savingrecommend',
          component: SavingRecommendView
        },
      ]
      
    },
    {
      path: '/',
      component: SubsidyLayOutView,
      children: [
        {
          path: '/subsidy',
          name: 'subsidy',
          component: SubsidyListView
        },
        {
          path: '/subsidy/detail/:id',
          name: 'subsidydetail',
          component: SubsidyDetailView 
        },
        {

          path: '/subsidy/recommend',
          name: 'subsidyrecommend',
          component: SubsidyRecommendView
        },
        {

          path: '/subsidy/detail/:id/review',
          name: 'subsidyreview',
          component: SubsidyReviewView
        },
      ]
      
    },
  ],

})

import { useAccountStore } from '@/stores/account'
router.beforeEach((to, from) => {
  const store = useAccountStore()
  // 만약 이동하는 목적지가 메인 페이지이면서
  // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
  if (to.name === 'profile' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  }

  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
  // 메인 페이지로 보냄
  if ((to.name === 'signup' || to.name === 'login') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'home' }
  }
})


export default router
