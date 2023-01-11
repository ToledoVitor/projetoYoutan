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
          :houses="houses"
          @createItem="createHouse"
          @sellItem="sellItem"
          @update="update"
        />
      </div>
        
      <div class="column is-12">
        <VehicleSummary
          :vehicles="vehicles"
          @createItem="createVehicle"
          @sellItem="sellItem"
          @update="update"
        />
      </div>
  
    </div>
    
    <CreateHouseModal 
      :isModalOpen="isCreateHouseModalOpen"
      @closeModal="closeHouseModal"
    />

    <CreateVehicleModal 
      :isModalOpen="isCreateVehicleModalOpen"
      @closeModal="closeVehicleModal"
    />

    <SellModal
      :isModalOpen="isSellModalOpen"
      :item="itemToSell"
      :entities="entities"
      @close-modal="closeSellModal"
    />
  </div>
</template>

<script>
import axios from 'axios'
import LanceSummary from '@/components/LanceSummary.vue'
import HouseSummary from '@/components/HouseSummary.vue'
import CreateHouseModal from '@/components/CreateHouseModal.vue'

import VehicleSummary from '@/components/VehicleSummary.vue'
import CreateVehicleModal from '@/components/CreateVehicleModal.vue'

import SellModal from '@/components/SellModal.vue'

export default {
  name: 'ProfileView',
  components: {
    LanceSummary,
    HouseSummary,
    CreateHouseModal,
    VehicleSummary,
    CreateVehicleModal,
    SellModal,
  },

  data() {
    return {
      itemToSell: {},

      isSellModalOpen: false,
      isCreateHouseModalOpen: false,
      isCreateVehicleModalOpen: false,

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

    async getMyHouses() {
      await axios
        .get('/api/v1/houses/')
        .then(response => {
          this.houses = response.data
        })
        .catch(error => {
          console.log(error)
        })          
    },
    
    async getMyVehicles() {
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

    createHouse() {
      this.isCreateHouseModalOpen = true
    },

    closeHouseModal() {
      this.isCreateHouseModalOpen = false
      this.update()
    },

    createVehicle() {
      this.isCreateVehicleModalOpen = true
    },

    closeVehicleModal() {
      this.isCreateVehicleModalOpen = false
      this.update()
    },

    sellItem(item) {
      this.itemToSell = item
      this.isSellModalOpen = true
    },

    closeSellModal() {
      this.itemToSell = {}
      this.isSellModalOpen = false
    },
  }
}
</script>
