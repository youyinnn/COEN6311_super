<template>
  <v-app>
    <v-app-bar app dense color="primary" elevation="3">
      <div class="d-flex align-center">
        <v-chip class="ma-2 unselectable" color="cyan" label text-color="white">
          <v-img
            max-height="20"
            max-width="20"
            src="../src/assets/img/graduation-cap.png"
          ></v-img>
        </v-chip>
      </div>

      <v-spacer></v-spacer>

      <v-btn v-if="isLogin" small raised color="teal">
        <span class="mr-2">Sign Out</span>
        <v-icon>mdi-logout-variant</v-icon>
      </v-btn>
      <div v-else>
        <v-btn small raised color="teal" class="mr-4">
          <span class="mr-2 white--text">Sign Up</span>
          <v-icon>mdi-login-variant</v-icon>
        </v-btn>
        <v-btn small raised color="teal">
          <span class="mr-2 white--text">Sign In</span>
          <v-icon>mdi-login-variant</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer padless height="30" class="d-flex align-center justify-center">
      <div style="font-size: 15px">
        <strong>FALL2021 - Concordia University - COEN6311 Group Super</strong>
      </div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    isLogin: false,
  }),
};
</script>

<style scoped>
@import "../src/assets/css/index.less";
</style>
