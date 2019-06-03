import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import DateFilter from '@/filters/date'

Vue.config.productionTip = false

Vue.use(BootstrapVue)

new Vue({
	router,
	store,
	render: h => h(App)
}).$mount('#app')


Vue.filter('formatDate', DateFilter) // register filter globally

Vue.directive('visible', (el, bind) => {
	el.style.visibility = (bind.value) ? 'visible' : 'hidden';
}); 