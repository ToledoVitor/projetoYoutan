<template>
  <div class="leilao-page">

    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img v-bind:src="item.get_item_object?.image">
        </figure>

        <h1 class="title">{{ item.get_item_object?.name }}</h1>

        <p>{{ item }}</p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Informações</h2>

        <p><strong>Lance atual: </strong></p>

        <div class="field has-addons mt-6">
          <div class="control">
            <a class="button is-dark">-</a>
            <a class="button is-dark">Dar Lance</a>
            <a class="button is-dark">+</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LeilaoDetails',
  data () {
    return {
      item: {},
    }
  },

  mounted() {
    this.getLeilaoDetails()
  },
  
  methods: {
    getLeilaoDetails() {
      const leilao_id = this.$route.params.leilao_id
    }
  }
}
</script>