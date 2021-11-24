<template>
  <div id="team-page" class="team-page mx-auto">
    <div class="team-list">
      <div class="create-team-box">
        <v-list dense>
          <v-subheader>
            <span>Create a Team</span>
            <v-spacer></v-spacer>
            <v-btn
              width="60"
              x-small
              color="info"
              class="mr-2"
              @click="createTeam"
            >
              Create</v-btn
            >
          </v-subheader>
          <v-text-field
            dense
            persistent-placeholder
            placeholder="team name"
            single-line
            hide-details="auto"
            class="mt-2 mb-2 ml-4 mr-4 elevation-4"
            v-model="newTeamName"
            solo
          ></v-text-field>
        </v-list>
        <v-divider></v-divider>
      </div>
      <transition name="he" mode="out-in">
        <div
          v-show="leaderOfCurrentTeam"
          key="invite-box"
          class="create-team-box"
        >
          <v-list dense>
            <v-subheader>
              <span>Invite a Member to This Team</span>
              <v-spacer></v-spacer>
              <v-btn
                width="60"
                x-small
                color="green"
                class="mr-2 white--text"
                @click="inviteMember"
              >
                Invite</v-btn
              >
            </v-subheader>
            <v-text-field
              dense
              single-line
              persistent-placeholder
              placeholder="email"
              hide-details="auto"
              class="mt-2 mb-2 ml-4 mr-4 elevation-4"
              v-model="newMemberEmail"
              solo
            ></v-text-field>
          </v-list>
          <v-divider></v-divider>
        </div>
      </transition>

      <v-card class="mx-auto" elevation="0" max-width="300" tile>
        <v-list dense>
          <v-subheader>
            <span>Teams</span>
          </v-subheader>

          <v-list-group v-model="expandTeamList">
            <template v-slot:activator>
              <v-list-item-icon class="mr-4">
                <v-icon>mdi-forum</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Joined</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item-group v-model="selectedTeamIndex" mandatory>
              <v-list-item
                v-for="team in teamList"
                :key="team.team_id"
                @click="selectTeam(team)"
              >
                <v-list-item-icon>
                  <v-icon>mdi-menu-right</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="team.name"></v-list-item-title>
                </v-list-item-content>
                <v-list-item-icon v-show="team.leader_id === getUserId">
                  <v-icon>mdi-account-tie</v-icon>
                </v-list-item-icon>
              </v-list-item>
            </v-list-item-group>
          </v-list-group>

          <v-list-group>
            <template v-slot:activator>
              <v-list-item-icon class="mr-4">
                <v-icon>mdi-account-multiple-plus-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title class="d-flex align-center">
                  <span class="mr-2">Invitations</span>
                  <v-badge
                    class="ma-0"
                    inline
                    color="primary"
                    :content="
                      invitations.length == 0 ? '0' : invitations.length
                    "
                  ></v-badge>
                </v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item-group>
              <v-list-item
                v-for="(invitation, i) in invitations"
                :key="i"
                two-line
              >
                <v-list-item-title style="padding: 5px">
                  <p class="ma-0 mb-2 clearfix">
                    <span style="float: left">From: {{ invitation.name }}</span>
                    <span style="float: right; font-weight: 300">{{
                      invitation.time
                    }}</span>
                  </p>
                  <div>
                    <v-btn
                      x-small
                      style="float: right"
                      color="error"
                      @click="handleAuth(invitation.auth_id, 3)"
                      >Reject</v-btn
                    >
                    <v-btn
                      class="mr-4"
                      style="float: right"
                      x-small
                      color="success"
                      @click="handleAuth(invitation.auth_id, 1)"
                      >Accept</v-btn
                    >
                  </div>
                </v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list-group>
        </v-list>
      </v-card>
    </div>

    <div class="team-box">
      <div v-if="hasTeam" class="has-team">
        <v-card class="team-activities-box" elevation="5">
          <v-card-text
            style="font-weight: 900; font-size: 16px; font-family: 'Roboto'"
            >Member activities of &lt;
            <strong>{{ currentTeam.name }}</strong> &gt;
          </v-card-text>
          <v-divider></v-divider>
          <div
            :class="{
              'timeline-box': true,
              animate__animated: true,
              animate__fadeIn: teamMemberActivitiesAminate,
            }"
          >
            <v-timeline
              key="no-team-activities"
              v-if="teamActivities.length === 0"
              align-top
              dense
            >
              <v-timeline-item small>
                <div class="text-subtitle-2"></div>
                <div class="text-body-2">No activities here.</div>
              </v-timeline-item>
            </v-timeline>
            <v-timeline
              :key="activity.id"
              v-for="activity in teamActivities"
              align-top
              dense
            >
              <v-timeline-item
                small
                fill-dot
                :color="activity.iconColor"
                :icon="activity.icon"
              >
                <div class="d-flex align-center text-subtitle-2 mb-2">
                  <strong v-html="activity.user_name" class="mr-2"></strong>
                  <strong class="mr-2">{{ activity.label }}</strong>
                  <span>{{ activity.create_time }}</span>
                </div>
                <div class="text-body-2" v-html="activity.content"></div>
              </v-timeline-item>
            </v-timeline>
          </div>
        </v-card>
        <v-card class="team-member-box" elevation="5">
          <v-card-text>Team member</v-card-text>
          <v-divider></v-divider>
          <v-list-item-group
            :class="{
              'team-member-group-box': true,
              animate__animated: true,
              animate__fadeIn: teamMemberListFadeInAminate,
            }"
          >
            <v-list-item
              v-for="member in currentTeamBoxMember"
              :key="selectedTeamIndex + '-' + member.email"
              dense
              three-line
              @click="clickMember(member)"
            >
              <v-list-item-content>
                <v-list-item-title>{{ member.name }}</v-list-item-title>
                <v-list-item-subtitle>
                  {{ member.role_tag }}
                </v-list-item-subtitle>
                <v-list-item-subtitle>
                  {{ member.email }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-card>
      </div>
      <div
        v-else
        class="align-center d-flex fill-height justify-center no-team"
      >
        <div class="unselectable" style="transform: translateY(-20px)">
          <v-img height="250" width="250" src="@/assets/img/alone.png"> </v-img>
          <div class="mt-4 text-button" style="text-align: center">
            You haven't join a team yet!
          </div>
          <!-- <div class="text-button" style="text-align: center">
            Loneliness is a terrible thing
          </div> -->
          <div class="text-button" style="text-align: center">Find a team~</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "animate.css";
const dayjs = require("dayjs");

export default {
  data: () => ({
    selectedTeamIndex: 0,
    invitations: [],
    teamList: [],
    teamMemmberMap: null,
    teamActivities: [],
    newTeamName: "",
    currentTeamBoxMember: [],
    expandTeamList: true,
    teamMemberListFadeInAminate: true,
    teamMemberActivitiesAminate: true,
    newMemberEmail: "",
    currentTeam: "",
    leaderOfCurrentTeam: false,
  }),
  mounted: function () {
    const isLogin = this.$store.state.isLogin;
    if (!isLogin) {
      this.$router.push("/404");
      this.errorToast("You should login first!");
    }
    const thiz = this;
    this.fetchTeam(() => {
      if (thiz.teamList.length > 0) {
        thiz.currentTeam = thiz.teamList[0];
        thiz.selectTeam(thiz.teamList[0]);
      }
    });
  },
  computed: {
    hasTeam: function () {
      return this.teamList.length !== 0;
    },
    hasTeamInvitatuon: function () {
      return this.invitations.length !== 0;
    },
    getUserId: function () {
      const token = localStorage.getItem("token");
      const info = JSON.parse(Buffer.from(token.split(".")[1], "base64"));
      return info.id;
    },
  },
  methods: {
    fetchTeam: function (cb) {
      this.ax.get(
        this.config.testEnvBackEndUrl + "team/list",
        {},
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            const body = response.data.body;
            if (code === 0) {
              this.teamList = [...body.joined_list];
              for (let invite of body.pending_list) {
                invite.time = dayjs(invite.auth_create_time).format(
                  "YYYY/MM/DD HH:mm"
                );
              }
              this.invitations = [...body.pending_list];
              if (this.invitations.length === 0) {
                this.invitations = [];
              }
              if (cb !== undefined) cb();
            }
          },
        }
      );
    },
    handleAuth: function (auth_id, decision) {
      this.ax.post(
        this.config.testEnvBackEndUrl + "team/invite/handle",
        { auth_id, decision },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            const msg = response.data.message;
            if (code === 1 || code === 2 || code === 3 || code === 4) {
              this.errorToast(msg);
            }
            if (code === 0) {
              this.successToast(msg);
            }
            this.fetchTeam();
          },
        }
      );
    },
    createTeam: function () {
      if (!this.newTeamName) {
        this.errorToast("Please input a team name.", {
          position: "top-right",
        });
      } else {
        this.ax.post(
          this.config.testEnvBackEndUrl + "team/create",
          { name: this.newTeamName },
          {
            isAuth: true,
            success: (response) => {
              const code = response.data.code;
              const msg = response.data.message;
              if (code === 1) {
                this.errorToast(msg);
              }
              if (code === 0) {
                this.successToast(msg);
              }
              this.fetchTeam();
            },
          }
        );
      }
    },
    fetchTeamMemberList: function (team_id) {
      this.teamMemberListFadeInAminate = false;
      this.teamMemberActivitiesAminate = false;
      this.ax.get(
        this.config.testEnvBackEndUrl + "team/member/list",
        { team_id },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            const msg = response.data.message;
            if (code === 0) {
              this.teamMemmberMap = new Map();
              for (let member of response.data.body.member_list) {
                if (member.role_tag === "") {
                  member.role_tag = "<no role>";
                }
                this.teamMemmberMap.set(member.id, member.name);
              }
              this.currentTeamBoxMember = response.data.body.member_list;
              this.teamMemberListFadeInAminate = true;
              this.fetchTeamMemberActivities(team_id);
            } else {
              this.errorToast(msg);
            }
          },
        }
      );
    },
    selectTeam: function (team) {
      this.currentTeam = team;
      const leaderId = team.leader_id;
      if (leaderId === this.getUserId) {
        this.leaderOfCurrentTeam = true;
      } else {
        this.leaderOfCurrentTeam = false;
      }
      this.fetchTeamMemberList(team.team_id);
    },
    clickMember: function (member) {
      console.log(member);
    },
    inviteMember: function () {
      const newMemberEmail = this.newMemberEmail;
      if (!newMemberEmail) {
        this.errorToast("Please input an email.", {
          position: "top-right",
        });
      } else {
        this.ax.post(
          this.config.testEnvBackEndUrl + "team/invite",
          {
            team_id: this.currentTeam.team_id,
            invitee_email: this.newMemberEmail,
          },
          {
            isAuth: true,
            success: (response) => {
              const code = response.data.code;
              const msg = response.data.message;
              if (code === 1) {
                this.errorToast(msg);
              } else if (code === 0) {
                this.successToast("Invitation is sent.");
              } else {
                this.infoToast(msg);
              }
            },
          }
        );
      }
    },
    fetchTeamMemberActivities(team_id) {
      this.ax.get(
        this.config.testEnvBackEndUrl + "icde/team-activities",
        { team_id },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            if (code === 0) {
              const body = response.data.body;
              const records = body.records;
              const token = localStorage.getItem("token");
              const info = JSON.parse(
                Buffer.from(token.split(".")[1], "base64")
              );
              for (let record of records) {
                record.create_time = dayjs(record.create_time).format(
                  "YYYY/MM/DD HH:mm"
                );
                if (record.user_id === info.id) {
                  record.user_name = `<span style="color: green">You</span>`;
                } else {
                  record.user_name = this.teamMemmberMap.get(record.user_id);
                }
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
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_origin_click":
                    record.label = "Visiting origin";
                    record.icon = "mdi-share";
                    record.iconColor = "red";
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_like_click":
                    record.label = "Likes";
                    record.icon = "mdi-thumb-up";
                    record.iconColor = "green";
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_dislike_click":
                    record.label = "Dislikes";
                    record.icon = "mdi-thumb-down";
                    record.iconColor = "orange";
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_share":
                    record.label = "Shared";
                    record.icon = "mdi-share-variant";
                    record.iconColor = "cyan";
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                  case "paper_comment":
                    record.label = "Commented";
                    record.icon = "mdi-comment-processing";
                    record.iconColor = "pink lighten-2";
                    record.content = `<a href="/#/paper/${record.paper_title}/${record.paper_id}">${record.paper_title}</a>`;
                    break;
                }
              }
              // console.log(records);
              this.teamActivities = records;
              this.teamMemberActivitiesAminate = true;
            }
          },
        }
      );
    },
  },
};
</script>

<style scoped>
.team-page {
  right: 0;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  height: hidden;
}
.team-list {
  position: absolute;
  width: 270px;
  border-right: 1px gainsboro solid;
  margin: 2rem 0;
  top: 0px;
  bottom: 0;
}
.team-box {
  position: absolute;
  margin: 2rem 0;
  padding: 0 1rem;
  top: 0;
  bottom: 0;
  right: 0;
  left: 270px;
}
.team-member-box {
  position: absolute;
  background-color: #4242421c !important;
  height: 100%;
  width: 220px;
  right: 1rem;
}
.team-activities-box {
  position: absolute;
  margin: 0 1rem;
  height: 100%;
  right: 236px;
  left: 0;
  overflow: hidden;
}
.team-member-group-box {
  overflow: auto;
  position: absolute;
  bottom: 0;
  top: 56px;
  animation-duration: 0.7s;
  animation-delay: 0.2s;
}

.he-enter-active {
  transition: all 0.4s ease;
  height: 110px;
}
.he-leave-active {
  transition: all 0.4s ease;
  height: 110px;
}
.he-enter, .he-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  height: 0;
}

.v-timeline {
  padding-top: 12px;
}
.v-timeline-item {
  padding-bottom: 12px;
}
.timeline-box {
  overflow: auto;
  overflow-x: hidden;
  bottom: 0;
  position: absolute;
  top: 54px;
  padding-bottom: 3rem;
  right: 0;
  left: 0;
  animation-duration: 0.9s;
  animation-delay: 0.4s;
}
</style>
