<template>
    <div class="page-dashboard">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Mesa de Operações</h1>
                <table>
                    <tr class="tr">
                        <th>id</th>
                        <th>Nome</th>
                        <th>CPF</th>
                        <th>Valor</th>
                        <th>Data Solicitação</th>
                        <th>status</th>
                    </tr>

                    <tr v-for="proposal in data.proposals.results" :key="proposal.id">
                        <td class="td">{{ proposal.id }}</td>
                        <td class="td">{{ proposal.full_name }}</td>
                        <td class="td">{{ proposal.document }}</td>
                        <td class="td">{{ proposal.proposal_value }}</td>
                        <td class="td">{{ proposal.created_at }}</td>
                        <td>
                            <div class="status" :class="{
                                'status-pending': proposal.status === 'pending',
                                'status-accept': proposal.status === 'accepted',
                                'status-declined': proposal.status === 'declined',
                                'status-expired': proposal.status === 'expired',
                            }">
                                {{ proposal.status }}
                            </div>
                        </td>
                        </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Dashboard",
    data() {
        return {
            data: {
                proposals: [],
            },
        };
    },
    methods: {
        getProposals() {
            axios
                .get("http://localhost:8000/api/proposals/")
                .then((response) => {
                    this.data.proposals = response.data;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
    async beforeMount() {
        await this.getProposals();
    },
};
</script>

<style scoped>
.title {
    margin-bottom: 20px;
    font-weight: bold;
    text-align: center;
}

.button {
    border-radius: 10px;
}

.status {
    text-align: center;
    padding: 2px;
    border-radius: 8px;
    font-weight: bold;
    text-transform: uppercase;
}

.status-accept {
    background-color: lightgreen;
    color: white;
}
.status-declined {
    background-color: rgba(255, 0, 0, 0.8);
    color: white;
}

.status-pending {
    background-color: rgb(243, 243, 117);
    color: grey;
}

.status-expired {
    background-color: grey;
    color: black;
}

table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

table td, table th {
  border: 1px solid #000000;
  padding: 8px;
  text-align: center;
}

.tr th {
    text-align: center;
    text-transform: uppercase;
}

table tr:nth-child(even){background-color: #f2f2f2;}

table tr:hover {background-color: #ddd;}

table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: rgba(54, 54, 54, 0.9);
  color: white;
}
</style>