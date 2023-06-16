import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      username: '',
    },
    isAuthenticated: false,
    token: '',
    refresh: '',
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.refresh = localStorage.getItem('refresh')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, access_token, refresh_token) {
      state.token = access_token
      state.refresh = refresh_token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
