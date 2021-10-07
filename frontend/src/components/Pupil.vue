<template>
  <div class="single-pupil col-xs-4 col-md-3 col-lg-2 text-center">
    <h2>
      <router-link
        v-if="pupil.room"
        :to="{
          name: 'pupil-activities',
          params: { schoolSlug: pupil.school_slug, pupilId: pupil.id },
        }"
      >
        {{ pupil.first_name }} {{ pupil.last_name }}
      </router-link>
      <router-link
        v-else
        :to="{
          name: 'pupil-edit',
          params: { schoolSlug: pupil.school_slug, pupilId: pupil.id },
        }"
      >
        {{ pupil.first_name }} {{ pupil.last_name }}
      </router-link>
    </h2>
  </div>
</template>

<script>
export default {
  name: "PupilComponent",
  props: {
    pupil: {
      type: Object,
      required: true,
    },
  },
};
</script>
