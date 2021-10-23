<template>
  <div class="single-pupil col-6 col-md-3 col-lg-2 text-center">
    <router-link
      v-if="pupil.room"
      :to="{
        name: 'pupil-activities',
        params: { schoolSlug: pupil.school_slug, pupilId: pupil.id },
      }"
      class="tile"
    >
      <RoundPhotoComponent :pupil="pupil" />
      {{ pupil.first_name }} {{ pupil.last_name }}
    </router-link>
    <router-link
      v-else
      :to="{
        name: 'pupil-edit',
        params: { schoolSlug: pupil.school_slug, pupilId: pupil.id },
      }"
      class="tile"
    >
      <RoundPhotoComponent :pupil="pupil" />
      {{ pupil.first_name }} {{ pupil.last_name }}
    </router-link>
  </div>
</template>

<script>
import RoundPhotoComponent from "../components/RoundPhoto.vue";
export default {
  name: "PupilComponent",
  props: {
    pupil: {
      type: Object,
      required: true,
    },
  },
  components: {
    RoundPhotoComponent,
  },
};
</script>

<style scoped>
.tile {
  font-size: 1.3rem;
}
</style>
