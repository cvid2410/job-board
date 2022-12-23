<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    default: "",
  },
});
</script>

<template>
  <header>
    <h1>{{ props.title }}</h1>
  </header>
</template>
