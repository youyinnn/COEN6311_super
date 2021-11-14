<template>
  <div id="user-info" class="user-info">
    <v-card
      class="info-box mx-auto mt-12 mb-12 clearfix d-flex justify-center"
      elevation="0"
    >
      <div
        :class="{
          'info-avatar': true,
          animate__animated: true,
          animate__fadeIn: animateAvatar,
        }"
      >
        <v-img :src="userAvatarSrc"> </v-img>
        <v-card-actions class="d-flex justify-center mt-4 v-card__actions">
          <v-btn color="primary" small @click="updateInfo">
            Update Profile
          </v-btn>
        </v-card-actions>
      </div>
      <div class="divider"></div>
      <div class="info-detail elevation-0">
        <div class="text-h5 mb-4 unselectable">Information</div>
        <v-divider></v-divider>

        <v-card-title class="mb-4">
          <v-text-field
            hide-details
            label="Username"
            v-model="userInfo.username"
            disabled
          ></v-text-field>
          <v-text-field
            hide-details
            label="Name"
            v-model="userInfo.name"
          ></v-text-field>
        </v-card-title>

        <v-card-subtitle class="pb-0 d-flex">
          <v-text-field
            hide-details
            class="mb-4"
            label="Title"
            v-model="userInfo.title"
          ></v-text-field>
          <v-text-field
            hide-details
            class="mb-4"
            label="Area"
            v-model="userInfo.area"
          ></v-text-field>
        </v-card-subtitle>

        <v-card-text class="text--primary">
          <v-text-field
            hide-details
            class="mb-4"
            label="E-mail"
            v-model="userInfo.email"
          ></v-text-field>
          <v-text-field
            class="mb-4"
            hide-details
            label="Password"
            type="password"
            v-model="userInfo.password"
          ></v-text-field>
        </v-card-text>
        <div class="text-h5 mb-4 unselectable">Activities</div>
        <v-divider></v-divider>
        <div class="op-activities">
          <v-timeline align-top dense>
            <v-timeline-item small>
              <div class="text-subtitle-2">2021/10/15 17:39</div>
              <div class="text-body-2">
                A dynamic segment is denoted by a colon :. When a route is
                matched, the value of the dynamic segments will be exposed as
                this.$route.params in every component. Therefore, we can render
                the current user ID by updating User's template to this:
              </div>
            </v-timeline-item>
          </v-timeline>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
const axios = require("axios").default;
import "animate.css";

export default {
  data: () => ({
    userInfo: {
      username: "jack123",
      email: "jack@gmail.com",
      name: "Jack Simith",
      area: "AI,Cloud",
      title: "PhD",
    },
    animateAvatar: false,
    avatarHide: true,
  }),
  computed: {
    userAvatarSrc: function () {
      return this.config.getRandomAvatars();
    },
  },
  mounted: function () {
    const isLogin = this.$store.state.isLogin;
    if (!isLogin) {
      this.$router.push("/404");
      this.errorToast("You should login first!");
    }
    const token = localStorage.getItem("token");
    const info = JSON.parse(Buffer.from(token.split(".")[1], "base64"));
    // console.log(info);
    this.userInfo = {
      ...info,
    };
    this.animateAvatar = true;
  },
  methods: {
    updateInfo: function () {
      console.log(this.userInfo);
      const thiz = this;
      const formData = new FormData();
      const token = localStorage.getItem("token");

      formData.append("name", this.userInfo.name);
      if (!this.password) {
        formData.append("password", this.userInfo.password);
      }
      formData.append("email", this.userInfo.email);
      formData.append("area", this.userInfo.area);
      formData.append("title", this.userInfo.title);

      var config = {
        method: "post",
        url: this.config.testEnvBackEndUrl + "user/update",
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `bearer ${token}`,
        },
        data: formData,
      };

      axios(config)
        .then(function (response) {
          // console.log(response.data);
          const code = response.data.code;
          if (code === 0) {
            thiz.successToast("Update succeed!");
          } else {
            thiz.errorToast(response.data.message);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.info-avatar {
  float: left;
  height: 200px !important;
  width: 200px !important;
  border-radius: 200px !important;
  animation-duration: 1s;
  animation-delay: 0.2s;
}
.divider {
  float: left;
  height: 100%;
  border-right: 2px #e1e2e7 dashed;
  margin: 1rem;
  margin-left: 2rem;
}
.info-box {
  width: 90%;
}
.info-detail {
  float: left;
  width: 70%;
}
.v-input {
  max-width: 300px;
  margin-right: 3rem;
}
</style>
