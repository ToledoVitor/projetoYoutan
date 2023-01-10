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
          @make-lance="makeLance"
        />
      </div>
    </div>

    <MakeLance
      :itemToBuy="itemToBuy"
      :isModalOpen="isModalOpen"
      @close-modal="closeModal"
    />
  </div>
</template>

<script>
import axios from 'axios'

import itemCard from '@/components/itemCard.vue'
import MakeLance from '@/components/MakeLance.vue';

export default {
  name: 'ListLeilaoView',
  components: {
    itemCard,
    MakeLance,
},

  data () {
    return {
      items: [],

      itemToBuy: null,
      isModalOpen: false,
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
        })
        .catch(error => {
          console.log(error)
        })
    },

    makeLance (item) {
      this.itemToBuy = item
      this.isModalOpen = true
    },
    
    closeModal () {
      this.isModalOpen = false
      this.getLatestLeiloes()
    }
  }
}
</script>