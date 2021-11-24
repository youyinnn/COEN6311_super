import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/Register.vue"),
  },
  {
    path: "/papers",
    name: "Papers",
    component: () => import("@/views/PaperSearchResult.vue"),
  },
  {
    path: "/paper/:paperTitle/:id",
    name: "Paper",
    component: () => import("@/views/PaperDetail.vue"),
  },
  {
    path: "/user-info",
    name: "UserInfo",
    component: () => import("@/views/UserInfo.vue"),
  },
  {
    path: "/team",
    name: "TeamPage",
    component: () => import("@/views/TeamPage.vue"),
  },
  {
    path: "*",
    name: "PageNotFound",
    component: () => import("@/views/PageNotFound.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
