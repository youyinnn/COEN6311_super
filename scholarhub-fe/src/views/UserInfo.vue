<template>
  <div id="user-info" class="user-info">
    <v-card
      class="info-box mx-auto mt-12 clearfix"
      max-width="700"
      elevation="0"
    >
      <v-img :src="userAvatarSrc" class="info-avatar mr-4"> </v-img>
      <div class="info-detail">
        <v-card-title>{{ userInfo.name }}</v-card-title>

        <v-card-subtitle class="pb-0"> {{ userInfo.title }} </v-card-subtitle>

        <v-card-text class="text--primary">
          <div>{{ userInfo.area }}</div>

          <div>{{ userInfo.email }}</div>
        </v-card-text>
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
.user-info {
}
.info-avatar {
  float: left;
  height: 200px;
  width: 200px;
}
.info-detail {
  float: left;
}
</style>
