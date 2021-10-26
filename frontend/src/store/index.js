import { createStore } from "vuex";
import { apiService } from "@/common/api.service.js";

export const store = createStore({
  state() {
    return {
      conversations: [],
      messages: {
        results: [],
        next: null,
      },
      activeChat: null,
      log: [],
    };
  },
  mutations: {
    SET_ACTIVE_CHAT(state, chatId) {
      state.activeChat = chatId;
    },
    UNSET_ACTIVE_CHAT(state) {
      state.activeChat = null;
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
    SEND_MESSAGE(state, message) {
      state.messages.results.push(message);
    },

    // Websocket implementation
    // CREDIT: https://github.com/aogz/django-vue-websocket-chat
    SOCKET_ONOPEN(state, event) {
      console.info("Connected to websockets server.. ");
      state.log.push(event);
    },
    SOCKET_ONCLOSE(state, event) {
      console.info("Websocket connection closed.");
      state.log.push(event);
    },
    SOCKET_ONERROR(state, event) {
      console.error("Error: ", event);
      state.log.push(event);
    },
    SOCKET_ONMESSAGE(state, message) {
      if (
        state.activeChat === message.sender ||
        state.activeChat === message.receiver
      ) {
        state.messages.results.push(message);
      } else {
        for (var i = 0; i < state.conversations.length; i++) {
          if (state.conversations[i].id === message.sender) {
            state.conversations[i].unread = true;
          }
        }
      }
    },
    // mutations for reconnect methods
    SOCKET_RECONNECT(state, count) {
      console.info("Reconnect: ", count);
      state.log.push({ reconnect: count });
    },
    SOCKET_RECONNECT_ERROR(state, event) {
      console.error("Reconnecting error.");
      state.log.push(event);
    },
  },
  actions: {
    async loadConversations(context) {
      // Fetches conversation list from API and commits to state
      const endpoint = "/api/chats/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        context.commit("SET_CONVERSATIONS", data.body);
      }
    },
    async loadMessages(context, { chat_id, next }) {
      // Fetches messages of active conversation from API and commits to state
      let endpoint = `/api/chats/${chat_id}/`;
      if (next) {
        const host = window.location.host;
        const split_path = context.state.messages.next.split(host);
        endpoint = split_path[split_path.length - 1];
      }

      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        if (next) {
          context.commit("ADD_MESSAGES", data.body);
        } else {
          context.commit("SET_MESSAGES", data.body);
        }
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
      context.dispatch("loadConversations");
    },
    clearChat(context) {
      context.commit("UNSET_ACTIVE_CHAT");
    },
  },
});
