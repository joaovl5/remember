<template>
  <div class="suggestion-container">
    <SearchSuggestion text="What time is my meeting?" />
    <SearchSuggestion text="Today’s highlights" />
    <SearchSuggestion text="Summarize my Python links" />
  </div>
</template>

<script setup>
import SearchSuggestion from "./SearchSuggestion.vue";
</script>

<style scoped>
.suggestion-container {
  display: flex;
  gap: 10px;
}
</style>
