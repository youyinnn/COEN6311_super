<template>
  <div class="clearfix search-form">
    <v-form ref="form" class="" @submit="submitSearch">
      <v-text-field
        :label="searchLabel"
        color="teal"
        class="search-text-field"
        v-model="searchTerm"
        outlined
        hide-details="auto"
        :dense="dense"
      ></v-text-field>
      <!-- v-show="hasLoading" -->
      <v-progress-circular
        v-if="this.$props.loading !== undefined"
        indeterminate
        color="green"
        style="opacity: 0; transition: all 1s"
        :class="{
          'class-show-loading': classForShowLoading,
          'ml-4': true,
          'class-loading': true,
          'fill-height': true,
        }"
      ></v-progress-circular>
    </v-form>
  </div>
</template>

<script>
export default {
  props: ["dense", "loading"],
  data: () => ({
    searchLabel: "Search Paper",
    valid: false,
    classForShowLoading: false,
    searchTerm: "",
  }),
  methods: {
    submitSearch(e) {
      e.preventDefault();
      console.log(this.searchTerm);
      this.$router.push("/papers").catch(() => {});
      this.showLoading();
      setTimeout(() => {
        this.hideLoading();
      }, 3000);
    },
    showLoading() {
      if (this.$props.loading !== undefined) {
        this.classForShowLoading = true;
      }
    },
    hideLoading() {
      this.classForShowLoading = false;
    },
  },
  computed: {},
};
</script>

<style scoped>
.search-form {
  width: 480px;
  margin: auto;
}
.search-text-field {
  float: left;
  width: 30em;
  margin: auto;
  left: 0;
  right: 0;
}
.class-show-loading {
  opacity: 1 !important;
}
.class-loading {
  height: 40px !important;
  width: 40px !important;
  transform: translateX(-64px) scale(0.5);
  position: absolute;
}
</style>
