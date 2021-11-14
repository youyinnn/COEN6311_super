<template>
  <div id="team-page" class="team-page mx-auto">
    <div class="team-list">
      <div class="create-team-box">
        <v-list dense>
          <v-subheader>
            <span>Create A Team</span>
            <v-spacer></v-spacer>
            <v-btn x-small color="info" class="mr-2" @click="createTeam">
              Create a team</v-btn
            >
          </v-subheader>
          <v-text-field
            dense
            label="Name of the Team"
            single-line
            hide-details="auto"
            class="mt-2 mb-2 ml-4 mr-4"
            v-model="newTeamName"
          ></v-text-field>
        </v-list>
        <v-divider></v-divider>
      </div>
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
            <v-list-item-group v-model="selectedTeamId" mandatory>
              <v-list-item
                v-for="team in teamList"
                :key="team.id"
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
        <div class="team-activities-box"></div>
        <v-card class="team-member-box">
          <v-card-text>Team member</v-card-text>
          <v-divider></v-divider>
          <v-list-item-group
            class="team-member-group-box"
            :class="{
              'team-member-group-box': true,
              animate__animated: true,
              animate__fadeIn: teamMemberListFadeInAminate,
            }"
          >
            <v-list-item
              v-for="member in currentTeamBoxMember"
              :key="selectedTeamId + '-' + member.email"
              dense
              three-line
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
const axios = require("axios").default;
const dayjs = require("dayjs");

export default {
  data: () => ({
    selectedTeamId: 0,
    invitations: [],
    teamList: [],
    newTeamName: "",
    currentTeamBoxMember: [],
    expandTeamList: true,
    teamMemberListFadeInAminate: true,
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
      const thiz = this;
      const token = localStorage.getItem("token");
      var config = {
        method: "get",
        url: this.config.testEnvBackEndUrl + "team/list",
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `bearer ${token}`,
        },
      };
      axios(config)
        .then(function (response) {
          const code = response.data.code;
          const body = response.data.body;
          if (code === 0) {
            thiz.teamList = [...body.joined_list];
            for (let invite of body.pending_list) {
              invite.time = dayjs(invite.auth_create_time).format(
                "YYYY/MM/DD HH:mm"
              );
            }
            thiz.invitations = [...body.pending_list];
            if (thiz.invitations.length === 0) {
              thiz.invitations = [];
            }
            if (cb !== undefined) cb();
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    handleAuth: function (auth_id, decision) {
      const thiz = this;
      const formData = new FormData();
      const token = localStorage.getItem("token");

      formData.append("auth_id", auth_id);
      formData.append("decision", decision);

      var config = {
        method: "post",
        url: this.config.testEnvBackEndUrl + "team/invite/handle",
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
          const msg = response.data.message;
          if (code === 1 || code === 2 || code === 3 || code === 4) {
            thiz.errorToast(msg);
          }
          if (code === 0) {
            thiz.successToast(msg);
          }
          thiz.fetchTeam();
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    createTeam: function () {
      if (!this.newTeamName) {
        this.errorToast("Please input a team name.", {
          position: "top-right",
        });
      } else {
        const thiz = this;
        const formData = new FormData();
        const token = localStorage.getItem("token");

        formData.append("name", this.newTeamName);

        var config = {
          method: "post",
          url: this.config.testEnvBackEndUrl + "team/create",
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
            const msg = response.data.message;
            if (code === 1) {
              thiz.errorToast(msg);
            }
            if (code === 0) {
              thiz.successToast(msg);
            }
            thiz.fetchTeam();
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    fetchTeamMemberList: function (team_id) {
      this.teamMemberListFadeInAminate = false;
      const thiz = this;
      const token = localStorage.getItem("token");
      var config = {
        method: "get",
        url: this.config.testEnvBackEndUrl + "team/member/list",
        params: {
          team_id,
        },
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `bearer ${token}`,
        },
      };
      axios(config)
        .then(function (response) {
          const code = response.data.code;
          const msg = response.data.message;
          if (code === 0) {
            for (let member of response.data.body.member_list) {
              if (member.role_tag === "") {
                member.role_tag = "<no role>";
              }
            }
            thiz.currentTeamBoxMember = response.data.body.member_list;
            thiz.teamMemberListFadeInAminate = true;
          } else {
            thiz.errorToast(msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    selectTeam: function (team) {
      this.fetchTeamMemberList(team.team_id);
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
}
.team-member-group-box {
  overflow: auto;
  position: absolute;
  bottom: 0;
  top: 56px;
  animation-duration: 0.7s;
  animation-delay: 0.2s;
}
</style>
