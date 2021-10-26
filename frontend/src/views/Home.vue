<template><section id="home"></section></template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Home",
  methods: {
    async getUser() {
      // Fetches the user data from API
      const data = await apiService("/api/rest-auth/user/");
      if (data.status >= 200 && data.status < 300) {
        const user = data.body;
        const schoolSlug = user.school_slug;
        const roomId = user.room;
        const user_type = user.user_type;
        switch (user_type) {
          case 1:
            this.$router.push({ name: "manager-schools" });
            break;
          case 2:
            if (schoolSlug && roomId)
              this.$router.push(`/schools/${schoolSlug}/${roomId}`);
            else this.$router.push({ name: "user_account" });
            break;
          case 3:
            this.$router.push({ name: "parent-children" });
            break;

          default:
            this.$router.push({ name: "user_account" });
            break;
        }
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403) this.updatePermission(false);
      }
    },
  },
  created() {
    this.getUser();
  },
};
</script>
