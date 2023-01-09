<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Minha conta</h1>
      </div>

      <hr>

      <div class="column is-12">
        <LanceSummary
        :lances="lances"
        />
      </div>

      <div class="column is-12">
        <HouseSummary
        :houses="houses"
        />
      </div>
        
      <div class="column is-12">
        <VehicleSummary
        :vehicles="vehicles"
        />
      </div>
  
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LanceSummary from '@/components/LanceSummary.vue'
import HouseSummary from '@/components/HouseSummary.vue'
import VehicleSummary from '@/components/VehicleSummary.vue'

export default {
  name: 'ProfileView',
  components: {
    LanceSummary,
    HouseSummary,
    VehicleSummary,
  },

  data() {
    return {
      lances: [],
      houses: [],
      vehicles: [],
    }
  },

  async mounted() {
    document.title = 'Minha conta | Leiloẽs Já!'

    this.$store.commit('setIsLoading', true)
    await this.getMyHouses()
    await this.getMyVehicles()
    await this.getMyLances()
    this.$store.commit('setIsLoading', false)
  },

  methods: {
    async getMyHouses () {
      await axios
        .get('/api/v1/houses/')
        .then(response => {
          this.houses = response.data
        })
        .catch(error => {
          console.log(error)
        })          
    },
    
    async getMyVehicles () {
      await axios
        .get('/api/v1/vehicles/')
        .then(response => {
          this.vehicles = response.data
        })
        .catch(error => {
          console.log(error)
        })        
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
