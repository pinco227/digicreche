import { createStore } from "vuex";
import { apiService } from "@/common/api.service.js";

export const store = createStore({
  state() {
    return {
      conversations: [],
      messages: {
        results: [],
        count: 0,
        next: null,
      },
      activeChat: null,
    };
  },
  mutations: {
    SET_ACTIVE_CHAT(state, chatId) {
      state.activeChat = chatId;
    },
    SET_CONVERSATIONS(state, conversations) {
      state.conversations = conversations;
    },
    SET_MESSAGES(state, messages) {
      state.messages = messages;
      state.messages.results = state.messages.results.reverse();
    },
    ADD_MESSAGES(state, messages) {
      state.messages.results = [
        ...messages.results.reverse(),
        ...state.messages.results,
      ];
      state.messages.next = messages.next;
    },
  },
  actions: {
    async loadConversations(context) {
      const endpoint = "/api/chats/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        context.commit("SET_CONVERSATIONS", data.body);
      } else {
        // TODO: error handling
      }
    },
    async loadMessages(context, { chat_id, next }) {
      let endpoint = `/api/chats/${chat_id}/`;
      if (next) endpoint = context.state.messages.next;

      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        if (next) {
          context.commit("ADD_MESSAGES", data.body);
        } else {
          context.commit("SET_MESSAGES", data.body);
        }
      } else {
        // TODO: error handling
      }
    },
    loadMore(context) {
      context.dispatch("loadMessages", {
        chat_id: context.state.activeChat,
        next: true,
      });
    },
    selectChat(context, chat_id) {
      context.commit("SET_ACTIVE_CHAT", chat_id);
      context.dispatch("loadMessages", { chat_id: chat_id });
    },
  },
});
