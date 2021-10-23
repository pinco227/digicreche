<template>
  <section id="chat">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div class="col-6 text-end">
        <button
          v-if="activeChat"
          type="button"
          class="btn btn-secondary d-inline-block d-md-none"
          @click.prevent="unsetChat"
        >
          <i class="fas fa-list"></i>
        </button>
      </div>
    </div>
    <div class="row">
      <ConversationList />
      <ConversationComponent />
    </div>
  </section>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { setPageTitle } from "@/common/functions.js";
import ConversationComponent from "@/components/Conversation.vue";
import ConversationList from "@/components/ConversationList.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "Chat",
  props: {
    chatId: {
      type: Number,
      required: false,
    },
  },
  computed: mapState(["activeChat"]),
  components: {
    ConversationList,
    ConversationComponent,
    GoBackComponent,
  },
  data() {
    return {
      messages: [],
      newMessage: null,
      next: null,
    };
  },
  methods: {
    ...mapActions(["clearChat", "selectChat"]),
    unsetChat() {
      this.clearChat();
      this.$router.push({ name: "chat" });
    },
  },
  created() {
    if (this.chatId) {
      this.selectChat(this.chatId);
    }
    setPageTitle("Chat");
  },
};
</script>
