<template>
  <v-app id="app" class="app">
    <TopBar />

    <v-main>
      <!-- <transition name="fade">
        <router-view></router-view>
      </transition> -->
      <transition name="slide-fade" mode="out-in">
        <!-- <keep-alive> -->
        <router-view></router-view>
        <!-- </keep-alive> -->
      </transition>
    </v-main>
    <LoginBox padless></LoginBox>
  </v-app>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import LoginBox from "@/components/LoginBox.vue";

export default {
  name: "App",
  components: {
    TopBar,
    LoginBox,
  },
  data: () => ({}),
};
</script>

<style>
@import "../src/assets/css/index.less";
app {
  overflow-x: scroll;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  /* right: -10%; */
  transform: translateX(-10px);
  opacity: 0;
}

.slide-r-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-r-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-r-fade-enter, .slide-r-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  /* right: -10%; */
  transform: translateX(10px);
  opacity: 0;
}

.small-slide-r-fade-enter-active {
  transition: all 0.3s ease;
}
.small-slide-r-fade-leave-active {
  transition: all 0.3s ease;
}
.small-slide-r-fade-enter, .small-slide-r-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  /* right: -10%; */
  transform: translateX(3px);
  opacity: 0;
}

.v-main {
  padding: 0 !important;
}
</style>
