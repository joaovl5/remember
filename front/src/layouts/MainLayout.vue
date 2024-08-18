<template>
  <div class="layout-container">
    <div class="side-bar">
      <router-link to="/" class="no-link">
        <q-btn size="16px" dense flat round icon="sym_o_search" />
      </router-link>
      <q-btn size="16px" dense flat round icon="sym_o_attach_file" />
      <router-link to="/snapshots" class="no-link">
        <q-btn size="16px" dense flat round icon="sym_o_photo_camera" />
      </router-link>
    </div>
    <div class="content-container">
      <div class="header">
        <div></div>
        <div class="row items-center snapshot-container">
          <p class="last-snapshot-label">Last snapshot 20s ago</p>
          <RecordToggle />
        </div>
      </div>
      <router-view />
    </div>
  </div>
</template>

<script setup>
import RecordToggle from "src/components/RecordToggle.vue";
</script>

<style lang="css" scoped>
.layout-container {
  display: flex;
  width: 100vw;
  height: 100vh;
}

.no-link {
  color: inherit;
  text-decoration: none;
}

.side-bar {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  gap: 5px;

  padding: 5px;

  width: 55px;
  height: 100%;
  border: 1px solid #ddd;
  color: #1d1b20;
}

.content-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;

  width: 100%;
  height: 50px;
  border-bottom: 1px solid #ddd;
  padding: 15px;
}

.header p {
  margin: 0;
}

.snapshot-container {
  gap: 15px;
}

.last-snapshot-label {
  font-weight: 500;
  color: #757575;
}
</style>
