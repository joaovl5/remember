import { boot } from "quasar/wrappers";
import { plugin as vueTransitionsPlugin } from "@morev/vue-transitions";
import "@morev/vue-transitions/styles";

export default boot(({ app }) => {
  app.use(vueTransitionsPlugin, {
    // Plugin options (optional, described below)
  });
});
