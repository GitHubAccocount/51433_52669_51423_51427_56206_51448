import axios from "axios";
import { ref } from "vue";

const token = ref(localStorage.getItem("user.access") || "");

axios.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;
