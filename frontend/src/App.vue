<template>
  <main>
    <DefaultNavbarComponent />
    <div class="container-xxl">
      <div v-if="permission">
        <router-view @setPermission="updatePermission"></router-view>
      </div>
      <NoPermissionComponnent v-else />
    </div>
  </main>
</template>

<script>
import DefaultNavbarComponent from "@/components/Navbar.vue";
import NoPermissionComponnent from "@/components/NoPermission.vue";
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";

export default {
  name: "App",
  components: {
    DefaultNavbarComponent,
    NoPermissionComponnent,
  },
  data() {
    return {
      permission: true,
    };
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/rest-auth/user/");
      if (data.status >= 200 && data.status < 300) {
        window.localStorage.setItem("user", JSON.stringify(data.body));
      } else {
        // TODO: error handling
        if (data.status == 403) this.updatePermission(false);
      }
    },
    updatePermission(value) {
      this.permission = value;
      if (!value) setPageTitle("Forbidden");
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
