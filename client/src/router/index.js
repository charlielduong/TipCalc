import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/form',
    name: 'form',
    component: () => import(/* webpackChunkName: "form" */ '../views/FormView.vue')
  },
  {
    path: '/history',
    name: 'history',
    component: () => import(/* webpackChunkName: "form" */ '../views/HistoryView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "form" */ '../views/LoginView.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
