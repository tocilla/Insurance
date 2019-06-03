import riskTypeService from '@/services/riskTypeService'

const state = {
	risk_types: [],
	errors: null
}

const actions = {
	async getRiskTypes({commit}) {
		var risk_types = await riskTypeService.getRiskTypes()
		commit("SET_RISK_TYPES", risk_types.results)
	},
	async createRiskType({commit}, risk_type) {
		try {
			commit("ADD_RISK_TYPE", await riskTypeService.createRiskType(risk_type));
		} catch (errors) {
			commit("RISK_TYPE_FAILED", errors);
		}

	},
	// async deleteRiskType({commit},riskTypeId) {
	//   commit("DELETE_RISK_TYPE",await riskTypeService.deleteRiskType(riskTypeId));
	// }
}

const mutations = {
	SET_RISK_TYPES(state, value) {
		state.risk_types = value;
		state.errors = null;
	},
	ADD_RISK_TYPE(state, risk_type) {
		state.risk_types.push(risk_type)
		state.errors = null;
	},
	RISK_TYPE_FAILED(state, errors) {
		state.errors = errors;
	}
	// DELETE_RISK_TYPE(state, riskTypeId) {
	//   state.risk_types = state.risk_types.filter(obj => obj.id !== riskTypeId)
	// }
}

const getters = {
	risk_types: state => {
		return state.risk_types
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
}