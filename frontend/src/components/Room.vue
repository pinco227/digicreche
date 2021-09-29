<template>
  <div class="single-room col-xs-6 col-md-4 col-lg-3 text-center">
    <h2>
      <router-link :to="{ name: 'manager-schools' }">
        {{ room.name }}
      </router-link>
    </h2>
    <span v-if="room.has_teacher">Teacher(s): {{ room.teacher_name }}</span>
    <span v-else>Assign a teacher</span>
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
