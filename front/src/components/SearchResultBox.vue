<template>
  <div class="result-box">
    <q-btn
      dense
      round
      flat
      icon="sym_o_close"
      class="close-button"
      @click="handleClose"
    />
    <div v-if="searchStore.searchResult.loading" class="error-box">
      <q-spinner-grid color="" size="2em" />
    </div>
    <div v-else>
      <div v-if="searchStore.searchResult.data.success" class="success-box">
        <p class="summary">{{ searchStore.searchResult.data.summary }}</p>
        <div class="screenshot-container">
          <q-img :src="resultScreenshot" />
        </div>
      </div>
      <div v-else class="error-box">
        <p class="error-title">
          <q-icon
            name="sym_o_sentiment_very_dissatisfied"
            style="margin-right: 5px"
          /><span>No results</span>
        </p>
        <p class="error-description">
          We couldn't find an accurate result for what you're looking for.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useSearchStore } from "src/stores/search";
import { computed } from "vue";
const searchStore = useSearchStore();

const resultScreenshot = computed(() => {
  return "data:image/png;base64," + searchStore.searchResult.screenshot;
});

const handleClose = () => {
  searchStore.searchResult.shown = false;
};
</script>

<style scoped>
.result-box {
  border: 1px solid #d9d9d9;
  border-radius: 10px;
  padding: 15px;
  position: relative;

  width: max(20%, 700px);
  box-shadow: 1px 2px 8px 0px rgba(0, 0, 0, 0.15);
}

.success-box {
  display: flex;
  margin-right: 20px;
  gap: 12px;
}

.screenshot-container {
  flex: 1;
}

.error-box {
  display: flex;
  align-items: center;
  flex-direction: column;
  font-size: 1.25em;
  font-weight: 500;
}

.summary {
  font-size: 1.15em;
  font-weight: 500;
  flex: 2;
}

.close-button {
  position: absolute;
  top: 5px;
  right: 5px;
  font-size: 0.9em;
}

.error-box {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100%;
}

.error-title {
  color: #db3434;
}

.error-description {
  color: #333;
  font-size: 0.9em;
}

.error-box p {
  margin: 0;
}
</style>
