<template>
  <v-container fill-height>
    <v-form class="searchForm d-flex align-center">
      <v-img
        max-width="200"
        src="@/assets/img/man.png"
        class="manLogo mr-8"
      ></v-img>
      <v-text-field
        label="Search your paper"
        color="teal"
        class="searchTextField"
        outlined
      ></v-text-field>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["msg"],
  data: () => ({
    valid: false,
  }),
};
</script>

<style scoped>
.manLogo {
  float: left;
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
}
</style>
