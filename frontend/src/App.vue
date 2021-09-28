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
import { apiService } from "./common/api.service.js";

export default {
  name: "App",
  components: {
    DefaultNavbarComponent,
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/rest-auth/user/");
      window.localStorage.setItem("user_type", data["user_type"]);
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Arima+Madurai:wght@300;400;500;700;800;900&family=Open+Sans:wght@300;400;600;700;800&display=swap");

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
  font-family: "Open Sans", sans-serif;
  font-weight: 300;
}
</style>
