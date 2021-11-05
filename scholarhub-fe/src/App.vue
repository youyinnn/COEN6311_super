<template>
  <v-app>
    <v-app-bar app dense color="primary" elevation="3" dark>
      <div class="d-flex align-center">
        <v-chip class="ma-2 unselectable" color="cyan" label text-color="white">
          <v-img
            max-height="20"
            max-width="20"
            src="../src/assets/img/graduation-cap.png"
            class="mr-2"
          ></v-img>
          Scholar HUB
        </v-chip>
      </div>

      <v-spacer></v-spacer>

      <v-btn v-if="isLogin" small raised color="teal">
        <span class="mr-2">logout</span>
        <v-icon>mdi-logout-variant</v-icon>
      </v-btn>
      <v-btn v-else small raised color="teal">
        <span class="mr-2">Login</span>
        <v-icon>mdi-login-variant</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-footer padless height="30" class="d-flex align-center justify-center">
      <div style="font-size: 15px">
        FALL2021 - <strong>CONCORDIA UNIVERSITY</strong> -
        <strong>COEN6311 Group Super</strong>
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
