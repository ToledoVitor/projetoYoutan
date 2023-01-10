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
        <label>Nome:</label>
        <div class="mb-4 control">
          <input type="text" class="input" v-model="createForm.name">
        </div>

        <div class="columns">
          <div class="column">
            <div class="mb-2 field">
              <label>Placa:</label>
              <div class="control">
                <input type="text" class="input" v-model="createForm.placa">
              </div>
            </div>
          </div>

          <div class="column">
            <div class="mb-2 field">
              <label>Ano:</label>
              <div class="control">
                <input type="text" class="input" v-model="createForm.ano">
              </div>
            </div>
          </div>
        </div>

        <label>Tipo de Veículo:</label> <br>
        <div class="mb-4 select is-normal">
          <select v-model="createForm.tipo_veiculo">
            <option
              v-for="tipo in tipoImovelChoices"
              v-bind:key="tipo"
            >
              {{tipo}}
            </option>
          </select>
        </div>

        <div class="file has-name">
          <label class="file-label">
            <input class="file-input" type="file" name="image" v-on:change="setFile">
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                Escolha uma imagem
              </span>
            </span>
            <span class="file-name">
              {{ image?.name }}
            </span>
          </label>
        </div>


        <div class="mt-4 notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">
            {{ error }}
          </p>
        </div>
      </section>

      <footer class="is-flex is-justify-content-end modal-card-foot">
        <button @click="closeModal" class="button is-danger">Cancelar</button>
        <button @click="createVehicle" class="button is-primary">Criar</button>
      </footer>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'CreateVehicleModal',
  props: {
    isModalOpen: {
      type: Boolean,
      default: false
    },
  },

  data() {
    return {
      createForm: {
        name: '',
        tipo_veiculo: '',
        placa: '',
        ano: '',
      },
      image: null,

      tipoImovelChoices: [
        'moto',
        'carro',
        'van',
      ],

      errors: [],
    }
  },

  methods: {
    setFile(event) {
      var files = event.target.files || event.dataTransfer.files
      if (!files.length)
        return this.image = null
    
      this.image = files[0]
    },

    closeModal() {
      this.$emit('close-modal')
    },

    createVehicle() {
      this.errors = []

      if (Object.values(this.createForm).some(value => !Boolean(value))) {
        this.errors.push('Confira os dados informados.')
      }

      if (!this.errors.length) {
        var formData = new FormData()
        formData.append("image", this.image)

        Object.keys(this.createForm).forEach((key) => {
          formData.append(key, this.createForm[key])
        })

        axios
          .post('/api/v1/vehicles/', formData)
          .then(response => {
            toast({
                message: 'Veículo criado com sucess.',
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