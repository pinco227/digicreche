<template>
  <nav class="navbar dc-navbar navbar-light">
    <div class="container-xxl position-relative">
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >Digi<strong>Creche</strong>
      </router-link>
      <ul class="nav me-5 pe-3">
        <li class="nav-item">
          <router-link :to="{ name: 'home' }" class="nav-link"
            ><i class="far fa-star"></i>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'home' }" class="nav-link"
            ><i class="far fa-futbol"></i>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'home' }" class="nav-link"
            ><i class="far fa-comments"></i>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'home' }" class="nav-link"
            ><i class="far fa-user"></i>
          </router-link>
        </li>
      </ul>
      <button
        class="navbar-toggler position-absolute top-0 end-0 me-3 mt-1"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-link" href="#">Account</a>
          <a class="nav-link" href="#">Log Out</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "DefaultNavbarComponent",
};
</script>

<style scoped>
.dc-navbar {
  background-color: #fffdfd;
  border-bottom: 2px solid #00da0b;
}
.navbar-brand {
  font-family: "Arima Madurai", cursive;
  background: linear-gradient(
    90deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 35%,
    transparent 35%,
    transparent 36%,
    var(--green-accent) 36%,
    var(--green-accent-light) 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent !important;
  font-weight: 400;
  font-size: 2rem;
  padding: 0;
}
.navbar-brand strong {
  font-weight: 900;
}
.nav-link {
  display: block;
  padding: 0.5rem 1rem;
  color: #0d6efd;
  text-decoration: none;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out;
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
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out;
  font-size: 1.4rem;
}
.nav-link:focus,
.nav-link:hover {
  color: var(--orange-accent);
}
</style>
