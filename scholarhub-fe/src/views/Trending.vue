<template>
  <div class="trending-box">
    <p class="trending-header text-h4">
      <v-icon large color="blue-gray" class="mr-1">mdi-trending-up</v-icon>

      Top 30 Trending
    </p>
    <v-divider class="elevation-4"></v-divider>
    <v-toolbar
      class="trending-tab-bar mt-2 d-flex align-end"
      color="blue-gray"
      flat
      height="40px"
      width="700px"
    >
      <v-tabs class="mt-2" v-model="tab" color="green">
        <v-tab>Search Terms</v-tab>
        <v-tab>Click Rates</v-tab>
        <v-tab>Likes</v-tab>
        <v-tab>Dislikes</v-tab>
        <v-tab>Most shared</v-tab>
      </v-tabs>
    </v-toolbar>
    <div
      :class="{
        'mt-6': true,
        'trending-list-box': true,
        animate__animated: true,
        animate__fadeIn: true,
      }"
    >
      <transition name="slide-r-fade" mode="out-in">
        <v-data-table
          v-if="tab === 0"
          key="tab0"
          :headers="termHeader"
          :items="displayTrendingData[tab]"
          class="elevation-4 data-table"
          hide-default-footer
          disable-pagination
          disable-sort
          disable-filtering
        >
          <template v-slot:[`item.paper_title`]="{ item }">
            <a :href="item.href">{{ item.paper_title }}</a>
          </template>
        </v-data-table>
        <v-data-table
          v-else-if="tab === 1"
          key="tab1"
          :headers="titleHeader"
          :items="displayTrendingData[tab]"
          class="elevation-4 data-table"
          hide-default-footer
          disable-pagination
          disable-sort
          disable-filtering
        >
          <template v-slot:[`item.paper_title`]="{ item }">
            <a :href="item.href">{{ item.paper_title }}</a>
          </template>
        </v-data-table>
        <v-data-table
          v-else-if="tab === 2"
          key="tab2"
          :headers="titleHeader"
          :items="displayTrendingData[tab]"
          class="elevation-4 data-table"
          hide-default-footer
          disable-pagination
          disable-sort
          disable-filtering
        >
          <template v-slot:[`item.paper_title`]="{ item }">
            <a :href="item.href">{{ item.paper_title }}</a>
          </template>
        </v-data-table>
        <v-data-table
          v-else-if="tab === 3"
          key="tab3"
          :headers="titleHeader"
          :items="displayTrendingData[tab]"
          class="elevation-4 data-table"
          hide-default-footer
          disable-pagination
          disable-sort
          disable-filtering
        >
          <template v-slot:[`item.paper_title`]="{ item }">
            <a :href="item.href">{{ item.paper_title }}</a>
          </template>
        </v-data-table>
        <v-data-table
          v-else-if="tab === 4"
          key="tab4"
          :headers="titleHeader"
          :items="displayTrendingData[tab]"
          class="elevation-4 data-table"
          hide-default-footer
          disable-pagination
          disable-sort
          disable-filtering
        >
          <template v-slot:[`item.paper_title`]="{ item }">
            <a :href="item.href">{{ item.paper_title }}</a>
          </template>
        </v-data-table>
      </transition>
    </div>
    <Footer abs />
  </div>
</template>

<script>
import "animate.css";

const termHeader = [
  {
    text: "Rank",
    align: "center",
    value: "rank",
    width: "50px",
  },
  { text: "Term", align: "start", value: "input_text" },
  { text: "Count", align: "center", width: "50px", value: "count" },
];

const titleHeader = [
  {
    text: "Rank",
    align: "center",
    value: "rank",
    width: "50px",
  },
  { text: "Title", align: "start", value: "paper_title" },
  { text: "Count", align: "center", width: "50px", value: "count" },
];

export default {
  data: () => ({
    tab: 0,
    termHeader,
    titleHeader,
    headers: termHeader,
    displayTrendingData: [[]],
  }),
  methods: {
    fetchAllTrendingList() {
      this.ax.get(
        this.config.testEnvBackEndUrl + "icde/access/all-trending",
        {},
        {
          success: (request) => {
            const code = request.data.code;
            if (code === 0) {
              this.displayTrendingData = request.data.body.tranding_list;
              for (let list of this.displayTrendingData) {
                for (let record_index in list) {
                  list[record_index].rank = Number(record_index) + 1;
                  if (list[record_index].paper_title !== undefined) {
                    list[
                      record_index
                    ].href = `${location.origin}/#/paper/${list[record_index].paper_title}/${list[record_index].paper_id}`;
                  }
                }
              }
            }
          },
        }
      );
    },
  },
  watch: {
    tab: function (newV) {
      if (newV === 0) {
        this.headers = termHeader;
      } else {
        this.headers = titleHeader;
      }
    },
  },
  mounted: function () {
    this.fetchAllTrendingList();
  },
};
</script>

<style scoped>
.trending-box {
  margin: auto;
  max-width: 900px;
  bottom: 0;
  top: 0;
  right: 0;
  left: 0;
}
.trending-header {
  max-width: 700px;
  margin: 2rem auto 0.5rem;
}
.trending-tab-bar {
  margin: auto;
}
.trending-list-box {
  animation-duration: 0.6s;
  animation-delay: 0.2s;
  animation-timing-function: ease-in-out;
}
.data-table {
  margin: auto;
  margin-bottom: 4rem;
  width: 700px;
}
</style>
