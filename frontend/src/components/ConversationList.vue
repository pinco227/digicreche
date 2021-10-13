<template>
  <div
    class="col-12"
    :class="{
      'col-md-5 col-lg-6 d-none d-md-block': activeChat,
    }"
  >
    <h2>Chats</h2>
    <div class="list-group">
      <button
        class="list-group-item list-group-item-action"
        v-for="chat in conversations"
        :key="chat.id"
        :class="{ active: activeChat == chat.id }"
        @click="setChat(chat.id)"
      >
        <span :class="{ 'fw-bolder': chat.unread }">{{ chat.name }}</span>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  name: "ConversationList",
  computed: mapState(["conversations", "activeChat"]),
  methods: {
    ...mapActions(["loadConversations", "selectChat"]),
    setChat(id) {
      this.selectChat(id);
      this.$router.push({ name: "chat", params: { chatId: id } });
    },
  },
  created() {
    this.loadConversations();
  },
};
</script>
