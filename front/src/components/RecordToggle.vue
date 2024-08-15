<template>
  <q-btn
    class="button"
    no-caps
    unelevated
    :color="state ? 'positive' : 'negative'"
    @click="handleClick"
    ><div class="row items-center no-wrap button-state-container">
      <transition name="slide-up">
        <div v-if="state" class="button-state">
          <q-icon class="icon" left name="sym_o_check" />
          <span>Recording</span>
        </div>
        <div v-else class="button-state">
          <q-icon class="icon" left name="sym_o_close" />
          <span>Stopped</span>
        </div>
      </transition>
    </div>
  </q-btn>
</template>

<script setup>
import { ref } from "vue";

const state = ref(true);

const handleClick = () => {
  state.value = !state.value;
};
</script>

<style scoped>
.button {
  transition: all 0.2s cubic-bezier(0.445, 0.05, 0.55, 0.95);
  border-radius: 10px;
  height: 1em;
  width: 110px;
}

.button-state-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button-state {
  position: absolute;
  display: flex;
  align-items: center;
}

.icon {
  margin: 0;
  font-size: 1.6em;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.25s ease-out;
}

.slide-up-enter-from {
  opacity: 0;
  transform: translateY(30px);
}

.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

span {
  font-size: 1.2em;
}
</style>
