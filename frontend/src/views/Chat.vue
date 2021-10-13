<template>
  <section id="chat">
    <div class="row">
      <ConversationList />
      <ConversationComponent />
    </div>
  </section>
</template>

<script>
import { mapActions, mapState } from "vuex";
import ConversationComponent from "@/components/Conversation.vue";
import ConversationList from "@/components/ConversationList.vue";

export default {
  name: "Chat",
  props: {
    chatId: {
      type: Number,
      required: false,
    },
  },
  components: {
    ConversationList,
    ConversationComponent,
  },
  data() {
    return {
      messages: [],
      newMessage: null,
      next: null,
    };
  },
  computed: mapState(["activeChat"]),
  methods: mapActions(["selectChat"]),
  created() {
    if (this.chatId) {
      this.selectChat(this.chatId);
    }
  },
};
</script>

<style scoped>
.chat-view {
  overflow-x: hidden;
  overflow-y: scroll;
  padding-bottom: 4.5rem;
  height: calc(100vh - 67px);
  background-color: #f6f6f6;
}
</style>
