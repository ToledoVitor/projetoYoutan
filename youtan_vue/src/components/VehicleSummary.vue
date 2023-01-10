<template>
  <div class="box mb-4">
    <div class="is-flex">
      <h3 class="is-size-4 mb-6">Meus Veículos</h3>
      <button @click="createItem" class="ml-4 button is-primary">Criar novo</button>
    </div>

    <table class="table is-striped is-narrow is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>ID</th>
          <th>Tipo</th>
          <th>Nome</th>
          <th>Ano</th>
          <th>Placa</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="vehicle in vehicles"
          v-bind:key="vehicle.id"
        >
          <td>#{{ vehicle.id }}</td>
          <td>{{ vehicle.tipo_veiculo }}</td>
          <td>{{ vehicle.name }}</td>
          <td>{{ vehicle.ano }}</td>
          <td>{{ vehicle.placa }}</td>
          <td class="is-flex is-justify-content-end">
            <button @click="sellItem(vehicle)" class="ml-4 button is-primary">Leiloar</button>
            <button @click="deleteItem(vehicle.id)" class="ml-4 button is-danger">Apagar</button>
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
  name: 'VehicleSummary',
  props: {
    vehicles: {
      type: Array,
      default: [],
    },
  },

  methods: {
    sellItem(item) {
      const newItem = {...item}
      newItem.item_type = 'vehicle'
      this.$emit('sell-item', newItem)
    },

    async deleteItem(itemId) {
      axios
        .delete(`/api/v1/vehicles/${itemId}`)
        .then(response => {
          toast({
              message: 'Veículo removido com sucesso.',
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
