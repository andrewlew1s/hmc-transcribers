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
      state.data.first = payload
    },
    updateLast(state, payload){  
      state.data.last = payload
    },
    updateEmail(state, payload){  
      state.data.email = payload
    },
    updateLast(state, payload){  
      state.data.last = payload
    },
    updateAddress(state, payload){  
      state.data.address = payload
    },
    updatePhone(state, payload){  
      state.data.phone = payload
    },
    updateState(state, payload){  
      state.data.state = payload
    },
    updateTitle(state, payload){  
      state.data.title = payload
    }
  }
})

// store.commit('updateData')
