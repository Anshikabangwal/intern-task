import { createRouter, createWebHistory } from 'vue-router';
import SignupForm from '../components/SignupForm.vue';
import LoginForm from '../components/LoginForm.vue';
import DashboardEntry from '../components/DashboardEntry.vue';

const routes = [
  { path: '/signup', component: SignupForm },
  { path: '/login', component: LoginForm },
  { path: '/dashboard', component: DashboardEntry },
  { path: '/', redirect: '/signup' }, // Default route to signup
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
