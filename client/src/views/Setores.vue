<script setup>
import { getAPI } from "../assets/axios";
import { onMounted, ref } from "vue";
import ModalSetor from "../components/modaisSetores/ModalSetor.vue";
import ModalEditSetor from "../components/modaisSetores/ModalEditSetor.vue";

const setores = ref([]);
const fetchSetor = () => {
  getAPI
    .get("/setores/")
    .then((response) => {
      setores.value = response.data;
    })
    .catch((err) => console.log(err));
};

const apagarSetor = (id) => {
  getAPI
    .delete("/setores/" + id)
    .then(() => {
      location.reload();
    })
    .catch((err) => {
      console.log(err);
    });
};

const dadosSetor = ref({
  id: 0,
  nome: "",
  chefe: "",
  capacidadeSetor: "",
});

const editarSetor = (setor) => {
  dadosSetor.value.id = setor.id;
  dadosSetor.value.nome = setor.nome;
  dadosSetor.value.chefe = setor.chefe;
  dadosSetor.value.capacidadeSetor = setor.capacidadeSetor;
};

onMounted(fetchSetor);
</script>

<template>
  <ModalSetor />

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
    <div v-for="setor in setores" :key="setores.id" class="container-fluid">
      <div class="row align-content-center justify-content-center mx-2 mb-4">
        <div class="col-8 col-sm-8 col-lg-7 bg-light rounded shadow">
          <div class="row align-items-center px-3 p-2">
            <div class="col-12 col-sm-4 col-lg-3 p-2">
              <div class="d-flex flex-column justify-content-center">
                <p class="fw-semibold text-center mb-0">Setor</p>
                <p class="text-center mb-0">{{ setor.nome }}</p>
              </div>
            </div>
            <div class="col-12 col-sm-4 col-lg-3 p-2">
              <div class="d-flex flex-column">
                <div class="d-flex flex-column justify-content-center">
                  <p class="fw-semibold text-center mb-0">Chefe</p>
                  <p class="text-center mb-0">{{ setor.chefe }}</p>
                </div>
              </div>
            </div>
            <div class="col-12 col-sm-4 col-lg-2 p-2">
              <div class="d-flex flex-column">
                <div class="d-flex flex-column justify-content-center">
                  <p class="fw-semibold text-center mb-0">Capacidade</p>
                  <p class="text-center mb-0">{{ setor.capacidadeSetor}}</p>
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
                data-bs-target="#exampleModal"
                @click="editarSetor(setor)" 
              >
                Editar
              </button>
            </div>
            <div
              class="col-12 col-sm-4 col-lg-2 d-flex justify-content-center align-self-center"
            >
              <button
                @click="apagarSetor(setor.id)"
                class="btn btn-danger fw-bold shadow"
              >
                Apagar
              </button>
            </div>
            
            <ModalEditSetor :dadosSetor="dadosSetor" />
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
