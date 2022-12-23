<template>
  <main>
    <div class="container">
      <button @click="setResourceTab('StoredResources')">
        Stored Resources
      </button>
      <button @click="setResourceTab('AddResource')">Add Resources</button>
    </div>
  </main>
  <component :is="tabs[state.selectedTab]" />
</template>

<script setup lang="ts">
import { reactive } from "vue";
import AddResource from "./AddResources.vue";
import StoredResources from "./StoredResources.vue";

const tabs = {
  AddResource,
  StoredResources,
};

const state = reactive({ selectedTab: "StoredResources" });

let setResourceTab = (tab: string): void => {
  state.selectedTab = tab;
};
</script>
