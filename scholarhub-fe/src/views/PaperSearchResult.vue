<template>
  <v-container>
    <div class="search-bar-box">
      <SearchBar dense loading></SearchBar>
    </div>
    <v-divider class="mt-4 mb-4"></v-divider>
    <div class="paper-list-box">
      <v-hover class="paper-card" v-for="paper in paperData" :key="paper.id">
        <template v-slot:default="{ hover }">
          <v-card
            class="mx-auto default-transit3 mb-4"
            max-width="700"
            :elevation="hover ? 8 : 2"
          >
            <v-card-title>{{ paper.title }}</v-card-title>

            <v-card-subtitle class="pb-0">
              <div>
                <span class="paper-data-label"><strong>Author(s)</strong></span>
                <span v-if="paper.authors.size == 0">No Author</span>
                <v-chip
                  class="mr-2"
                  v-else
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
            </v-card-text>
            <v-card-actions class="paper-card-action d-flex justify-end">
              <v-btn small class="ma-2" outlined color="red"> Downloads </v-btn>
              <v-btn small class="ma-2" outlined color="indigo">
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
    </div>
  </v-container>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  data: () => ({
    paperData: [
      {
        id: "4c17fca90e8bfb3e0c66887a0b119774dd70ca3c",
        title: "Personal Health Record Using Cloudcomputing Technology",
        abstract: null,
        venue: "Indian Journal of Public Health Research & Development",
        year: 2020,
        citationCount: 0,
        authors: [],
      },
      {
        id: "d30ab3e78db2131b4e92a87afa235a2db2275d2d",
        title:
          "ARTIFICIAL INTELLIGENCE BASED INTRUSIONDETECTION ANALYSIS USING CLOUDCOMPUTING",
        abstract:
          "A model for intrusion detection may be based on the methods based on an structure and focus. We will create a \nmodel for the identification of intrusion to recognise frame assaults and develop the structures using the \ncollected information. The acquired NSLKDD information index can be decreased and the location of \ninterruption can be enhanced by using the collected information by using the highlight determination method in \nAI. Through AI methods, the structure of interruption position can be created through increasing the number of \nnew occult attacks. IDS help to shield the framework from the assailant. In this examination work, IDS is \nintended to recognize malevolent hub by utilizing improvement and AI (Artificial Intelligence) strategies. The \ninformation is improved utilizing firefly calculation. The firefly calculation is a meta-heuristic methodology \nwhich is motivated by the conduct of fireflies. The improvement calculation assists with finding the best \nelement. Based on removed highlights the SVM (Support vector machine) is prepared. SVM is a double \nclassifier which is utilized to take care of multi-class issues. In this exploration work, SVM is utilized to \nrecognize assailant hubs and authentic hubs. Subsequently, rather than passing information to the aggressor hub, \nthe hub passes the information to the certifiable hub and consequently, the framework is ensured. To know the \npresentation of the framework, QoS (Quality of administration) boundaries, for example, PDR (Packet \nconveyance proportion), vitality utilization rate and complete postponement with and without anticipation \ncalculation are estimated. The execution has been done in CLOUDSIM condition.",
        venue: "",
        year: 2020,
        citationCount: 0,
        authors: [
          {
            authorId: "152673317",
            name: "V. Suryanarayana",
          },
          {
            authorId: "2019917597",
            name: "P.Jagadeesh",
          },
          {
            authorId: "2110180079",
            name: "Avinash Kumar",
          },
          {
            authorId: "144185355",
            name: "M. V. Rao",
          },
        ],
      },
      {
        id: "b00fdf9dc71befab368f5f038793a3a97762d71b",
        title:
          "HASH ALGORITHM FOR SECURE DATA TRANSMISSION USING QR CODE IN CLOUDCOMPUTING",
        abstract:
          "It has huge calculation capacity and immense memory space requiring little to no effort. \nEstablishments that offer types of assistance in distributed computing are called suppliers. Validation and \ninformation security is a major test for arranging, building and system activity. Distributed computing is a \nsignificant pattern in Information Technology all through the world through application advancement, enormous \ninformation stockpiling and recuperation, site facilitating, on-request programming conveyance. Presently a \ndays cloud information security strategy utilizes symmetric and uneven encryption calculations with the solid \nconfirmation procedures. Distributed computing is the coordinated frameworks over the web. This paper \nsuggests that another technique to approve the advanced archives utilizing hash calculation with QR Code \nencryption. It gives secure information partaking in distributed computing in cutting edge technique.",
        venue: "",
        year: 2020,
        citationCount: 0,
        authors: [
          {
            authorId: "2004298091",
            name: "S. Thulasidass",
          },
          {
            authorId: "2003351538",
            name: "S. Vanakovarayan",
          },
          {
            authorId: "1750368358",
            name: "D. Murali",
          },
          {
            authorId: "52424631",
            name: "T. Priyaradhikadevi",
          },
        ],
      },
      {
        id: "2c23a421922fed91319373ad4f0cd07ebcb28e32",
        title:
          "LOAD BALANCING ALGORITHM FOR OPTIMAL RESOURCE UTILIZATION IN CLOUDCOMPUTING ENVIRONMENT",
        abstract: null,
        venue: "",
        year: 2019,
        citationCount: 0,
        authors: [
          {
            authorId: "1573561007",
            name: "Bekema Gidissa Dadi",
          },
        ],
      },
      {
        id: "5c1d5b83be47c612d017431aafaa92af4351fe53",
        title: "Integrating Wireless Sensor Networks with Cloudcomputing",
        abstract:
          "wireless sensor network (WSN) is an unmistakable innovation for a long while. In most genuine applications, the immense measure of information assembled utilizing sensors are required to be put away and be made accessible for whenever, anyplace get to. However, WSNs are made out of asset obliged gadgets which absence of abilities to store gigantic lump of information and perform ensuing preparing of the information. WSNs can be increased by cloud condition which offers such administrations. Thus, a Sensor-Cloud structure is imagined in this proposition coordinating remote sensor connect with cloud condition. The coordinated system is appropriate for versatile and unavoidable figuring applications empowering Internet of Things (IoT) and planned to be utilized in genuine applications. Creating countries need proportionate social insurance conveyance answers for serve gigantic populace. This proposition features the issues identified with medicinal services conveyance that might be tended to utilizing the incorporated system. It might be utilized for empowering individuals, networks, medicinal services associations to gather and transmit wellbeing data as and when required so as to improve social insurance administrations for the provincial and urban populace. Inside the IoT empowered structure, few difficulties are recognized for examination. This theory stresses on difficulties including remote sensors and gives specialized answers for these difficulties. WSNs ordinarily work on IEEE 802.15.4 standard utilizing exclusive conventions which includes structure and the board unpredictability when combined with Internet. This postulation furnishes answer for coordinate sensor worldview with cloud condition which depends on",
        venue:
          "International Journal of Innovative Technology and Exploring Engineering",
        year: 2019,
        citationCount: 0,
        authors: [
          {
            authorId: "143948343",
            name: "G. N. Reddy",
          },
          {
            authorId: "2069712495",
            name: "B. Reddy",
          },
          {
            authorId: "7785753",
            name: "E. Babu",
          },
          {
            authorId: "35990103",
            name: "P. Prakash",
          },
        ],
      },
      {
        id: "f0a97f598d66e1578021b45b2ba7d3acb111b4ac",
        title: "Afandi.19421058.CloudComputing.2",
        abstract: "Afandi.19421058.CloudComputing.2",
        venue: "",
        year: 2021,
        citationCount: 0,
        authors: [
          {
            authorId: "2136244377",
            name: "Afandi Akbar",
          },
        ],
      },
      {
        id: "b012a7f316808987b3e4d06f8f29da2474c10a32",
        title: "Afandi.19421058.CloudComputing.3",
        abstract: "Afandi.19421058.CloudComputing.3",
        venue: "",
        year: 2021,
        citationCount: 0,
        authors: [
          {
            authorId: "2136244377",
            name: "Afandi Akbar",
          },
        ],
      },
      {
        id: "d93b841d18d37cc70eadc25446483cabc70edd12",
        title:
          "Konsep Sistem Informasi Akreditasi Perguruan Tinggi Berbasis Cloudcomputing",
        abstract:
          "Akreditasi perguruan tinggi adalah bentuk pengakuan pemerintah berupa penilaian terhadap lembaga penyelenggara pendidikan tinggi yang meliputi semua aspek yang ada berdasarkan standar nasional pendidikan tinggi, dalam menunjang proses belajar. Akreditasi ini dilaksanakan oleh Badan Akreditasi Nasional Perguruan Tinggi yang dibentuk pemerintah. Banyaknya persiapan data yang diperlukan untuk pelaksanaan Akreditasi perguruan tinggi yang hampir sebagian besar masih menggunakan cara manual atau semi komputerisasi yang tidak saling terhubung, merupakan sebuah kondisi yang masih terjadi sekarang ini. Tahapan yang akan dilakukan adalah mengumpulkan seluruh dokumen yang ada dalam akreditasi perguruan tinggi untuk dikonversi berbasis elektronik. Tujuan penelitian ini adalah merancang sistem informasi akreditasi perguruan tinggi berbasis cloudcomputing yang akan memudahkan komunikasi ilmiah antara perguruan tinggi dengan asesor dalam pengolahan data. Metode penelitian yang digunakan adalah importif terapan, langkah ini diambil untuk menerapkan, menguji dan mengevaluasi kondisi yang ada berkenaan dengan penemuan dan pengembangan ilmu dalam memudahkan sistem akreditasi perguruan tinggi sekarang ini, semua yang akan terlibat dapat melaksanakan tugas masing-masing dimana dan kapan saja, adapun hasil yang ingin dicapai pada penelitian ini adalah memudahkan perguruan tinggi dalam menyiapkan data akreditasi yang telah terkoneksi dengan sistsm informasi kampus dan juga memudahkan asesor dalam pelaksanaan tugas.  Kata kunci: Sistem Informasi Akreditasi Perguruan Tinggi, Cloudcomputing",
        venue: "",
        year: 2018,
        citationCount: 0,
        authors: [
          {
            authorId: "2093781026",
            name: "Sulfikar Sallu",
          },
          {
            authorId: "133846330",
            name: "D. N.",
          },
        ],
      },
      {
        id: "09be3798ee74ebbbd924a1e1dbdd63acef6a16ab",
        title:
          "Guaranted QOS with Profit Maximization Scheme in CloudComputing",
        abstract: null,
        venue: "",
        year: 2018,
        citationCount: 0,
        authors: [
          {
            authorId: "145572814",
            name: "A. S. Archana",
          },
        ],
      },
      {
        id: "89a879cf8f7658ea963dd4ab5af44e4f1e85fb01",
        title:
          "Guaranted QOS with Profit Maximization Scheme in CloudComputing",
        abstract: null,
        venue: "",
        year: 2018,
        citationCount: 0,
        authors: [
          {
            authorId: "97851317",
            name: "S. AnushaK",
          },
          {
            authorId: "98292985",
            name: "C. ArchanaH",
          },
          {
            authorId: "97510530",
            name: "M. JeevithaH",
          },
          {
            authorId: "153824947",
            name: "P. Sindhu",
          },
          {
            authorId: "98253798",
            name: "D. NandishKumar",
          },
        ],
      },
    ],
  }),
  components: {
    SearchBar,
  },
};
</script>

<style scoped>
.search-bar-box {
}
.paper-data-label {
  width: 62px;
  display: inline-block;
  margin-right: 10px;
}
.v-expansion-panel-header {
}
.paper-list-box {
}
.paper-card {
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
</style>
