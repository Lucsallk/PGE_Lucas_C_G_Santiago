<script setup>
import { getAPI } from "../assets/axios";
import { onMounted, ref } from "vue";

const estagiario = ref([]);
const fetchEstagiarios = () => {
  getAPI
    .get("/estagiarios/")
    .then((response) => {
      console.log("data fetched");
      console.log(response.data);
      estagiario.value = response.data;
    })
    .catch((err) => console.log(err));
};
onMounted(fetchEstagiarios);
</script>

<template>
  <main class="container mt-5">
    <div v-for="estagiario in estagiarios" :key="estagiario.id" class="row">
      <div class="card mb-4 shadow">
        <p>
          <span class="fw-semibold">Nome </span> {{ estagiario.nomeCompleto }}
        </p>
      </div>
    </div>
  </main>
</template>
