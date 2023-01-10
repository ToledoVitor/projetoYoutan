<template>
  <div class="box mb-4">
    <h3 class="is-size-4 mb-6">Meus Lances</h3>

    <table class="table is-striped is-narrow is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Lance</th>
          <th>Leilão ID</th>
          <th>Incremento Mínimo</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="lance in lances"
          v-bind:key="lance.id"
        >
          <td>{{ lance.id }}</td>
          <td>{{ formatMoney(lance.money_value) }}</td>
          <td>#{{ lance.get_leilao.id }}</td>
          <td>{{ formatMoney(lance.get_leilao.minimum_increment) }}</td>
          <td class="is-flex is-justify-content-end">
            <button @click="deleteItem(lance.id)" class="ml-4 button is-danger">Apagar</button>
          </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

const currencyFormat = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
  minimumFractionDigits: 2,
});

export default {
  name: 'LanceSummary',
  props: {
    lances: {
      type: Array,
      default: [],
    },
  },

  methods: {
    formatMoney(money) {
      return currencyFormat.format(money)
    },

    async deleteItem(itemId) {
      axios
        .delete(`/api/v1/lances/${itemId}`)
        .then(response => {
          toast({
              message: 'Lance removido com sucesso.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2 * 1000,
              position: 'bottom-center',
            })

          this.$emit('update')
        })
        .catch(error => {
          console.log(error)
        })          
    } 
  }
}
</script>
