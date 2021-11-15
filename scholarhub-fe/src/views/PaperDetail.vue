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
            <span>{{ paper.title }}</span></v-card-title
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
            <v-btn small class="ma-2 white--text" color="red">
              Downloads
            </v-btn>
            <v-btn small class="ma-2 white--text" color="green">
              <span class="mr-2">{{ paperOperatedData.likes }}</span>
              <span>Likes</span>
              <v-icon small color="white" class="ml-2"
                >mdi-thumb-up-outline</v-icon
              >
            </v-btn>
            <v-btn small class="ma-2 white--text darken-2" color="grey">
              <span class="mr-2">{{ paperOperatedData.dislikes }}</span>

              <span>Dislikes</span>
              <v-icon small color="white" class="ml-2"
                >mdi-thumb-down-outline</v-icon
              >
            </v-btn>
            <v-btn small class="ma-2 white--text" color="cyan">
              <span class="mr-2">{{ paperOperatedData.shared }}</span>

              <span>Share</span>

              <v-icon small color="white" class="ml-2"
                >mdi-share-variant-outline</v-icon
              >
            </v-btn>
          </div>
          <div v-else key="action-before-user-data">
            <v-skeleton-loader
              class="ma-2"
              type="button"
              max-height="28"
              style="display: inline-block"
            ></v-skeleton-loader
            ><v-skeleton-loader
              class="ma-2"
              type="button"
              max-height="28"
              style="display: inline-block"
            ></v-skeleton-loader
            ><v-skeleton-loader
              class="ma-2"
              type="button"
              max-height="28"
              style="display: inline-block"
            ></v-skeleton-loader
            ><v-skeleton-loader
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
            <strong>Abstract</strong>
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
      <div class="comment-box" v-show="isLogin">
        <v-card elevation="6">
          <v-card-subtitle class="unselectable"> Add Comments </v-card-subtitle>
          <v-divider></v-divider>
          <v-card-text>
            <v-textarea
              dense
              clear-icon="mdi-close-circle"
              v-model="comment"
              hide-details
            ></v-textarea>
          </v-card-text>
          <v-card-text class="clearfix pt-1">
            <v-btn
              style="float: right"
              small
              color="success"
              @click="addComment"
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
        <div v-else>
          <v-divider></v-divider>
          <div v-for="comment in paperComments" :key="comment.id" class="">
            <div class="commenter">
              <strong class="mr-2">{{ comment.name }}</strong>
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
export default {
  data: () => ({
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
    },
    paperOperatedData: {
      likes: 0,
      dislikes: 0,
      shared: 0,
    },
    paperComments: [],
    userActionLoaded: false,
    paperCommentFetched: false,
  }),
  methods: {
    getDetail(id) {
      console.log(id);
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
            // TODO: user action Data
            setTimeout(() => {
              this.userActionLoaded = true;
            }, 800);
            // TODO: paper comment
            setTimeout(() => {
              this.paperCommentFetched = true;
              this.paperComments = [
                {
                  id: "123",
                  name: "Jack",
                  time: "2021/10/1 18:30",
                  content: `Because of the subtleties of finding partial phrase matches in
                        different parts of the document, be cautious about interpreting
                        the total field as a count of documents containing any particular
                        word in the query.`,
                },
                {
                  id: "456",
                  name: "Jack",
                  time: "2021/10/1 18:30",
                  content: `Because of the subtleties of finding partial phrase matches in
                        different parts of the document, be cautious about interpreting
                        the total field as a count of documents containing any particular
                        word in the query.`,
                },
                {
                  id: "789",
                  name: "Jack",
                  time: "2021/10/1 18:30",
                  content: `Because of the subtleties of finding partial phrase matches in
                        different parts of the document, be cautious about interpreting
                        the total field as a count of documents containing any particular
                        word in the query.`,
                },
              ];
            }, 800);
          },
          error: () => {
            this.errorToast("Search API went wrong!");
          },
          final: this.fixHeight,
        }
      );
    },
    addComment: function () {
      const comment = this.comment;
      // TODO: time and request
      const obj = {
        content: comment,
        time: new Date().getTime(),
        id: new Date().getTime(),
        name: "Jack",
      };
      console.log(obj);
      this.paperComments.unshift(obj);
    },
    fixHeight: function () {
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
  },
  computed: {
    hasDetail: function () {
      return this.paper.paperId !== "";
    },
    isLogin: function () {
      return this.$store.state.isLogin;
    },
  },
  mounted: function () {
    this.getDetail(location.hash.split("/")[2]);
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
  padding: 0 16px;
  padding-top: 8px;
}
.comment {
  padding: 0 16px;
  padding-top: 4px;
  padding-bottom: 12px;
}
</style>
