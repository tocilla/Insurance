<template>
	<b-form-group>
		<b-form-row>
			<b-col sm="2">
				<label :for="field.name" :class="{ required: field.required }">{{field.name}}:</label>
			</b-col>
			<b-col sm="10">
				<b-form-input :id="field.name" v-model="input.value" type="number" step="any" v-bind:required="field.required"></b-form-input>
			</b-col>
		</b-form-row>
	</b-form-group>
</template>

<script>
export default {
	name: "decimal-input",
	props: {
		field: {
			type: Object,
			required: true
		},
		input:{
			type: Object,
			required: true
		}
	}
};
</script>