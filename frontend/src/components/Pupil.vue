<template>
  <div class="single-pupil col-xs-4 col-md-3 col-lg-2 text-center">
    <h2>
      <router-link
        :to="{
          name: 'manager-schools',
          params: { schoolSlug: pupil.school_slug },
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
