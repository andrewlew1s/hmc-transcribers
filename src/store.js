import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  namespaced: true,
  state: {
    data: [
      {first: '', last: '', email: '', address: '', address2: '', phone: 0, fax: 0, city: '', state: '', zip: 0, country: '', title: '', company: ''}
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
    updateAddress2(state, payload){
      state.data.address2 = ''  
      state.data.address2 = payload
    },
    updatePhone(state, payload){
      state.data.phone = 0  
      state.data.phone = payload
    },
    updateFax(state, payload){
      state.data.fax = ''  
      state.data.fax = payload
    },
    updateCity(state, payload){
      state.data.city = ''  
      state.data.city = payload
    },
    updateState(state, payload){
      state.data.state = ''  
      state.data.state = payload
    },
    updateZip(state, payload){
      state.data.zip = ''  
      state.data.zip = payload
    },
    updateCountry(state, payload){
      state.data.country = ''  
      state.data.country = payload
    },
    updateTitle(state, payload){
      state.data.title = ''  
      state.data.title = payload
    },
    updateCompany(state, payload){
      state.data.company = ''  
      state.data.company = payload
    },
    addData(state, array){
      state.data.push(array)
    }
  }
})