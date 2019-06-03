
import api from './api';

export default {
	login(username, password) {
		return api.execute('post', '/auth/login/', {
			username,
			password
		});
	},
	logout() {
		return api.execute('post', '/auth/logout/', {});
	},
	createAccount(username, password1, password2, email) {
		return api.execute('post', '/registration/', {
			username,
			password1,
			password2,
			email
		});
	},
	changeAccountPassword(password1, password2) {
		return api.execute('post', '/auth/password/change/', {
			password1,
			password2
		});
	},
	sendAccountPasswordResetEmail(email) {
		return api.execute('post', '/auth/password/reset/', {
			email
		});
	},
	resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
		return api.execute('post', '/auth/password/reset/confirm/', {
			uid,
			token,
			new_password1,
			new_password2
		});
	},
	getAccountDetails() {
		return api.execute('get', '/auth/user/');
	},
	updateAccountDetails(data) {
		return api.execute('patch', '/auth/user/', data);
	},
	verifyAccountEmail(key) {
		return api.execute('post', '/registration/verify-email/', {
			key
		});
	},
};