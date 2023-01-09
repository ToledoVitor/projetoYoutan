<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6 main-section">
      <div class="has-light-grey-background hero-body has-text-centered">
        <p class="title has-text-black has-text-weight-bold mb-6">
          Bem vindo ao Leiloẽs Já!
        </p>
        <p class="subtitle has-text-black has-text-weight-bold">
          O maior site de leilões da receita federal. 
        </p>
      </div>
    </section>

    <div class="is-flex is-justify-content-center buttons are-large">
      <router-link to="/leiloes/ver" class="button is-dark">
        <h2 class="is-size-4 has-text-centered">Confira já os últimos leilões.</h2>
      </router-link>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {}
  },

  mounted() {
    document.title = 'Home | Leiloẽs Já!'
  }
}
</script>

<style scoped>
.main-section {
  background-image: url(https://www.maripademinas.mg.gov.br/wp/wp-content/uploads/2019/11/1940866.png);
}

.has-light-grey-background{
  background-color: #80808075;
}
</style>