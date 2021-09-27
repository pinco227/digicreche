<template>
  <div class="home"></div>
</template>

<script>
export default {
  name: "Home",
  beforeCreate() {
    switch (window.localStorage.getItem("user_type")) {
      case "1":
        this.$router.push("/schools");
        break;
      case "2":
        this.$router.push("/schools");
        break;

      default:
        this.$router.push("/schools");
        break;
    }
  },
};
</script>
