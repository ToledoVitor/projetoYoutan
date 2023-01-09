import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store';

import HomeView from '../views/HomeView.vue'
import CreateLeilaoView from '../views/CreateLeilaoView.vue'
import ListLeilaoView from '../views/ListLeilaoView.vue'
import LeilaoDetailsView from '../views/LeilaoDetailsView.vue'
import ProfileView from '../views/ProfileView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/leiloes/ver',
    name: 'ver-leiloes',
    component: ListLeilaoView
  },
  {
    path: '/leiloes/criar',
    name: 'criar-leiloes',
    component: CreateLeilaoView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/leiloes/:leilao_id',
    name: 'leilao',
    component: LeilaoDetailsView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
