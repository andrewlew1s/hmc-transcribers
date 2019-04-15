import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  namespaced: true,
  state: {
    data: [
      {type: '', confidence: 0, start_pos: 0, end_pos: 0, text: 0}
    ]
  },

  mutations: {
    updateData(state, payload){  
      state.data.type = payload
    }
  }
})

// store.commit('updateData')
