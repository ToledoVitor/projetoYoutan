<template>
  <div class="box">
    <figure class="image">
      <img :src="item.get_item_object?.thumbnail">
    </figure>

    <p class="mt-2 is-size-4 has-text-success">{{ getNextLance }}</p>
    <span
      class="tag is-medium is-justify-content-flex-end"
      :class="{
        'is-info is-light': isHouse,
        'is-warning is-light': isVehicle,
      }"
    >
      {{ isHouse ? 'Imóveis' : 'Veículos' }}
    </span>

    <hr>

    <h3 class="mb-2 is-size-5 is-flex is-justify-content-space-between">
      {{ item.get_item_object?.name }}
    </h3>

    <template v-if="isHouse">
      Tipo: {{ item.get_item_object?.tipo_imovel }} <br>
      {{ item.get_item_object?.logradouro }} {{ item.get_item_object?.numero }} <br>
      {{ item.get_item_object?.bairro }} <br>
      {{ item.get_item_object?.cidade }} - {{ item.get_item_object?.estado }}
    </template>

    <template v-else>
      Tipo: {{ item.get_item_object?.tipo_veiculo }} <br>
      Placa: {{ item.get_item_object?.placa }} <br>
      Ano: {{ item.get_item_object?.ano }}
    </template>

    <div class="mt-4 is-flex is-justify-content-center">
      <button @click="makeLance(item)" class="ml-4 button is-primary">Dar lance</button>
    </div>
  </div>
</template>

<script>
const currencyFormat = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
  minimumFractionDigits: 2,
});

export default {
  name: 'ItemCard',
  props: {
    item: {
      type: Object,
      default: {},
    },
  },

  methods: {
    makeLance (item) {
      this.$emit('make-lance', item)
    },
  },

  computed: {
    getNextLance () {
      if (!this.item) {
        return ''
      }
      return currencyFormat.format(this.item.get_latest_lance_value)
    },

    isHouse () {
      return this.item?.get_item_type === "core | imovel"
    },

    isVehicle () {
      return this.item?.get_item_type === "core | veiculo"
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
