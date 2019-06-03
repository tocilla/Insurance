import Vue from 'vue'
import Vuex from 'vuex'
import risk_types from './modules/risk_types'
import risks from './modules/risks'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		risk_types,
		risks,
		auth
	}
})