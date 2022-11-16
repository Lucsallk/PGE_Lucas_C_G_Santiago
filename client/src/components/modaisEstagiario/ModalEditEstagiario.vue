<script setup>
import { ref, onMounted } from "vue";
import { getAPI } from "../../assets/axios";
const props = defineProps(["dadosEstagiario"]);

const editarEstagiario = (dadosEstagiario) => {
  console.log(dadosEstagiario);
  console.log(dadosEstagiario.dataNascimento);
  getAPI
    .patch("/estagiarios/" + dadosEstagiario.id + "/", {
      id: dadosEstagiario.id,
      nomeCompleto: dadosEstagiario.nomeCompleto,
      cpf: dadosEstagiario.cpf,
      dataNascimento: dadosEstagiario.dataNascimento,
      cursoGrad: dadosEstagiario.cursoGrad,
      instEnsino: dadosEstagiario.instEnsino,
      cargaHoraria: dadosEstagiario.cargaHoraria,
      setorAlocado: dadosEstagiario.setorAlocado,
    })
    .then(() => {
      location.reload();
    })
    .catch((err) => console.log(err));
};

const setores = ref([]);

const listarSetores = () => {
  getAPI
    .get("/setores/")
    .then((response) => {
      setores.value = response.data;
    })
    .catch((err) => console.log(err));
};

onMounted(listarSetores);
</script>

<template>
  <div
    class="modal fade"
    id="editModal"
    tabindex="-1"
    aria-labelledby="cadModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="cadModalLabel">
            Adicionar Estagiário
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <div class="row">
            <div class="mb-3">
              <label for="nomeCompleto" class="form-label"
                >Nome completo:</label
              >
              <input
                v-model="props.dadosEstagiario.nomeCompleto"
                id="nomeCompleto"
                class="form-control"
                placeholder="Fulado da Silva"
                type="text"
              />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-7">
              <label for="cursoGrad" class="form-label"
                >Curso de gradução:</label
              >
              <input
                v-model="props.dadosEstagiario.cursoGrad"
                id="cursoGrad"
                class="form-control"
                type="text"
              />
            </div>

            <div class="col-5">
              <label for="dataNascimento" class="form-label"
                >Data de nascimento</label
              >
              <input
                v-model="props.dadosEstagiario.dataNascimento"
                id="dataNascimento"
                class="form-control"
                type="date"
              />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-8">
              <label for="instEnsino" class="form-label"
                >Instituição de ensino</label
              >
              <input
                v-model="props.dadosEstagiario.instEnsino"
                id="instEnsino"
                class="form-control"
                type="text"
              />
            </div>

            <div class="col-4">
              <label for="cargaHoraria" class="form-label">Carga horária</label>
              <input
                v-model="props.dadosEstagiario.cargaHoraria"
                id="cargaHoraria"
                class="form-control"
                type="number"
              />
            </div>
          </div>

          <div class="row">
            <div class="mb-3">
              <label for="setorAlocado" class="form-label">Setor alocado</label>
              <select
                v-model="props.dadosEstagiario.setorAlocado"
                id="setorAlocado"
                class="form-select"
              >
                <option v-for="setor in setores" :key="setor.id" :value="setor.id">{{ setor.nome }}</option>
              </select>
            </div>
          </div>
        </div>

        <div class="modal-footer justify-content-center">
          <button
            type="button"
            class="btn btn-danger fw-semibold"
            data-bs-dismiss="modal"
          >
            Cancelar
          </button>
          <button
            @click="editarEstagiario(props.dadosEstagiario)"
            type="button"
            class="btn btn-success fw-semibold"
          >
            Save changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
