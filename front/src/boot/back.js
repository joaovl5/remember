import { boot } from "quasar/wrappers";

const api = window.pywebview.api;

const backService = {
  async search(query) {
    return await api.global_search(query);
  },
  getScreenshot(screenshot_path) {
    return new Promise((resolve) => {
      api
        .get_screenshot_image(screenshot_path)
        .then((res) => {
          resolve(res);
        })
        .catch((err) => {});
    });
  },
};

export default boot(({ app }) => {
  app.config.globalProperties.$back = backService;
});

export { backService };
