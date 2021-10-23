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
      else setPageTitle("");
    },
  },
  created() {
    this.setUserInfo();
  },
  watch: {
    $route() {
      // Set default permission when route change
      // to allow the router-view to update permission if needed
      this.permission = true;
    },
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
  --orange-accent-dark: #a74809;
  --body-text: #454545;
}

body {
  background-color: var(--body-bg);
  font-family: "Open Sans", sans-serif;
  font-weight: 300;
  color: var(--body-text);
}
.head-tile {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 1rem;
  background: linear-gradient(90deg, var(--light-bg) 0%, var(--body-bg) 100%);
  box-shadow: 3px 5px 10px -10px var(--body-text);
}
.head-tile p {
  margin: 0;
}
.tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  justify-content: flex-start;
  gap: 0.5rem;
  padding: 1rem;
  background: linear-gradient(180deg, var(--light-bg) 0%, var(--body-bg) 100%);
  color: var(--orange-accent-dark);
  font-size: 1.5rem;
  font-weight: bolder;
  text-decoration: none;
  height: 100%;
  box-shadow: 0px 4px 9px -9px var(--body-text);
}
.tile:hover {
  background: var(--light-bg);
  color: var(--orange-accent);
}
.tile i {
  font-size: 2rem;
  color: var(--body-text);
}
.tile:hover i {
  color: var(--orange-accent);
}
.tile .tile-caption {
  font-size: 1rem;
  color: var(--body-text);
  margin: 0;
}
.round-photo-container {
  width: 50%;
  position: relative;
  overflow: hidden;
  border-radius: 50%;
  box-shadow: 3px 5px 10px -10px var(--body-text);
  background-color: var(--light-bg);
}
.round-photo-container:after {
  content: "";
  display: block;
  padding-bottom: 100%;
}
.round-photo-container img {
  position: absolute;
  min-width: 100%;
  min-height: 100%;
  top: 0;
  left: 0;
  object-fit: cover;
  max-width: 120%;
  height: auto;
}
.no-photo {
  position: absolute;
  top: 0;
  left: 0;
  background: gray;
  width: 100%;
  height: 100%;
  color: white;
  display: flex;
  align-content: center;
  justify-content: center;
  align-items: center;
}
</style>
