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
      path: "/book/:id",
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
    {
      path: "/my-borrowings",
      name: "my-borrowings",
      component: () => import("../views/MyBorrowings.vue"),
    },
  ],
});

router.beforeEach((to, from) => {
  const userStore = useUserStore();
  const isAuthenticated = computed(() => userStore.user.isAuthenticated);
  const isSuperUser = computed(() => userStore.user.is_superuser);
  if (!isAuthenticated.value && to.name !== "login" && to.name !== "register") {
    // redirect the user to the login page
    return { name: "login" };
  }
  if (isAuthenticated.value && (to.name == "login" || to.name == "register")) {
    return { name: "home" };
  }
  if (
    isAuthenticated.value &&
    isSuperUser.value === false &&
    (to.name == "admin" || to.name == "register")
  ) {
    return { name: "home" };
  }
});
export default router;
