<template>
  <div class="round-photo-container">
    <img v-if="pupil.photo" :src="pupil.photo" :alt="pupil.first_name" />
    <span class="no-photo" v-else>No Photo</span>
  </div>
</template>

<script>
export default {
  name: "RoundPhotoComponent",
  props: {
    pupil: {
      type: Object,
      required: true,
    },
  },
};
</script>
