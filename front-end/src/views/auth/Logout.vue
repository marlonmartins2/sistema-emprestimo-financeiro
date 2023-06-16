<template>
    <div class="page-logout">
        <h1 class="title">Logout</h1>

        <button @click="logout()" class="button is-danger">Logout</button>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'Logout',
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')

            localStorage.removeItem('refresh')

            this.$store.commit('removeToken')

            toast({
                message: 'Logout Concluído',
                type: 'is-warning',
                dismissible: true,
                pauseOnHover: true,
                position: 'top-center',
                duration: 2000
            })

            this.$router.push('/')
        }
    }
}
</script>