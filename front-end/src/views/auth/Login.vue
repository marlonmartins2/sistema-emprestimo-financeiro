<template>
    <div class="page-login">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Login</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Usuário</label>
                        <div class="control">
                            <input class="input" type="text" required="" name="username" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Senha</label>
                        <div class="control">
                            <input class="input" type="password" required="" name="password" v-model="password">
                        </div>
                    </div>

                    <div class="notification is_danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Login</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password,
            }

            if (formData.username === '') {
                this.errors.push('Usuário é obrigatório.')
            }

            if (formData.password === '') {
                this.errors.push('Senha é obrigatória.')
            }

            axios
                .post("/api/login/", formData)
                .then(response => {
                    const token = response.data.access

                    const refresh = response.data.refresh

                    this.$store.commit('setToken', token, refresh)
                    
                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + token

                    localStorage.setItem('token', token)

                    localStorage.setItem('refresh', refresh)
                    
                    this.$router.push('/dashboard')
                })
                .catch(error => {
                    this.errors.push('Usuário ou senha inválidos.')
                })
        }
    }
}
</script>