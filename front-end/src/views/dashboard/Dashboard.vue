<template>
    <div class="page-dashboard">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Mesa de Operações</h1>
                <pre> {{ data.proposals }}</pre>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Dashboard',
    data() {
        return {
            data: {
                proposals: []
            }
        }
    },
    methods: {
        getProposals() {
            axios
                .get('http://localhost:8000/api/proposals/')
                .then(response => {
                    this.data.proposals = response.data
                })
                .catch(e => {
                    console.log(e)
                })
        }
    },
    async beforeMount() {
        await this.getProposals()
    }
}
</script>