<template>
    <div class="page-signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Cadastro</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input class="input" type="text" name="username" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>CPF</label>
                        <div class="control">
                            <input type="text" class="input" name="document" v-model="document">
                        </div>
                    </div>

                    <div class="field">
                        <label>Senha</label>
                        <div class="control">
                            <input class="input" type="password"  name="password" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Cadastrar</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data () {
        return {
            username: '',
            password: '',
            document: '',
            errors: []
        }
    },
    methods: {
        submitForm (e) {
            const formData = {
                username: this.username,
                password: this.password,
                document: this.document,
            }

            if (formData.username === '') {
                this.errors.push('Username é obrigatório.')
            }

            if (formData.password === '') {
                this.errors.push('Senha é obrigatória.')
            }

            if (formData.document === '') {
                this.errors.push('CPF é obrigatório.')
            }

            if (formData.password.length < 8) {
                this.errors.push('Senha deve ter no mínimo 8 caracteres.')
            }

            if (!this.errors.length) {
                axios
                    .post("api/user/", formData)
                    .then(response => {
                        toast({
                            message: 'Cadastro realizado com sucesso!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            position: 'top-center',
                            duration: 2000
                        })
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            console.log(JSON.stringify(error.message))
                        } else {
                            console.log(JSON.stringify(error.response.data))
                        }

                        toast({
                            message: this.errors,
                            type: 'is-danger',
                            dismissible: true,
                            pauseOnHover: true,
                            position: 'top-center',
                            duration: 2000
                        })
                    })
            }
        }
    }
}
</script>