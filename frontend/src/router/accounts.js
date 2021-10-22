import Account from "@/views/Account.vue";
import Subscriptions from "@/views/Subscriptions.vue";

const AccountRoutes = [
  {
    path: "/account",
    name: "user_account",
    component: Account,
  },
  {
    path: "/subscriptions",
    name: "subscription-list",
    component: Subscriptions,
  },
];

export default AccountRoutes;
