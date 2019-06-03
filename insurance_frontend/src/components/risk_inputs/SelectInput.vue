<template>
	<b-form-group>
		<b-form-row>
			<b-col sm="2">
				<label :for="field.name" :class="{ required: field.required }">{{field.name}}:</label>
			</b-col>
			<b-col sm="10">
				<b-form-select :id="field.name" v-model="input.value"  v-bind:required="field.required">
					<option :value="null" disabled>Choose...</option>
					<option v-for="field_options in field.field_options" :key="field_options.id">
							{{ field_options.content }}
					</option>
				</b-form-select>
			</b-col>
		</b-form-row>
	</b-form-group>
</template>

<script>
export default {
	name: "select-input",
	props: {
		field: {
			type: Object,
			required: true
		},
		input:{
			type: Object,
			required: true,
			value:null
		}
	}
};
</script>