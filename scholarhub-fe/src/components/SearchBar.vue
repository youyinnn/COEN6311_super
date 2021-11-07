<template>
  <div id="searchBar" class="clearfix search-form">
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
          'class-loading-dense': denseData,
          'class-loading': !denseData,
          'fill-height': true,
        }"
      ></v-progress-circular>
    </v-form>
  </div>
</template>

<script>
const axios = require("axios").default;

export default {
  props: ["dense", "loading", "justGo"],
  data: () => ({
    searchLabel: "Search Paper",
    valid: false,
    classForShowLoading: false,
    searchTerm: "",
  }),
  methods: {
    submitSearch(e) {
      if (e !== undefined) {
        e.preventDefault();
      }
      const sT = this.searchTerm;
      if (sT === "" || sT.length === 0) {
        return;
      }
      if (this.$props.justGo !== undefined) {
        return;
      }
      this.showLoading();
      this.searchTerm = "";
      const url = this.config.paperSearchUrl;
      const thiz = this;
      axios
        .get(url, {
          params: {
            query: sT,
            fields:
              "url,title,authors,abstract,venue,year,referenceCount,isOpenAccess,fieldsOfStudy",
          },
        })
        .then(function (response) {
          console.log(response);
          //   console.log(thiz.vueMap);
          thiz.hideLoading();
          thiz.vueMap.get("paperSearchResult").showResult(sT, response.data);
          if (window.location.hash !== "#/papers") {
            thiz.$router
              .push({
                path: `/papers`,
                query: {
                  query: sT,
                },
              })
              .catch(() => {});
          }
        })
        .catch(function (error) {
          console.log(error);
        })
        .then(function () {
          // 总是会执行
        });
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
  computed: {
    denseData: function () {
      return this.$props.dense !== undefined;
    },
  },
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
.class-loading-dense {
  height: 40px !important;
  width: 40px !important;
  transform: translateX(-64px) scale(0.5);
  position: absolute;
}
.class-loading {
  height: 57px !important;
  width: 40px !important;
  transform: translateX(-64px) scale(0.7);
  position: absolute;
}
</style>
