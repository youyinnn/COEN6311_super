<template>
  <div id="paperSearchResult" class="paper-search-result">
    <div class="search-bar-box">
      <SearchBar ref="searchBar" dense loading></SearchBar>
    </div>
    <div style="width: 100%; max-width: 900px; margin: auto" class="mt-4 mb-4">
      <v-divider></v-divider>
    </div>
    <transition name="slide-fade" mode="out-in">
      <div key="paper-list-box" v-if="hasResult" class="paper-list-box">
        <div class="hint">
          <strong class="mr-2">{{ dataTotal }} result of:</strong
          ><span>{{ historySearchTerm }}</span>
        </div>
        <div v-if="hasResult" class="text-center mt-2 mb-6 unselectable">
          <v-pagination
            v-model="page"
            :length="pageTotal"
            :total-visible="7"
            @input="pageChange"
          ></v-pagination>
        </div>
        <transition-group name="fade" mode="out-in">
          <v-hover
            class="paper-card"
            v-for="paper in paperData"
            :key="paper.paperId"
          >
            <template v-slot:default="{ hover }">
              <v-card
                :class="{
                  'mx-auto': true,
                  'default-transit3': true,
                  'mb-4': true,
                }"
                max-width="700"
                :elevation="hover ? 10 : 1"
              >
                <v-card-title>{{ paper.title }}</v-card-title>

                <v-card-subtitle class="pb-0">
                  <div>
                    <span style="width: 70px" class="paper-data-label"
                      ><strong>Author(s)</strong></span
                    >
                    <v-chip
                      class="mr-2 mt-1 mb-1"
                      v-for="author in paper.authors"
                      :key="author.authorId"
                      small
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
                <v-card-actions class="paper-card-action d-flex justify-end">
                  <v-btn small class="ma-2" outlined color="red">
                    Downloads
                  </v-btn>
                  <v-btn
                    small
                    class="ma-2"
                    outlined
                    color="indigo"
                    @click="goDetail(paper.paperId)"
                  >
                    Details
                  </v-btn>
                </v-card-actions>
                <v-expansion-panels>
                  <v-expansion-panel>
                    <v-expansion-panel-header>
                      Abstract
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
            </template>
          </v-hover>
          <div key="unuse" style="height: 1px" class="mb-6"></div>
        </transition-group>

        <Footer />
      </div>
      <div
        key="no-result"
        v-else
        class="no-result d-flex align-center justify-center"
      >
        <div style="transform: translateY(-20%)">
          <!-- <div> -->
          <v-img max-height="200" max-width="200" src="@/assets/img/search.png">
          </v-img>
          <div style="padding: 10px">Key in you searh term</div>
        </div>
        <Footer abs />
      </div>
    </transition>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  data: () => ({
    dataTotal: 0,
    page: 1,
    pageTotal: 1,
    paperData: [],
    historySearchTerm: "<nothing>",
  }),
  components: {
    SearchBar,
  },
  methods: {
    showResult(st, data, page) {
      this.clearResult();
      this.historySearchTerm = st;
      if (data.total > 9999) {
        this.pageTotal = 999;
      } else {
        this.pageTotal = Math.floor(data.total / 10);
      }
      this.dataTotal = data.total;
      this.paperData = data.data;
      if (page !== undefined) {
        this.page = page;
        sessionStorage.setItem("currentPage", page);
      }
    },
    clearResult() {
      this.paperData = [];
      this.page = 1;
      this.dataTotal = 0;
      this.pageTotal = 0;
    },
    pageChange(e) {
      const currentPage = Number(sessionStorage.getItem("currentPage"));
      if (currentPage !== e) {
        // console.log(e);
        // console.log(this.historySearchTerm);
        // console.log(this.$refs);
        this.$refs.searchBar.search(this.historySearchTerm, e);
        this.$router.push({
          path: `/papers`,
          query: {
            query: this.historySearchTerm,
            page: e,
          },
        });
        sessionStorage.setItem("currentPage", e);
      }
    },
    goDetail(id) {
      this.$router.push({
        path: `/paper/${id}`,
      });
    },
  },
  beforeRouteEnter(to, from, next) {
    // console.log(from);
    // console.log(next);
    // called before the route that renders this component is confirmed.
    // does NOT have access to `this` component instance,
    // because it has not been created yet when this guard is called!
    next((ins) => {
      ins.historySearchTerm = to.query.query;
      ins.page = Number(to.query.page);
      //   console.log(ins.historySearchTerm);
      if (ins.historySearchTerm !== undefined) {
        ins.$refs.searchBar.search(ins.historySearchTerm, ins.page);
        ins.clearResult();
      }
    });
  },
  computed: {
    hasResult: function () {
      return this.dataTotal > 0;
    },
  },
};
</script>

<style scoped>
.paper-search-result {
  position: absolute;
  margin: auto;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  padding-top: 20px;
}
.search-bar-box {
  width: 100%;
}
.paper-data-label {
  width: 150px;
  display: inline-block;
  margin-right: 10px;
}
.v-expansion-panel-header {
}
.paper-list-box {
  width: 100%;
}
.paper-card {
}
.no-result {
  margin: auto;
  position: absolute;
  top: 90px;
  bottom: 0;
  left: 0;
  right: 0;
}
.paper-card-action > button {
  float: right;
}
.paper-card {
  /* background-color: #fefbf3 !important; */
}
.paper-card > .v-card__title {
  background-color: #bcd8d3;
}
.paper-card > .v-card__subtitle {
  margin-top: 16px;
}
.paper-card > .v-card__text {
  padding-bottom: 0;
}
.paper-card > .v-card__actions {
  padding-top: 0;
  padding-bottom: 0;
}
.paper-card > .v-expansion-panels > * {
  /* background-color: #f8f0df !important; */
}
.hint {
  max-width: 700px;
  margin: auto;
  margin-bottom: 1rem;
}
</style>
