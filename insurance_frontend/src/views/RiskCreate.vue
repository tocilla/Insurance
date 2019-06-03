<template>
	<b-container>
		<h2>New Risk</h2>
		<b-form class="mt-5"  @submit.prevent="handleRisk">
			<b-form-group id="risk-name-input-group" label="Risk name:" label-for="name-input" label-cols="2">
				<b-form-input id="name-input" v-model="name" required placeholder="Enter risk name"></b-form-input>
			</b-form-group>
			<b-form-group id="risk-type-input-group" label="Risk type:" label-for="type-input" label-cols="2">
				<b-form-select  v-model="risk_type" id="type-input" required>
					<option :value="null" disabled>Choose...</option>
					<option v-for="risk_type in risk_types" v-bind:key="risk_type.id" :value="risk_type">
						{{ risk_type.name }}
					</option>
				</b-form-select>
			</b-form-group>
			<b-form-group  v-if="risk_type">
				<template  v-for="field in risk_type.risk_fields">
					<component v-bind:is="components[field.type]" v-bind:field="field" :input.sync="field" v-bind:key="field.id"></component>
				</template>
			</b-form-group>
			<b-alert :show="errors != null" variant="danger">
				<li v-for="error in errors" :key="error">{{error}}</li>
			</b-alert>
			<b-button type="submit" variant="primary" class="float-right">Submit</b-button>
		</b-form>
	</b-container>
</template>

<script>

import { mapState, mapActions } from 'vuex'

const TextInput = () => import('@/components/risk_inputs/TextInput.vue');
const NumberInput = () => import('@/components/risk_inputs/NumberInput.vue');
const DecimalInput = () => import('@/components/risk_inputs/DecimalInput.vue');
const DateInput = () => import('@/components/risk_inputs/DateInput.vue');
const SelectInput = () => import('@/components/risk_inputs/SelectInput.vue');
const CheckboxInput = () => import('@/components/risk_inputs/CheckboxInput.vue');

export default{
	components: {
		text:TextInput,
		number:NumberInput,
		decimal:DecimalInput,
		date:DateInput,
		option:SelectInput,
		boolean:CheckboxInput
	},
	data (){
		return{
			name: '',
			// field_types: {"text": "Text", "number": "Number","boolean": "Boolean","option": "Option","date": "Date"},
			// fields: [],
			risk_type:null,
			// field_options: [],
			components: this.$options.components,
			test:''
			
		}
	},
	computed: mapState({
		risk_types: state => state.risk_types.risk_types,
		errors: state => state.risks.errors,
	}),
	methods: {
		...mapActions('risks', [
			'createRisk',
		]),
		async handleRisk(){
			var risk_inputs = this.risk_type.risk_fields.map(e => { 
				return { 
					risk_field: e.id,
					value: e.value 
				}
			});
			var risk = {
				name: this.name,
				risk_type: this.risk_type.id,
				risk_inputs: risk_inputs
			};
			// console.log(JSON.stringify(risk));
			await this.createRisk(risk);// this.$store.dispatch('risks/createRisk',risk);
			if(!this.errors)
				this.$router.push("/risks");
		}
	},
	created() {
		this.$store.dispatch('risks/getRisks');
		this.$store.dispatch('risk_types/getRiskTypes');
	}
}
</script>
<style scoped>

</style>