<template>
  <div id="user-info" class="user-info d-flex justify-center">
    <v-card class="info-box mx-auto mt-12 mb-12 clearfix" elevation="0">
      <div class="info-avatar">
        <v-img :src="userAvatarSrc"> </v-img>
        <v-card-actions class="d-flex justify-center mt-4 v-card__actions">
          <v-btn color="primary" small> Update Profile </v-btn>
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
            :value="userInfo.username"
            disabled
          ></v-text-field>
          <v-text-field
            hide-details
            label="Name"
            :value="userInfo.name"
          ></v-text-field>
        </v-card-title>

        <v-card-subtitle class="pb-0 d-flex">
          <v-text-field
            hide-details
            class="mb-4"
            label="Title"
            :value="userInfo.title"
          ></v-text-field>
          <v-text-field
            hide-details
            class="mb-4"
            label="Area"
            :value="userInfo.area"
          ></v-text-field>
        </v-card-subtitle>

        <v-card-text class="text--primary">
          <v-text-field
            hide-details
            class="mb-4"
            label="E-mail"
            :value="userInfo.email"
          ></v-text-field>
          <v-text-field
            class="mb-4"
            hide-details
            label="Password"
            type="password"
            :value="userInfo.password"
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
const random = require("lodash.random");

import man1 from "@/assets/img/avatars/man-1.png";
import man2 from "@/assets/img/avatars/man-2.png";
import man3 from "@/assets/img/avatars/man-3.png";
import man4 from "@/assets/img/avatars/man-4.png";
import man5 from "@/assets/img/avatars/man-5.png";
import man6 from "@/assets/img/avatars/man-6.png";

import woman1 from "@/assets/img/avatars/woman-1.png";
import woman2 from "@/assets/img/avatars/woman-2.png";
import woman3 from "@/assets/img/avatars/woman-3.png";
import woman4 from "@/assets/img/avatars/woman-4.png";
import woman5 from "@/assets/img/avatars/woman-5.png";
import woman6 from "@/assets/img/avatars/woman-6.png";

const avatars = [
  man1,
  man2,
  man3,
  man4,
  man5,
  man6,
  woman1,
  woman2,
  woman3,
  woman4,
  woman5,
  woman6,
];

export default {
  data: () => ({
    userInfo: {
      username: "jack123",
      email: "jack@gmail.com",
      name: "Jack Simith",
      area: "AI,Cloud",
      title: "PhD",
    },
  }),
  computed: {
    userAvatarSrc: function () {
      return avatars[random(0, 11)];
    },
  },
  mounted: function () {
    const isLogin = this.$store.state.isLogin;
    if (!isLogin) {
      this.$router.push("/404");
      this.errorToast("You should login first!");
    }
  },
};
</script>

<style scoped>
.info-avatar {
  float: left;
  height: 200px;
  width: 200px;
  border-radius: 200px !important;
}
.divider {
  float: left;
  height: 100%;
  border-right: 2px #e1e2e7 dashed;
  margin: 1rem;
  margin-left: 2rem;
}
.info-detail {
  float: left;
  max-width: 700px;
}
.v-input {
  max-width: 250px;
  margin-right: 3rem;
}
</style>
