<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Minha conta</h1>
      </div>

      <hr>

      <div class="column is-12">
        <LanceSummary
          @sellItem="sellItem"
          @update="update"
          :lances="lances"
        />
      </div>

      <div class="column is-12">
        <HouseSummary
          @sellItem="sellItem"
          @update="update"
          :houses="houses"
        />
      </div>
        
      <div class="column is-12">
        <VehicleSummary
          @sellItem="sellItem"
          @update="update"
          :vehicles="vehicles"
        />
      </div>
  
    </div>
    
    <SellModal
      :isModalOpen="isModalOpen"
      :item="itemToSell"
      :entities="entities"
      @close-modal="closeModal"
    />
  </div>
</template>

<script>
import axios from 'axios'
import LanceSummary from '@/components/LanceSummary.vue'
import HouseSummary from '@/components/HouseSummary.vue'
import VehicleSummary from '@/components/VehicleSummary.vue'
import SellModal from '@/components/SellModal.vue'

export default {
  name: 'ProfileView',
  components: {
    LanceSummary,
    HouseSummary,
    VehicleSummary,
    SellModal,
  },

  data() {
    return {
      isModalOpen: false,
      itemToSell: {},

      entities: [],
      lances: [],
      houses: [],
      vehicles: [],
    }
  },

  async mounted() {
    document.title = 'Minha conta | Leiloẽs Já!'

    this.$store.commit('setIsLoading', true)
    await this.update()
    this.$store.commit('setIsLoading', false)
  },

  methods: {
    async update() {
      await this.getMyHouses()
      await this.getMyVehicles()
      await this.getMyLances()
      await this.getEntities()
    },

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
          this.lances = response.data
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

    async getEntities() {
      await axios
        .get('/api/v1/entidade-financeira/')
        .then(response => {
          this.entities = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

    sellItem(item) {
      this.itemToSell = item
      this.isModalOpen = true
    },

    closeModal() {
      this.itemToSell = {}
      this.isModalOpen = false
    },
  }
}
</script>
