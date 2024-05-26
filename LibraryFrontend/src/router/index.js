import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { useUserStore } from "@/stores/user";
import { computed } from "vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/RegisterView.vue"),
    },
    {
      path: "/search",
      name: "search",
      component: () => import("../views/SearchView.vue"),
    },
    {
      path: "/book",
      name: "book",
      component: () => import("../views/BookView.vue"),
    },
    {
      path: "/bookEdit",
      name: "bookEdit",
      component: () => import("../views/BookEditView.vue"),
    },
    {
      path: "/bookAdd",
      name: "bookAdd",
      component: () => import("../views/BookAddView.vue"),
    },
    {
      path: "/user",
      name: "user",
      component: () => import("../views/UserView.vue"),
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("../views/AdminView.vue"),
    },
    {
      path: "/adminBooks",
      name: "adminBooks",
      component: () => import("../views/AdminBooksView.vue"),
    },
    {
      path: "/adminUsers",
      name: "adminUsers",
      component: () => import("../views/AdminUsersView.vue"),
    },
    {
      path: "/reservationList",
      name: "reservationList",
      component: () => import("../views/ReservationListView.vue"),
    },
  ],
});

router.beforeEach((to, from) => {
  const userStore = useUserStore();
  const isAuthenticated = computed(() => userStore.user.isAuthenticated);
  if (
    // make sure the user is authenticated
    !isAuthenticated.value &&
    // ❗️ Avoid an infinite redirect
    to.name !== "login" &&
    to.name !== "register" &&
    to.name !== "search" &&
    to.name !== "book" &&
    to.name !== "bookEdit" &&
    to.name !== "bookAdd" &&
    to.name !== "home" &&
    to.name !== "user" &&
    to.name !== "admin" &&
    to.name !== "adminBooks" &&
    to.name !== "adminUsers" &&
    to.name !== "reservationList"
  ) {
    // redirect the user to the login page
    return { name: "login" };
  }
  if (isAuthenticated.value && (to.name == "login" || to.name == "register")) {
    return { name: "home" };
  }
});
export default router;
