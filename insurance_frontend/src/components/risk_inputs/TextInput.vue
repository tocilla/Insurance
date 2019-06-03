<template>
	<b-form-group>
		<b-form-row>
			<b-col sm="2">
				<label :for="field.name" :class="{ required: field.required }">{{field.name}}:</label>
			</b-col>
			<b-col sm="10">
				<template>
					<b-form-input :id="field.name" v-model="input.value" type="text" v-bind:required="field.required"></b-form-input>
				</template>
			</b-col>
		</b-form-row>
	</b-form-group>
</template>

<script>
export default {
	name: "text-input",
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