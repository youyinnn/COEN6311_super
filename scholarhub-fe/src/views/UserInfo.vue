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
        <div class="text-h5 mb-4 unselectable">
          Activities
          <span class="text-subtitle-2">{{ activities.length }} Records</span>
        </div>
        <v-divider></v-divider>
        <div class="op-activities">
          <div>
            <v-tabs v-model="tab" align-with-title>
              <v-tabs-slider></v-tabs-slider>

              <v-tab v-for="item in items" :key="item">
                {{ item }}
              </v-tab>
            </v-tabs>
            <v-divider></v-divider>
            <v-timeline
              v-if="displayActivities[tab].length === 0"
              align-top
              dense
            >
              <v-timeline-item small>
                <div class="text-subtitle-2"></div>
                <div class="text-body-2">You have no activities here.</div>
              </v-timeline-item>
            </v-timeline>
            <v-tabs-items v-else v-model="tab">
              <v-tab-item v-for="item in items" :key="item" transition="none">
                <v-timeline
                  :key="activity.id"
                  v-for="activity in displayActivities[tab]"
                  align-top
                  dense
                >
                  <v-timeline-item small :color="activity.iconColor">
                    <div class="d-flex align-center text-subtitle-2 mb-2">
                      <v-icon :color="activity.iconColor" class="mr-2">
                        {{ activity.icon }}
                      </v-icon>
                      <strong class="mr-2">{{ activity.label }}</strong>
                      <span>{{ activity.create_time }}</span>
                    </div>
                    <div class="text-body-2" v-html="activity.content"></div>
                  </v-timeline-item>
                </v-timeline>
              </v-tab-item>
            </v-tabs-items>
          </div>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
const dayjs = require("dayjs");
import "animate.css";

export default {
  data: () => ({
    userInfo: {
      username: "",
      email: "",
      name: "",
      area: "",
      title: "",
    },
    animateAvatar: false,
    avatarHide: true,
    activities: [],
    displayActivities: [[], [], [], [], []],
    tab: 0,
    items: ["Search", "Visit", "Like/Dislike", "Share", "Comment"],
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
    this.fetchInfo();
    this.animateAvatar = true;
    this.getUserActivities();
  },
  methods: {
    fetchInfo() {
      const token = localStorage.getItem("token");
      const info = JSON.parse(Buffer.from(token.split(".")[1], "base64"));
      // console.log(info);
      this.userInfo = {
        ...info,
      };
    },
    updateInfo() {
      // console.log(this.userInfo);
      const formDataMap = {
        name: this.userInfo.name,
        email: this.userInfo.email,
        area: this.userInfo.area,
        title: this.userInfo.title,
      };
      if (this.userInfo.password !== undefined) {
        formDataMap["password"] = this.userInfo.password;
      }
      this.ax.post(this.config.testEnvBackEndUrl + "user/update", formDataMap, {
        isAuth: true,
        success: (response) => {
          const code = response.data.code;
          if (code === 0) {
            this.successToast("Update succeed!");
            // console.log(response.data.body.new_token);
            this.$store.commit("login", {
              token: response.data.body.new_token,
            });
          } else {
            this.errorToast(response.data.message);
          }
        },
        final: () => {
          this.fetchInfo();
        },
      });
    },
    getUserActivities() {
      this.ax.get(
        this.config.testEnvBackEndUrl + "icde/access/user-activities",
        {},
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            if (code === 0) {
              const body = response.data.body;
              const records = body.records;
              for (let record of records) {
                record.create_time = dayjs(record.create_time).format(
                  "YYYY/MM/DD HH:mm"
                );
                record.icon = "mdi-close";
                record.iconColor = "green";
                switch (record.operation_type) {
                  case "paper_search":
                    record.label = "Searching";
                    record.icon = "mdi-text-search";
                    record.iconColor = "blue";
                    record.content = `In <strong>'${record.input_text}'</strong>`;
                    break;
                  case "paper_detail_click":
                    record.label = "Visiting details";
                    record.icon = "mdi-card-text";
                    record.iconColor = "indigo lighten-1";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_origin_click":
                    record.label = "Visiting origin";
                    record.icon = "mdi-share";
                    record.iconColor = "red";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_like_click":
                    record.label = "Likes";
                    record.icon = "mdi-thumb-up";
                    record.iconColor = "green";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_dislike_click":
                    record.label = "Dislikes";
                    record.icon = "mdi-thumb-down";
                    record.iconColor = "orange";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_share":
                    record.label = "Shared";
                    record.icon = "mdi-share-variant";
                    record.iconColor = "cyan";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a> to <strong>Team-${record.team_name}</strong>`;
                    break;
                  case "paper_comment":
                    record.label = "Commented";
                    record.icon = "mdi-comment-processing";
                    record.iconColor = "pink lighten-2";
                    record.content = `<a href="${location.origin}/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                }
              }
              this.activities = records;
              this.displayActivities[0] = records.filter(
                (record) => record.operation_type === "paper_search"
              );
              this.displayActivities[1] = records.filter(
                (record) =>
                  record.operation_type === "paper_detail_click" ||
                  record.operation_type === "paper_origin_click"
              );
              this.displayActivities[2] = records.filter(
                (record) =>
                  record.operation_type === "paper_like_click" ||
                  record.operation_type === "paper_dislike_click"
              );
              this.displayActivities[3] = records.filter(
                (record) => record.operation_type === "paper_share"
              );
              this.displayActivities[4] = records.filter(
                (record) => record.operation_type === "paper_comment"
              );
            }
          },
        }
      );
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
.tab-item {
  transition: all 0.8s ease-in-out;
}
.v-timeline-item {
  padding-bottom: 12px;
}
</style>
