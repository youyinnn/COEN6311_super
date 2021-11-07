<template>
  <v-app id="app" class="app">
    <TopBar v-bind:isLogin="isLogin" />

    <v-main>
      <!-- <transition name="fade">
        <router-view></router-view>
      </transition> -->
      <transition name="slide-fade" mode="out-in">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </v-main>
    <v-footer padless height="30" class="d-flex align-center justify-center">
      <div style="font-size: 15px">
        <strong>FALL2021 - Concordia University - COEN6311 Group Super</strong>
      </div>
    </v-footer>
    <LoginBox></LoginBox>
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
  data: () => ({
    isLogin: false,
  }),
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
  transform: translateX(-10px);
  opacity: 0;
}
</style>
