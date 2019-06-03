<template>
	<b-container class="risk-type">
		<b-row>
			<b-col>
				<h2>{{title}}</h2>
			</b-col>
			<b-col>
				<router-link tag="button" style="float: right" class="btn  btn-primary" to="/risk_types/create">New Risk Type</router-link>
			</b-col>
		</b-row>
		<p v-show="loading">Loading...</p>
		<br><br>
		<table class="table table-condensed">
			<thead>
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Description</th>
					<th>Created At</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="risk_type in risk_types" :key="risk_type.id">
					<td>{{risk_type.id}}</td>
					<td>{{risk_type.name}}</td>
					<td>{{risk_type.description}}</td>
					<td>{{risk_type.created_at | formatDate}}</td>
				</tr>
			</tbody>
		</table>
	</b-container>
</template>
<script>
	// import api from '@/api'
	// export default{
	//     name:'RiskTypeList',
	//     data (){
	//         return{
	//             title:'Risk Types',
	//             loading: false,
	//             risk_types: {},
	//             model: {}
	//         }
	//     },
	//     async created () {
	//         this.refreshRiskTypes()
	//     },
	//     methods: {
	//         async refreshRiskTypes () {
	//             this.loading = true
	//             this.risk_types = await api.getRiskTypes()
	//             this.loading = false
	//         }
	//     }
	// }


	import { mapState, mapActions } from 'vuex'
	export default {
		name: "RiskTypeList",
		data() {
			return {
				title:'Risk Types',
				loading: false,
				//risk_types: [],
			};
		},
		computed: mapState({
			risk_types: state => state.risk_types.risk_types
		}),
		methods: mapActions('risk_types', [
			'createRiskType',
		]),
		created() {
			this.$store.dispatch('risk_types/getRiskTypes')
		}
	};

</script>
<style scoped>
	th {
		text-align: left;
	}
</style>