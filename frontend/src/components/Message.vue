<template>
  <div
    id="single-message"
    class="row align-items-center"
    :class="{ sent: sent }"
  >
    <div
      class="col-9 message-card"
      :class="{ 'order-1': !sent, 'order-2': sent }"
    >
      <span v-if="!sent" class="sender-name"
        >{{ message.sender_name }} <br
      /></span>
      {{ message.message }}
    </div>
    <div class="col-3 timestamp" :class="{ 'order-1': sent, 'order-2': !sent }">
      <timeago :datetime="message.timestamp" :autoUpdate="true" />
    </div>
  </div>
</template>

<script>
export default {
  name: "MessageComponent",
  props: {
    sent: {
      type: Boolean,
      required: false,
      default: false,
    },
    username: {
      type: String,
      required: false,
    },
    message: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
#single-message {
  padding: calc(var(--bs-gutter-x) * 0.5);
}
#single-message .message-card {
  padding: 0.5rem 1rem;
  background-color: rgba(0, 218, 11, 0.5);
  border-radius: 2rem;
  line-height: 1.2rem;
}
#single-message .timestamp {
  font-size: 0.7rem;
}
#single-message .sender-name {
  font-size: 0.7rem;
  line-height: 0.5rem;
  color: #515151;
  letter-spacing: 0.3px;
}
#single-message.sent .message-card {
  text-align: right;
  background-color: rgba(255, 161, 60, 0.5);
}
#single-message.sent .timestamp {
  text-align: right;
}
</style>
