<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Minha conta</h1>
      </div>

      <div class="column is-12">
        <button @click="logout()" class="button is-danger">Sair</button>
      </div>

      <hr>

      <div class="column is-12">
        <h2 class="subtitle">Meus lances</h2>

        <!-- <OrderSummary
          v-for="order in orders"
          v-bind:key="order.id"
          v-bind:order="order"
        /> -->
      </div>

      <div class="column is-12">
        <h2 class="subtitle">Meus leilões</h2>

        <!-- <OrderSummary
          v-for="order in orders"
          v-bind:key="order.id"
          v-bind:order="order"
        /> -->
      </div>

    </div>
  </div>
</template>

<script>
import { awaitExpression } from '@babel/types';
import axios from 'axios'
// import OrderSummary from '@/components/OrderSummary.vue'

export default {
  name: 'MyAccount',
  components: {
    // OrderSummary
  },

  data() {
    return {
      orders: []
    }
  },

  async mounted() {
    document.title = 'Minha conta | Leiloẽs Já!'

    this.$store.commit('setIsLoading', true)
    await this.getMyLances()
    await this.getMyLeiloes()
    this.$store.commit('setIsLoading', false)
  },

  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")
      this.$store.commit('removeToken')
      this.$router.push('/')
    },

    async getMyLances() {
      await axios
        .get('/api/v1/lances/')
        .then(response => {
          this.orders = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

    async getMyLeiloes() {
      await axios
        .get('/api/v1/leiloes/')
        .then(response => {
          this.orders = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
  }
}
</script>
