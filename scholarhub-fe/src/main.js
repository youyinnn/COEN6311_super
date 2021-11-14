import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";
import Footer from "@/components/Footer.vue";
import vuetify from "./plugins/vuetify";
import router from "./plugins/router";
import Toasted from "vue-toasted";
import config from "@/config/config";

Vue.config.productionTip = false;

Vue.use(Toasted);

const vueMap = new Map();
Vue.mixin({
  data: function () {
    return {
      vueMap: vueMap,
      mapKey: "",
      config: config,
    };
  },
  mounted: function () {
    // 方便在任意组件访问其他组件
    this.vueMap.set(this.$el.id, this);
    this.mapKey = this.$el.id;
  },
  methods: {
    toast(type, text, option) {
      let duration = 5000,
        closeable = false,
        position = "top-left",
        containerClass = "my-toast-container-left";
      if (option !== undefined) {
        if (option.closeable !== undefined) {
          closeable = option.closeable;
          if (closeable) {
            duration = 0;
          }
        } else if (option.duration !== undefined) {
          duration = option.duration;
        }
        if (option.position !== undefined) {
          position = option.position;
          if (position.endsWith("right")) {
            containerClass = "my-toast-container-right";
          }
        }
      }
      let toastOption = {
        position,
        duration,
        keepOnHover: true,
        className: "my-toast",
        containerClass,
        action: closeable
          ? {
              text: "CLOSE",
              onClick: (e, toastObject) => {
                toastObject.goAway(200);
              },
            }
          : undefined,
      };
      switch (type) {
        case "info":
          this.$toasted.info(text, toastOption);
          break;
        case "success":
          this.$toasted.success(text, toastOption);
          break;
        case "error":
          this.$toasted.error(text, toastOption);
          break;
      }
    },
    infoToast(text, option) {
      this.toast("info", text, option);
    },
    successToast(text, option) {
      this.toast("success", text, option);
    },
    errorToast(text, option) {
      this.toast("error", text, option);
    },
  },
});

Vue.use(Vuex);

const token = localStorage.getItem("token");
const isLogin = token !== null;

const store = new Vuex.Store({
  state: {
    isLogin: isLogin,
    token: token,
  },
  mutations: {
    login(state, payload) {
      state.isLogin = true;
      state.token = payload.token;
      localStorage.setItem("token", payload.token);
    },
    logout(state) {
      state.isLogin = false;
      state.token = "";
      localStorage.removeItem("token");
    },
  },
});

Vue.component("Footer", Footer);

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
