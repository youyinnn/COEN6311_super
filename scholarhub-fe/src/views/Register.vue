<template>
  <v-container id="register" fill-height class="d-flex align-center">
    <div class="regBox">
      <div class="regLogo mr-6">
        <v-img
          v-if="gender == 'm'"
          max-width="200"
          src="@/assets/img/m-scholar.png"
        ></v-img>
        <v-img v-else max-width="200" src="@/assets/img/f-scholar.png"></v-img>
      </div>
      <v-form ref="regForm" class="regFormBox" v-model="valid" lazy-validation>
        <v-text-field
          v-model="name"
          :rules="nameRules"
          label="Name"
          required
        ></v-text-field>
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          label="Username"
          required
        ></v-text-field>
        <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Password"
          type="password"
          required
        ></v-text-field>

        <!-- <v-radio-group v-model="gender" row>
          <span class="mr-4">Gender</span>
          <v-radio label="Male" value="m"></v-radio>
          <v-radio label="Female" value="f"></v-radio>
        </v-radio-group> -->

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field v-model="area" label="Area"></v-text-field>
        <v-text-field v-model="title" label="Title" class="mb-6"></v-text-field>

        <div class="clearfix">
          <v-btn
            style="float: right"
            :disabled="!valid"
            color="success"
            @click="submit"
          >
            Submit
          </v-btn>
          <v-btn style="float: right" color="grey" class="mr-4" @click="reset">
            Reset Form
          </v-btn>
        </div>
      </v-form>
    </div>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [(v) => !!v || "Name is required"],
    username: "",
    usernameRules: [(v) => !!v || "Username is required"],
    password: "",
    passwordRules: [(v) => !!v || "Password is required"],
    gender: "m",
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    area: [],
    title: "",
  }),
  methods: {
    submit() {
      const isValid = this.$refs.regForm.validate();
      if (isValid) {
        this.ax.post(
          this.config.testEnvBackEndUrl + "user",
          {
            name: this.name,
            username: this.username,
            password: this.password,
            email: this.email,
            area: this.area,
            title: this.title,
          },
          {
            success: (response) => {
              const code = response.data.code;
              if (code === 0) {
                this.successToast("Register successed!");
                this.$router.push("/").catch(() => {});
              }
              if (code === 1) {
                this.errorToast("Username has been used!");
              }
              if (code === 2) {
                this.errorToast("Email has been used!");
              }
            },
          }
        );
      }
    },
    reset() {
      this.$refs.regForm.reset();
    },
  },
  computed: {},
};
</script>

<style scoped>
.regLogo {
  float: left;
  width: 200px;
  height: 200px;
}
.regBox {
  margin: auto;
  transform: translateY(-3rem);
}
.regFormBox {
  float: left;
  width: 400px;
}
</style>
