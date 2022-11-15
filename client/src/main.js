import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "bootstrap/dist/css/bootstrap.css";
import boostrap from "bootstrap/dist/js/bootstrap.bundle.js";
const app = createApp(App);

app.use(router);
app.use(boostrap);
app.mount("#app");
