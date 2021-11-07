<template>
  <v-app-bar
    class="top-bar"
    id="topBar"
    app
    dense
    color="primary"
    elevation="3"
    hide-on-scroll
  >
    <!-- <transition-group> -->
    <v-btn key="go-home-btn" small raised color="teal" @click="goHome">
      <v-img
        max-height="20"
        max-width="20"
        src="@/assets/img/graduation-cap.png"
      ></v-img>
      <span class="mr-2 white--text">Home</span>
    </v-btn>

    <v-spacer key="spacer"></v-spacer>

    <transition name="fade" mode="out-in">
      <v-btn
        key="sign-out-btn"
        v-if="isLogin"
        small
        raised
        color="teal"
        @click="signOut"
      >
        <span class="mr-2 white--text">Sign Out</span>
        <v-icon color="white">mdi-logout-variant</v-icon>
      </v-btn>
      <div key="sign-up-in-btns" v-else>
        <v-btn small raised color="teal" class="mr-4" @click="goSignUp">
          <span class="mr-2 white--text">Sign Up</span>
          <v-icon color="white">mdi-clipboard-account</v-icon>
        </v-btn>
        <v-btn small raised color="teal" @click="showLoginBox">
          <span class="mr-2 white--text">Sign In</span>
          <v-icon color="white">mdi-login-variant</v-icon>
        </v-btn>
      </div>
    </transition>
    <!-- </transition-group> -->
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    goSignUp() {
      this.$router.push("/register").catch(() => {});
    },
    goHome() {
      this.$router.push("/").catch(() => {});
    },
    showLoginBox() {
      this.vueMap.get("loginBox").showBox();
    },
    signOut() {
      this.$store.commit("logout");
      this.successToast("Sign out succeed!");
    },
  },
  computed: {
    isLogin: function () {
      return this.$store.state.isLogin;
    },
  },
};
</script>

<style scoped>
.top-bar {
  position: relative !important;
  max-height: 48px;
}
</style>
