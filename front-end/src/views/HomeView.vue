<template>
  <div class="page-signup">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Solicitação de empréstimo</h1>

        <form @submit.prevent="submitForm">

          <div class="field">
            <label>Nome Completo</label>
            <div class="control">
                <input class="input" type="text" name="full_name" v-model="full_name">
            </div>
          </div>

          <div class="field">
            <label>CPF</label>
              <div class="control">
                <input type="text" class="input" name="document" v-model="document">
              </div>
          </div>

          <div class="field">
            <label>Endereço</label>
              <div class="control">
                <input type="text" class="input" name="address" v-model="address">
              </div>
          </div>

          <div class="field">
            <label>Complemento</label>
              <div class="control">
                <input type="text" class="input" name="complement" v-model="complement">
              </div>
          </div>

          <div class="field">
            <label>CEP</label>
              <div class="control">
                <input type="text" class="input" name="zip_code" v-model="zip_code">
              </div>
          </div>

          <div class="field">
            <label>Valor do empréstimo</label>
            <div class="control">
                <input class="input" type="text"  name="proposal_value" v-model.number="proposal_value">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Enviar proposta</button>
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
  name: 'HomeView',
  data () {
      return {
        full_name: '',
        document: '',
        address: '',
        complement: '',
        zip_code: '',
        proposal_value: '',
        errors: []
      }
  },
  methods: {
    submitForm (e) {
      const formData = {
        full_name: this.full_name,
        document: this.document,
        address: this.address,
        complement: this.complement,
        zip_code: this.zip_code,
        proposal_value: this.proposal_value
      }
      
      if (formData.full_name === '') {
        this.errors.push('Nome é obrigatório.')
      }

      if (formData.document === '') {
        this.errors.push('CPF é obrigatório.')
      }

      if (formData.proposal_value === '') {
        this.errors.push('Valor do empréstimo é obrigatório.')
      }

      formData.address = {
        "address": formData.address,
        "complement": formData.complement,
        "zip_code": formData.zip_code,
      }

      delete formData.complement
      delete formData.zip_code

      axios.post('http://localhost:8000/api/proposals/', formData)
        .then(response => {
          console.log(response)
        })
        .catch(e => {
          console.log(e)
        })
    }
  },
}
</script>

<style scoped>
.title {
  font-size: 3em;
  text-align: center;
}

.field {
  text-align: center;
}

.input {
  border-radius: 50px;
}

.button {
  border-radius: 50px;
  margin-top: 20px;
  width: 100%;
}
</style>