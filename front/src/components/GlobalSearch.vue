<template>
  <div class="search-input">
    <q-input
      borderless
      label-slot
      size="1.5px"
      hide-bottom-space
      input-class="search-input-inner"
      v-model="searchStore.text"
      @keydown.enter="handleSearch"
    >
      <template v-slot:label>
        <span class="search-label">Ask anything...</span>
      </template>
      <template v-slot:append>
        <q-icon @click="handleSearch" name="sym_o_search" class="search-icon" />
      </template>
    </q-input>
  </div>
</template>

<script setup>
import { useSearchStore } from "src/stores/search";

const searchStore = useSearchStore();

const handleSearch = async () => {
  searchStore.handleSearch();
};
</script>

<style>
.search-input {
  border: 1px solid #d9d9d9;
  border-radius: 17px;

  padding: 5px 10px;
  width: max(20%, 500px);
  height: 75px;
  box-shadow: 1px 2px 8px 0px rgba(0, 0, 0, 0.15);
}

.search-label,
.search-icon {
  color: #1e1e1e;
  font-size: 1.4em;
  font-weight: 500;
  margin-right: 5px;
  cursor: pointer;
}

.search-input-inner {
  color: #1e1e1e;
  font-weight: 500;
  font-size: 1.5em;
}
</style>
