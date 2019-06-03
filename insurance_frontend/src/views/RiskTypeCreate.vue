<template>
	<b-container class="pb-3 mb-5">
		<h2>New Risk</h2>
		<b-form class="mt-5"  @submit.prevent="handleNewRiskType">
			<b-form-group class="required" id="name-input-group" label="Name:" label-for="name-input" label-cols="1">
				<b-form-input id="name-input" v-model="name" required placeholder="Enter risk type name"></b-form-input>
			</b-form-group>
			<b-form-group id="description-input-group" label="Description:" label-for="description-input" label-cols="1">
				<b-form-textarea  id="description-input" v-model="description" placeholder="Risk description..." rows="3" max-rows="6" required></b-form-textarea>
			</b-form-group>

			<b-form-group label="Fields:" label-cols="1">
				<b-card bg-variant="white">
					<b-form-group v-for="(field, fieldIdx) in fields" v-bind:key="fieldIdx">
						<b-row style="align-items:center">
							<b-col>
								<b-form-group label="Name:" label-for="name-input" label-cols="3">
									<b-form-input id="name-input"  v-model="field.name" required></b-form-input>
								</b-form-group>
							</b-col>
							<b-col>
								<b-form-group label="Type:" label-for="type-input" label-cols="3">
									<b-form-select  v-model="field.type" @change="onTypeChange(fieldIdx,field.type)" id="type-input" required>
										<option :value="null" disabled>Choose...</option>
										<option v-for="(field_type,field_type_key) in field_types" v-bind:key="field_type_key" :value="field_type_key">
											{{ field_type }}
										</option>
									</b-form-select>
								</b-form-group>
							</b-col>
							<b-col>
								<b-form-group>
									<b-form-checkbox v-model="field.required">Required</b-form-checkbox>
								</b-form-group>
							</b-col>
							<b-col>
								<b-form-group>
									<b-button v-visible="fieldIdx != 0" @click="deleteField(fieldIdx)" variant="danger">Delete field</b-button>
								</b-form-group>
							</b-col>
							<!-- <b-col-3>
								<b-button v-visible="fieldIdx != 0" @click="deleteField(fieldIdx)" variant="danger">Delete field</b-button>
							</b-col-3> -->
						</b-row>

						<b-form-group v-if="field.type === 'option'" label="Options:">
							<b-form-group  label-cols="1" inline v-for="(field_option, optionIdx) in field.field_options" v-bind:key="optionIdx">
								<!-- <label :for="'option-input-'+optionIdx">Text</label> -->
								<b-row>
									<b-col>
										<b-input :id="'option-input-'+optionIdx" class="mb-2 mr-sm-2 mb-sm-0" v-model="field_option.content" required></b-input>
									</b-col>
									<b-col>
										<b-button  n v-if="optionIdx>1" @click="deleteFieldOption(fieldIdx,optionIdx)" variant="danger">Delete option</b-button>
									</b-col>
								</b-row>
							</b-form-group>
							<b-button class="form-control col-md-2" variant="secondary" @click="addFieldOption(fieldIdx)">Add more option</b-button>
						</b-form-group>
						<hr class="col-xs-12">
					</b-form-group>
					<b-button @click="addField" variant="secondary">Add more field</b-button>
				</b-card>
			</b-form-group>
			<b-alert :show="errors != null" variant="danger">
				<li v-for="error in errors" :key="error">{{error}}</li>
			</b-alert>
			<b-button type="submit" variant="primary" class="float-right">Submit</b-button>
		</b-form>
		<!-- {{$data.fields}} -->
	</b-container>
</template>
<script>
	import { mapState } from 'vuex'
	export default{
		data (){
			return{
				name: '',
				description: '',
				// field_types: ["Text","Number","Boolean","Option","Date"],
				field_types: {"text": "Text", "number": "Number", "decimal":"Decimal", "boolean": "Boolean","option": "Option","date": "Date"},
				fields: [],
				// field_options: []
			}
		},
		computed: mapState({
			errors: state => state.risk_types.errors
		}),
		methods: {
			addField() {
				this.fields.push({
					name: '',
					description: '',
					type: null,
					field_options: [],
					required: false
				});

				var scrollingElement = (document.scrollingElement || document.body);
				//scrollingElement.scrollTop = scrollingElement.scrollHeight;
				setTimeout(function(){ scrollingElement.scrollTop = scrollingElement.scrollHeight }, 100);
			},
			deleteField(fieldIdx) {
				this.fields.splice(fieldIdx,1)
			},
			addFieldOption(fieldIdx){
				this.fields[fieldIdx].field_options.push({
					content: ''
				});
			},
			deleteFieldOption(fieldIdx,optionIdx) {
				this.fields[fieldIdx].field_options.splice(optionIdx,1)
			},
			onTypeChange(fieldIdx,field_type){
				if(field_type == 'option'){
					this.fields[fieldIdx].field_options = [
						{content:''},
						{content:''}
					];
				}
				else{
					this.fields[fieldIdx].field_options = [];
				}

			},
			async handleNewRiskType(){
				var risk_type = {
					name: this.name,
					description: this.description,
					risk_fields: this.fields
				};
				console.log(risk_type);
				await this.$store.dispatch('risk_types/createRiskType',risk_type);
				if(!this.errors)
					this.$router.push("/risk_types");
			}
		},
		created() {
			this.addField();
		}
	}
</script>
<style scoped>

</style>