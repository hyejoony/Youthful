import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/Account/SignUpView.vue'
import AccountLayOutView from '@/views/Account/AccountLayOutView.vue'
import LoginView from '@/views/Account/LoginView.vue'
import ProfileView from '@/views/Account/ProfileView.vue'
import ExchangeView from '@/views/Exchange/ExchangeView.vue'
import SearchBankView from '@/views/SearchBank/SearchBankView.vue'

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
      children : [
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
  ],
})

export default router
