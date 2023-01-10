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
        <p class="modal-card-title">Dar lance</p>
        <button class="delete" aria-label="close"></button>
      </header>

      <section class="modal-card-body">
        <div class="columns">
          <div class="column">
            <div class="mb-4 field">
              <label class="is-size-5 has-text-primary">
                Defina seu lance:
              </label>
              <br>

              <label>
                Incremento mínimo {{ formatMoney(itemToBuy?.minimum_increment) }} 
              </label>
              <br>

              <div class="mt-5 is-flex is-justify-content-center">
                <button class="button is-link is-light" @click="decrementLance">
                  -
                </button>

                <button class="ml-2 mr-2 button is-link is-light">
                  {{ value }}
                </button>

                <button class="button is-link is-light" @click="incrementLance">
                  +
                </button>
              </div>
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
        <button @click="makeLance" class="button is-primary">Dar Lance</button>
      </footer>
    </div>

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
  name: 'MakeLance',
  props: {
    isModalOpen: {
      type: Boolean,
      default: false
    },
    itemToBuy: {
      type: Object,
      default: {}
    }
  },

  data() {
    return {
      value: 0,
      minimal_value: 0,
      errors: [],
    }
  },

  watch: {
    itemToBuy(item) {
      this.value = parseInt(item.get_latest_lance_value) + parseInt(item.minimum_increment)
      this.minimal_value = this.value 
    }
  },

  methods: {
    closeModal() {
      this.$emit('close-modal')
    },

    formatMoney(money) {
      if (!money) {
        return
      }
      return currencyFormat.format(money)
    },

    decrementLance () {
      if (this.value <= this.minimal_value) {
        return
      }

      this.value -= parseInt(this.itemToBuy.minimum_increment)
    },

    incrementLance () {
      // Valor aleatório para limitar lance máximo
      if (this.value >= 10 * 1000 * 1000) {
        return
      }

      this.value += parseInt(this.itemToBuy.minimum_increment)
    },

    makeLance() {
      this.errors = []

      if (!this.value || this.value <= parseInt(this.minimal_value)) {
        this.errors.push('Lance inválido.')
      }

      if (this.value % this.itemToBuy.minimum_increment !== 0) {
        this.errors.push('Lance não é um múltiplo do incremento.')
      }

      if (!this.errors.length) {
        const createLanceData = {
          leilao_id: this.itemToBuy.id,
          value: this.value,
        }

        axios
          .post('/api/v1/lances/', createLanceData)
          .then(response => {
            toast({
                message: 'Lance feito com sucesso.',
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