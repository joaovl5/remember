<template>
  <div class="suggestion-card" @click="handleSuggestion">{{ props.text }}</div>
</template>

<script setup>
import { defineProps } from "vue";
import { useSearchStore } from "src/stores/search";

const props = defineProps(["text"]);
const searchStore = useSearchStore();

const handleSuggestion = () => {
  searchStore.text = props.text;
  searchStore.handleSearch();
};
</script>

<style scoped>
.suggestion-card {
  border: 1px solid #b2b2b2;
  border-radius: 10px;
  padding: 5px 12px;
  font-weight: 500;
  box-shadow: 1px 2px 10px 0px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
</style>
