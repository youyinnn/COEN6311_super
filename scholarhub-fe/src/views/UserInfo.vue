<template>
  <div id="user-info" class="user-info d-flex justify-center">
    <v-card class="info-box mx-auto mt-12 mb-12 clearfix" elevation="0">
      <v-img :src="userAvatarSrc" class="info-avatar mr-8"> </v-img>
      <div class="info-detail elevation-3">
        <v-card-title class="mb-4">
          <v-text-field
            hide-details
            label="Username"
            :value="userInfo.username"
            disabled
          ></v-text-field>
          <v-spacer></v-spacer>
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
          <v-spacer></v-spacer>
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
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" small> Update </v-btn>
          </v-card-actions>
        </v-card-text>
        <v-divider></v-divider>
        <div class="op-history">
          <v-timeline align-top dense>
            <v-timeline-item small
              >A dynamic segment is denoted by a colon :. When a route is
              matched, the value of the dynamic segments will be exposed as
              this.$route.params in every component. Therefore, we can render
              the current user ID by updating User's template to
              this:</v-timeline-item
            >
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
            <v-timeline-item small>timeline item</v-timeline-item>
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
};
</script>

<style scoped>
.info-avatar {
  float: left;
  height: 200px;
  width: 200px;
  border-radius: 200px !important;
}
.info-detail {
  float: left;
  max-width: 700px;
}
</style>
