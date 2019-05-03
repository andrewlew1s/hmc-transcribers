import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  namespaced: true,
  state: {
    data: [
      {first: '', last: '', email: '', address: '', phone: 0, state: '', title: ''}
    ]
  },

  mutations: {
    updateFirst(state, payload){
      state.data.first = ''  
      state.data.first = payload
    },
    updateLast(state, payload){
      state.data.last = ''  
      state.data.last = payload
    },
    updateEmail(state, payload){
      state.data.email = ''  
      state.data.email = payload
    },
    updateAddress(state, payload){
      state.data.address = ''  
      state.data.address = payload
    },
    updatePhone(state, payload){
      state.data.phone = 0  
      state.data.phone = payload
    },
    updateState(state, payload){
      state.data.state = ''  
      state.data.state = payload
    },
    updateTitle(state, payload){
      state.data.title = ''  
      state.data.title = payload
    },
    addData(state, array){
      state.data.push(array)
    }
  }
})

// store.commit('updateData')
