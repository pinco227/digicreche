<template>
  <nav class="navbar dc-navbar navbar-light">
    <div class="container-xxl position-relative p-0 justify-content-center">
      <!-- BRAND LOGO -->
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >Digi<strong>Creche</strong>
      </router-link>
      <ul class="nav">
        <!-- SCHOOLS (for managers) -->
        <li class="nav-item" v-if="user.user_type == 1">
          <router-link
            :to="{ name: 'manager-schools' }"
            class="nav-link"
            aria-label="My schools"
          >
            <i class="fas fa-school"></i>
          </router-link>
        </li>
        <!-- SCHOOL PUPILS (for managers) -->
        <!-- shows if a school is selected -->
        <li
          class="nav-item"
          v-if="user.user_type == 1 && $route.params.schoolSlug"
        >
          <router-link
            :to="{
              name: 'school-pupils',
              params: {
                schoolSlug: $route.params.schoolSlug,
              },
            }"
            class="nav-link"
            aria-label="School pupils"
          >
            <i class="fas fa-users"></i>
          </router-link>
        </li>
        <!-- SCHOOL ROOMS (for managers) -->
        <!-- shows if a school is selected -->
        <li
          class="nav-item"
          v-if="user.user_type == 1 && $route.params.schoolSlug"
        >
          <router-link
            :to="{
              name: 'school-rooms',
              params: {
                schoolSlug: $route.params.schoolSlug,
              },
            }"
            class="nav-link"
            aria-label="School rooms"
          >
            <i class="fas fa-book-open"></i>
          </router-link>
        </li>
        <!-- ROOM PUPILS (for managers and teachers) -->
        <!-- shows if a school is selected or if user is a teacher and is assigned to a room -->
        <li
          class="nav-item"
          v-if="
            (user.user_type == 1 &&
              $route.params.schoolSlug &&
              $route.params.roomId) ||
            (user.user_type == 2 && user.school_slug && user.room)
          "
        >
          <router-link
            :to="{
              name: 'room-pupils',
              params: {
                schoolSlug: user.school_slug || $route.params.schoolSlug,
                roomId: user.room || $route.params.roomId,
              },
            }"
            class="nav-link"
            aria-label="Room pupils"
          >
            <i class="fas fa-user-friends"></i>
          </router-link>
        </li>
        <!-- CHILDREN (for parents) -->
        <li class="nav-item" v-if="user.user_type == 3">
          <router-link
            :to="{ name: 'parent-children' }"
            class="nav-link"
            aria-label="My children"
          >
            <i class="fas fa-user-friends"></i>
          </router-link>
        </li>
        <!-- PUPIL ACTIVITIES -->
        <!-- shows if a school is selected, a user is assigned to a school (parent or teacher), or a pupil is selected -->
        <li
          class="nav-item"
          v-if="
            (user.school_slug || $route.params.schoolSlug) &&
            $route.params.pupilId
          "
        >
          <router-link
            :to="{
              name: 'pupil-activities',
              params: {
                schoolSlug: user.school_slug || $route.params.schoolSlug,
                pupilId: $route.params.pupilId,
              },
            }"
            class="nav-link"
            aria-label="Pupil activities"
          >
            <i class="fas fa-basketball-ball"></i>
          </router-link>
        </li>
        <!-- CHAT -->
        <li class="nav-item">
          <router-link
            :to="{ name: 'chat' }"
            class="nav-link"
            aria-label="Chat"
          >
            <i class="fas fa-comments"></i>
          </router-link>
        </li>
        <!-- USER ACCOUNT -->
        <li class="nav-item">
          <router-link
            :to="{ name: 'user_account' }"
            class="nav-link"
            aria-label="User account"
          >
            <i class="fas fa-user-circle"></i>
          </router-link>
        </li>
        <!-- DROPDOWN MENU -->
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            id="navbarDropdown"
            role="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
            aria-label="Menu"
          >
            <i class="fas fa-ellipsis-v"></i>
          </a>
          <ul
            class="dropdown-menu dropdown-menu-end"
            aria-labelledby="navbarDropdown"
          >
            <!-- PRICING (for managers) -->
            <li v-if="user.user_type == 1">
              <router-link
                :to="{
                  name: 'pricing',
                }"
                class="dropdown-item"
              >
                Pricing <i class="fas fa-tags"></i>
              </router-link>
            </li>
            <!-- SUBSCRIPTIONS (for managers) -->
            <!-- a list of schools sorted by subscription status -->
            <li v-if="user.user_type == 1">
              <router-link
                :to="{
                  name: 'subscription-list',
                }"
                class="dropdown-item"
              >
                My Subscriptions <i class="fas fa-wallet"></i>
              </router-link>
            </li>
            <!-- SUBSCRIPTION (for managers) -->
            <!-- shows only if a school is selected -->
            <li v-if="user.user_type == 1 && $route.params.schoolSlug">
              <router-link
                :to="{
                  name: 'school-subscription',
                  params: { schoolSlug: $route.params.schoolSlug },
                }"
                class="dropdown-item"
              >
                Manage Subscription <i class="far fa-credit-card"></i>
              </router-link>
            </li>
            <!-- CONTACT MANAGER (for teachers and parents) -->
            <li v-if="user.manager">
              <router-link
                :to="{
                  name: 'chat',
                  params: { chatId: user.manager },
                }"
                class="dropdown-item"
              >
                Contact Manager <i class="fas fa-comment"></i>
              </router-link>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <!-- Log out -->
            <li>
              <a href="/accounts/logout/" class="dropdown-item">
                Log Out <i class="fas fa-sign-out-alt"></i>
              </a>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { Dropdown } from "bootstrap";
export default {
  name: "DefaultNavbarComponent",
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    new Dropdown(document.querySelector(".dropdown-toggle"));
  },
};
</script>

<style scoped>
.dc-navbar {
  background: linear-gradient(0deg, var(--light-bg) 50%, var(--body-bg) 150%);
  border-bottom: 3px solid #00da0b;
  padding: 0;
}
.navbar-brand {
  font-family: "Arima Madurai", cursive;
  background: linear-gradient(
    90deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 37%,
    transparent 38%,
    transparent 36%,
    var(--green-accent) 36%,
    var(--green-accent-light) 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent !important;
  font-weight: 400;
  font-size: 2rem;
  padding: 0 1rem;
  margin: 0;
}
.navbar-brand strong {
  font-weight: 900;
}
.nav {
  flex-grow: 1;
  justify-content: space-evenly;
}
.nav-item {
  flex-grow: 1;
}
.nav-link {
  background: linear-gradient(
    90deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  display: block;
  padding: 0.5rem 1rem;
  color: transparent;
  text-decoration: none;
  transition: none;
  font-size: 1.4rem;
  text-align: center;
}
.nav-link:focus,
.nav-link:hover,
.nav-link:active,
.nav-link.router-link-active {
  background: linear-gradient(
    180deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
  background-clip: initial;
  -webkit-background-clip: initial;
  color: var(--light-bg);
  margin-bottom: -5px;
  border-bottom: 5px solid var(--orange-accent);
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}
.dropdown-menu {
  min-width: 13rem;
  background-color: var(--light-bg);
  color: var(--orange-accent-light);
  border: 0;
  border-radius: 0;
}
.dropdown-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}
.dropdown-item:focus,
.dropdown-item:hover {
  color: var(--orange-accent);
  background: none;
}
.dropdown-toggle::after {
  display: none;
}
</style>
