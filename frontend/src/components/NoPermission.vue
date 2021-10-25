<template>
  <div class="my-2 row justify-content-center">
    <div class="col-12">
      <button type="button" @click="goBack" class="btn btn-light">Back</button>
    </div>
    <div class="col-12 col-md-10 col-lg-8">
      <div class="alert alert-warning">
        You do not have permission to see this page!
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NoPermissionComponent",
  methods: {
    goBack() {
      this.$router.back();
    },
  },
};
</script>
