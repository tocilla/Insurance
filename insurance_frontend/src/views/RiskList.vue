<template>
	<b-container class="risk-type">
		<b-row>
			<b-col>
				<h2>{{title}}</h2>
			</b-col>
			<b-col>
				<router-link tag="button" style="float: right" class="btn  btn-primary" to="/risks/create">New Risk</router-link>
			</b-col>
		</b-row>
 
		<p v-show="loading">Loading...</p>

		<br><br>
		<table class="table table-condensed">
			<thead>
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Risk Type</th>
					<th>Created At</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="risk in risks" :key="risk.id">
					<td>{{risk.id}}</td>
					<td>{{risk.name}}</td>
					<td>{{risk.risk_type.name}}</td>
					<td>{{risk.created_at | formatDate}}</td>
				</tr>
			</tbody>
		</table>
		{{$data.risks}}
	</b-container>
</template>
<script>
	// import api from '@/api'
	// export default{
	//     name:'RiskList',
	//     data (){
	//         return{
	//             title:'Risks',
	//             loading: false,
	//             risks: {},
	//             model: {}
	//         }
	//     },
	//     async created () {
	//         this.refreshRiskTypes()
	//     },
	//     methods: {
	//         async refreshRiskTypes () {
	//             this.loading = true
	//             this.risks = await api.getRiskTypes()
	//             this.loading = false
	//         }
	//     }
	// }


	import { mapState, mapActions } from 'vuex'
	export default {
		name: "RiskList",
		data() {
			return {
				title:'Risks',
				loading: false,
				//risks: [],
			};
		},
		computed: mapState({
			risks: state => state.risks.risks
		}),
		methods: mapActions('risks', [
			'getRisks',
		]),
		created() {
			this.$store.dispatch('risks/getRisks')
		}
	};

</script>
<style scoped>
	th {
		text-align: left;
	}
</style>