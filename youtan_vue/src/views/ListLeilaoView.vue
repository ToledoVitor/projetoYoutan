<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <p class="title">
          Leilões ativos
        </p>
        <p class="subtitle">
          Confira nossos leilões e faça seu lance!
        </p>
      </div>

    </section>

    <div class="pt-4 columns is-multiline">
      <div class="column is-3" v-for="item in items" v-bind:key="item.id">
        <itemCard
          :item="item"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import itemCard from '@/components/itemCard.vue'

export default {
  name: 'ListLeilaoView',
  components: {
    itemCard
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
        .get('/api/v1/leiloes/')
        .then(response => {
          this.items = response.data
          this.vehicles = response.data.vehicles
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>