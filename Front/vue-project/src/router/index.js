import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/Account/SignUpView.vue'
import AccountLayOutView from '@/views/Account/AccountLayOutView.vue'
import LoginView from '@/views/Account/LoginView.vue'
import ProfileView from '@/views/Account/ProfileView.vue'
import ExchangeView from '@/views/Exchange/ExchangeView.vue'
import SearchBankView from '@/views/SearchBank/SearchBankView.vue'
import CommunityLayOutView from '@/views/Community/CommunityLayOutView.vue'
import CommunityMainPageView from '@/views/Community/CommunityMainPageView.vue'
import CommunityDetailPageView from '@/views/Community/CommunityDetailPageView.vue'
import CommunityWriteView from '@/views/Community/CommunityWriteView.vue'
import { useAccountStore } from '@/stores/account'

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
          // path: '/profile/:id',
          path: '/profile',
          name: 'profile',
          component: ProfileView
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
      path: '/community/',
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
  ],

})


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
