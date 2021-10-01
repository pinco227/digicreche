<template>
  <div class="single-room col-xs-6 col-md-4 col-lg-3 text-center">
    <h2>
      <router-link
        :to="{
          name: 'room-pupils',
          params: { schoolSlug: room.school_slug, id: room.id },
        }"
      >
        {{ room.name }}
      </router-link>
    </h2>
    <span v-if="room.has_teacher">
      <span v-if="room.teachers.length > 1">
        Teacher(s): {{ room.teachers.length }}
      </span>
      <span v-else v-for="teacher in room.teachers" :key="teacher.id">
        Teacher: {{ teacher.name }}
      </span>
    </span>
    <span v-else>Assign a teacher</span>
    <p>Pupils: {{ room.pupils_count }}</p>
  </div>
</template>

<script>
export default {
  name: "RoomComponent",
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
};
</script>
