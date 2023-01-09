<template>
  <div class="box">
    <figure class="image">
      <img :src="vehicle.get_thumbnail">
    </figure>

    <h3 class="is-size-4 is-flex is-justify-content-space-between">
      {{ vehicle.name }}
    </h3>
    <span
      class="tag is-medium is-danger is-justify-content-flex-end"
    >
      Veículos
    </span>
    
    <p class="mt-2 is-size-4 has-text-success">{{ humanizeMoney }}</p>

    <hr>

    <a class="buttons is-flex is-justify-content-center">
      <router-link to="/leilao" class="button is-dark is-normal">
        Dar lance
      </router-link>
    </a>
  </div>
</template>

<script>
export default {
  name: 'vehicleCard',
  props: {
    vehicle: {
      type: Object,
      default: {},
    }
  },

  computed: {
    humanizeMoney() {
      return `R$ ${this.vehicle.money_value},00`
    }
  }
}
</script>

<style scoped>
.image{
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
