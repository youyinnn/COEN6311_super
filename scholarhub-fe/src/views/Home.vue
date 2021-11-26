<template>
  <v-container id="home" class="home" fill-height>
    <div class="home-box d-flex align-center">
      <div class="man-logo mr-8">
        <v-img max-width="200" src="@/assets/img/man.png"></v-img>
      </div>
      <div style="float: left">
        <div class="unselectable slogan mb-4 text-h2 overline">
          Scholar <span class="teal--text">H</span
          ><span class="red--text">u</span><span class="orange--text">b</span>
        </div>
        <div>
          <SearchBar just-go loading></SearchBar>
        </div>
      </div>
    </div>
    <Footer abs />
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
  transform: translateY(-4em);
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
