import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Estagiarios from "../views/Estagiarios.vue";
import Setores from "../views/Setores.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/estagiarios",
      name: "estagiarios",
      component: Estagiarios,
    },
    {
      path: "/setores",
      name: "setores",
      component: Setores,
    },
  ],
});

export default router;
