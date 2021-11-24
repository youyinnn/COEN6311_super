<template>
  <div id="paper-detail-box" class="paper-detail-box">
    <v-card
      ref="card"
      :class="{
        'detail-card': true,
        'mx-auto': true,
        'default-transit3': true,
        'mt-8': true,
      }"
      max-width="750"
      elevation="6"
    >
      <div class="head-box default-transit5">
        <transition name="fade" mode="out-in">
          <v-skeleton-loader
            key="title-sk-loader"
            class="mx-auto"
            type="card-heading"
            v-if="!hasDetail"
          ></v-skeleton-loader>
          <v-card-title v-else key="card-title">
            <span>{{ paperTitle }}</span></v-card-title
          >
        </transition>
      </div>
      <v-divider></v-divider>

      <div class="detail-box default-transit5">
        <transition name="fade" mode="out-in">
          <v-skeleton-loader
            v-if="!hasDetail"
            key="details-sk-loader"
            class="mx-auto p-5"
            type="list-item-two-line,table-tfoot,list-item"
          ></v-skeleton-loader>
          <div v-else key="details">
            <v-card-subtitle class="pb-0">
              <div
                key="author-box"
                :class="{ 'd-flex': !hasDetail, 'align-center': !hasDetail }"
              >
                <span style="width: 70px" class="paper-data-label"
                  ><strong>Author(s)</strong></span
                >
                <v-chip
                  small
                  class="mr-2 mt-1 mb-1"
                  v-for="author in paper.authors"
                  :key="author.authorId"
                  >{{ author.name }}
                </v-chip>
              </div>
            </v-card-subtitle>

            <v-card-text class="">
              <div>
                <span class="paper-data-label"><strong>Year</strong></span>
                <span>{{ paper.year }}</span>
              </div>
              <div>
                <span class="paper-data-label"><strong>Venue</strong></span>
                <span>{{ paper.venue }}</span>
              </div>
              <div>
                <span class="paper-data-label"
                  ><strong>Reference Count</strong></span
                >
                <span>{{ paper.referenceCount }}</span>
              </div>
              <div>
                <span class="paper-data-label"
                  ><strong>Citation Count</strong></span
                >
                <span>{{ paper.citationCount }}</span>
              </div>
              <div>
                <span class="paper-data-label"
                  ><strong>Open Access</strong></span
                >
                <span v-if="paper.isOpenAccess">Yes</span>
                <span v-else>No</span>
              </div>
              <div>
                <span class="paper-data-label"
                  ><strong>Fields of study</strong></span
                >
                <span
                  class="mr-1"
                  v-for="field in paper.fieldsOfStudy"
                  :key="field"
                  small
                  >[{{ field }}]
                </span>
              </div>
            </v-card-text>
          </div>
        </transition>
      </div>

      <v-card-actions class="paper-card-action d-flex justify-end pt-0">
        <transition name="slide-r-fade" mode="out-in">
          <div v-if="userActionLoaded" key="action-after-user-data">
            <v-btn
              small
              class="ma-2 white--text lighten-1"
              color="red"
              @click="newTab()"
            >
              <span>Origin</span>
              <v-icon small color="white" class="ml-2">mdi-share</v-icon>
            </v-btn>
            <v-btn
              color="green"
              :class="{
                'ma-2': true,
                'white--text': true,
                'mr-0': true,
                animate__animated: true,
                animate__bounceIn: likeNumberAnimate,
              }"
              style="padding: 0"
              min-width="30"
              small
            >
              {{ paperOperatedData.likes }}
            </v-btn>
            <v-btn
              :disabled="likeBtnDisable"
              small
              class="ma-2 white--text ml-1"
              color="green"
              @click="putAttitude(1)"
            >
              <span>Likes</span>
              <v-icon small color="white" class="ml-2">mdi-thumb-up</v-icon>
            </v-btn>
            <v-btn
              color="orange"
              :class="{
                'ma-2': true,
                'white--text': true,
                'mr-0': true,
                animate__animated: true,
                animate__bounceIn: dislikeNumberAnimate,
              }"
              style="padding: 0"
              min-width="30"
              small
            >
              {{ paperOperatedData.dislikes }}
            </v-btn>
            <v-btn
              :disabled="dislikeBtnDisable"
              small
              class="ma-2 white--text ml-1"
              color="orange"
              @click="putAttitude(0)"
            >
              <span>Dislikes</span>
              <v-icon small color="white" class="ml-2">mdi-thumb-down</v-icon>
            </v-btn>
            <v-btn
              color="cyan"
              :class="{
                'ma-2': true,
                'white--text': true,
                'mr-0': true,
                animate__animated: true,
                animate__bounceIn: sharedNumberAnimate,
              }"
              style="padding: 0"
              min-width="30"
              small
            >
              {{ paperOperatedData.shared }}
            </v-btn>
            <v-btn
              :disabled="!isLogin"
              small
              class="ma-2 white--text ml-1"
              color="cyan"
              @click="
                () => {
                  teamListShow = !teamListShow;
                }
              "
            >
              <span>Share</span>
              <v-icon small color="white" class="ml-2"
                >mdi-share-variant</v-icon
              >
            </v-btn>
            <transition name="fade" mode="out-in">
              <v-card
                key="teamList"
                v-if="teamListShow"
                :class="{
                  team_list_class: true,
                  unselectable: true,
                }"
                @mouseleave="
                  () => {
                    teamListShow = false;
                  }
                "
              >
                <div v-if="teamList.length > 0">
                  <v-btn
                    small
                    tile
                    class="team_item"
                    :key="team.team_id"
                    v-for="team in teamList"
                    dense
                    :disabled="team.shared"
                    @click="shareThisPaperTo(team.team_id, team.name)"
                  >
                    <span style="color: black !important">{{ team.name }}</span>
                    <v-spacer></v-spacer>
                    <transition name="small-slide-r-fade" mode="out-in">
                      <v-icon
                        key="shard-close"
                        v-if="!team.shared"
                        class="ml-3"
                        small
                        color="gray darken-2"
                      >
                        mdi-close-outline
                      </v-icon>
                      <v-icon
                        v-else
                        key="shard-check"
                        class="ml-3"
                        small
                        style="color: green !important"
                      >
                        mdi-check-outline
                      </v-icon>
                    </transition>
                  </v-btn>
                </div>
                <v-list-item v-else dense dark>
                  <v-list-item-content>
                    <v-list-item-title
                      >You do not joined any team</v-list-item-title
                    >
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </transition>
          </div>
          <div v-else key="action-before-user-data">
            <v-skeleton-loader
              v-for="i in [1, 2, 3, 4, 5, 6, 7]"
              :key="i"
              class="ma-2"
              type="button"
              max-height="28"
              style="display: inline-block"
            ></v-skeleton-loader>
          </div>
        </transition>
      </v-card-actions>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong class="unselectable">Abstract</strong>
            <template v-slot:actions>
              <v-icon color="primary"> $expand </v-icon>
            </template>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            {{ paper.abstract !== null ? paper.abstract : "empty" }}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-card>
    <transition name="fade">
      <div class="comment-box">
        <v-card elevation="6">
          <v-card-subtitle class="unselectable"> Add Comment </v-card-subtitle>
          <v-divider></v-divider>
          <v-card-text>
            <v-textarea
              dense
              clear-icon="mdi-close-circle"
              v-model="comment"
              rows="2"
              hide-details
            ></v-textarea>
          </v-card-text>
          <v-card-text class="clearfix pt-1">
            <v-btn
              class="white--text"
              style="float: right"
              small
              color="pink lighten-2"
              @click="addComment"
              :disabled="!isLogin"
              >Submit</v-btn
            >
          </v-card-text>
        </v-card>
      </div>
    </transition>
    <div class="comment-box">
      <v-card elevation="6">
        <v-card-subtitle class="unselectable"> Comments </v-card-subtitle>
        <div v-if="!paperCommentFetched">
          <v-skeleton-loader
            class="mx-auto"
            type="table-heading"
          ></v-skeleton-loader>
          <v-skeleton-loader
            class="mx-auto pa-4"
            type="paragraph"
          ></v-skeleton-loader>
        </div>
        <div style="padding-bottom: 2rem" v-else>
          <v-divider></v-divider>
          <div v-for="comment in paperComments" :key="comment.id" class="">
            <div class="commenter">
              <strong class="mr-2">{{ comment.name }}</strong>
              <span class="mr-2" style="font-size: 14px; color: grey">{{
                comment.email
              }}</span>
              <span style="font-size: 12px; color: grey">{{
                comment.time
              }}</span>
            </div>
            <div class="comment">{{ comment.content }}</div>
          </div>
        </div>
      </v-card>
    </div>
  </div>
</template>

<script>
const dayjs = require("dayjs");
import "animate.css";

export default {
  data: () => ({
    teamListShow: false,
    comment: "",
    paper: {
      paperId: "",
      title: " ",
      authors: [],
      year: 0,
      venue: "",
      referenceCount: 0,
      isOpenAccess: false,
      fieldsOfStudy: [],
      abstract: " ",
      url: "",
    },
    paperOperatedData: {
      likes: 0,
      dislikes: 0,
      shared: 0,
    },
    paperComments: [],
    userActionLoaded: false,
    paperCommentFetched: false,
    paperId: "",
    paperTitle: "",
    userAttitudeExist: false,
    userLikeThisPaper: false,
    likeNumberAnimate: false,
    dislikeNumberAnimate: false,
    sharedNumberAnimate: false,
    teamList: [],
    teamListShowLock: false,
  }),
  methods: {
    getDetail() {
      const id = this.paperId;
      this.ax.get(
        `${this.config.paperDetailUrl}/${id}`,
        {
          fields:
            "url,title,authors,abstract,venue,year,referenceCount,isOpenAccess,fieldsOfStudy,citationCount",
        },
        {
          isAuth: true,
          success: (response) => {
            this.paper = response.data;
            this.getPaperAttitudeRecords();
            this.getPaperComments();
          },
          error: () => {
            this.errorToast("Search API went wrong!");
          },
          final: this.fixHeight,
        }
      );
    },
    getPaperAttitudeFromUser() {
      if (this.isLogin) {
        this.ax.get(
          this.config.testEnvBackEndUrl + "paper/like/user",
          { paper_id: this.paperId },
          {
            isAuth: true,
            success: (response) => {
              this.userAttitudeExist = response.data.body.exist;
              this.userLikeThisPaper =
                response.data.body.like === undefined
                  ? false
                  : response.data.body.like;
            },
          }
        );
      }
    },
    getPaperAttitudeRecords() {
      this.ax.get(
        this.config.testEnvBackEndUrl + "paper/like/count",
        { paper_id: this.paperId },
        {
          success: (response) => {
            const result = response.data.body.result;
            if (result !== undefined) {
              this.paperOperatedData.likes = result.like;
              this.paperOperatedData.dislikes = result.dislike;
              this.getPaperAttitudeFromUser();
            }
            this.userActionLoaded = true;
          },
        }
      );
    },
    putAttitude(like) {
      this.ax.post(
        this.config.testEnvBackEndUrl + "paper/like",
        { paper_id: this.paperId, like, paper_title: this.paper.title },
        {
          isAuth: true,
          success: () => {
            this.getPaperAttitudeRecords();
            if (like === 1) {
              this.likeNumberAnimate = false;
              setTimeout(() => {
                this.likeNumberAnimate = true;
              }, 10);
            } else {
              this.dislikeNumberAnimate = false;
              setTimeout(() => {
                this.dislikeNumberAnimate = true;
              }, 10);
            }
          },
        }
      );
    },
    getPaperComments() {
      this.paperCommentFetched = true;
      this.ax.get(
        this.config.testEnvBackEndUrl + "paper/comments",
        { paper_id: this.paperId },
        {
          success: (response) => {
            this.paperCommentFetched = true;
            for (let comment of response.data.body.comment_list) {
              comment.time = dayjs(comment.time).format("YYYY/MM/DD HH:mm");
            }
            this.paperComments = response.data.body.comment_list;
          },
        }
      );
    },
    newTab() {
      window.open(this.paper.url, "_blank").focus();
      this.ax.post(
        this.config.testEnvBackEndUrl + "icde/go-paper-origin",
        {
          is_login: this.$store.state.isLogin,
          paper_id: this.paperId,
          paper_title: this.paperTitle,
        },
        {
          isAuth: this.$store.state.isLogin,
        }
      );
    },
    addComment() {
      this.ax.post(
        this.config.testEnvBackEndUrl + "paper/comment",
        {
          paper_id: this.paperId,
          comment: this.comment,
          paper_title: this.paper.title,
        },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            if (code === 0) {
              this.successToast("Comment success.");
              this.comment = "";
            }
          },
          final: () => {
            this.getPaperComments();
          },
        }
      );
    },
    fixHeight() {
      setTimeout(() => {
        // console.log(thiz.$refs.card.$el.scrollHeight);
        this.$refs.card.$el
          .getElementsByClassName("head-box")[0]
          .style.setProperty(
            "height",
            `${
              this.$refs.card.$el.getElementsByClassName("head-box")[0]
                .scrollHeight
            }px`
          );
        this.$refs.card.$el
          .getElementsByClassName("detail-box")[0]
          .style.setProperty(
            "height",
            `${
              this.$refs.card.$el.getElementsByClassName("detail-box")[0]
                .scrollHeight
            }px`
          );
      }, 350);
    },
    fetchTeamListAndSharedData(cb) {
      this.ax.get(
        this.config.testEnvBackEndUrl + "icde/shared-team-list",
        {
          paper_id: this.paperId,
        },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            const body = response.data.body;
            if (code === 0) {
              this.teamList = [...body.joined_team_list];
              this.paperOperatedData.shared = body.total_shared;
              if (cb !== undefined) cb();
            }
          },
        }
      );
    },
    shareThisPaperTo(team_id, team_name) {
      this.ax.post(
        this.config.testEnvBackEndUrl + "icde/share-paper",
        {
          paper_id: this.paperId,
          paper_title: this.paperTitle,
          team_id,
          team_name,
        },
        {
          isAuth: true,
          success: (response) => {
            const code = response.data.code;
            if (code === 0) {
              this.successToast("Share succeed.");
              this.sharedNumberAnimate = false;
              setTimeout(() => {
                this.sharedNumberAnimate = true;
              }, 10);
              this.fetchTeamListAndSharedData();
            }
          },
        }
      );
    },
  },
  computed: {
    hasDetail: function () {
      return this.paper.paperId !== "";
    },
    isLogin: function () {
      this.getPaperAttitudeRecords();
      return this.$store.state.isLogin;
    },
    likeBtnDisable: function () {
      if (this.isLogin) {
        if (!this.userAttitudeExist) {
          // attitude btn can be click
          return false;
        } else {
          if (this.userLikeThisPaper) {
            return true;
          } else {
            return false;
          }
        }
      }
      // disable when logout
      return true;
    },
    dislikeBtnDisable: function () {
      if (this.isLogin) {
        if (!this.userAttitudeExist) {
          return false;
        } else {
          if (this.userLikeThisPaper) {
            return false;
          } else {
            return true;
          }
        }
      }
      return true;
    },
  },
  mounted: function () {
    const routeParams = this.$route.params;
    this.paperId = routeParams.id;
    this.paperTitle = routeParams.paperTitle;
    // console.log(this.paperId);
    // console.log(this.paperTitle);
    this.getDetail(this.paperId);
    this.fetchTeamListAndSharedData();
    this.ax.post(
      this.config.testEnvBackEndUrl + "icde/go-paper-detail-page",
      {
        is_login: this.$store.state.isLogin,
        paper_id: this.paperId,
        paper_title: this.paperTitle,
      },
      {
        isAuth: this.$store.state.isLogin,
      }
    );
  },
  // beforeRouteEnter(to, from, next) {
  //   // console.log(to);
  //   // console.log(from);
  //   // console.log(next);
  //   next((ins) => {
  //     //   ins.getDetail(to.params.id);
  //   });
  // },
};
</script>

<style scoped>
.paper-detail-box {
  padding-bottom: 4em;
}
.comment-box {
  max-width: 750px;
  margin: auto;
  margin-top: 1rem;
}
.paper-data-label {
  width: 150px;
  display: inline-block;
  margin-right: 10px;
}
.v-card__title {
  padding: 12px 16px;
}
.detail-box {
  height: 192px;
}
.head-box {
  height: 56px;
}
.commenter {
  padding: 0 20px;
  padding-top: 20px;
}
.comment {
  margin: 8px 16px;
  padding: 6px 12px;
  border: solid 1px rgb(0 0 0 / 28%);
  border-radius: 4px;
}
.team_list_class {
  position: absolute;
  z-index: 10;
  right: 16px;
}
.team_item {
  display: block;
  width: 100%;
}
</style>
