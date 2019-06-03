<template>
	<b-form-group :for="field.name" label-cols="2">
		<b-form-checkbox :id="field.name" v-model="input.value" :true-value="'true'" :false-value="'false'">{{field.name}}</b-form-checkbox>
	</b-form-group>
</template>

<script>
export default {
	name: "checkbox-input",
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