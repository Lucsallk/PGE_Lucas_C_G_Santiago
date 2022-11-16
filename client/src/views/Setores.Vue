<script setup>
import { getAPI } from "../assets/axios";
import { onMounted, ref } from "vue";

// import ModalEstagiarios from "../components/modaisEstagiario/ModalEstagiarios.vue";
// import ModalEditEstagiario from "../components/modaisEstagiario/ModalEditEstagiario.vue";

const setores = ref([]);
const fetchSetores = () => {
  getAPI
    .get("/estagiarios")
    .then((response) => {
      setores.value = response.data;
      console.log(response)
    })
    .catch((err) => console.log(err));
};

onMounted(fetchSetores);
</script>

<template>
    {{ setores }}
</template>
