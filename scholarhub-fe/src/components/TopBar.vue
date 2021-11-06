<template>
  <v-app-bar app dense color="primary" elevation="3" hide-on-scroll>
    <v-btn small raised color="teal" @click="goHome">
      <v-img
        max-height="20"
        max-width="20"
        src="@/assets/img/graduation-cap.png"
      ></v-img>
      <span class="mr-2 white--text">Home</span>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn v-if="isLogin" small raised color="teal">
      <span class="mr-2">Sign Out</span>
      <v-icon>mdi-logout-variant</v-icon>
    </v-btn>
    <div v-else>
      <v-btn small raised color="teal" class="mr-4" @click="goSignUp">
        <span class="mr-2 white--text">Sign Up</span>
        <v-icon color="white">mdi-clipboard-account</v-icon>
      </v-btn>
      <v-btn small raised color="teal">
        <span class="mr-2 white--text">Sign In</span>
        <v-icon color="white">mdi-login-variant</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  props: ["isLogin"],
  setup() {},
  methods: {
    goSignUp() {
      this.$router.push("/register").catch(() => {});
    },
    goHome() {
      this.$router.push("/").catch(() => {});
    },
  },
};
</script>
