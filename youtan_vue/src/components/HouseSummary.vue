<template>
  <div class="box mb-4">
    <div class="is-flex">
      <h3 class="is-size-4 mb-6">Meus Imóveis</h3>
      <button @click="createItem" class="ml-4 button is-primary">Criar novo</button>
     </div>

    <table class="table is-striped is-narrow is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Tipo</th>
          <th>Nome</th>
          <th>Cidade</th>
          <th>Estado</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="house in houses"
          v-bind:key="house.id"
        >
          <td>#{{ house.id }}</td>
          <td>{{ house.tipo_imovel }}</td>
          <td>{{ house.name }}</td>
          <td>{{ house.cidade }}</td>
          <td>{{ house.estado }}</td>
          <td class="is-flex is-justify-content-end">
            <button @click="sellItem(house)" class="ml-4 button is-primary">Leiloar</button>
            <button @click="deleteItem(house.id)" class="ml-4 button is-danger">Apagar</button>
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
  name: 'HouseSummary',
  props: {
    houses: {
      type: Array,
      default: [],
    },
  },

  methods: {
    sellItem(item) {
      const newItem = {...item}
      newItem.item_type = 'house'
      this.$emit('sell-item', newItem)
    },

    async deleteItem(itemId) {
      axios
        .delete(`/api/v1/houses/${itemId}`)
        .then(response => {
          toast({
              message: 'Imóvel removido com sucesso.',
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
    },

    createItem() {
      this.$emit('createItem')
    }
  }
}
</script>
