<template>
  <div class="box mb-4">
    <h3 class="is-size-4 mb-6">Meus Lances</h3>

    <table class="table is-striped is-narrow is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Valor</th>
          <th>Leilão</th>
          <th>Incremento</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="lance in lances"
          v-bind:key="lance.id"
        >
          <td>{{ lance.id }}</td>
          <td>{{ lance.money_value }}</td>
          <td>#{{ lance.get_leilao.id }}</td>
          <td>{{ lance.get_leilao.minimum_increment }}</td>
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

export default {
  name: 'LanceSummary',
  props: {
    lances: {
      type: Array,
      default: [],
    },
  },

  methods: {
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
        })
        .catch(error => {
          console.log(error)
        })          
    } 
  }
}
</script>
