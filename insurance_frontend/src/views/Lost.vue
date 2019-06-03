<template>
    <b-container class="h-100 d-flex justify-content-center align-items-center" id="lost-view">
        <div>
            <h1>Page Not Found</h1>
            <h4>One of us is lost.</h4>
            <router-link to="/">Take me home.</router-link>
        </div>
    </b-container>
</template>
<script>
    export default {
        name: 'lost',
    };
</script>