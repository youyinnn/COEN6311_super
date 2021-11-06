<template>
  <v-container class="home" fill-height>
    <v-form
      ref="form"
      class="searchForm d-flex align-center"
      @submit="submitSearch"
    >
      <div class="manLogo mr-8">
        <v-img max-width="200" src="@/assets/img/man.png"></v-img>
      </div>
      <div>
        <div class="slogan mb-4">
          Scholar <span class="teal--text">H</span
          ><span class="red--text">u</span><span class="orange--text">b</span>
        </div>
        <div class="d-flex align-center">
          <v-text-field
            :label="searchLabel"
            color="teal"
            class="searchTextField mr-4"
            v-model="searchTerm"
            outlined
            hide-details="auto"
          ></v-text-field>
          <v-progress-circular
            indeterminate
            color="green"
            style="opacity: 0; transition: all 1s"
            :class="{ enterSearch: enterSearch }"
          ></v-progress-circular>
        </div>
      </div>
    </v-form>
  </v-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  props: ["msg"],
  data: () => ({
    searchLabel: "Search Paper",
    valid: false,
    enterSearch: false,
    searchTerm: "",
  }),
  methods: {
    submitSearch(e) {
      e.preventDefault();
      console.log(this.searchTerm);
      this.enterSearch = true;
    },
  },
};
</script>

<style scoped>
.home {
  height: 100%;
}
.manLogo {
  float: left;
  width: 200px;
  height: 200px;
}
.searchTextField {
  float: left;
  width: 30em;
  margin: auto;
  left: 0;
  right: 0;
}
.searchForm {
  margin: auto;
  height: 200px;
  position: relative;
  top: -3em;
}
.enterSearch {
  opacity: 1 !important;
}
.slogan {
  font-size: 40px;
}
</style>
