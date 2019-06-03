<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="navbar">
            <b-navbar-brand href="#">Insurance System</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <router-link tag="b-nav-item" to="/">Home</router-link>
                    <router-link tag="b-nav-item" to="/risks">Risks</router-link>
                    <router-link tag="b-nav-item" to="/risk_types">Risk Types</router-link>
                    <router-link tag="b-nav-item" to="/about">About</router-link>
                </b-navbar-nav>
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown text="User" right>
                        <router-link tag="b-dropdown-item" to="/profile">Profile</router-link>
                        <router-link  tag="b-dropdown-item" to="/logout">Logout</router-link>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>
<script>
    export default {
    	name: 'navbar',
    };
</script>
<style scoped>
    .bg-navbar{
		background: #2c2c2c;
    }
</style>