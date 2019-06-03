import Vue from 'vue'
import Router from 'vue-router'

// Dynamic imports for Lazy loading
const Home = () => import ('@/views/Home.vue');
const About = () => import ('@/views/About.vue');

const Login = () => import ('@/views/Login');
const Lost = () => import ('@/views/Lost');
const PasswordReset = () => import ('@/views/PasswordReset');
const PasswordResetConfirm = () => import ('@/views/PasswordResetConfirm');

const RiskTypeList = () => import ('@/views/RiskTypeList.vue');
const RiskTypeCreate = () => import ('@/views/RiskTypeCreate.vue');
const RiskTypeDetail = () => import ('@/views/RiskTypeDetail.vue');
const RiskList = () => import ('@/views/RiskList.vue');
const RiskCreate = () => import ('@/views/RiskCreate.vue');
const RiskDetail = () => import ('@/views/RiskDetail.vue');
const RiskEdit = () => import ('@/views/RiskEdit.vue');

import store from '@/store'

const requireAuthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (!store.getters['auth/isAuthenticated']) {
                next('/login');
            } else {
                next();
            }
        });
};

const requireUnauthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (store.getters['auth/isAuthenticated']) {
                next('/home');
            } else {
                next();
            }
        });
};

const redirectLogout = (to, from, next) => {
    store.dispatch('auth/logout')
        .then(() => next('/login'));
};

Vue.use(Router)

export default new Router({
	routes: [{
			path: '/',
			name: 'home',
			component: Home,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/about',
			name: 'about',
			component: About,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/login',
			component: Login,
			beforeEnter: requireUnauthenticated
		},
		{
			path: '/logout',
			beforeEnter: redirectLogout
		},
		{
			path: '/risk_types',
			name: 'RiskTypeList',
			component: RiskTypeList,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risk_types/create',
			name: 'RiskTypeCreate',
			component: RiskTypeCreate,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risk_types/:riskTypeId',
			name: 'RiskTypeDetail',
			component: RiskTypeDetail,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risks',
			name: 'RiskList',
			component: RiskList,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risks/create',
			name: 'RiskCreate',
			component: RiskCreate,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risks/:riskId',
			name: 'RiskDetail',
			component: RiskDetail,
			beforeEnter: requireAuthenticated
		},
		{
			path: '/risks/edit',
			name: 'RiskEdit',
			component: RiskEdit,
			beforeEnter: requireAuthenticated
		},
		{
			path: '*',
			component: Lost,
		}
	]
})