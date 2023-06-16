<template>
    <div class="page-logout">
        <h1 class="title">Logout</h1>

        <button @click="logout()" class="button is-danger">Logout</button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Logout',
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')

            localStorage.removeItem('refresh')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>