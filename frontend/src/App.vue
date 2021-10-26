<template>
  <main>
    <DefaultNavbarComponent :user="user" />
    <div class="container-xxl position-relative">
      <div v-if="permission">
        <router-view
          @setPermission="updatePermission"
          @updateUser="setUserInfo"
        ></router-view>
      </div>
      <NoPermissionComponnent v-else />
      <SpinnerComponent />
    </div>
  </main>
</template>

<script>
import DefaultNavbarComponent from "@/components/Navbar.vue";
import NoPermissionComponnent from "@/components/NoPermission.vue";
import SpinnerComponent from "@/components/Spinner.vue";
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";

export default {
  name: "App",
  components: {
    DefaultNavbarComponent,
    NoPermissionComponnent,
    SpinnerComponent,
  },
  data() {
    return {
      user: {},
      permission: true,
    };
  },
  methods: {
    async setUserInfo() {
      // Fetches the user data from API and saves it into local storage
      // to be accessed gobally
      const data = await apiService("/api/rest-auth/user/");
      if (data.status >= 200 && data.status < 300) {
        this.user = data.body;
        window.localStorage.setItem("user", JSON.stringify(data.body));
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403) this.updatePermission(false);
      }
    },
    updatePermission(value) {
      // Updates global permission when it is emitted from a component
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
/* GLOBAL STYLES */
/* IMPORTS */
@import url("https://fonts.googleapis.com/css2?family=Arima+Madurai:wght@300;400;500;700;800;900&family=Open+Sans:wght@300;400;600;700;800&display=swap");

/* VARIABLES */
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
/* BODY & TYPOGRAPHY */
body {
  background-color: var(--body-bg);
  font-family: "Open Sans", sans-serif;
  font-weight: 300;
  color: var(--body-text);
}

a {
  color: var(--green-accent);
}
a:hover {
  color: var(--green-accent-light);
}
/* BUTTONS */
.btn {
  border-radius: 0;
}
.btn-link {
  color: var(--green-accent-dark);
}
.btn-link:hover {
  color: var(--orange-accent-dark);
}
.btn-light {
  color: var(--body-text);
  background-color: var(--light-bg);
  border-color: var(--light-bg);
}
.btn-success {
  color: #fff;
  background-color: var(--green-accent);
  border-color: var(--green-accent);
}
.btn-check:focus + .btn-success,
.btn-success:focus,
.btn-check:focus + .btn,
.btn:focus {
  box-shadow: 0 0 0 0.25rem rgba(0, 218, 11, 0.15);
}
.btn-primary {
  color: #fff;
  border-color: var(--orange-accent);
  background: linear-gradient(
    180deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
}
.btn-primary:hover {
  border-color: var(--orange-accent-dark);
}
.btn-primary.disabled,
.btn-primary:disabled {
  border-color: var(--orange-accent-dark);
}
.btn-check:active + .btn-primary,
.btn-check:checked + .btn-primary,
.btn-primary.active,
.btn-primary:active,
.show > .btn-primary.dropdown-toggle {
  border-color: var(--orange-accent-dark);
}
.btn-check:focus + .btn-primary,
.btn-primary:focus {
  box-shadow: 0 0 0 0.25rem rgba(255, 161, 60, 0.5);
}
.btn-group-sm > .btn {
  border-radius: 0;
}
/* LISTS & FORMS */
.list-group {
  border-radius: 0;
}
.list-group-item.active {
  font-weight: bold;
  border-color: var(--orange-accent);
  background: linear-gradient(
    90deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
}
.invalid .form-label,
.invalid small {
  color: red;
}
.invalid .form-control {
  border: 1px solid red;
}
.form-control {
  border-radius: 0;
}
.form-control:focus {
  border-color: #00da0b;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(0, 218, 11, 0.15);
}
.form-select:focus {
  border-color: #00da0b;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(0, 218, 11, 0.15);
}
.form-check-input:checked {
  background-color: var(--orange-accent);
  border-color: var(--orange-accent);
}
.form-check-input:focus {
  border-color: #00da0b;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(0, 218, 11, 0.15);
}
/* POPOVERS */
.popover {
  border-radius: 0;
  border: 0;
  background: linear-gradient(180deg, var(--light-bg) 0%, var(--body-bg) 100%);
  box-shadow: 3px 5px 10px -10px var(--body-text);
}
.popover-header {
  background: none;
}

.bs-popover-auto[data-popper-placement^="bottom"] > .popover-arrow::before,
.bs-popover-bottom > .popover-arrow::before {
  border-bottom-color: #fffdfd;
}
.bs-popover-auto[data-popper-placement^="bottom"] > .popover-arrow::after,
.bs-popover-bottom > .popover-arrow::after {
  border-bottom-color: #fffdfd;
}
/* TILES */
.head-tile {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 1rem;
  background: linear-gradient(90deg, var(--light-bg) 0%, var(--body-bg) 100%);
  box-shadow: 3px 5px 10px -10px var(--body-text);
  height: 100%;
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
/* RADIO TILES */
.price-radio {
  display: none;
}
.price-radio:checked + .price-tile {
  border: 3px solid var(--orange-accent);
  background: var(--light-bg);
  color: var(--orange-accent-dark);
}
.price-radio:checked + .price-tile .price-title strong {
  color: var(--orange-accent);
}
.price-tile {
  color: var(--body-text);
  padding: 0;
}
.price-tile:hover {
  color: var(--orange-accent-dark);
  cursor: pointer;
}
.price-tile:hover .price-title strong {
  color: var(--orange-accent);
}
.price-tile .card-body {
  text-align: center;
}
.price-tile .list-group {
  border: none;
}
.price-tile .list-group-item {
  background: none;
  font-size: 1.25rem;
  padding: 0.2rem 1.5rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.price-tile .list-group-item i {
  font-size: 1rem;
  color: var(--green-accent-light);
}
.price-tile .price-title {
  font-size: 1.5rem;
  font-weight: 300;
}
.price-tile .price-title strong {
  font-size: 3rem;
  font-weight: bolder;
  display: block;
  text-align: center;
  color: var(--orange-accent-dark);
}
.price-tile p {
  font-weight: 400;
  font-size: 1.25rem;
  color: var(--green-accent);
}
/* PUPIL */
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
