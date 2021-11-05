<template>
  <div class="home">
    <SearchPage msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchPage from "@/components/SearchPage.vue";

export default {
  name: "Home",
  components: {
    SearchPage,
  },
};
</script>

<style scoped>
.home {
  height: 100%;
}
</style>
