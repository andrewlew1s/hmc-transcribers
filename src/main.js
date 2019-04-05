import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router';
import Vuetify from 'vuetify'
import VueScrollTo from 'vue-scrollto';
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)
Vue.use(VueScrollTo, { offset: -61, duration: 800, });
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
