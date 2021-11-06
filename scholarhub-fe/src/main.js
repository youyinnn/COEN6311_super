import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import Toasted from "vue-toasted";

Vue.config.productionTip = false;

Vue.use(Toasted);

const vueMap = new Map();
Vue.mixin({
  data: function () {
    return {
      vueMap: vueMap,
      mapKey: "",
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
        closeable = false;
      if (option !== undefined) {
        if (option.closeable !== undefined) {
          closeable = option.closeable;
          if (closeable) {
            duration = 0;
          }
        } else if (option.duration !== undefined) {
          duration = option.duration;
        }
      }
      let toastOption = {
        position: "top-right",
        duration: duration,
        keepOnHover: true,
        className: "my-toast",
        containerClass: "my-toast-container",
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

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
