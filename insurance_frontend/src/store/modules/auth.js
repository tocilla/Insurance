import authService from '@/services/authService';
import api from '@/services/api';

const state = {
	authenticating: false,
	errors: null,
	token: null,
};

const getters = {
	isAuthenticated: state => !!state.token,
};

const actions = {
	async login({commit},{username,password}){
		commit("LOGIN_BEGIN");
		try
		{
			var result = await authService.login(username, password);
			commit("SET_TOKEN", result.key);
			commit("LOGIN_SUCCESS");
		}
		catch (errors)
		{
				commit("LOGIN_FAILURE", errors);
		}
	},
	async logout({commit}){
		await authService.logout();
		commit("LOGOUT");
		commit("REMOVE_TOKEN")
	},
	initialize({commit}){
		const token = localStorage.getItem('token');

		if (token)
		{
			commit("SET_TOKEN", token);
		}
		else
		{
			commit("REMOVE_TOKEN");
		}
	},
};

const mutations = {
	LOGIN_BEGIN(state){
		state.authenticating = true;
		state.errors = null;
	},
	LOGIN_FAILURE(state, errors){
		state.authenticating = false;
		state.errors = errors;
	},
	LOGIN_SUCCESS(state){
		state.authenticating = false;
		state.errors = null;
	},
	LOGOUT(state){
		state.authenticating = false;
		state.errors = null;
	},
	SET_TOKEN(state, token){
		localStorage.setItem('token', token);
		api.setAuthorizationToken(token);
		state.token = token;
	},
	REMOVE_TOKEN(state){
		localStorage.removeItem('token');
		api.removeAuthorizationToken();
		state.token = null;
	},
};

export default
{
	namespaced: true,
	state,
	getters,
	actions,
	mutations,
};