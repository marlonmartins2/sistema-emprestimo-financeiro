<template>
  <div class="home">
    <h1 class="title">Bem vindo ao Serviço de empréstimo pessoal.</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
.title {
  font-size: 3em;
  text-align: center;
}
</style>