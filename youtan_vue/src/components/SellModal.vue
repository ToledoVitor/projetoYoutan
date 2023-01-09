<template>
  <div
    class="modal"
    :class="{
      'is-active': isModalOpen
    }"
  >

  <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Criar Leilão</p>
        <button class="delete" aria-label="close"></button>
      </header>

      <section class="modal-card-body">
        <div class="mb-4 field">
          <label>Defina o lance mínimo:</label>
          <div class="control">
            <input type="money" class="input" v-model="minimum_increment">
          </div>
        </div>

        <figure class="image">
          <img :src="item.get_thumbnail">
        </figure>

      </section>

      <footer class="is-flex is-justify-content-end modal-card-foot">
        <button @click="closeModal" class="button is-danger">Cancelar</button>
        <button @click="sellItem" class="button is-primary">Leiloar</button>
      </footer>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'SellModal',
  props: {
    isModalOpen: {
      type: Boolean,
      default: false
    },
    item: {
      type: Object,
      default: {}
    }
  },

  data() {
    return {
      minimum_increment: 0,
    }
  },

  methods: {
    closeModal() {
      this.$emit('close-modal')
    },

    sellItem() {
      const createFormData = {
        item_id: this.item.id,
        item_type: this.item.item_type,
        minimum_increment: this.minimum_increment,
      }

      if (this.minimum_increment < 0) {
        return
      }

      axios
        .post('/api/v1/leiloes/', createFormData)
        .then(response => {
          toast({
              message: 'Leilão criado com sucesso.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2 * 1000,
              position: 'bottom-center',
            })
          
          this.$emit('close-modal')
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>