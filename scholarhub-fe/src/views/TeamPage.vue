<template>
  <div id="team-page" class="team-page mx-auto">
    <div class="team-list">
      <v-card class="mx-auto" elevation="0" max-width="300" tile>
        <v-list dense>
          <v-subheader>TEAMS</v-subheader>

          <v-list-group :disabled="!hasTeam" :value="hasTeam">
            <template v-slot:activator>
              <v-list-item-icon class="mr-4">
                <v-icon>mdi-forum</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Joined</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item-group v-model="selectedTeam" mandatory>
              <v-list-item v-for="(team, i) in teamList" :key="i">
                <v-list-item-icon>
                  <v-icon>mdi-menu-right</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="team.name"></v-list-item-title>
                </v-list-item-content>
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
                    :content="invitations.length"
                  ></v-badge>
                </v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item
              v-for="(invitation, i) in invitations"
              :key="i"
              link
              two-line
            >
              <v-list-item-title style="padding: 5px">
                <p class="ma-0 mb-2 clearfix">
                  <span style="float: left"
                    >From: {{ invitation.teamname }}</span
                  >
                  <span style="float: right; font-weight: 300"
                    >2021/10/3 18:30</span
                  >
                </p>
                <div>
                  <v-btn x-small style="float: right" color="error"
                    >Reject</v-btn
                  >
                  <v-btn
                    class="mr-4"
                    style="float: right"
                    x-small
                    color="success"
                    >Accept</v-btn
                  >
                </div>
              </v-list-item-title>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-card>
    </div>
    <div class="team-activities-box">
      <div v-if="hasTeam" class="has-team"></div>
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
export default {
  data: () => ({
    selectedTeam: 0,
    invitations: [
      { teamname: "team a", id: 123 },
      { teamname: "team b", id: 456 },
    ],
    teamList: [
      //   {
      //     id: 123,
      //     name: "group a",
      //   },
      //   {
      //     id: 456,
      //     name: "group b",
      //   },
      //   {
      //     id: 789,
      //     name: "group c",
      //   },
    ],
  }),
  mounted: function () {
    const isLogin = this.$store.state.isLogin;
    if (!isLogin) {
      this.$router.push("/404");
      this.errorToast("You should login first!");
    }
  },
  computed: {
    hasTeam: function () {
      return this.teamList.length !== 0;
    },
  },
  methods: {
    changeTeam: function (v) {
      for (let i = 0; i < this.teamList.length; i++) {
        if (this.teamList[i].id === v.id) {
          this.teamList[i].active = true;
          return;
        }
      }
      console.log(v);
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
  width: 300px;
  border-right: 1px gainsboro solid;
  margin: 2rem 0;
  top: 0px;
  bottom: 0;
}
.team-activities-box {
  position: absolute;
  margin: 2rem 0;
  padding: 0 1rem;
  top: 0;
  bottom: 0;
  right: 0;
  left: 300px;
}
</style>
