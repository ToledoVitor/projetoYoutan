<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">
          Criar conta
        </h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Usuário</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Senha</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>

          <div class="field">
            <label>Repita a Senha</label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
              {{ error }}
            </p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">
                Criar conta
              </button>
            </div>
          </div>

          <hr>
        
          Ou <router-link to="/login">clique aqui</router-link> para fazer login!

        </form>

      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast'

export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      errors: [],
    }
  },

  mounted() {
    document.title = 'Cadastrar | Leiloẽs Já!'
  },

  methods: {
    submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('Digite um nome válido.')
      }

      if (this.password.length < 8 ) {
        this.errors.push('A senha é muito curta.')
      }

      if (this.password != this.password2) {
        this.errors.push('As senhas são diferentes')
      }

      if (!this.errors.length) {
        const userData = {
          username: this.username,
          password: this.password,
        }

        axios
          .post('/api/v1/users/', userData)
          .then(response => {
            toast({
              message: 'Conta criada! Por favor faça seu login.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2 * 1000,
              position: 'bottom-center',
            })

            this.$router.push('/login')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }

              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Algo deu errado. Tente novamente mais tarde.')

              console.log(JSON.stringify(error))
            }
          })
      }
    },
  }
}

</script>