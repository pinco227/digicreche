<template>
  <section id="conversation-list">
    <h2>Chats</h2>
    <div class="list-group">
      <button
        class="list-group-item list-group-item-action"
        v-for="chat in conversations"
        :key="chat.id"
        :class="{ active: activeChat == chat.id }"
        @click="selectChat(chat.id)"
      >
        <span :class="{ 'fw-bolder': chat.unread }">{{ chat.name }}</span>
      </button>
    </div>
  </section>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  name: "ConversationList",
  created() {
    this.loadConversations();
  },
  computed: mapState(["conversations", "activeChat"]),
  methods: mapActions(["loadConversations", "selectChat"]),
};
</script>
