<template>
	<div id="app">
		<navbar v-if="isAuthenticated"  class="mb-5"></navbar>
		<router-view/>
	</div>
</template>
<script>
	import { mapGetters } from 'vuex';
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap-vue/dist/bootstrap-vue.css'
	import Navbar from './components/TheNavbar';
	
	export default {
		name: 'App',
		components: {
			Navbar,
		},
		computed: mapGetters('auth', [
			'isAuthenticated',
		]),
	}
</script>
<style>
	form label.required:after{
		content: '*';
		color: red
	}
	li{
		list-style-type: none;
	}
</style>