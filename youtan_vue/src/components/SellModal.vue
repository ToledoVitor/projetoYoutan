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
        <button
          @click="closeModal"
          class="delete"
          aria-label="close"
        />
      </header>

      <section class="modal-card-body">
        <div class="columns">
          <div class="column">
            <div class="mb-4 field">
              <label>Defina o lance mínimo:</label>
              <div class="control">
                <input type="money" class="input" v-model="minimum_increment">
              </div>
            </div>
          </div>

          <div class="column">
            <label>Escolha a instituição financeira:</label> <br>
            <div class="select is-normal">
              <select v-model="financial_entity">
                <option
                  v-for="entity in entities"
                  v-bind:key="entity.id"
                >
                  {{entity.name}}
                </option>
              </select>
            </div>
          </div>
        </div>

        <div class="mt-4 notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">
            {{ error }}
          </p>
        </div>
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
    },
    entities: {
      type: Array,
      default: []
    },
  },

  data() {
    return {
      minimum_increment: 0,
      financial_entity: null,
      errors: [],
    }
  },

  methods: {
    closeModal() {
      this.$emit('close-modal')
    },

    sellItem() {
      this.errors = []

      if (!this.financial_entity) {
        this.errors.push('Escolha uma instituição financeira válida.')
      }

      if (!this.minimum_increment || parseInt(this.minimum_increment) <= 0) {
        this.errors.push('Valor mínimo de incremento inválido.')
      }

      if (!this.errors.length) {
        const createFormData = {
          item_id: this.item.id,
          item_type: this.item.item_type,
          financial_entity: this.financial_entity,
          minimum_increment: this.minimum_increment,
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
}
</script>