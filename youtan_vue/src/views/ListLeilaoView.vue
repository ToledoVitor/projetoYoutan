<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">
          Imóveis
        </p>
        <p class="subtitle">
          Faça seu lance
        </p>
      </div>

      <div class="column is-3" v-for="house in houses" v-bind:key="house.id">
        <houseCard
          :house="house"
        />
      </div>
    </section>

    <div>ALGUMA COISA NO MEIO PRA TIRAR O BURACO</div>


    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">
          Veículos
        </p>
        <p class="subtitle">
          Faça seu lance
        </p>
      </div>

      <div class="column is-3" v-for="vehicle in vehicles" v-bind:key="vehicle.id">
        <vehicleCard
          :vehicle="vehicle"
        />
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

import houseCard from '@/components/houseCard.vue'
import vehicleCard from '@/components/vehicleCard.vue'

export default {
  name: 'ListLeilaoView',
  components: {
    houseCard,
    vehicleCard,
  },

  data () {
    return {
      houses: [],
      vehicles: [],

      items: [
        {
          id: 1,
          name: 'Teste',
          money_value: 1000,
          get_thumbnail: 'https://images.adsttc.com/media/images/613f/df13/8580/2b01/6405/340e/newsletter/whatsapp-image-2021-02-09-at-10-9.jpg?1631575834',
        }
      ]
    }
  },

  mounted() {
    document.title = 'Leilões | Leiloẽs Já!'

    this.getLatestLeiloes()
  },

  methods: {
    getLatestLeiloes() {
      axios
        .get('/api/v1/get_latest_leiloes/')
        .then(response => {
          this.houses = response.data.houses
          this.vehicles = response.data.vehicles
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>