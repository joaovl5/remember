<template>
  <div class="page-container">
    <GlobalSearch />
    <div class="transition-container">
      <transition-fade>
        <SearchResultBox
          v-if="searchStore.searchResult.shown"
          class="transition-item"
        />
        <SearchSuggestionBox v-else class="transition-item" />
      </transition-fade>
    </div>
  </div>
</template>

<script setup>
import GlobalSearch from "src/components/GlobalSearch.vue";
import SearchResultBox from "src/components/SearchResultBox.vue";
import SearchSuggestionBox from "src/components/SearchSuggestionBox.vue";
import { TransitionFade } from "@morev/vue-transitions";

import { useSearchStore } from "src/stores/search";

const searchStore = useSearchStore();
</script>

<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding-top: 30px;
}

.transition-container {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  justify-items: center;
}

.transition-item {
  grid-column: 1;
  grid-row: 1;

  position: relative;
  height: fit-content;
  /* position: relative; */
  /* top: 0; */
  /* left: 0; */
}
</style>
