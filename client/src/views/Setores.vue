<script setup>
import { getAPI } from "../assets/axios";
import { onMounted, ref } from "vue";
// import ModalEstagiarios from "../components/modaisEstagiario/ModalEstagiarios.vue";
// import ModalEditEstagiario from "../components/modaisEstagiario/ModalEditEstagiario.vue";

const setores = ref([]);
const fetchSetor = () => {
  getAPI
    .get("/setores/")
    .then((response) => {
      setores.value = response.data;
      console.log(response)
    })
    .catch((err) => console.log(err));
};

onMounted(fetchSetor)
</script>

<template>
  <main class="mb-auto">
    <div class="container-fluid mb-3">
      <div class="d-flex justify-content-center">
        <button
          type="button"
          class="btn btn-success fw-semibold shadow"
          data-bs-toggle="modal"
          data-bs-target="#setorModal"
        >
          <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24">
            <path
              d="M10.675 19.35V13.3h-6.05v-2.65h6.05V4.6h2.65v6.05h6.05v2.65h-6.05v6.05Z"
            />
          </svg>
          Adicionar Setor
        </button>
      </div>
    </div>
    <div
      v-for="setor in setores"
      :key="setores.id"
      class="container-fluid"
    >
      <div class="row justify-content-center mx-2 mb-4">
        <div class="col-8 col-sm-8 col-lg-5 bg-light rounded shadow">
          <div class="row px-3 p-2">
            <div class="col-12 col-sm-4 col-lg-3 p-2">
              <div class="d-flex flex-column justify-content-center">
                <p class="fw-semibold text-center">Setor</p>
                <p class="text-center mb-0">{{ setor.nome }}</p>
              </div>
            </div>
            <div class="col-12 col-sm-4 col-lg-3 p-2">
              <div class="d-flex flex-column">
                <div class="d-flex flex-column justify-content-center">
                  <p class="fw-semibold text-center">Chefe</p>
                  <p class="text-center mb-0">Ayrton Hora</p>
                </div>
              </div>
            </div>
            <div class="col-12 col-sm-4 col-lg-2 p-2">
              <div class="d-flex flex-column">
                <div class="d-flex flex-column justify-content-center">
                  <p class="fw-semibold text-center">Capacidade</p>
                  <p class="text-center mb-0">10</p>
                </div>
              </div>
            </div>

            <div
              class="col-12 col-sm-4 col-lg-2 d-flex justify-content-center align-self-center p-2"
            >
              <button
                type="button"
                class="btn btn-warning fw-semibold shadow"
                data-bs-toggle="modal"
                data-bs-target="#editModal"
                @click="editarEstagiario(estagiario)"
              >
                Editar
              </button>
            </div>
            <div
              class="col-12 col-sm-4 col-lg-2 d-flex justify-content-center align-self-center"
            >
              <button
                @click="apagarEstagiario(estagiario.id)"
                class="btn btn-danger fw-bold shadow"
              >
                Apagar
              </button>
            </div>

            <!-- <ModalEditEstagiario :dadosEstagiario="dadosEstagiario"/> -->
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
