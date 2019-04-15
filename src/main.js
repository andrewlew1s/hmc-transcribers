import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router';
import Vuetify from 'vuetify'
import VueScrollTo from 'vue-scrollto';
import 'vuetify/dist/vuetify.min.css'
import * as firebase from 'firebase'
import Vuex from 'vuex'
import { store } from './store';


Vue.use(Vuex)
Vue.use(Vuetify)
Vue.use(VueScrollTo, { offset: -61, duration: 800, });
Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
  created () {
    firebase.initializeApp({
      apiKey: "AIzaSyCrQrzpGmwxtICzplBfV4kFw02CYPYHxdc",
      authDomain: "hmc-transcribers.firebaseapp.com",
      databaseURL: "https://hmc-transcribers.firebaseio.com",
      projectId: "hmc-transcribers",
      storageBucket: "gs://hmc-transcribers.appspot.com",
      messagingSenderId: "859954806298"
    }) 
  }
}).$mount('#app')
