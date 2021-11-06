<template>
  <v-container class="home" fill-height>
    <div class="home-box">
      <div class="man-logo mr-8">
        <v-img max-width="200" src="@/assets/img/man.png"></v-img>
      </div>
      <div style="float: left">
        <div class="slogan mb-4">
          Scholar <span class="teal--text">H</span
          ><span class="red--text">u</span><span class="orange--text">b</span>
        </div>
        <div>
          <SearchBar></SearchBar>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "Home",
  props: ["msg"],
  data: () => ({}),
  methods: {},
  components: {
    SearchBar,
  },
};
</script>

<style scoped>
.home {
  height: 100%;
}
.home-box {
  margin: auto;
  position: relative;
  top: -2em;
}
.man-logo {
  float: left;
  width: 200px;
  height: 200px;
}

.slogan {
  font-size: 40px;
}
</style>
