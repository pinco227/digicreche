<template>
    <main>
        <DefaultNavbarComponent />
        <div class="container-xxl">
            <router-view />
        </div>
    </main>
</template>

<script>
import DefaultNavbarComponent from "./components/Navbar.vue";
export default {
    name: "App",
    components: {
        DefaultNavbarComponent,
    },
};
</script>

<style>
:root {
    --body-bg: #ebebeb;
    --light-bg: #fffdfd;
    --green-accent-light: #00da0b;
    --green-accent: #33670a;
    --orange-accent-light: #ffa13c;
    --orange-accent: #e25a00;
}
body {
    background-color: #ebebeb;
}
</style>
