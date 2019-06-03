<template>
    <b-container class="d-flex flex-column min-vh-100">
        <b-row class="flex-grow-1 justify-content-center align-items-center mx-auto login-form">
            <b-form @submit.prevent="login(inputs)" class="col-12">
                <h4 class="text-center">Log in</h4>
                <b-form-group id="username-group" label="Username:" label-for="username">
                    <b-form-input id="username" v-model="inputs.username" type="text" required placeholder="Enter username"></b-form-input>
                </b-form-group>
                <b-form-group id="password-group" label="Password:" label-for="password">
                    <b-form-input id="password" v-model="inputs.password" type="password" required placeholder="Enter password"></b-form-input>
                </b-form-group>
                <div class="clearfix">
                    <router-link class="float-left" to="/password_reset">Forgot password?</router-link>
                </div>
                <b-alert :show="errors != null" variant="danger">
                    <li v-for="error in errors" :key="error">{{error}}</li>
                </b-alert>
                <div class="clearfix">
                    <b-button type="submit" class="float-right" variant="primary">Submit</b-button>
                </div>
            </b-form>
        </b-row>
        <!-- {{error}} -->
    </b-container>
</template>
<script>
    import {
        mapState,
        mapActions
    } from 'vuex'
    export default {
        data() {
            return {
                inputs: {
                    username: '',
                    password: '',
                },
            };
        },
        computed: mapState({
            errors: state => state.auth.errors
        }),
        methods: {
            async login({username,password}) {
                await this.$store.dispatch('auth/login', {username,password});
                this.$router.push('/');
            },
        },
    };
</script>
<style scoped>
    .login-form {
        width: 370px;
    }
    .login-form form {
        margin-bottom: 15px;
        border: 1px solid #e3e3e3;
        border-radius: 4px;
        padding: 30px;
    }
    .form-control {
        min-height: 38px;
    }
</style>