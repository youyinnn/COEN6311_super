// https://cli.vuejs.org/config/#global-cli-config

module.exports = {
  publicPath: "./",

  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Scholar Hub";
      return args;
    });
  },

  transpileDependencies: [
    'vuetify'
  ]
};
