<template><section id="home"></section></template>

<script>
export default {
  name: "Home",
  created() {
    const user = JSON.parse(window.localStorage.getItem("user"));
    let schoolSlug = null;
    let roomId = null;
    let user_type = null;
    if (Object.keys(user).length) {
      schoolSlug = user.school_slug;
      roomId = user.room;
      user_type = user.user_type;
    }

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
  },
};
</script>
