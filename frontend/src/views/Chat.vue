<template>
  <section id="chat">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
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
  computed: mapState(["activeChat"]),
  methods: mapActions(["selectChat"]),
  created() {
    if (this.chatId) {
      this.selectChat(this.chatId);
    }
    setPageTitle("Chat");
  },
};
</script>