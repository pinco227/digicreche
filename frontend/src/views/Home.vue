<template>
  <div class="home"></div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Home",
  async beforeCreate() {
    const endpoint = "/api/rest-auth/user/";
    const userData = await apiService(endpoint);
    const schoolSlug = userData.school_slug;
    const roomId = userData.room;

    switch (window.localStorage.getItem("user_type")) {
      case "1":
        this.$router.push({ name: "manager-schools" });
        break;
      case "2":
        this.$router.push(`/schools/${schoolSlug}/${roomId}`);
        break;

      default:
        this.$router.push("/schools");
        break;
    }
  },
};
</script>
