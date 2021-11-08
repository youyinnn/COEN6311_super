<template>
  <div id="paper-detail-box" class="paper-detail-box">details</div>
</template>

<script>
const axios = require("axios").default;

export default {
  data: () => ({}),
  methods: {
    getDetail(id) {
      console.log(id);
      const thiz = this;
      axios
        .get(`${thiz.config.paperDetailUrl}/${id}`)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
          thiz.errorToast("Search API went wrong!");
        })
        .then(function () {});
    },
  },
  beforeRouteEnter(to, from, next) {
    // console.log(to);
    // console.log(from);
    // console.log(next);
    next((ins) => {
      ins.getDetail(to.params.id);
    });
  },
};
</script>

<style scoped></style>
