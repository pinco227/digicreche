<template>
  <div class="spinner-overlay" id="spinner" style="display: none">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpinnerComponent",
};
</script>

<style scoped>
.spinner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100%;
  background-color: rgba(255, 161, 60, 0.1);
}
.spinner-border {
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 4rem;
  height: 4rem;
  color: var(--orange-accent);
}
</style>
