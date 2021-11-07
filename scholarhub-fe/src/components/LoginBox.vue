<template>
  <v-container
    id="loginBox"
    :class="{
      'login-box': true,
      'elevation-5': true,
      'login-box-hide': boxHide,
      'entirely-hide': boxEntirelyHide,
    }"
  >
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="username"
        :rules="rules"
        label="Username"
        required
        hide-details
        dark
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        :rules="rules"
        required
        type="password"
        hide-details
        dark
      ></v-text-field>
      <div class="d-flex justify-end mt-4">
        <v-btn small class="mr-4" color="error" @click="hideBox"> Close </v-btn>
        <v-btn small class="" color="success" @click="login"> Login </v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    username: "",
    rules: [(v) => !!v || "Required"],
    password: "",
    boxHide: true,
    boxEntirelyHide: true,
  }),

  methods: {
    login() {
      this.$refs.form.validate();
    },
    showBox() {
      this.boxHide = false;
      this.boxEntirelyHide = false;
    },
    hideBox() {
      this.boxHide = true;
      //   setTimeout(() => {
      //     this.boxEntirelyHide = true;
      //   }, 600);
    },
  },
};
</script>

<style scoped>
.login-box {
  position: absolute;
  background-color: #2c394b;
  right: 1rem;
  z-index: 3;
  top: 4rem;
  padding: 1rem;
  border-radius: 1rem;
  width: 300px;
  transition: all 0.6s;
  opacity: 1;
  right: 1rem;
}
.login-box-hide {
  /* top: -16%; */
  right: -31%;
  opacity: 0;
}
.entirely-hide {
  right: -31%;
}
</style>
