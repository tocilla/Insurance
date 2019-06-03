import riskService from '@/services/riskService'

const state = {
	risks: [],
	errors: null
}

const actions = {
	async getRisks({commit}) {
		var risks = await riskService.getRisks()
		commit("SET_RISKS", risks.results)
	},
	async createRisk({commit}, risk) {
		try {
			commit("ADD_RISK", await riskService.createRisk(risk));
		} catch (errors) {
			commit("RISK_FAILED",errors)
		}
	},
	async deleteRisk({commit}, riskId) {
		commit("DELETE_RISK", await riskService.deleteRisk(riskId));
	}
}

const mutations = {
	SET_RISKS(state, value) {
		state.risks = value;
		state.errors = null;
	},
	ADD_RISK(state, risk) {
		state.risks.push(risk)
		state.errors = null;
	},
	EDIT_RISK(state, risk) {
		state.risks[state.risks.findIndex(x => x.id == risk.id)] = risk;
		state.erros = null;
	},
	DELETE_RISK(state, RiskId) {
		state.risks = state.risks.filter(obj => obj.id !== RiskId)
		state.errors = null;
	},
	RISK_FAILED(state,errors) {
		state.errors = errors;
	}
}

const getters = {
	risks: state => {
		return state.risks
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
}