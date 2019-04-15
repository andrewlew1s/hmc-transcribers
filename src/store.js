import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  namespaced: true,
  state: {
    data: []
  },

  mutations: {
    updateData(state, payload){  
      state.data.push(payload)
    }
  }
})

// store.commit('updateData')
