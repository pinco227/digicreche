<template>
  <button type="button" @click="goBack" class="btn btn-light">Back</button>
</template>

<script>
export default {
  name: "GoBackComponent",
  methods: {
    goBack() {
      this.$router.back();
    },
  },
};
</script>
