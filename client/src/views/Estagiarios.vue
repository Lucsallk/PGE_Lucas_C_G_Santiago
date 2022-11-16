<script setup>
import { getAPI } from "../assets/axios";
import { onMounted, ref } from "vue";
import ModalEstagiarios from "../components/modaisEstagiario/ModalEstagiarios.vue";
import ModalEditEstagiario from "../components/modaisEstagiario/ModalEditEstagiario.vue";

const estagiarios = ref([]);
const fetchEstagiarios = () => {
  getAPI
    .get("/estagiarios/")
    .then((response) => {
      estagiarios.value = response.data;
    })
    .catch((err) => console.log(err));
};

const apagarEstagiario = (id) => {
  getAPI
    .delete("/estagiarios/" + id)
    .then(() => {
      console.log("apagado com sucesso");
      location.reload();
    })
    .catch((err) => {
      console.log(err);
    });
};

const dadosEstagiario = ref({
  id: 0,
  nomeCompleto: "",
  cpf: "",
  dataNascimento: "",
  setorAlocado: 0,
  cursoGrad: "",
  instEnsino: "",
  cargaHoraria: ""
})

const editarEstagiario = (estagiario) => {
  dadosEstagiario.value.id = estagiario.id
  dadosEstagiario.value.nomeCompleto = estagiario.nomeCompleto
  dadosEstagiario.value.cpf = estagiario.cpf
  dadosEstagiario.value.dataNascimento = estagiario.dataNascimento
  dadosEstagiario.value.setorAlocado = estagiario.setorAlocado
  dadosEstagiario.value.cursoGrad = estagiario.cursoGrad
  dadosEstagiario.value.instEnsino = estagiario.instEnsino
  dadosEstagiario.value.cargaHoraria = estagiario.cargaHoraria
}

onMounted(fetchEstagiarios);
</script>

<template>
  <ModalEstagiarios />
  <main class="mb-auto">
    <div class="container-fluid mb-3">
      <div class="d-flex justify-content-center">
        <button
          type="button"
          class="btn btn-success fw-semibold shadow"
          data-bs-toggle="modal"
          data-bs-target="#cadModal"
        >
          <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24">
            <path
              d="M10.675 19.35V13.3h-6.05v-2.65h6.05V4.6h2.65v6.05h6.05v2.65h-6.05v6.05Z"
            />
          </svg>
          Adicionar Estagiário
        </button>
      </div>
    </div>
    <div
      v-for="estagiario in estagiarios"
      :key="estagiario.id"
      class="container-fluid"
    >
      <div class="row justify-content-center mx-2 mb-4">
        <div class="col-12 col-sm-10 bg-light rounded shadow">
          <div class="row px-3">
            <div class="col-12 col-sm-4 p-2">
              <div class="d-flex flex-column">
                <span>
                  <span class="fw-semibold">Nome</span>
                  {{ estagiario.nomeCompleto }}
                </span>
                <span>
                  <span class="fw-semibold">CPF</span>
                  {{ estagiario.cpf }}
                </span>
                <span>
                  <span class="fw-semibold">Data de nascimento</span>
                  {{ estagiario.dataNascimento }}
                </span>
                <span>
                  <span class="fw-semibold">Setor alocado</span>
                  {{ estagiario.setorAlocado }}
                </span>
              </div>
            </div>
            <div class="col-12 col-sm-4 col-lg-6 p-2">
              <div class="d-flex flex-column">
                <span>
                  <span class="fw-semibold">Curso de graduação</span>
                  {{ estagiario.cursoGrad }}
                </span>
                <span>
                  <span class="fw-semibold">Insituição de ensino</span>
                  {{ estagiario.instEnsino }}
                </span>
                <span>
                  <span class="fw-semibold">Carga Horária</span>
                  {{ estagiario.cargaHoraria }}
                </span>
              </div>
            </div>

            <div class="col-6 col-sm-2 col-lg-1 d-flex justify-content-center align-self-center p-2">
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
            <div class="col-6 col-sm-2 col-lg-1 p-2 d-flex justify-content-center align-self-center">
              <button
                @click="apagarEstagiario(estagiario.id)"
                class="btn btn-danger fw-bold shadow"
              >
                Apagar
              </button>
            </div>

            <ModalEditEstagiario :dadosEstagiario="dadosEstagiario"/>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
