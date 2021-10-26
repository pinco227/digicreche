<template>
  <div
    class="assigned-teacher btn-group btn-group-sm bg-light me-1"
    role="group"
  >
    <button type="button" class="btn btn-outline-secondary" disabled>
      {{ teacher.name }}
    </button>
    <button
      v-if="isManager"
      type="button"
      class="btn btn-outline-danger"
      @click="triggerUnassignTeacher"
      :class="{
        disabled: noSubscription,
      }"
      aria-label="Remove teacher from room"
    >
      <i class="fa fa-trash"></i>
    </button>
  </div>
</template>

<script>
export default {
  name: "AssignedTeacherComponent",
  props: {
    teacher: {
      type: Object,
      required: true,
    },
    noSubscription: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    triggerUnassignTeacher() {
      // Emits unassign teacher signal to parent component
      this.$emit("unassign-teacher", this.teacher);
    },
  },
};
</script>
