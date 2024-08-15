import { defineStore } from "pinia";
import { backService } from "src/boot/back";

export const useSearchStore = defineStore("search", {
  state: () => ({
    text: "",
    searchResult: {
      shown: false,
      loading: false,
      data: {
        success: false,
        snapshot: {
          timestamp: 0,
          description: "",
          screenshot_path: "",
        },
        summary: "",
      },
      screenshot: "",
    },
  }),
  actions: {
    handleSearch() {
      this.searchResult.shown = true;
      this.searchResult.loading = true;
      return new Promise((resolve) => {
        backService.search(this.text).then((res) => {
          this.searchResult.data = res;
          this.getScreenshot()
            .then((b64) => {
              this.searchResult.screenshot = b64;
            })
            .finally(() => {
              this.searchResult.loading = false;
              resolve();
            });
        });
      });
    },

    getScreenshot() {
      return new Promise((resolve) => {
        backService
          .getScreenshot(this.searchResult.data.snapshot.screenshot_path)
          .then((res) => {
            resolve(res);
          });
      });
    },
  },
});
