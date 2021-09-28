<template>
  <div class="school mt-2">
    <div class="row">
      <div class="col-6">
        <a href="#" class="btn btn-light">Back</a>
      </div>
      <div class="col-6 text-end">
        <a href="#" class="btn btn-light">Edit School</a>
        <a href="#" class="btn btn-success">Add Room</a>
      </div>
    </div>
    <h2>{{ slug }}</h2>
  </div>
</template>

<script>
export default {
  name: "SchoolRooms",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
};
</script>