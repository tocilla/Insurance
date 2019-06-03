import axios from 'axios'
// import Cookies from 'js-cookie'
import router from '@/router'

const client = axios.create({
	baseURL: 'http://localhost:8000/', //  baseURL: config.API_URL,
	json: true,
})

export default {
	async execute(method, resource, data) {
		return client({
			method,
			url: resource,
			data,
			timeout: 5000,
			headers: {
				//Authorization: `Bearer ${accessToken}`
			},
		}).then(response => {
			return response.data
		}).catch(error => {
			if (error.response) {
				// The request was made and the server responded with a status code
				// that falls out of the range of 2x
				if (error.response.status == "400") {
					var errors = [];
					var data = error.response.data;
					for (var key in data) {
						var obj = data[key];
						for (var prop in obj) {
							if(obj.hasOwnProperty(prop)){
								if(key == "non_field_errors")
									errors.push(obj[prop]);
								else
									errors.push(key + '-' + obj[prop]);

							}
						}
					}
					//throw error.response.data;
					throw errors;
				} else if (error.response.status == "401") {
					// console.log('unauthorized, logging out ...');
					router.replace('/logout');
				} else if (error.response.status == 403) {
					throw ['Forbidden resource can\'t be accessed.'];
				} else if (error.response.status == 404) {
					throw ['The requested resource not found.'];
				} else if (error.response.status == 500) {
					throw ['Internal Server Error.'];
				} else {
					throw ['Service unavailable'];
				}

			} else if (error.request) {
				// The request was made but no response was received
				// `error.request` is an instance of XMLHttpRequest in the browser and an instance of
				// http.ClientRequest in node.js
				throw [error];
			} else {
				// Something happened in setting up the request that triggered an Error
				throw [error.message];
			}
			//console.log(error.config);
		})
	},
	setAuthorizationToken(token) {
		client.defaults.headers.Authorization = `Token ${token}`;
	},
	removeAuthorizationToken() {
		delete client.defaults.headers.Authorization;
	}
}