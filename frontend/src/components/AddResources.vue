<template>
  <div>Add Resources</div>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">Title</label>
      <input id="title" type="text" ref="titleInput" />
    </div>
    <div>
      <label for="description">Description</label>
      <textarea id="description" rows="3" ref="descInput"></textarea>
    </div>
    <div>
      <label for="link">Link</label>
      <input id="link" type="url" ref="linkInput" />
    </div>
    <div>
      <button type="submit">Add Resource</button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

const titleInput = ref<HTMLInputElement | null>(null);
const descInput = ref<HTMLInputElement | null>(null);
const linkInput = ref<HTMLInputElement | null>(null);

let onSubmit = () => {
  console.dir(titleInput.value?.value);
  console.dir(descInput.value?.value);
  console.dir(linkInput.value?.value);
};
</script>
