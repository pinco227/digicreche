<script>
// import { apiService } from "@/common/api.service.js";
export default {
  name: "Home",
  async beforeCreate() {
    const user = JSON.parse(window.localStorage.getItem("user"));
    const schoolSlug = user.school_slug;
    const roomId = user.room;
    console.log(user);
    switch (user.user_type) {
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
  },
};
</script>
